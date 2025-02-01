import os
import logging
from threading import Event
import hashlib
import json
import shutil  # added for cache removal


import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser, Document
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import InMemoryStore
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings


logger = logging.getLogger(__name__)


# ===========================
# Environment Variables
# ===========================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")


# ===========================
# Global RAG variables
# ===========================
rag_chain = None
rag_initialized = False
pdf_path_global = None
stop_rag_event = Event()




def _pdf_md5(pdf_path: str) -> str:
   """Compute an MD5 hash of the entire PDF file contents."""
   md5 = hashlib.md5()
   with open(pdf_path, "rb") as f:
       md5.update(f.read())
   return md5.hexdigest()




def _rag_cache_dir(pdf_path: str) -> str:
   """Get the base 'rag_cache' folder next to the PDF."""
   return os.path.join(os.path.dirname(pdf_path), "rag_cache")




def chunk_with_tables(pdf_path):
   """Convert PDF to markdown with table preservation. Skips on error or stop event."""
   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered before chunking. Exiting chunk_with_tables early.")
       return []


   try:
       md_text = pymupdf4llm.to_markdown(pdf_path, write_images=False)
   except Exception as e:
       logger.error(f"Cannot parse PDF text: {e}")
       return []


   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered after PDF->markdown. Exiting.")
       return []


   splitter = MarkdownTextSplitter(chunk_size=5000, chunk_overlap=400)
   chunks = splitter.split_text(md_text)


   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered after splitting text. Exiting.")
       return []


   return chunks




def build_rag_system(pdf_path):
   """
   Build the RAG pipeline using the unfiltered PDF, checking for a cached
   FAISS vector store + docstore so we can skip chunking/summarizing if already done.
   """
   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered at start of build_rag_system.")
       return None


   # 1) Attempt to load from disk cache
   pdf_hash = _pdf_md5(pdf_path)
   cache_folder = os.path.join(_rag_cache_dir(pdf_path), pdf_hash)
   vectorstore_dir = os.path.join(cache_folder, "vectorstore")
   docstore_json = os.path.join(cache_folder, "docstore.json")


   if os.path.isdir(vectorstore_dir) and os.path.isfile(docstore_json):
       logger.info(f"[RAG Cache] Found existing cache for hash={pdf_hash}. Attempting to load.")
       if stop_rag_event.is_set():
           logger.info("Stop event was set before loading cache. Exiting build_rag_system.")
           return None
       try:
           embedder = HuggingFaceEmbeddings(
               model_name="nomic-ai/nomic-embed-text-v1.5",
               model_kwargs={"device": "cpu", "trust_remote_code": True}
           )
           # Load the FAISS index with dangerous deserialization allowed.
           vectorstore = FAISS.load_local(
               vectorstore_dir,
               embeddings=embedder,
               allow_dangerous_deserialization=True
           )
           # Load docstore from JSON
           with open(docstore_json, "r", encoding="utf-8") as f:
               stored_docs = json.load(f)  # list of [doc_id, doc_content]
           docstore = InMemoryStore()
           for (doc_id, content) in stored_docs:
               docstore.mset([(doc_id, Document(page_content=content, metadata={"doc_id": doc_id}))])
           retriever = MultiVectorRetriever(
               vectorstore=vectorstore,
               docstore=docstore,
               id_key="doc_id",
               search_kwargs={"k": 3}
           )
           logger.info("[RAG Cache] Successfully loaded RAG cache!")
           return retriever


       except Exception as e:
           logger.warning(f"[RAG Cache] Failed to load from cache: {e}. Removing cache folder and proceeding with normal pipeline.")
           try:
               shutil.rmtree(cache_folder)
           except Exception as re:
               logger.error(f"Failed to remove cache folder {cache_folder}: {re}")


   # 2) No valid cache found; proceed with chunking & summarizing.
   chunks = chunk_with_tables(pdf_path)
   if stop_rag_event.is_set() or not chunks:
       logger.info("Stop RAG event triggered or no chunks found. Exiting build_rag_system.")
       return None


   summarize_prompt = ChatPromptTemplate.from_template("""
Create a concise summary of this text chunk from a sustainability report
optimized for retrieval purposes.
Focus on:
- Key numerical data and metrics
- Table and figure descriptions
- Technical terms and definitions
Original text: {chunk}
Summary:""")




   # ===================================================================
   # To switch to DeepSeek, comment out the OpenAI lines and uncomment
   # the DeepSeek lines below:
   #
   summarizer = (
       {"chunk": RunnablePassthrough()}
       | summarize_prompt
       | ChatOpenAI(
           # --- OPENAI (default) ---
           openai_api_key=OPENAI_API_KEY,
           model="gpt-4o-mini",
           # ------------------------
           # --- DEEPSEEK (comment out the above lines, then uncomment below) ---
           # openai_api_key=DEEPSEEK_API_KEY,
           # base_url="https://api.deepseek.com",
           # model="deepseek-chat",
           # -------------------------------------------------------
           temperature=0.2
       )
       | StrOutputParser()
   )
   # ===================================================================


   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered before summarizing. Exiting.")
       return None


   summaries = summarizer.batch(chunks)
   if stop_rag_event.is_set() or not summaries:
       logger.info("Stop event was set after summarizing. Exiting.")
       return None


   summary_docs = [
       Document(page_content=s, metadata={"doc_id": str(i)})
       for i, s in enumerate(summaries)
   ]
   original_docs = [
       Document(page_content=c, metadata={"doc_id": str(i)})
       for i, c in enumerate(chunks)
   ]


   embedder = HuggingFaceEmbeddings(
       model_name="nomic-ai/nomic-embed-text-v1.5",
       model_kwargs={"device": "cpu", "trust_remote_code": True}
   )


   if stop_rag_event.is_set():
       logger.info("Stop RAG event triggered before embedding. Exiting.")
       return None


   vectorstore = FAISS.from_documents(summary_docs, embedder)
   docstore = InMemoryStore()
   docstore.mset([
       (str(i), original_docs[i]) for i in range(len(original_docs))
   ])


   # 3) Save new cache if not stopped
   if not stop_rag_event.is_set():
       try:
           os.makedirs(cache_folder, exist_ok=True)
           vectorstore.save_local(vectorstore_dir)
           # Save docstore to JSON
           doc_data = []
           for i, c in enumerate(chunks):
               doc_data.append((str(i), c))
           with open(docstore_json, "w", encoding="utf-8") as f:
               json.dump(doc_data, f, indent=2)
           logger.info(f"[RAG Cache] Saved new RAG cache to {cache_folder}")
       except Exception as e:
           logger.error(f"[RAG Cache] Failed to save cache: {e}")


   retriever = MultiVectorRetriever(
       vectorstore=vectorstore,
       docstore=docstore,
       id_key="doc_id",
       search_kwargs={"k": 3}
   )


   return retriever




def build_final_system(pdf_path):
   """
   Wrap the retriever in a final prompt chain that answers user queries.
   """
   if stop_rag_event.is_set():
       logging.info("Stop RAG event triggered at start of build_final_system.")
       return None


   retriever = build_rag_system(pdf_path)
   if stop_rag_event.is_set() or retriever is None:
       logging.info("Stop RAG event triggered or retriever is None. Exiting build_final_system.")
       return None


   prompt = ChatPromptTemplate.from_template("""
Analyze this parsed text and poorly formatted markdown tables from a sustainability report:
{context}


Respond as a sustainability report assistant providing relevant information in detail.
Create your own tables if applicable. If data is not available, say "Data not available".


Question: {input}
""")


   if stop_rag_event.is_set():
       logging.info("Stop RAG event triggered before returning final pipeline. Exiting build_final_system.")
       return None


   # ===================================================================
   # To switch to DeepSeek, comment out the OpenAI lines and uncomment
   # the DeepSeek lines below:
   #
   final_pipeline = (
       {
           "context": retriever
               | RunnableLambda(lambda docs: "\n\n".join(d.page_content for d in docs)),
           "input": RunnablePassthrough()
       }
       | prompt
       | ChatOpenAI(
           # --- OPENAI ---
           openai_api_key=OPENAI_API_KEY,
           model="gpt-4o",
           # ------------------------
           # --- DEEPSEEK ---
           # openai_api_key=DEEPSEEK_API_KEY,
           # base_url="https://api.deepseek.com",
           # model="deepseek-chat",
           # -------------------------------------------------------
           temperature=0.2
       )
       | StrOutputParser()
   )


   return final_pipeline