Project Structure:
├── LICENSE
├── README.md
├── data
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── company_names_tickers.csv
│   ├── company_names_tickers_news.csv
│   ├── diagram.md
│   ├── emissimap3.csv
│   ├── main.py
└── tests
    ├── __init__.py


.pre-commit-config.yaml
```
1 | repos:
2 |   - repo: local
3 |     hooks:
4 |       - id: black
5 |         name: black
6 |         entry: black
7 |         language: system
8 |         types: [python]
9 |       - id: flake8
10 |         name: flake8
11 |         entry: flake8
12 |         args: ["--ignore=E501,W503"]
13 |         language: system
14 |         types: [python]
15 |       - id: isort
16 |         name: isort
17 |         entry: isort
18 |         language: system
19 |         args: ["--profile", "black"]
20 |         types: [python]
```

requirements.txt
```
1 | # project requirements
2 | pandas
3 | numpy==1.26.4
4 | python-dotenv
5 | loguru
6 | pydantic
7 | requests
8 | flask
9 | docling
10 | PyPDF2
11 | openai
12 | docling
13 | google-search-results  # serpapi
14 | yfinance
15 | llama_parse
16 | tabula-py
17 | 
18 | # dev requirements
19 | pre-commit
20 | black
21 | flake8
22 | isort
23 | pytest
24 | 
25 | Flask-SocketIO
26 | folium
27 | 
28 | # The main LangChain library
29 | langchain
30 | langchain_community
31 | langchain_core
32 | pymupdf4llm
33 | langchain_openai
```

.github/pull_request_template.md
```
1 | ### Title
2 | ---
3 | 
4 | 
5 | ### Key Changes
6 | ---
```

tests/__init__.py
```
```

src/__init__.py
```
```

src/company_names_tickers.csv
```
1 | ﻿Symbol,Company Name,Industry,Country,Sector,ISIN Number
2 | AAPL,Apple Inc.,Consumer Electronics,United States,Technology,US0378331005

```

src/main.py
```
1 | import csv
2 | import logging
3 | import os
4 | import re
5 | import sys
6 | import threading
7 | from io import BytesIO
8 | from threading import Event
9 | 
10 | import folium
11 | import pandas as pd
12 | import yfinance as yf
13 | from dotenv import load_dotenv
14 | from flask import (
15 |     Flask,
16 |     Response,
17 |     jsonify,
18 |     redirect,
19 |     render_template,
20 |     request,
21 |     send_file,
22 |     send_from_directory,
23 |     url_for,
24 | )
25 | from flask_socketio import SocketIO
26 | 
27 | load_dotenv()
28 | # append path
29 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
30 | logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
31 | 
32 | import src.utils.rag_utils as rag_utils  # noqa: E402
33 | from src.find.company_profile import CompanyProfile  # noqa: E402
34 | from src.find.esg_reports import ESGReports  # noqa: E402
35 | from src.scripts.retrieve_emissions_data import get_emissions_data  # noqa: E402
36 | 
37 | # LLM-based table extraction
38 | from src.scripts.retrieve_emissions_data_pro import get_emissions_data_pro  # noqa: E402
39 | from src.utils.data_models import TableParsers  # noqa: E402
40 | 
41 | # Globals for RAG
42 | rag_chain = None
43 | rag_initialized = False
44 | pdf_path_global = None
45 | 
46 | app = Flask(__name__)
47 | socketio = SocketIO(app, cors_allowed_origins="*")  # Allows cross-origin requests
48 | 
49 | for rule in app.url_map.iter_rules():
50 |     print(rule)
51 | 
52 | # Get the absolute path of the correct static folder
53 | BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
54 | STATIC_FOLDER = os.path.join(BASE_DIR, "static", "images")
55 | 
56 | # Ensure the correct static/images directory exists
57 | os.makedirs(STATIC_FOLDER, exist_ok=True)
58 | 
59 | 
60 | def dms_to_decimal(dms):
61 |     match = re.match(r"(-?\d+)°(\d+)?", dms)  # Support negative values
62 |     if match:
63 |         degrees = int(match.group(1))  # Handle negative degrees
64 |         minutes = int(match.group(2)) if match.group(2) else 0
65 |         return degrees + (minutes / 60)
66 |     return None  # Return None if format is incorrect
67 | 
68 | 
69 | df = pd.read_csv("src/emissimap3.csv")
70 | # Ensure required columns exist
71 | print(df.head())
72 | df["Latitude"] = df["Latitude"].apply(dms_to_decimal)
73 | df["Longitude"] = df["Longitude"].apply(dms_to_decimal)
74 | print(df)
75 | 
76 | # Create a base map
77 | m = folium.Map(location=[20, 0], zoom_start=2)
78 | 
79 | 
80 | # Define a color scale based on emissions level
81 | def get_color(emissions):
82 |     if emissions < 1000:
83 |         return "green"
84 |     elif 1000 <= emissions < 5000:
85 |         return "orange"
86 |     else:
87 |         return "red"
88 | 
89 | 
90 | # Add markers for each company
91 | for _, row in df.iterrows():
92 |     print(
93 |         f"Adding marker: {row['Company']} ({row['Latitude']}, {row['Longitude']}) - {row['Emissions']} CO2"
94 |     )
95 | 
96 |     folium.CircleMarker(
97 |         location=[row["Latitude"], row["Longitude"]],
98 |         radius=5 + (row["Emissions"] / 1000),
99 |         color="red",
100 |         fill=True,
101 |         fill_color="red",
102 |         fill_opacity=0.7,
103 |         popup=f"{row['Company']} - {row['Emissions']} CO2",
104 |     ).add_to(m)
105 | 
106 | # Save map to an HTML file
107 | map_path = os.path.join(STATIC_FOLDER, "emissions_map.html")
108 | m.save(map_path)
109 | 
110 | print(f"Map saved as {map_path}")
111 | 
112 | 
113 | @app.route("/static/images/emissions_map.html")
114 | def serve_emissions_map():
115 |     return send_from_directory("static/images", "emissions_map.html")
116 | 
117 | 
118 | @app.route("/emissions_map")
119 | def emissions_map():
120 |     return render_template("maps.html")
121 | 
122 | 
123 | @app.route("/firstpage")
124 | def firstpage():
125 |     return render_template("firstpage.html")
126 | 
127 | 
128 | @app.route("/instructions")
129 | def instructions():
130 |     return render_template("instructions.html")
131 | 
132 | 
133 | @app.route("/instructionspremium")
134 | def instructionspremium():
135 |     return render_template("instructionspremium.html")
136 | 
137 | 
138 | def normalize_name(name):
139 |     """Normalize company name for better matching."""
140 |     name = name.strip().upper()
141 | 
142 |     # Remove common suffixes
143 |     name = re.sub(r"[.,'’]", "", name)  # Remove punctuation
144 |     name = re.sub(
145 |         r"\b(INC|LTD|CO|CORPORATION|CORP|LLC|GROUP|HOLDINGS|PLC)\b", "", name
146 |     )  # Remove suffixes
147 |     name = re.sub(r"\s+", " ", name).strip()  # Remove extra spaces
148 | 
149 |     print(f"[DEBUG] Normalized name: '{name}'")  # Debugging output
150 |     return name
151 | 
152 | 
153 | @app.route("/get_news", methods=["POST"])
154 | def get_news_route():
155 |     company_name = request.form.get("company_name")
156 |     if not company_name:
157 |         return jsonify({"error": "Please enter a company name."}), 400
158 | 
159 |     news_data = get_news(company_name)
160 | 
161 |     print(f"News data for {company_name}: {news_data}")
162 | 
163 |     return jsonify(
164 |         {
165 |             "company_name": company_name,
166 |             "news_data": news_data,
167 |         }
168 |     )
169 | 
170 | 
171 | def format_news(raw_news):
172 |     """Helper function to format news data correctly, including images."""
173 |     if not raw_news or not isinstance(raw_news, list):
174 |         print("[ERROR] News data is empty or not a list")
175 |         return []
176 | 
177 |     news_data = []
178 |     for article in raw_news:
179 |         try:
180 |             content = article.get("content", {})
181 |             if not isinstance(content, dict):
182 |                 print(f"[ERROR] Invalid content format: {content}")
183 |                 continue
184 | 
185 |             title = content.get("title", "No title available")
186 |             publisher = content.get("provider", {}).get("displayName", "Unknown source")
187 | 
188 |             # Extract the news link
189 |             link_data = content.get("clickThroughUrl") or content.get("canonicalUrl")
190 |             link = link_data.get("url") if isinstance(link_data, dict) else "#"
191 | 
192 |             # Extract the image URL
193 |             image_url = (
194 |                 content.get("thumbnail", {}).get("resolutions", [{}])[0].get("url", "")
195 |             )
196 | 
197 |             news_data.append(
198 |                 {
199 |                     "title": title,
200 |                     "publisher": publisher,
201 |                     "link": link,
202 |                     "image": image_url,  # Add image URL
203 |                 }
204 |             )
205 |         except Exception as e:
206 |             print(f"[ERROR] Error formatting news article: {e}")
207 | 
208 |     return news_data
209 | 
210 | 
211 | TICKER_CSV_PATH = "src/company_names_tickers_news.csv"
212 | 
213 | 
214 | # Function to load tickers from CSV file
215 | def load_ticker_map(csv_path):
216 |     ticker_map = {}
217 |     isin_map = {}
218 | 
219 |     try:
220 |         with open(csv_path, mode="r", encoding="utf-8") as file:
221 |             reader = csv.DictReader(file)
222 |             headers = [header.strip().upper() for header in reader.fieldnames]
223 | 
224 |             if (
225 |                 not headers
226 |                 or "COMPANY NAME" not in headers
227 |                 or "SYMBOL" not in headers
228 |                 or "ISIN NUMBER" not in headers
229 |             ):
230 |                 print(f"[ERROR] CSV file is missing required headers: {headers}")
231 |                 return {}, {}
232 | 
233 |             for row in reader:
234 |                 company = normalize_name(
235 |                     row["Company Name"]
236 |                 )  # Normalize before storing
237 |                 ticker = row["Symbol"].strip().upper()
238 |                 isin = row["ISIN Number"].strip().upper()
239 | 
240 |                 if company and ticker:
241 |                     ticker_map[company] = ticker
242 |                 if isin and ticker:
243 |                     isin_map[isin] = ticker
244 | 
245 |         print(f"[DEBUG] Ticker map loaded with {len(ticker_map)} entries")
246 |         print(f"[DEBUG] ISIN map loaded with {len(isin_map)} entries")
247 | 
248 |     except Exception as e:
249 |         print(f"[ERROR] Failed to load ticker map: {e}")
250 | 
251 |     return ticker_map, isin_map
252 | 
253 | 
254 | # Load at startup
255 | MANUAL_TICKER_MAP, MANUAL_ISIN_MAP = load_ticker_map(TICKER_CSV_PATH)
256 | 
257 | 
258 | def get_ticker(identifier):
259 |     """Retrieve the stock ticker symbol for a given company name or ISIN."""
260 |     identifier = normalize_name(identifier)  # Normalize user input
261 | 
262 |     print(f"[DEBUG] Normalized identifier: '{identifier}'")
263 | 
264 |     # First, check if it's an ISIN
265 |     if identifier in MANUAL_ISIN_MAP:
266 |         print(f"[DEBUG] Found ticker in ISIN map: {MANUAL_ISIN_MAP[identifier]}")
267 |         return MANUAL_ISIN_MAP[identifier]
268 | 
269 |     # Second, check if it's an exact company name match
270 |     if identifier in MANUAL_TICKER_MAP:
271 |         print(f"[DEBUG] Found ticker in company map: {MANUAL_TICKER_MAP[identifier]}")
272 |         return MANUAL_TICKER_MAP[identifier]
273 | 
274 |     # Third, try to find a close match in the manual map
275 |     for stored_name, ticker in MANUAL_TICKER_MAP.items():
276 |         if identifier in stored_name or stored_name in identifier:
277 |             print(f"[DEBUG] Found ticker by fuzzy match: {stored_name} -> {ticker}")
278 |             return ticker
279 | 
280 |     print(f"[DEBUG] {identifier} not found in manual maps, searching Yahoo Finance...")
281 | 
282 |     # If no match, try to query Yahoo Finance
283 |     try:
284 |         search_results = yf.Ticker(identifier)
285 |         if search_results.history(period="1d").empty:
286 |             print(f"[DEBUG] No historical data found for: {identifier}")
287 |             return None
288 | 
289 |         print(f"[DEBUG] Found ticker dynamically: {search_results.ticker}")
290 |         return search_results.ticker
291 |     except Exception as e:
292 |         print(f"[ERROR] Error retrieving ticker: {e}")
293 |         return None
294 | 
295 | 
296 | def get_news(company_name):
297 |     try:
298 |         ticker_symbol = get_ticker(company_name)
299 |         if not ticker_symbol:
300 |             print(f"[DEBUG] No ticker found for {company_name}")
301 |             return []
302 | 
303 |         ticker = yf.Ticker(ticker_symbol)
304 |         raw_news = ticker.news
305 | 
306 |         if not isinstance(
307 |             raw_news, list
308 |         ):  # Ensure raw_news is a list before processing
309 |             print(
310 |                 f"[ERROR] Unexpected news format for {ticker_symbol}: {type(raw_news)}"
311 |             )
312 |             return []
313 | 
314 |         print(f"[DEBUG] Raw news data for {ticker_symbol}: {raw_news}")
315 | 
316 |         return format_news(raw_news)
317 | 
318 |     except Exception as e:
319 |         print(f"[ERROR] Error retrieving news: {e}")
320 |         return []
321 | 
322 | 
323 | print(get_news("Apple"))
324 | 
325 | 
326 | @app.route("/download_table")
327 | def download_table():
328 |     """Generate and serve the emissions data as a CSV file for download."""
329 |     company_name = request.args.get("company_name")
330 |     parser = TableParsers.DOCLING
331 | 
332 |     if not company_name:
333 |         return "Company name is required!", 400
334 | 
335 |     data, report_url = get_emissions_data(company_name, idType="name", parser=parser)
336 | 
337 |     if not isinstance(data, pd.DataFrame) or data.empty:
338 |         return "No data available for download.", 404
339 | 
340 |     csv_buffer = BytesIO()
341 |     data.to_csv(csv_buffer, index=False)
342 |     csv_buffer.seek(0)
343 | 
344 |     return send_file(
345 |         csv_buffer,
346 |         mimetype="text/csv",
347 |         as_attachment=True,
348 |         download_name=f"{company_name}_emissions.csv",
349 |     )
350 | 
351 | 
352 | stop_rag_event = Event()
353 | 
354 | 
355 | ################################################################
356 | # 1) Tables on the left
357 | ################################################################
358 | @app.route("/index", methods=["GET", "POST"])
359 | def home():
360 |     """
361 |     Updated route to handle form submissions for a new company,
362 |     re-run LLM extraction, and pass data to index.html for the
363 |     chatbot, chart, and extracted tables.
364 |     """
365 |     company_name = None
366 |     report_url = None
367 |     llm_markdown = ""
368 |     pdf_path = None
369 | 
370 |     if request.method == "POST":
371 |         # Force-stop any old RAG job
372 |         rag_utils.stop_rag_event.set()
373 | 
374 |         # Clear out old chain
375 |         rag_utils.rag_chain = None
376 |         rag_utils.rag_initialized = False
377 | 
378 |         # Normal "search" logic
379 |         company_name = request.form.get("company_name", "").strip()
380 |         selected_id_type = request.form.get("idType", "name")
381 | 
382 |         if company_name:
383 |             parser = TableParsers.DOCLING
384 |             df, pdf_path = get_emissions_data_pro(
385 |                 company_name, selected_id_type, parser
386 |             )
387 |             if not df.empty and "LLM_Output" in df.columns:
388 |                 llm_markdown = df["LLM_Output"].iloc[0]
389 |             else:
390 |                 llm_markdown = "No emissions data found for this company."
391 | 
392 |             # Store the PDF path in rag_utils
393 |             rag_utils.pdf_path_global = pdf_path
394 | 
395 |             esg_reports = ESGReports(CompanyProfile(company_name, selected_id_type))
396 |             print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging
397 | 
398 |             # Extract the first available report URL
399 |             if esg_reports.urls:
400 |                 report_url = next(
401 |                     iter(esg_reports.urls.values())
402 |                 )  # Get first URL dynamically
403 | 
404 |             print(f"DEBUG: Selected Report URL -> {report_url}")
405 | 
406 |     return render_template(
407 |         "index.html",
408 |         company_name=company_name,
409 |         report_url=report_url,
410 |         llm_markdown=llm_markdown,
411 |     )
412 | 
413 | 
414 | ################################################################
415 | # 3) RAG Endpoints
416 | ################################################################
417 | @app.route("/rag_init", methods=["POST"])
418 | def rag_init():
419 |     """
420 |     Trigger RAG building in a background thread so it doesn't block.
421 |     """
422 |     if rag_utils.rag_chain is not None or rag_utils.rag_initialized:
423 |         return jsonify({"status": "RAG already initialized"})
424 | 
425 |     if not rag_utils.pdf_path_global or not os.path.isfile(rag_utils.pdf_path_global):
426 |         return jsonify({"status": "No valid original PDF to build RAG from."})
427 | 
428 |     # Clear the stop event
429 |     rag_utils.stop_rag_event.clear()
430 | 
431 |     def init_rag_in_background(path):
432 |         logging.info("Starting RAG initialization in background...")
433 |         try:
434 |             if rag_utils.stop_rag_event.is_set():
435 |                 logging.info("Stop event was set before starting RAG initialization")
436 |                 return
437 |             chain = rag_utils.build_final_system(path)
438 |             if rag_utils.stop_rag_event.is_set() or chain is None:
439 |                 logging.info(
440 |                     "Stop event was set during RAG initialization or chain creation failed"
441 |                 )
442 |                 return
443 |             rag_utils.rag_chain = chain
444 |             rag_utils.rag_initialized = True
445 |             logging.info("RAG system successfully initialized.")
446 |         except Exception as e:
447 |             logging.error(f"Failed to build RAG: {e}")
448 |             rag_utils.rag_chain = None
449 |             rag_utils.rag_initialized = False
450 | 
451 |     thread = threading.Thread(
452 |         target=init_rag_in_background, args=(rag_utils.pdf_path_global,)
453 |     )
454 |     thread.start()
455 | 
456 |     return jsonify({"status": "RAG initialization started"})
457 | 
458 | 
459 | @app.route("/ask", methods=["POST"])
460 | def ask_question():
461 |     """
462 |     POST route for user queries to the RAG.
463 |     """
464 |     question = request.form.get("question", "")
465 |     if not question:
466 |         return jsonify({"answer": "No question provided."})
467 | 
468 |     if not rag_utils.rag_chain or not rag_utils.rag_initialized:
469 |         return jsonify({"answer": "RAG is not initialized yet. Please wait."})
470 | 
471 |     try:
472 |         answer = rag_utils.rag_chain.invoke(question)
473 |         return jsonify({"answer": answer})
474 |     except Exception as e:
475 |         logging.error(f"Error in RAG QA: {e}")
476 |         return jsonify({"answer": f"Error: {str(e)}"})
477 | 
478 | 
479 | @app.route("/reset_rag", methods=["POST"])
480 | def reset_rag():
481 |     rag_utils.stop_rag_event.set()
482 |     rag_utils.rag_chain = None
483 |     rag_utils.rag_initialized = False
484 |     return jsonify({"status": "RAG reset"})
485 | 
486 | 
487 | df = pd.read_csv("src/company_names_tickers.csv")
488 | 
489 | unique_countries = sorted(df["Country"].dropna().astype(str).unique().tolist())
490 | unique_sectors = sorted(df["Sector"].dropna().astype(str).unique().tolist())
491 | unique_industries = sorted(df["Industry"].dropna().astype(str).unique().tolist())
492 | 
493 | 
494 | @app.route("/advanced_search")
495 | def advanced_search():
496 |     return render_template(
497 |         "advanced_search.html",
498 |         countries=unique_countries,
499 |         sectors=unique_sectors,
500 |         industries=unique_industries,
501 |         companies=[],
502 |         selected_company=None,
503 |         emissions_data=None,
504 |         report_url=None,
505 |     )
506 | 
507 | 
508 | @app.route("/submit", methods=["POST"])
509 | def submit():
510 |     # Retrieve form data
511 |     sector = request.form["sector"]
512 |     country = request.form["country"]
513 |     industry = request.form["industry"]
514 |     selected_company = request.form.get("company")  # Get the selected company
515 | 
516 |     filtered_df = df
517 |     if sector != "all":
518 |         filtered_df = filtered_df[filtered_df["Sector"] == sector]
519 |     if country != "all":
520 |         filtered_df = filtered_df[filtered_df["Country"] == country]
521 |     if industry != "all":
522 |         filtered_df = filtered_df[filtered_df["Industry"] == industry]
523 | 
524 |     selected_companies = filtered_df["Company Name"].drop_duplicates().tolist()
525 | 
526 |     report_url = None
527 |     emissions_data = None
528 |     if selected_company:
529 |         try:
530 |             parser = TableParsers.DOCLING
531 |             emissions_data, report_url = get_emissions_data(
532 |                 selected_company, idType="name", parser=parser
533 |             )
534 | 
535 |         except Exception as e:
536 |             print(f"Error retrieving emissions data for {selected_company}: {e}")
537 |             emissions_data = None
538 | 
539 |             esg_reports = ESGReports(CompanyProfile(selected_company, idType="name"))
540 |             print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging
541 | 
542 |             # Extract the first available report URL
543 |             if esg_reports.urls:
544 |                 report_url = next(
545 |                     iter(esg_reports.urls.values())
546 |                 )  # Get first URL dynamically
547 | 
548 |             print(f"DEBUG: Selected Report URL -> {report_url}")
549 | 
550 |     return render_template(
551 |         "advanced_search.html",
552 |         companies=selected_companies,
553 |         countries=unique_countries,
554 |         sectors=unique_sectors,
555 |         industries=unique_industries,
556 |         selected_company=selected_company,
557 |         report_url=report_url,
558 |         emissions_data=(
559 |             emissions_data.to_html(index=False) if emissions_data is not None else None
560 |         ),
561 |     )
562 | 
563 | 
564 | @app.route("/test", methods=["GET", "POST"])
565 | def test():
566 |     table_html = ""
567 |     report_url = None
568 |     company_name = ""
569 |     news_data = []
570 | 
571 |     if request.method == "POST":
572 |         company_name = request.form.get("company_name")  # Get the text input
573 |         parser = TableParsers.DOCLING
574 |         selected_id_type = request.form.get("idType", "name")
575 | 
576 |         if company_name:
577 |             result = get_emissions_data(
578 |                 company_name, idType=selected_id_type, parser=parser
579 |             )
580 | 
581 |             if isinstance(result, tuple) and len(result) == 2:
582 |                 data, report_url = result
583 |                 table_html = (
584 |                     data.to_html(index=False)
585 |                     if isinstance(data, pd.DataFrame) and not data.empty
586 |                     else "<p>No data found.</p>"
587 |                 )
588 |             else:
589 |                 # Handle cases where no data is returned
590 |                 data, report_url = None, None
591 |                 table_html = "<p>No data found.</p>"
592 | 
593 |     news_data = get_news(company_name)
594 | 
595 |     return render_template(
596 |         "test.html",
597 |         table_html=table_html,
598 |         report_url=report_url,
599 |         company_name=company_name,
600 |         news_data=news_data,
601 |     )
602 | 
603 | 
604 | @app.route("/progress/<socketid>", methods=["POST"])
605 | def progress(socketid):
606 |     def background_task():
607 |         for x in range(1, 6):  # Updates from 20% to 100%
608 |             socketio.emit("update_progress", {"progress": x * 20}, room=socketid)
609 |             socketio.sleep(5)  # Wait 5 seconds before sending the next update
610 | 
611 |         # Emit event when progress reaches 100%
612 |         socketio.emit("progress_complete", room=socketid)
613 | 
614 |     socketio.start_background_task(background_task)
615 |     return Response(status=204)
616 | 
617 | 
618 | @app.route("/register")
619 | def register():
620 |     return render_template("register.html")
621 | 
622 | 
623 | VALID_USERS = {"test@example.com": "password123"}
624 | 
625 | 
626 | @app.route("/login", methods=["GET", "POST"])
627 | def login():
628 |     if request.method == "POST":
629 |         email = request.form.get("email")
630 |         password = request.form.get("password")
631 | 
632 |         # Check credentials
633 |         if email in VALID_USERS and VALID_USERS[email] == password:
634 |             return redirect(url_for("home"))  # Redirects to the index page
635 | 
636 |         return render_template("login.html", error="Invalid email or password")
637 | 
638 |     return render_template("login.html")
639 | 
640 | 
641 | @app.route("/rag_status", methods=["GET"])
642 | def rag_status():
643 |     """
644 |     Returns whether the RAG system is initialized yet.
645 |     The front end can poll this to update the UI.
646 |     """
647 |     return jsonify({"initialized": rag_utils.rag_initialized})
648 | 
649 | 
650 | if __name__ == "__main__":
651 |     socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
```

.github/workflows/python-lint-and-test.yml
```
1 | # This workflow will install Python dependencies, run tests and lint with a single version of Python
2 | # For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
3 | 
4 | name: esg-data-retrieval
5 | 
6 | on:
7 |   push:
8 |     branches: [ "main" ]
9 |   pull_request:
10 |     branches: [ "main" ]
11 | 
12 | permissions:
13 |   contents: read
14 | 
15 | jobs:
16 |   build:
17 | 
18 |     runs-on: ubuntu-latest
19 | 
20 |     steps:
21 |     - uses: actions/checkout@v4
22 |     - name: Set up Python 3.10
23 |       uses: actions/setup-python@v3
24 |       with:
25 |         python-version: "3.10"
26 |     - name: Install dependencies
27 |       run: |
28 |         python -m pip install --upgrade pip
29 |         pip install isort black flake8 pytest
30 |         if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
31 |     - name: Lint with black
32 |       run: |
33 |         # stop build if any black errors spotted
34 |         black . --check
35 |     - name: Lint with flake8
36 |       run: |
37 |         # stop the build if there are Python syntax errors or undefined names
38 |         flake8 . --ignore=E501,W503
39 |     - name: Lint with isort
40 |       run: |
41 |         # stop build if any isort errors spotted
42 |         isort .
43 |     # - name: Test with pytest
44 |     #   run: |
45 |     #     pytest tests/ --verbose
```

data/cache/.gitkeep
```
```

data/cache/Units.csv
```
1 | Unnamed: 0,Unnamed: 1,FY20,FY21,FY22,FY23,Units
2 | 0,Revenue ($M),"143,015","168,088","198,270","211,915",Revenue
3 | 1,Scope 1,0.8,0.7,0.7,0.7,Revenue
4 | 2,Scope 2 (location-based),30.3,29.8,32.2,38.1,Revenue
5 | 3,Scope 2 (market-based),3.2,2.6,1.5,1.9,Revenue
6 | 4,Scope 3 (market-based) 1,81.5,82.3,81.3,78.4,Revenue
7 | 5,Scope 1 + 2 (location-based),31.1,30.5,32.9,38.8,Revenue
8 | 6,Scope 1 + 2 (market-based),4.0,3.3,2.2,2.6,Revenue
9 | 7,Scope 1 + 2 + 3 (market-based) 1,85.5,85.6,83.5,81.0,Revenue
```

data/cache/std_esg_data.csv
```
1 | Metric,2010,2021,2022,2023,Units
2 | Scope 1 Direct Emissions,"106,870","57,076","66,775","68,050",Metric tons CO2e
3 | Total Scope 1 and Location-Based Scope 2 Emissions,"1,785,417","658,982","701,285","678,063",Metric tons CO2e
4 | Reduction in Total Scope 1 and Location-Based Scope 2 Emissions,Not applicable,63%,61%,62%,Metric tons CO2e
5 | Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Metric tons CO2e
6 | Scope 1 Direct Emissions,"106,870","57,076","66,775","68,050",Metric tons CO2e
7 | Total Gross Scope 1 and Market-Based Scope 2 Emissions,"1,750,939","70,963","84,569","85,786",Metric tons CO2e
8 | Total Net Scope 1 and Market-Based Scope 2 Emissions,"1,750,939",0,0,0,Metric tons CO2e
9 | Reduction in Total Net Scope 1 and Market-Based Scope 2 Emissions,Not applicable,100%,100%,100%,Metric tons CO2e
10 | Total Scope 1 and Location-Based Scope 2 Emissions,"1,785,417","658,982","701,285","678,063",Metric tons CO2e
11 | Reduction in Total Scope 1 and Location-Based Scope 2 Emissions,Not applicable,63%,61%,62%,Metric tons CO2e
12 | Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Metric tons CO2e
13 | Total Gross Scope 1 and Market-Based Scope 2 Emissions,"1,750,939","70,963","84,569","85,786",Metric tons CO2e
14 | Total Net Scope 1 and Market-Based Scope 2 Emissions,"1,750,939",0,0,0,Metric tons CO2e
15 | Reduction in Total Net Scope 1 and Market-Based Scope 2 Emissions,Not applicable,100%,100%,100%,Metric tons CO2e
16 | Total Scope 1 and Location-Based Scope 2 Emissions,"1,785,417","658,982","701,285","678,063",Metric tons CO2e
17 | Reduction in Total Scope 1 and Location-Based Scope 2 Emissions,Not applicable,63%,61%,62%,Metric tons CO2e
18 | Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Metric tons CO2e
19 | Total Gross Scope 1 and Market-Based Scope 2 Emissions,"1,750,939","70,963","84,569","85,786",Metric tons CO2e
20 | Total Net Scope 1 and Market-Based Scope 2 Emissions,"1,750,939",0,0,0,Metric tons CO2e
21 | Reduction in Total Net Scope 1 and Market-Based Scope 2 Emissions,Not applicable,100%,100%,100%,Metric tons CO2e
22 | Location-Based Scope 2 Indirect Emissions,"1,678,547","601,906","634,510","610,013",Metric tons CO2e
23 | Total Scope 1 and Location-Based Scope 2 Emissions,"1,785,417","658,982","701,285","678,063",Metric tons CO2e
24 | Reduction in Total Scope 1 and Location-Based Scope 2 Emissions,Not applicable,63%,61%,62%,Metric tons CO2e
25 | Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Scope 1 and Market-Based Scope 2 Emissions,Metric tons CO2e
26 | Market-Based Scope 2 Indirect Emissions,"1,644,068","13,886","17,794","17,736",Metric tons CO2e
27 | Total Gross Scope 1 and Market-Based Scope 2 Emissions,"1,750,939","70,963","84,569","85,786",Metric tons CO2e
28 | Total Net Scope 1 and Market-Based Scope 2 Emissions,"1,750,939",0,0,0,Metric tons CO2e
29 | Reduction in Total Net Scope 1 and Market-Based Scope 2 Emissions,Not applicable,100%,100%,100%,Metric tons CO2e
```

tests/src/__init__.py
```
```

src/extract/__init__.py
```
```

src/extract/filtered_data.py
```
1 | import os
2 | import re
3 | import sys
4 | 
5 | import pandas as pd
6 | from dotenv import load_dotenv
7 | from loguru import logger
8 | from pydantic import BaseModel
9 | 
10 | load_dotenv()
11 | sys.path.append(os.getenv("ROOT_DIR"))
12 | 
13 | from src.utils.data_models import TableParsers  # noqa: E402
14 | from src.utils.standardize_table import standardize_table  # noqa: E402
15 | from src.utils.units import get_units_raw_input, infer_units_for_rows  # noqa: E402
16 | 
17 | if not sys.warnoptions:
18 |     import warnings
19 | 
20 |     warnings.simplefilter("ignore")
21 | 
22 | 
23 | class Filter(BaseModel):
24 |     # Regex to match 'Scope 1', 'Scope 2', and 'Scope 3'
25 |     regex_scope1: str = r"Scope\s1"
26 |     regex_scope2: str = r"Scope\s2"
27 |     regex_scope3: str = r"Scope\s3"
28 | 
29 |     # Regex to exclude rows with words like 'excluded' or 'avoided'
30 |     regex_exclude: str = (
31 |         r"(excluded|Excluded|avoided|Avoided|aim|Aim|goal|Goal|target|Target|forecast|Forecast|estimate|Estimate|projection|Projection|expectation|Expectation)"
32 |     )
33 | 
34 |     # Regex to match columns with various date formats
35 |     regex_date: str = r"(\bFY\d{2}\b|\b20\d{2}\b|\b[Ff]iscal\s[Yy]ear\b)"
36 | 
37 |     directory_path: str
38 |     parser: TableParsers
39 | 
40 |     filtered_df: pd.DataFrame = None
41 | 
42 |     class Config:
43 |         arbitrary_types_allowed = True
44 | 
45 |     def _load_dfs(self):
46 |         dfs = []
47 |         for filename in os.listdir(
48 |             os.path.join(self.directory_path, self.parser.value)
49 |         ):
50 |             if filename.endswith(".csv"):
51 |                 file_path = os.path.join(
52 |                     self.directory_path, self.parser.value, filename
53 |                 )
54 |                 df = pd.read_csv(file_path)
55 |                 dfs.append(df)
56 |         return dfs
57 | 
58 |     def extract_filtered_df(self):
59 |         docling_tables = self._load_dfs()
60 |         dfs = self._append_units_column(docling_tables)
61 |         filtered_dfs = self._filter_data_v2(dfs)
62 |         # dfs_to_concat = [df for df in filtered_dfs if df is not None]
63 |         # filtered_dfs = self._filter_for_scope(dfs)
64 |         # concatenated_df = self._filter_for_figures(filtered_dfs)
65 |         inferred_df = self._infer_units(pd.concat(filtered_dfs, ignore_index=True))
66 |         final_df = self._standardise_df(inferred_df)
67 | 
68 |         self.filtered_df = final_df
69 | 
70 |     def _append_units_column(self, docling_tables: list[pd.DataFrame]):
71 |         dfs = []
72 |         for df in docling_tables:
73 |             dfs.append(get_units_raw_input(df))
74 |         return dfs
75 | 
76 |     def _filter_data_v2(self, dfs: list[pd.DataFrame]):
77 |         scope_data = []
78 |         for idx, df in enumerate(dfs):
79 |             try:
80 |                 # Checks if scope 1 exists in table
81 |                 contains_scope1 = df.apply(
82 |                     lambda row: row.str.contains(
83 |                         self.regex_scope1, regex=True, na=False
84 |                     ).any(),
85 |                     axis=1,
86 |                 ).any()
87 |                 # Checks if scope 2 exists in table
88 |                 contains_scope2 = df.apply(
89 |                     lambda row: row.str.contains(
90 |                         self.regex_scope3, regex=True, na=False
91 |                     ).any(),
92 |                     axis=1,
93 |                 ).any()
94 | 
95 |                 if not (contains_scope1 and contains_scope2):
96 |                     print(
97 |                         f"Skipping file {idx} - does not contain both Scope 1 and Scope 2."
98 |                     )
99 |                     continue
100 | 
101 |                 # **Step 2: Remove rows where both 'Scope 1' and 'Scope 3' appear in the same row**
102 |                 scope1_and_scope3 = df.apply(
103 |                     lambda row: row.str.contains(
104 |                         self.regex_scope1, regex=True, na=False
105 |                     ).any()
106 |                     and row.str.contains(self.regex_scope3, regex=True, na=False).any(),
107 |                     axis=1,
108 |                 )
109 |                 df = df[~scope1_and_scope3]  # Remove those rows
110 | 
111 |                 # Checks if scope 3 exists in table
112 |                 contains_scope3 = df.apply(
113 |                     lambda row: row.str.contains(
114 |                         self.regex_scope3, regex=True, na=False
115 |                     ).any(),
116 |                     axis=1,
117 |                 ).any()
118 | 
119 |                 # Check if the table has a date column in the header
120 |                 date_columns = [
121 |                     col for col in df.columns if re.search(self.regex_date, str(col))
122 |                 ]
123 |                 if not date_columns:
124 |                     print(
125 |                         f"Skipping file {idx} as it has no date-related columns in the header."
126 |                     )
127 |                     continue
128 | 
129 |                 # Remove rows that contain excluded words
130 |                 df = df[
131 |                     ~df.astype(str).apply(
132 |                         lambda row: row.str.contains(
133 |                             self.regex_exclude, regex=True, na=False
134 |                         ).any(),
135 |                         axis=1,
136 |                     )
137 |                 ]
138 | 
139 |                 # Convert all columns to strings to avoid dtype issues
140 |                 df = df.astype(str)
141 | 
142 |                 if contains_scope3:
143 |                     # Find the index where 'Scope 3' appears and remove it and all rows below
144 |                     scope3_index = df.apply(
145 |                         lambda row: row.str.contains(
146 |                             self.regex_scope3, regex=True, na=False
147 |                         ).any(),
148 |                         axis=1,
149 |                     )
150 |                     if contains_scope3 and scope3_index.any():
151 |                         first_scope3_idx = scope3_index[scope3_index].index[
152 |                             0
153 |                         ]  # First occurrence
154 |                         df = df.loc[: first_scope3_idx - 1]  # Keep only rows above it
155 | 
156 |                 if contains_scope1:
157 |                     # Find the index where 'Scope 1' appears and remove all rows above it (excluding date rows)
158 |                     scope1_index = df.apply(
159 |                         lambda row: row.str.contains(
160 |                             self.regex_scope1, regex=True, na=False
161 |                         ).any(),
162 |                         axis=1,
163 |                     )
164 |                     if contains_scope1 and scope1_index.any():
165 |                         first_scope1_idx = scope1_index[scope1_index].index[
166 |                             0
167 |                         ]  # First occurrence
168 |                         df = df.loc[first_scope1_idx:]  # Keep 'Scope 1' row and below
169 | 
170 |                 # Store processed data
171 |                 scope_data.append(df)
172 | 
173 |             except Exception as e:
174 |                 logger.warning(f"Error processing df {idx}: {e}")
175 |                 continue
176 |         return scope_data
177 | 
178 |     def _filter_for_scope(self, dfs: list[pd.DataFrame]):
179 |         filtered_dfs = []
180 |         for df in dfs:
181 |             # Check if the table has a date column in the header
182 |             date_columns = [
183 |                 col for col in df.columns if re.search(self.regex_date, str(col))
184 |             ]
185 |             if not date_columns:
186 |                 continue  # Skip files without date columns
187 | 
188 |             filtered_df = df[
189 |                 df.apply(
190 |                     lambda row: row.astype(str)
191 |                     .str.contains(self.regex_scope, regex=True)
192 |                     .any(),
193 |                     axis=1,
194 |                 )
195 |             ]
196 |             filtered_df = filtered_df[
197 |                 ~filtered_df.apply(
198 |                     lambda row: row.astype(str)
199 |                     .str.contains(self.regex_exclude, regex=True)
200 |                     .any(),
201 |                     axis=1,
202 |                 )
203 |             ]
204 |             filtered_dfs.append(filtered_df)
205 |         return filtered_dfs
206 | 
207 |     def _filter_for_figures(self, dfs: list[pd.DataFrame]):
208 |         concatenated_df = pd.concat(dfs)
209 | 
210 |         # Identify the last column containing date-like information
211 |         date_columns = [
212 |             col
213 |             for col in concatenated_df.columns
214 |             if re.search(self.regex_date, str(col))
215 |         ]
216 | 
217 |         if date_columns:
218 |             # Find the index of the last date column
219 |             last_date_col_index = concatenated_df.columns.get_loc(date_columns[-1])
220 |             # Keep only columns up to and including the last date column
221 |             combined_scope_data = concatenated_df.iloc[:, : last_date_col_index + 1]
222 |             # add units column
223 |             combined_scope_data["Units"] = concatenated_df["Units"]
224 | 
225 |         # Drop the first column if necessary
226 |         if not combined_scope_data.empty and len(combined_scope_data.columns) > 0:
227 |             if combined_scope_data.columns[0] == "Unnamed: 0":
228 |                 combined_scope_data = combined_scope_data.iloc[:, 1:]
229 | 
230 |         # Drop empty columns
231 |         combined_scope_data = combined_scope_data.dropna(axis=1, how="all")
232 |         # Drop empty rows
233 |         combined_scope_data = combined_scope_data.dropna(how="all")
234 |         return combined_scope_data
235 | 
236 |     def _infer_units(self, df: pd.DataFrame):
237 |         inferred_df = infer_units_for_rows(df)
238 |         return inferred_df
239 | 
240 |     def _standardise_df(self, df: pd.DataFrame):
241 |         standard = standardize_table(df)
242 |         return standard
243 | 
244 | 
245 | if __name__ == "__main__":
246 |     ROOT_DIR = os.getenv("ROOT_OUTPUT_PATH")
247 |     filter_obj = Filter(
248 |         directory_path=os.path.join(ROOT_DIR, "META_PLATFORMS_INC-CLASS_A"),
249 |         parser=TableParsers.DOCLING,
250 |     )
251 |     filter_obj.extract_filtered_df()
252 | 
253 |     filter_obj.filtered_df.to_csv(os.path.join(ROOT_DIR, "testing_meta.csv"))
```

src/extract/llama.py
```
1 | """
2 | Scope 1 and 2 (location and market based) Emissions Extractor (llama)
3 | """
4 | 
5 | import json
6 | import os
7 | import re
8 | import sys
9 | from datetime import datetime
10 | 
11 | import pandas as pd
12 | from dotenv import load_dotenv
13 | from llama_parse import LlamaParse
14 | from loguru import logger
15 | from pydantic import BaseModel
16 | 
17 | # Load environment variables from .env file
18 | load_dotenv()
19 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
20 | LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")
21 | 
22 | 
23 | class LlamaExtractor(BaseModel):
24 |     api_key: str = LLAMA_API_KEY
25 | 
26 |     company_name: str
27 |     filtered_pdf_path: str
28 |     output_path: str
29 | 
30 |     def process_company(self):
31 |         # Main entry point: downloads PDF, identifies relevant pages, parses them, saves raw output, updates CSV.
32 |         logger.info(f"Processing company: {self.company_name}")
33 | 
34 |         emissions_data = self.extract_emissions_data(
35 |             self.filtered_pdf_path, self.company_name
36 |         )
37 |         if not emissions_data:
38 |             logger.warning(f"Parsing returned no data for {self.company_name}")
39 |             return
40 | 
41 |         output_path = f"{self.output_path}/esg_data.csv"
42 |         logger.info("Writing to CSV...")
43 |         # 5) Update CSV with extracted data
44 |         df = self.update_csv(self.company_name, emissions_data, output_path)
45 |         return df
46 | 
47 |     # Actually runs the LlamaParse logic on the relevant pages,
48 |     # and merges JSON blocks to find the best data
49 |     def extract_emissions_data(
50 |         self, pdf_file: str, company_name: str
51 |     ):  # -> tuple[dict | None, list]:
52 | 
53 |         try:
54 |             parser = LlamaParse(
55 |                 api_key=self.api_key,
56 |                 result_type="markdown",
57 |                 verbose=False,
58 |                 language="en",
59 |                 num_workers=4,
60 |                 table_extraction_mode="full",
61 |                 # target_pages=page_indices_str,
62 |                 parsing_instruction="""
63 |                 This is a company sustainability report. Extract Scope 1 and Scope 2 emissions data for all available years with units.
64 |                 For Scope 2, note if it's "market-based" or "location-based."
65 |                 If no data is available for a category, use null.
66 |                 Return a single JSON object:
67 |                 {
68 |                   "scope1": {"year": [value, unit]},
69 |                   "scope2_market": {"year": [value, unit]},
70 |                   "scope2_location": {"year": [value, unit]}
71 |                 }
72 |                 """,
73 |                 is_formatting_instruction=True,
74 |             )
75 | 
76 |             documents = parser.load_data(
77 |                 pdf_file,
78 |                 extra_info={
79 |                     "file_name": f"{company_name}.pdf",
80 |                     "processed_date": datetime.now().isoformat(),
81 |                 },
82 |             )
83 | 
84 |             final_data = self._combine_document_data(documents)
85 |             return final_data
86 | 
87 |         except Exception as exc:
88 |             logger.error(f"extract_emissions_data error for {company_name}: {exc}")
89 |             return None, []
90 | 
91 |     # Walks through each LlamaParse "document" output,
92 |     # looking for JSON code blocks and scoring them
93 |     def _combine_document_data(self, documents: list) -> dict:
94 |         best_data = None
95 |         max_points = 0
96 |         code_fence_pattern = re.compile(
97 |             r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE
98 |         )
99 |         year_pattern = re.compile(
100 |             r"^(?:FY)?\d{2,4}$"
101 |         )  # Matches FY20, 20, 2020, 1980, etc.
102 | 
103 |         for doc in documents:
104 |             content = doc.get_content()
105 |             if not content:
106 |                 continue
107 | 
108 |             blocks = code_fence_pattern.findall(content)
109 |             for block in blocks:
110 |                 try:
111 |                     data = json.loads(block.strip())
112 |                 except Exception as exc:
113 |                     logger.error(f"Failed to parse JSON block: {exc}")
114 |                     continue
115 | 
116 |                 # Skip if any keys contain non-year data
117 |                 is_year_based = True
118 |                 for scope_key in ["scope1", "scope2_market", "scope2_location"]:
119 |                     scope_dict = data.get(scope_key, {})
120 |                     if isinstance(scope_dict, dict):
121 |                         for year in scope_dict.keys():
122 |                             if not year_pattern.match(str(year)):
123 |                                 is_year_based = False
124 |                                 break
125 |                     if not is_year_based:
126 |                         break
127 | 
128 |                 if not is_year_based:
129 |                     continue
130 | 
131 |                 # Score the data by counting entries with valid numeric value + unit pairs
132 |                 current_points = 0
133 |                 for scope_key in ["scope1", "scope2_market", "scope2_location"]:
134 |                     scope_dict = data.get(scope_key, {})
135 |                     if isinstance(scope_dict, dict):
136 |                         for year_data in scope_dict.values():
137 |                             if (
138 |                                 isinstance(year_data, list)
139 |                                 and len(year_data) == 2
140 |                                 and year_data[0] is not None
141 |                                 and year_data[1] is not None
142 |                             ):
143 |                                 current_points += 1
144 | 
145 |                 if current_points > max_points:
146 |                     best_data = data
147 |                     max_points = current_points
148 |                     logger.debug(f"New best data found with {current_points} points")
149 | 
150 |         if not best_data:
151 |             return {"scope1": {}, "scope2_market": {}, "scope2_location": {}}
152 |         return best_data
153 | 
154 |     # Appends emissions data (company, year, scope1_value, scope1_unit, scope2_location_value, scope2_location_unit, scope2_market_value, scope2_market_unit) to CSV
155 |     def update_csv(self, company_name: str, emissions_data: dict, csv_path: str):
156 |         try:
157 |             s1_dict = emissions_data.get("scope1", {})
158 |             s2m_dict = emissions_data.get("scope2_market", {})
159 |             s2l_dict = emissions_data.get("scope2_location", {}) or {}
160 | 
161 |             standard_df = pd.DataFrame()
162 |             standard_df["Metric"] = [
163 |                 "Scope 1",
164 |                 "Scope 2 (market-based)",
165 |                 "Scope 2 (location-based)",
166 |             ]
167 |             # Gather all years
168 |             all_years = (
169 |                 set(s1_dict.keys()) | set(s2m_dict.keys()) | set(s2l_dict.keys())
170 |             )
171 |             logger.info(all_years)
172 |             # Crete empty dataframe with columns metric, all years units
173 |             for year in sorted(all_years):
174 |                 s1 = s1_dict.get(year, [None, None])
175 |                 s2m = s2m_dict.get(year, [None, None])
176 |                 s2l = s2l_dict.get(year, [None, None])
177 | 
178 |                 # Ensure each is [val, unit]
179 |                 if not isinstance(s1, list) or len(s1) != 2:
180 |                     s1 = [None, None]
181 |                 if not isinstance(s2m, list) or len(s2m) != 2:
182 |                     s2m = [None, None]
183 |                 if not isinstance(s2l, list) or len(s2l) != 2:
184 |                     s2l = [None, None]
185 | 
186 |                 standard_df[year] = [s1[0], s2m[0], s2l[0]]
187 | 
188 |             try:
189 |                 standard_df["Units"] = [
190 |                     (s1_dict.get(max(all_years)))[1],
191 |                     s2m_dict.get(max(all_years))[1],
192 |                     s2l_dict.get(max(all_years))[1],
193 |                 ]
194 |             except Exception:
195 |                 if s1_dict.get(max(all_years))[1] is not None:
196 |                     standard_df["Units"] = s1_dict.get(max(all_years))[1]
197 |                 else:
198 |                     standard_df["Units"] = None
199 |             standard_df.to_csv(csv_path, index=False)
200 | 
201 |             logger.info(f"Appended new results to {csv_path}")
202 | 
203 |             return standard_df
204 |         except Exception:
205 |             logger.info("Error parsing with LlamaParse. Returning empty dataframe.")
206 |             return pd.DataFrame()
207 | 
208 | 
209 | # Main script entry point
210 | if __name__ == "__main__":
211 |     if not LLAMA_API_KEY:
212 |         raise ValueError("Missing LLAMA_API_KEY in environment variables.")
213 | 
214 |     company_arg = "META"
215 |     pdf_url_arg = "https://sustainability.fb.com/wp-content/uploads/2023/07/Meta-2023-Sustainability-Report-1.pdf"
216 | 
217 |     extractor = LlamaExtractor(LLAMA_API_KEY)
218 |     extractor.process_company(company_arg, pdf_url_arg)
```

src/extract/news.py
```
1 | """
2 | # TODO (iman / esther)
3 | - use yfinance OR serpapi to get latest news for company (use name or ISIN)
4 | """
```

src/extract/pdf.py
```
1 | """
2 | Methods for parsing full pdf documents
3 | 
4 | NOTE: NOT TESTED YET!
5 | DOCUMENTATION: https://docs.cloud.llamaindex.ai/llamaparse/getting_started/python
6 | """
7 | 
8 | import os
9 | import sys
10 | 
11 | from dotenv import load_dotenv
12 | from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
13 | from llama_parse import LlamaParse
14 | from loguru import logger
15 | 
16 | load_dotenv()
17 | 
18 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
19 | 
20 | from src.utils.data_models import PDFParsers  # noqa: E402
21 | 
22 | 
23 | class PDFAgent:
24 | 
25 |     def __init__(self, file_path: str, parser: PDFParsers = PDFParsers.LLAMA_PARSE):
26 |         self.file_path = file_path
27 |         self.parser = parser.value
28 |         self.llama_api_key = os.getenv("LLAMA_API_KEY")  # get from .env
29 |         self.parsed_pdf = None
30 | 
31 |     def parse(self):
32 |         if self.parser == PDFParsers.LLAMA_PARSE.value:
33 |             parsed_pdf = self._parse_with_llama()
34 |             self.parsed_pdf = parsed_pdf
35 |             return parsed_pdf
36 |         else:
37 |             logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
38 |             return None
39 | 
40 |     def query(self, query: str):
41 |         if self.parser == PDFParsers.LLAMA_PARSE.value:
42 |             response = self._query_with_llama(query)
43 |             return response
44 |         else:
45 |             logger.warning(f"Invalid parser specified: {self.parser}. Returning None.")
46 |             return None
47 | 
48 |     def _parse_with_llama(self) -> str | None:
49 |         try:
50 |             # set up parser
51 |             parser = LlamaParse(
52 |                 api_key=self.api_key,
53 |                 language="en",
54 |                 result_type="markdown",
55 |             )
56 | 
57 |             # use SimpleDirectoryReader to parse file
58 |             file_extractor = {".pdf": parser}
59 |             documents = SimpleDirectoryReader(
60 |                 input_files=[self.file_path], file_extractor=file_extractor
61 |             ).load_data()
62 | 
63 |             parsed_content = "\n\n---\n\n".join(
64 |                 [doc.get_content() for doc in documents]
65 |             )
66 |             return parsed_content
67 | 
68 |         except Exception as exc:
69 |             logger.error(
70 |                 f"Unable to parse document with Llama - {self.file_path}: {exc}"
71 |             )
72 |             return None
73 | 
74 |     def _query_with_llama(self, query: str):
75 |         parsed_pdf = self.parsed_pdf if self.parsed_pdf is not None else self.parse()
76 |         if parsed_pdf is not None:
77 |             index = VectorStoreIndex.from_documents(parsed_pdf)
78 |             query_engine = index.as_query_engine()
79 |             response = query_engine.query(query)
80 |             return response
81 |         else:
82 |             return f"Unable to parse file {self.file_path}. Try again later!"
```

src/extract/tables.py
```
1 | """
2 | Methods for extracting emissions tables from ESG report using PyPDF and Docling
3 | """
4 | 
5 | import os
6 | import re
7 | import sys
8 | from datetime import datetime
9 | from pathlib import Path
10 | from typing import List, Union
11 | 
12 | import pandas as pd
13 | import tabula
14 | from docling.document_converter import DocumentConverter
15 | from dotenv import load_dotenv
16 | from loguru import logger
17 | from PyPDF2 import PdfReader, PdfWriter
18 | 
19 | from src.find.company_profile import CompanyProfile
20 | 
21 | load_dotenv()
22 | 
23 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
24 | 
25 | from src.utils.data_models import Company, RegexPatterns, TableParsers  # noqa: E402
26 | 
27 | 
28 | class TableExtractor:
29 |     """
30 |     Methods for extracting tables from PDF using docling or tabula
31 |     """
32 | 
33 |     def __init__(
34 |         self,
35 |         company: CompanyProfile,
36 |         file_path: str,
37 |         parser: Union[TableParsers, List[TableParsers]],
38 |         output_path: str,
39 |     ):
40 |         self.company = company
41 |         self.file_path = file_path
42 |         self.file_name = os.path.basename(file_path).replace(".pdf", "")
43 |         self.output_dir = output_path
44 |         self.parser = parser.value
45 | 
46 |         # create output dir
47 |         os.makedirs(self.output_dir, exist_ok=True)
48 | 
49 |     def extract(self):
50 |         """
51 |         1. Returns list of extracted tables as pandas dataframes
52 |         2. Saves tables to cache
53 |         """
54 | 
55 |         if isinstance(self.parser, List):
56 |             all_tables = []
57 |             for parser in self.parser:
58 |                 logger.info(f"Extracting data for {parser.value}")
59 |                 logger.info(datetime.now())
60 |                 # create output dir (if it doesn't exist)
61 |                 output_dir_parser = Path(f"{self.output_dir}/{parser}")
62 |                 output_dir_parser.mkdir(parents=True, exist_ok=True)
63 |                 # extract and save tables
64 |                 tables = self._extract(parser)
65 |                 self._save_tables(tables, output_dir_parser)
66 |                 all_tables.append(tables)
67 |         else:
68 |             # extract tables
69 |             all_tables = self._extract(self.parser)
70 |             output_dir_parser = Path(f"{self.output_dir}/{self.parser}")
71 |             output_dir_parser.mkdir(parents=True, exist_ok=True)
72 |             # save tables
73 |             self._save_tables(all_tables, output_dir_parser)
74 | 
75 |         return all_tables
76 | 
77 |     def _extract(self, parser):
78 |         """
79 |         Method for extracting tables for specified parser.
80 | 
81 |         Returns
82 |             emissions_tables (list[pd.DataFrame]): list of extracted tables
83 |         """
84 |         # Identify relevant pages
85 |         pdf = self._read_pdf()
86 |         pages, indeces = self._filter_pdf_pages(pdf)
87 |         if not pages:
88 |             logger.error(
89 |                 f"No relevant pages found for {self.company.name}. Returning None."
90 |             )
91 |             return None
92 | 
93 |         # parse document
94 |         if parser == TableParsers.DOCLING.value:
95 |             # write filtered pdf to cache
96 |             filtered_file_path = f"{self.output_dir}/{self.file_name}-filtered.pdf"
97 |             self._write_pages_to_pdf(pages, filtered_file_path)
98 |             # extract from filtered pdf
99 |             emissions_tables = self._extract_with_docling(filtered_file_path)
100 |             return emissions_tables
101 |         elif parser == TableParsers.TABULA.value:
102 |             emissions_tables = self._extract_with_tabula(indeces)
103 |             return emissions_tables
104 |         else:
105 |             logger.error(f"Invalid parsesr {self.parser} specified.")
106 |             return None
107 | 
108 |     def _extract_with_docling(self, file_path):
109 |         """
110 |         Extract tables using docling.
111 |         """
112 |         # parse document using docling
113 |         doc_converter = DocumentConverter()
114 |         conv_res = doc_converter.convert(file_path)
115 |         tables = [table.export_to_dataframe() for table in conv_res.document.tables]
116 |         return tables
117 | 
118 |     def _extract_with_tabula(self, page_indeces):
119 |         """
120 |         Extract tables using tabula.
121 |         """
122 |         tables = tabula.read_pdf(
123 |             self.file_path, pages=page_indeces, multiple_tables=True
124 |         )
125 |         return tables
126 | 
127 |     def _read_pdf(self):
128 |         """
129 |         Read PDF using PyPDF2.
130 | 
131 |         Returns
132 |             pages (list[PageObject]): list of page objects returned by PyPDF2
133 |         """
134 |         reader = PdfReader(self.file_path, strict=False)
135 |         return reader.pages
136 | 
137 |     def _write_pages_to_pdf(self, pages, path):
138 |         """
139 |         Write pages to pdf file.
140 | 
141 |         Args
142 |             pages (list[PageObject]): list of page objects to write to file
143 |             path (str): output file path to write pages to
144 |         """
145 |         writer = PdfWriter()
146 |         for page in pages:
147 |             writer.add_page(page)
148 |         with open(path, "wb") as file:
149 |             writer.write(file)
150 | 
151 |     def _save_tables(self, tables: Union[List[pd.DataFrame], None], output_dir):
152 |         """
153 |         Save tables to output dir
154 | 
155 |         Args
156 |             tables (list[pd.DataFrame]): list of tables to write to folder
157 |         """
158 |         if tables is None:
159 |             logger.error(f"No tables found for {self.company.isin}")
160 |             return None
161 | 
162 |         for idx, table in enumerate(tables):
163 |             # Save the table as csv
164 |             element_csv_filepath = os.path.join(
165 |                 output_dir, f"{self.file_name}-table-{idx + 1}.csv"
166 |             )
167 |             table.to_csv(element_csv_filepath)
168 | 
169 |     def _filter_pdf_pages(self, pdf_pages):
170 |         """
171 |         Locate pages that include relevant information.
172 | 
173 |         Args
174 |             pdf_pages (List[PageObject]): list of pages to filter
175 | 
176 |         Return
177 |             pages (List[PageObject]): list of pages that could include relevant information
178 |             indexed (List[int]): index of each page returned in pages list
179 |         """
180 |         pages = []
181 |         indeces = []
182 |         for idx, page in enumerate(pdf_pages):
183 |             try:
184 |                 page_text = page.extract_text().lower()
185 |                 if (
186 |                     re.search(RegexPatterns.SCOPE1.value, page_text, re.IGNORECASE)
187 |                     and re.search(RegexPatterns.SCOPE2.value, page_text, re.IGNORECASE)
188 |                     and any(
189 |                         [
190 |                             re.search(
191 |                                 RegexPatterns.YEAR_1.value, page_text, re.IGNORECASE
192 |                             ),
193 |                             re.search(
194 |                                 RegexPatterns.YEAR_2.value, page_text, re.IGNORECASE
195 |                             ),
196 |                         ]
197 |                     )
198 |                     and all(
199 |                         [
200 |                             re.search(
201 |                                 RegexPatterns.UNITS_1.value, page_text, re.IGNORECASE
202 |                             ),
203 |                             re.search(
204 |                                 RegexPatterns.UNITS_2.value, page_text, re.IGNORECASE
205 |                             ),
206 |                         ]
207 |                     )
208 |                 ):
209 |                     pages.append(page)
210 |                     indeces.append(idx)
211 |                     logger.debug(f"Page {idx} is relevant.")
212 |             except Exception as e:
213 |                 logger.warning(f"Unable to process page {idx}: {e}")
214 |         return pages, indeces
215 | 
216 | 
217 | if __name__ == "__main__":
218 |     company = Company(isin="US5949181045")
219 |     file_path = "data/cache/US5949181045/RW1lmju.pdf"
220 | 
221 |     extractor = TableExtractor(company, file_path, TableParsers.TABULA)
222 |     tables = extractor.extract()
223 |     logger.info(f"Emissions tables for {company.identifier} extracted!")
```

src/find/__init__.py
```
```

src/find/company_profile.py
```
1 | import os
2 | import sys
3 | import time
4 | 
5 | import requests
6 | from dotenv import load_dotenv
7 | from loguru import logger
8 | 
9 | load_dotenv()
10 | sys.path.append(os.getenv("ROOT_DIR"))
11 | 
12 | ROOT_DIR = os.getenv("ROOT_DIR")
13 | ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
14 | # OPENFIGI variables
15 | OPENFIGI_API_KEY = os.getenv("OPENFIGI_API_KEY")
16 | OPENFIGI_URL = os.getenv("OPENFIGI_URL")
17 | 
18 | 
19 | class CompanyProfile:
20 | 
21 |     def __init__(
22 |         self,
23 |         identifier,
24 |         idType,
25 |     ):  # idType is TICKER, NAME or ISIN
26 |         # initialise default attributes
27 |         self.identifier = identifier
28 |         self.idType = idType.lower()
29 |         self.isin = (
30 |             identifier
31 |             if self.idType.lower() == "isin" and self.is_valid_isin(identifier)
32 |             else None
33 |         )
34 | 
35 |         self.name = identifier if self.idType.lower() == "name" else None
36 |         self.ticker = identifier if self.idType.lower() == "ticker" else None
37 |         self.description = None
38 | 
39 |         # invoke company details function to retrieve missing attributes
40 |         self._complete_company_profile()
41 |         self.output_path = os.path.join(
42 |             ROOT_OUTPUT_PATH, self.name.replace(" ", "_").upper()
43 |         )
44 |         logger.debug(f"Company Identifier: {self.identifier}")
45 | 
46 |     @staticmethod
47 |     def is_valid_isin(ISIN):
48 |         """
49 |         Function to check if the input is a valid ISIN.
50 |             2 letters followed by any combination of letters or digits
51 |             for the next 10 characters (12 characters in total)
52 | 
53 |         Params:
54 |             ISIN (str): The input string to validate
55 | 
56 |         Returns:
57 |             bool: True if the ISIN is valid, False otherwise
58 |         """
59 |         if (
60 |             len(ISIN) == 12
61 |             and ISIN[:2].isalpha()
62 |             and all(c.isalnum() for c in ISIN[2:])
63 |         ):
64 |             return True
65 |         return False
66 | 
67 |     def get_profile_from_identifier(self, identifier, idType):
68 |         """
69 |         Function to fetch the ticker symbol from OpenFIGI API using the ISIN code.
70 |         """
71 |         # Send a POST request to the OpenFIGI API
72 |         openfigi_response = None
73 | 
74 |         if idType == "isin":
75 |             openfigi_response = self._openfigi_post_request(
76 |                 [{"idType": "ID_ISIN", "idValue": identifier}]
77 |             )
78 |         elif idType == "ticker":
79 |             openfigi_response = self._openfigi_post_request(
80 |                 [{"idType": "TICKER", "idValue": identifier}]
81 |             )
82 | 
83 |         if openfigi_response is not None:
84 |             try:
85 |                 comp_dict = dict(openfigi_response[0]["data"][0])
86 |                 return comp_dict
87 |             except Exception as e:
88 |                 logger.error(
89 |                     f"Error fetching details for identifier{identifier}: {e}. Returning None."
90 |                 )
91 |                 return None
92 | 
93 |     def _complete_company_profile(self) -> None:
94 |         """
95 |         Function to get corresponding details if ISIN provided.
96 |         """
97 |         if self.name is not None:  # for names keep user input
98 |             return
99 |             # Check if identifier is an ISIN
100 |         if self.identifier is not None:
101 | 
102 |             profile = self.get_profile_from_identifier(self.identifier, self.idType)
103 |             if profile is not None:
104 |                 self.name = profile.get("name")
105 |                 self.ticker = profile.get("ticker")
106 |                 self.description = profile.get("securityDescription")
107 |             else:
108 |                 logger.warning(
109 |                     f"ISIN {self.isin} not found. Unable to fetch the corresponding details."
110 |                 )
111 |                 sys.exit()
112 | 
113 |     @staticmethod
114 |     def _openfigi_post_request(data):
115 |         """
116 |         Function to send a POST request to the OpenFIGI API with the given data.
117 | 
118 |         Args:
119 |             data (list): List of dictionaries containing the data to send in the request
120 | 
121 |         Returns:
122 |             dict: Dictionary containing the response from the OpenFIGI API
123 |         """
124 |         headers = {
125 |             "Content-Type": "application/json",
126 |             "X-OPENFIGI-APIKEY": OPENFIGI_API_KEY,
127 |         }
128 |         try:
129 |             # Make the POST request to OpenFIGI API
130 |             response = requests.post(OPENFIGI_URL, json=data, headers=headers)
131 | 
132 |             # Handle rate-limiting with retries
133 |             while response.status_code == 429:
134 |                 logger.warning(
135 |                     "Rate limit reached for OPENFIGI, retrying in 3 seconds..."
136 |                 )
137 |                 time.sleep(3)
138 |                 response = requests.post(OPENFIGI_URL, json=data, headers=headers)
139 | 
140 |             # Return the JSON response
141 |             return response.json()
142 |         except Exception as e:
143 |             logger.error(f"Error sending POST request to OpenFIGI API: {e}")
144 |             return None
145 | 
146 | 
147 | # Main script to fetch company information
148 | if __name__ == "__main__":
149 |     # Ask the user for input
150 |     id_type = input("Enter idType (TICKER, NAME, ISIN): ").strip()
151 |     identifier = input("Enter ISIN, Ticker, or Company Name: ").strip()
152 |     company = CompanyProfile(identifier, id_type)
153 |     logger.info(f"Company Name: {company.name}, Ticker: {company.ticker}")
```

src/find/esg_reports.py
```
1 | import datetime as dt
2 | import json
3 | import os
4 | import re
5 | import sys
6 | from typing import List
7 | 
8 | import requests
9 | from dotenv import load_dotenv
10 | from loguru import logger
11 | from pydantic import BaseModel
12 | 
13 | from src.utils.data_models import SearchKeyWords
14 | 
15 | load_dotenv()
16 | sys.path.append(os.getenv("ROOT_DIR"))
17 | 
18 | ROOT_DIR = os.getenv("ROOT_DIR")
19 | ROOT_OUTPUT_PATH = os.getenv("ROOT_OUTPUT_PATH")
20 | API_KEY = os.getenv("GOOGLE_API_KEY")
21 | SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
22 | 
23 | if not any([API_KEY, SEARCH_ENGINE_ID]):
24 |     raise ValueError(
25 |         "Environment variables GOOGLE_API_KEY or GOOGLE_SEARCH_ENGINE_ID are not set."
26 |     )
27 | 
28 | from src.find.company_profile import CompanyProfile  # noqa: E402
29 | 
30 | 
31 | class ESGReports:
32 | 
33 |     def __init__(self, company: CompanyProfile):
34 |         self.company = company
35 |         self.urls = self._get_report_search_results()
36 | 
37 |         # set output path
38 |         try:
39 |             # set output path
40 |             self.output_path = os.path.join(
41 |                 ROOT_OUTPUT_PATH,
42 |                 str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
43 |             )
44 |         except Exception:
45 |             self.output_path = os.path.join(
46 |                 ROOT_OUTPUT_PATH,
47 |                 str(self.company.name).upper().replace(" ", "_").replace("/", "_"),
48 |             )
49 |         os.makedirs(self.output_path, exist_ok=True)
50 |         # dump company profile to json
51 |         self.save_profile()
52 | 
53 |     def _get_report_search_results(self) -> dict:
54 |         """
55 |         Retrieve the top 3 URLs of the company's ESG reports using Google Custom Search.
56 |         """
57 |         # Search parameters
58 |         current_year = str(dt.datetime.now().year)
59 |         search_query = f"{self.company.name} {current_year} ESG report filetype:pdf"
60 |         url = "https://www.googleapis.com/customsearch/v1"
61 |         params = {
62 |             "q": search_query,
63 |             "key": API_KEY,
64 |             "cx": SEARCH_ENGINE_ID,
65 |         }
66 | 
67 |         # Make the search request
68 |         response = requests.get(url, params=params)
69 |         response.raise_for_status()
70 |         search_results = response.json().get("items", [])[:5]  # Get top 5 results
71 | 
72 |         if not search_results:
73 |             logger.warning(f"No ESG reports found for {self.name}")
74 |             # TODO - return response to display in UI
75 |             sys.exit()
76 | 
77 |         sorted_results = self._sort_search_reults(
78 |             self.company.name, search_results
79 |         )  # Invoke function to get proper order of keywords
80 |         esg_urls = {
81 |             index: value.get("link", "") for index, value in enumerate(sorted_results)
82 |         }
83 |         logger.debug(f"ESG report urls for {self.company.name}: {esg_urls}")
84 |         return esg_urls
85 | 
86 |     @staticmethod
87 |     def _sort_search_reults(company_name: str, search_results: List[dict]):
88 | 
89 |         for result in search_results:
90 |             result_obj = SearchResult(
91 |                 company_name=company_name,
92 |                 url=result.get("link", ""),
93 |                 title=result.get("title", ""),
94 |                 description=result.get("snippet", ""),
95 |             )
96 |             result["score"] = result_obj.score_search()
97 | 
98 |         sorted_results = sorted(
99 |             search_results,
100 |             key=lambda item: item.get("score"),
101 |             reverse=True,
102 |         )
103 | 
104 |         return sorted_results
105 | 
106 |     def save_profile(self):
107 |         """Dumps the company profile as a JSON file into the specified folder."""
108 |         if not ROOT_DIR:
109 |             raise ValueError("ROOT_DIR is not set in the .env file.")
110 |         try:
111 |             # get attributes as dictionary
112 |             data = {
113 |                 "company": self.company.__dict__,
114 |                 "esg_reports": self.urls,
115 |             }
116 | 
117 |             file_path = f"{self.output_path}/profile.json"
118 |             with open(file_path, "w") as json_file:
119 |                 json.dump(data, json_file, indent=4)
120 |             logger.info(f"Company profile JSON saved to {file_path}")
121 |         except Exception as e:
122 |             print(f"Failed to save company profile JSON: {e}")
123 | 
124 | 
125 | class SearchResult(BaseModel):
126 |     company_name: str
127 |     url: str
128 |     title: str
129 |     description: str
130 | 
131 |     def score_search(self):
132 |         stripped_name = self.company_name.split(" ")[0].lower()
133 | 
134 |         text_score = (
135 |             self.score_text(self.title.lower())
136 |             + self.score_text(self.description.lower())
137 |             + (
138 |                 -5
139 |                 if (
140 |                     stripped_name not in self.title.lower()
141 |                     and stripped_name not in self.description.lower()
142 |                     and stripped_name not in self.url.lower()
143 |                 )
144 |                 else 1
145 |             )  # strongly penalize if name is not there
146 |         )
147 |         url_score = self.score_text(self.url) + (1 if self.company_name_lookup() else 0)
148 |         year_score = self.score_year(
149 |             self.title.lower() + self.description.lower() + self.url.lower()
150 |         )
151 |         return text_score + url_score + year_score
152 | 
153 |     @staticmethod
154 |     def score_text(text: str):
155 |         count = sum(keyword.value.lower() in text.lower() for keyword in SearchKeyWords)
156 |         return count
157 | 
158 |     def company_name_lookup(self):
159 |         # get the site name from url
160 |         url_index = re.search(
161 |             r"(?:https?://)?(?:www\.)?([a-zA-Z0-9]+)", self.url
162 |         ).group()
163 |         stripped_name = self.company_name.split(" ")[0].lower()
164 |         # check if company name starts with site name
165 |         if stripped_name in url_index:
166 |             return 2
167 |         else:
168 |             return 0
169 | 
170 |     @staticmethod
171 |     def score_year(text):
172 |         current_year = dt.datetime.now().year
173 |         year_lag = current_year - 1
174 |         two_year_lag = current_year - 2
175 |         three_year_lag = current_year - 3
176 | 
177 |         # Extract all years from the text
178 |         years_in_text = [int(year) for year in re.findall(r"\b\d{4}\b", text)]
179 | 
180 |         # Check for years that are 3 years older than the current year or older
181 |         if any(year < three_year_lag for year in years_in_text):
182 |             return -2
183 | 
184 |         # Check if the text contains the current year, year lag, or two-year lag
185 |         if current_year in years_in_text:
186 |             return 2
187 |         if any(
188 |             year in {current_year, year_lag, two_year_lag} for year in years_in_text
189 |         ):
190 |             return 1
191 | 
192 |         return -1
```

src/find/filters.py
```
1 | """
2 | https://ranaroussi.github.io/yfinance/reference/yfinance.sector_industry.html
3 | https://finance.yahoo.com/research-hub/screener/sec-ind_sec-largest-equities_industrials/?start=0&count=25
4 | 
5 | TODO - (iman / balazs)
6 | - get list of companies by sectors / countries / indeces
7 | - get aggregated figures (cache monthly) for top companies in each filter type
8 | """
```

src/scripts/__init__.py
```
```

src/scripts/retrieve_company_profile.py
```
1 | import os
2 | import sys
3 | 
4 | from dotenv import load_dotenv
5 | from loguru import logger
6 | 
7 | load_dotenv()
8 | sys.path.append(os.getenv("ROOT_DIR"))
9 | 
10 | from src.find.company_profile import CompanyProfile  # noqa: E402
11 | 
12 | # temporarily hardcoding variables here
13 | # TODO - switch to retrieve from inputs to flask app
14 | ROOT_DATA_DIR = os.getenv("ROOT_DIR")
15 | COMPANY_IDENTIFIER = (
16 |     "GB00BNC5T391"  # note: src/extract/tables.py requires ISIN currently
17 | )
18 | 
19 | if __name__ == "__main__":
20 |     # get the ticker symbol and company name from ISIN
21 |     company = CompanyProfile(COMPANY_IDENTIFIER, "ISIN")
22 |     logger.info(f"Retrieved details for {company.name}")
```

src/scripts/retrieve_emissions_data.py
```
1 | import json
2 | import os
3 | import sys
4 | import time
5 | from datetime import datetime, timedelta
6 | 
7 | import pandas as pd
8 | from dotenv import load_dotenv
9 | from loguru import logger
10 | 
11 | # Load environment variables from .env file
12 | load_dotenv()
13 | # Get ROOT_DIR from the environment variables
14 | ROOT_DIR = os.getenv("ROOT_DIR")
15 | OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
16 | # append path
17 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
18 | 
19 | from src.extract.filtered_data import Filter  # noqa: E402
20 | from src.extract.llama import LlamaExtractor  # noqa: E402
21 | from src.extract.tables import TableExtractor  # noqa: E402
22 | from src.find.company_profile import CompanyProfile  # noqa: E402
23 | from src.find.esg_reports import ESGReports  # noqa: E402
24 | from src.utils.data import download_pdf_from_urls  # noqa: E402
25 | from src.utils.data_models import TableParsers  # noqa: E402
26 | 
27 | 
28 | def get_emissions_data(identifier, idType, parser):
29 |     company = CompanyProfile(identifier, idType)
30 | 
31 |     # check cache for data
32 |     try:
33 |         cache_dir = os.path.join(OUTPUT_DIR)
34 |         if not os.path.exists(cache_dir):
35 |             logger.error(f"Cache directory does not exist: {cache_dir}")
36 |             return None
37 | 
38 |         esg_file_path = None
39 | 
40 |         def is_recent_file(file_path, days=30):
41 |             """Checks if a file was modified within the last `days` days."""
42 |             if os.path.exists(file_path):
43 |                 file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
44 |                 return file_mtime >= (datetime.now() - timedelta(days=days))
45 |             return False
46 | 
47 |         if idType == "name":
48 |             # Get all folder names in the cache directory
49 |             folder_names = [
50 |                 folder
51 |                 for folder in os.listdir(cache_dir)
52 |                 if os.path.isdir(os.path.join(cache_dir, folder))
53 |             ]
54 | 
55 |             # Find matching folder
56 |             matching_folder = next(
57 |                 (
58 |                     folder
59 |                     for folder in folder_names
60 |                     if company.name.upper().replace(" ", "_") in folder.upper()
61 |                     or folder.upper() in company.name.upper()
62 |                 ),
63 |                 None,
64 |             )
65 | 
66 |             if matching_folder:
67 |                 folder_path = os.path.join(cache_dir, matching_folder)
68 |                 esg_file_path = os.path.join(folder_path, "esg_data.csv")
69 | 
70 |         else:
71 |             # For other idTypes, check the standard company output path
72 |             folder_path = company.output_path
73 |             esg_file_path = os.path.join(company.output_path, "esg_data.csv")
74 | 
75 |         # If the ESG file exists and is recent, load it
76 |         if esg_file_path and os.path.exists(esg_file_path):
77 |             if is_recent_file(esg_file_path):
78 |                 try:
79 |                     data = pd.read_csv(esg_file_path)
80 |                     logger.info(f"data for company: {data}")
81 |                     logger.info(
82 |                         f"Loaded ESG data from {esg_file_path} for company {company.name}"
83 |                     )
84 |                     profile_path = os.path.join(folder_path, "profile.json")
85 | 
86 |                     # get report path
87 |                     if os.path.exists(profile_path):
88 |                         with open(os.path.join(folder_path, "profile.json")) as f:
89 |                             profile = json.load(f)
90 |                         logger.info(f"Loaded profile for {company.name}")
91 |                         report = next(
92 |                             iter(profile.get("esg_reports").values())
93 |                         )  # Get first URL dynamically
94 |                         # report = list(profile.get("esg_reports").values())[0]
95 |                     else:
96 |                         esg_reports = ESGReports(company)
97 |                         report = next(iter(esg_reports.urls.values()))
98 |                         # report = list(esg_reports.urls.values())[0]
99 | 
100 |                     logger.info(f"loaded data: {data} {report}")
101 |                     return data, report
102 |                 except Exception as e:
103 |                     logger.error(f"Error reading ESG data from {esg_file_path}: {e}")
104 |             else:
105 |                 logger.warning(
106 |                     f"ESG data file {esg_file_path} is older than one month, ignoring cache."
107 |                 )
108 | 
109 |         logger.info(f"No recent cached data found for {company.name}")
110 | 
111 |         # Load fresh data
112 |         # esg_file_path = os.path.join(company.output_path, "esg_data.csv")
113 |         # if is_recent_file(esg_file_path):
114 |         #     if os.path.exists(esg_file_path):
115 |         #         try:
116 |         #             data = pd.read_csv(esg_file_path)
117 |         #             logger.info(f"Loaded ESG data for {company.name}")
118 |         #             return data
119 |         #         except Exception as e:
120 |         #             logger.error(f" {esg_file_path}: {e}")
121 | 
122 |     except Exception:
123 |         logger.warning(
124 |             "Unable to retrieve recent cached data. Retrieving emissions data from web..."
125 |         )
126 | 
127 |     esg_reports = ESGReports(company)
128 |     # Loop over urls until emissions data retrieved
129 |     for url in esg_reports.urls.values():
130 |         logger.info(f"Trying extraction with {url}")
131 |         try:
132 |             # Download pdf file
133 |             path = download_pdf_from_urls([url], esg_reports.output_path)
134 |             # get emissions data
135 |             output = TableExtractor(
136 |                 company, path, parser, esg_reports.output_path
137 |             ).extract()
138 |             if output not in [None, [], False]:
139 |                 break
140 |             else:
141 |                 # delete file before moving on to next
142 |                 for file in os.listdir(esg_reports.output_path):
143 |                     if os.path.basename(path).replace(".pdf", "") in file:
144 |                         os.remove(os.path.join(esg_reports.output_path, file))
145 |                         logger.info(f"Deleted {file}")
146 |         except Exception as e:
147 |             logger.debug(f"Unable to parse data from {url}: {e}")
148 |             # delete file before moving on to next
149 |             for file in os.listdir(esg_reports.output_path):
150 |                 if isinstance(path, str) and (
151 |                     os.path.basename(path).replace(".pdf", "") in file
152 |                 ):
153 |                     os.remove(os.path.join(esg_reports.output_path, file))
154 |                     logger.info(f"Deleted {file}")
155 |             continue
156 | 
157 |     try:
158 |         # TODO - pass tables as objects
159 |         data_filter = Filter(directory_path=esg_reports.output_path, parser=parser)
160 |         data_filter.extract_filtered_df()
161 |         data = data_filter.filtered_df
162 |         data.to_csv(os.path.join(esg_reports.output_path, "esg_data.csv"))
163 |         # get filtered pdf path
164 | 
165 |         for file in os.listdir(esg_reports.output_path):
166 |             if file.endswith("filtered.pdf"):
167 |                 pdf_path = os.path.join(esg_reports.output_path, file)
168 |             else:
169 |                 pdf_path = None
170 | 
171 |         # if any column is completely null, run llama parse instead
172 |         if any([all(data[col].isna()) for col in data.columns]) or data is None:
173 |             logger.info("Retrieving via LlamaParse...")
174 |             if pdf_path is None:
175 |                 return pd.DataFrame()
176 |             extractor = LlamaExtractor(
177 |                 company_name=company.name,
178 |                 filtered_pdf_path=pdf_path,
179 |                 output_path=esg_reports.output_path,
180 |             )
181 |             data = extractor.process_company()
182 |     except Exception as e:
183 |         logger.warning(f"Retrieveing via LlamaParse...: {e}")
184 | 
185 |         for file in os.listdir(esg_reports.output_path):
186 |             logger.info(file)
187 |             if file.endswith("filtered.pdf"):
188 |                 pdf_path = os.path.join(esg_reports.output_path, file)
189 |             else:
190 |                 pdf_path = None
191 |         if pdf_path is None:
192 |             return pd.DataFrame()
193 |         extractor = LlamaExtractor(
194 |             company_name=company.name,
195 |             filtered_pdf_path=pdf_path,
196 |             output_path=esg_reports.output_path,
197 |         )
198 |         data = extractor.process_company()
199 | 
200 |     top_report = list(esg_reports.urls.values())[0]
201 |     return data, top_report
202 | 
203 | 
204 | if __name__ == "__main__":
205 |     start = time.time()
206 | 
207 |     identifier = "US5949181045"
208 |     idType = "isin"
209 |     parser = TableParsers.DOCLING
210 |     data = get_emissions_data(identifier, idType, parser)
211 | 
212 |     end = time.time()
213 |     total = end - start
214 | 
215 |     logger.info(f"time taken: {total}")
```

src/scripts/retrieve_emissions_data_pro.py
```
1 | import os
2 | import sys
3 | 
4 | import pandas as pd
5 | from dotenv import load_dotenv
6 | from loguru import logger
7 | 
8 | # Load environment variables
9 | load_dotenv()
10 | # Get ROOT_DIR from environment variables
11 | ROOT_DIR = os.getenv("ROOT_DIR")
12 | OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
13 | 
14 | 
15 | # Ensure project root is on sys.path
16 | sys.path.append(f"{os.getenv('ROOT_DIR')}")
17 | 
18 | 
19 | from src.extract.tables import TableExtractor  # noqa: E402
20 | from src.find.company_profile import CompanyProfile  # noqa: E402
21 | from src.find.esg_reports import ESGReports  # noqa: E402
22 | 
23 | # Use the LLM-based table filtering
24 | from src.utils import llm_table_data_filtering  # noqa: E402
25 | from src.utils.data import download_pdf_from_urls  # noqa: E402
26 | 
27 | 
28 | def get_emissions_data_pro(identifier, idType, parser):
29 |     """
30 |     Retrieve ESG emissions data using an LLM-based table filter.
31 |     Returns both the LLM output and path to the relevant PDF.
32 |     """
33 |     company = CompanyProfile(identifier, idType)
34 |     esg_reports = ESGReports(company)
35 | 
36 |     # Check for cached LLM data
37 |     llm_output_file = os.path.join(esg_reports.output_path, "esg_data_llm.md")
38 |     if os.path.isfile(llm_output_file):
39 |         logger.info(f"Found cached LLM data for {company.name} at {llm_output_file}")
40 |         with open(llm_output_file, "r", encoding="utf-8") as f:
41 |             llm_markdown = f.read()
42 |         # Look for PDFs but exclude ones with 'filtered' in the name
43 |         pdf_files = [
44 |             f
45 |             for f in os.listdir(esg_reports.output_path)
46 |             if f.endswith(".pdf") and "filtered" not in f.lower()
47 |         ]
48 |         pdf_path = None
49 |         if pdf_files:
50 |             pdf_path = os.path.join(esg_reports.output_path, pdf_files[0])
51 |         else:
52 |             logger.warning(
53 |                 f"No PDF found in {esg_reports.output_path} for cached data."
54 |             )
55 |         return pd.DataFrame({"LLM_Output": [llm_markdown]}), pdf_path
56 | 
57 |     logger.warning("No cached LLM data found. Retrieving emissions data from web...")
58 | 
59 |     # Attempt to download & parse ESG PDFs
60 |     successful_pdf_path = None
61 |     for url in esg_reports.urls.values():
62 |         logger.info(f"Trying extraction with {url}")
63 |         try:
64 |             local_pdf_path = download_pdf_from_urls([url], esg_reports.output_path)
65 |             output = TableExtractor(
66 |                 company, local_pdf_path, parser, esg_reports.output_path
67 |             ).extract()
68 |             if output not in [None, [], False]:
69 |                 successful_pdf_path = local_pdf_path
70 |                 break
71 |         except Exception as e:
72 |             logger.debug(f"Unable to parse data from {url}: {e}")
73 |             continue
74 | 
75 |     # Use the LLM-based filter
76 |     data = llm_table_data_filtering.filter_tables(esg_reports.output_path, parser)
77 | 
78 |     # Cache the LLM output as Markdown
79 |     if not data.empty and "LLM_Output" in data.columns:
80 |         llm_markdown = data["LLM_Output"].iloc[0]
81 |         with open(llm_output_file, "w", encoding="utf-8") as f:
82 |             f.write(llm_markdown)
83 |         logger.info(f"Cached LLM data to {llm_output_file}")
84 | 
85 |     return data, successful_pdf_path
```

src/static/style.css
```
1 | 
2 | h2 {
3 |     color: red;
4 |     text-align: center;
5 | }
```

src/templates/advanced_search.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Advanced Search</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
11 |   <style>
12 |           body {
13 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
14 |           background-color: #F5F5F5;
15 |           color: #333333;
16 |           margin: 0;
17 |           padding: 0;
18 |       }
19 |       table, th, td {
20 |           border: 1px solid black;
21 |      }
22 | 
23 |     .logo-header-container {
24 |        z-index: 10;
25 |        position: relative;
26 |        height: 160px;
27 |        width: 100%;
28 |        background-color: #063800;
29 |        display: flex;
30 |        align-items: center; /* Align items vertically */
31 |        justify-content: center; /* Center items horizontally */
32 |        gap: 20px; /* Add spacing between logo and text */
33 |        box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
34 |        text-align: center;
35 |     }
36 | 
37 | 
38 |     .logo {
39 |        max-height: 100px;
40 |        width: auto;
41 |     }
42 | 
43 | 
44 |     .div1 {
45 |        display: flex;
46 |        flex-direction: column; /* Stack heading and phrase */
47 |        align-items: center;
48 |        justify-content: center;
49 |     }
50 | 
51 | 
52 |     .catchy-phrase {
53 |        color: white;
54 |        font-size: 20px;
55 |        margin-top: 5px; /* Adjust spacing between header and phrase */
56 |     }
57 | 
58 |     .footer {
59 |           background-color: #2E8B57;
60 |           color: #FFFFFF;
61 |           text-align: center;
62 |           padding: 10px;
63 |           position: fixed;
64 |           left: 0;
65 |           bottom: 0;
66 |           width: 100%;
67 |           font-size: 0.9rem;
68 |       }
69 | 
70 |     .dropdown-container {
71 |           background-color: white;
72 |           display: flex;
73 |           padding: 10px;
74 |           gap: 30px;
75 |           align-items: center;
76 |           justify-content: center;
77 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
78 |       }
79 | 
80 | 
81 |     .dropdown-container label{
82 |           color: #1C1C1C;
83 |       }
84 | 
85 | 
86 |     .dropdown-container label,
87 | 
88 |     .dropdown-container select {
89 |           margin-right: 10px;
90 |       }
91 | 
92 |     .dropdown-container select {
93 |           width: 200px;
94 |           padding: 5px;
95 |           border: 1px solid #ccc;
96 |           border-radius: 4px;
97 |           background-color: #fff;
98 |           color: #333;
99 |           font-size: 16px;
100 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
101 |       }
102 | 
103 | 
104 |     .title-container {
105 |           text-align: center;
106 |           margin-bottom: 10px;
107 |       }
108 | 
109 |     .company-container {
110 |           display: flex;
111 |           gap: 10px;
112 |           align-items: center;
113 |           margin-top: 20px;
114 |           justify-content: center;
115 |           width: 100%;
116 |           margin-bottom: 20px;
117 |       }
118 | 
119 |     .company-container select {
120 |           width: 400px;
121 |           padding: 5px;
122 |           border: 1px solid #ccc;
123 |           border-radius: 4px;
124 |           background-color: #fff;
125 |           color: #333;
126 |           font-size: 16px;
127 |           box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
128 |       }
129 | 
130 |     .submit-button {
131 |           background-color: #063800;
132 |           color: #FFFFFF;
133 |           border: none;
134 |           padding: 10px 20px;
135 |           border-radius: 4px;
136 |           font-size: 16px;
137 |           cursor: pointer;
138 |       }
139 | 
140 | 
141 |     .submit-button:hover {
142 |           background-color: #1E6B47;
143 |       }
144 | 
145 |     .report-container{
146 |       background-color: #F5F5F5;
147 |       color: #1C1C1C;
148 |       display: flex;
149 |       padding: 10px;
150 |       gap: 30px;
151 |       align-items: center;
152 |       justify-content: center;
153 |       margin-bottom: 30px;
154 |     }
155 | 
156 |     .selected-company {
157 |       background-color: white;
158 |       padding: 20px;
159 |       margin: 20px auto;
160 |       align-items: center;
161 |       justify-content: center;
162 |       box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
163 |       border: 2px solid black;
164 |       display: inline-block;
165 |       width: 90%; /* Adjust width for better layout */
166 |       max-width: 1400px;
167 |     }
168 | 
169 |     /* Table Styling */
170 |     .selected-company table {
171 |       width: 100%;
172 |       border-collapse: collapse;
173 |     }
174 | 
175 |     .selected-company th, .selected-company td {
176 |       border: 1px solid black;
177 |       padding: 8px;
178 |       text-align: center;
179 |     }
180 | 
181 | 
182 |     .selected-company th {
183 |       background-color: #063800;
184 |       color: white;
185 |     }
186 | 
187 | 
188 |     /* Style the Download Button */
189 |     .selected-company a.btn-success {
190 |       display: block;
191 |       margin: 10px auto;
192 |       text-align: center;
193 |       background-color: #063800;
194 |       color: white;
195 |       padding: 10px 15px;
196 |       font-size: 16px;
197 |       border-radius: 5px;
198 |       text-decoration: none;
199 |       transition: background-color 0.3s ease;
200 |     }
201 | 
202 | 
203 |     .selected-company a.btn-success:hover {
204 |       background-color: #1E6B47;
205 |     }
206 | 
207 | 
208 |     .navigation {
209 |           position: absolute;
210 |           left:0;
211 |           width:100px;
212 |           height:100%;
213 |           background:  #063800;
214 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
215 |           display:center;
216 |           justify-content:center;
217 |           align-items:center;
218 |           flex-direction:column;
219 |           gap:10px;
220 |           transform: translateX(-100%);
221 |           transition: transform 0.3s ease;
222 | 
223 |       }
224 | 
225 | 
226 |     /* Class to toggle menu visibility */
227 |     .navigation.show {
228 |           transform: translateX(0);
229 |       }
230 | 
231 | 
232 | 
233 |     .navigation li {
234 |           position:relative;
235 |           list-style:none;
236 |           width:80px;
237 |           height: 80px;
238 |           display:flex;
239 |           justify-content:center;
240 |           margin: 0 5px;
241 |       }
242 | 
243 | 
244 | 
245 | 
246 |     .navigation li::before {
247 |           content: '';
248 |           position: absolute;
249 |           top:calc(50% - 2.5px);
250 |           left: 20px;
251 |           width:5px;
252 |           height: 5px;
253 |           border-radius:50%;
254 |           transition:0.5s;
255 | 
256 |       }
257 | 
258 | 
259 | 
260 | 
261 |     .navigation li.active::before {
262 |           background:white;
263 |           box-shadow:0 0 5px white,
264 |           0 0 10px white,
265 |           0 0 20px white,
266 |           0 0 30px white,
267 |           0 0 40px white;
268 |       }
269 | 
270 | 
271 |     .navigation li a {
272 |           display:flex;
273 |           justify-content:center;
274 |           align-items:center;
275 |           flex-direction:column;
276 |           text-decoration:none;
277 |       }
278 | 
279 | 
280 |     .navigation li a .icon {
281 |           color: white;
282 |           transition: 0.5s;
283 |           transition-delay: 0.2s;
284 |           font-size: 1.5em;
285 |       }
286 | 
287 |     .navigation li.active a .icon::before{
288 |           transform:scale(1);
289 |       }
290 | 
291 | 
292 |     .navigation li a .text{
293 |           position: absolute;
294 |           left:130px;
295 |           font-size:1.25em;
296 |           color:white;
297 |           visibility:hidden;
298 |           transition:0.5s;
299 |       }
300 | 
301 | 
302 |     .navigation li a .text::before {
303 |           content: '';
304 |           position: absolute;
305 |           top: 50%
306 |           left: -4px;
307 |           transform:translateY(-50%) rotate(45deg);
308 |           width:10px;
309 |           height:10px;
310 |       }
311 | 
312 |     .navigation li:hover a .text {
313 |           visibility: visible;
314 |       }
315 | 
316 |     .hamburger-icon {
317 |           font-size: 30px;
318 |           color: white;
319 |           cursor: pointer;
320 |           position: absolute;
321 |           top: 20px;
322 |           left: 20px;
323 |           z-index: 100;
324 |       }
325 | 
326 | 
327 |     .sidebar1 {
328 |           display: flex;
329 |           flex-direction: column;
330 |           align-items: center;
331 |           justify-content: center;
332 |           border: 1px solid #ccc;
333 |           border-radius: 8px;
334 |           margin-left: 50px;
335 |           margin-top: 40px;
336 |           float: left;
337 |           width: 250px;
338 |           height: 150px;
339 |           padding: 20px;
340 |           background-color: white;
341 |           color: white;
342 |           z-index: 1000;
343 |       }
344 | 
345 | 
346 |       .dropdown {
347 |             z-index: 15;
348 |             position: absolute;
349 |             top: 20px;
350 |             right: 20px;
351 |             display: inline-block;
352 |             border: 1px solid white;
353 |             background-color: white;
354 |             border-radius: 12px;
355 |             padding: 4px 7px;
356 |             font-size: 16px;
357 |             cursor: pointer;
358 |             align-items: center;
359 |       }
360 | 
361 | 
362 |       .dropdown-content {
363 |         display: none;
364 |         position: absolute;
365 |         padding: 5px 15px;
366 |         font-size: 16px;
367 |         background-color: white;
368 |         min-width: 100px;
369 |         box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
370 |         z-index: 1;
371 |       }
372 | 
373 | 
374 |       .dropdown-content a {
375 |         color: black;
376 |         padding: 12px 16px;
377 |         text-decoration: none;
378 |         display: block;
379 |       }
380 | 
381 | 
382 |       .dropdown-content a:hover {background-color: #2e8b563d;}
383 | 
384 | 
385 |       .dropdown:hover .dropdown-content {display: block;}
386 | 
387 | 
388 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
389 |       .dropbtn {
390 |         background-color: white;
391 |         color:  #063800;
392 |         padding: 16px;
393 |         font-size: 16px;
394 |         border: none;
395 |         cursor: pointer;
396 |       }
397 | 
398 | 
399 |       .nav-tabs .nav-link {
400 |          background-color: #063800 !important;
401 |          color: white !important; /* Ensure text is readable */
402 |          border: none !important; /* Optional: remove default border */
403 |      }
404 | 
405 | 
406 |      .nav-tabs .nav-link.active {
407 |          background-color: #045000 !important; /* Slightly darker shade for active tab */
408 |          color: white !important;
409 |      }
410 | 
411 | 
412 |     .nav-tabs {
413 |       border-bottom: none !important;
414 |       margin-bottom: 0 !important;
415 |       padding-bottom: 0 !important;
416 |     }
417 | 
418 |     .tab-content {
419 |       color:#F5F5F5;
420 |       background-color: #1C1C1C !important;
421 |       margin-top: -1px !important;
422 |       border-radius: 0 0 8px 8px;
423 |       border: none !important;
424 |     }
425 | 
426 | 
427 |     .tab-pane {
428 |       background-color: #1C1C1C !important;
429 |       margin: 0 !important;
430 |       border: none !important;
431 |     }
432 | 
433 | 
434 |     .tab-pane > div {
435 |       background-color: #1C1C1C !important;
436 |       border: none !important;
437 |       margin: 0 !important;
438 |       padding: 20px;
439 |     }
440 |     .page-bottom {
441 |       background-color: #1C1C1C !important;
442 |       padding: 50px 0; /* Adds spacing */
443 |       min-height: 1000px; /* Adjust as needed */
444 |     }
445 | 
446 |     #loading-spinner {
447 |                  display: none;
448 |                  width: 24px;
449 |                  height: 24px;
450 |                  border: 4px solid rgba(46, 139, 87, 0.3);
451 |                  border-top: 4px solid #2E8B57;
452 |                  border-radius: 50%;
453 |                  animation: spin 1s linear infinite;
454 |              }
455 | 
456 | 
457 |     @keyframes spin {
458 |                  0% { transform: rotate(0deg); }
459 |                  100% { transform: rotate(360deg); }
460 |              }
461 | 
462 |       .chart-container {
463 |            width: 100%;
464 |            max-width: 800px;
465 |            margin: 20px auto;
466 |        }
467 | 
468 | 
469 | 
470 |   </style>
471 | </head>
472 | <body>
473 |    <div class="logo-header-container">
474 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
475 |        <div class="div1">
476 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
477 |            <p class="catchy-phrase">Advanced Search</p>
478 |        </div>
479 |    </div>
480 | 
481 |   <div class="dropdown">
482 |       <button class="dropbtn">My Pro Account</button>
483 |       <div class="dropdown-content">
484 |           <a href="{{url_for('register')}}">Create an account</a>
485 |           <a href="{{url_for('login')}}">Login</a>
486 |       </div>
487 |   </div>
488 |   <div class="hamburger-icon">&#9776;</div>
489 |      <ul class="navigation">
490 |       <li class="active">
491 |           <a href="{{url_for('test')}}">
492 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
493 |           </a>
494 |       </li>
495 |       <li>
496 |           <a href="{{url_for('instructions')}}">
497 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
498 |           </a>
499 |       </li>
500 |       <li>
501 |           <a href="{{url_for('advanced_search')}}">
502 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
503 |           </a>
504 |       </li>
505 |       <li>
506 |           <a href="{{url_for('register')}}">
507 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
508 |           </a>
509 |       </li>
510 |       <li class="active">
511 |           <a href=/firstpage>
512 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
513 |           </a>
514 |       </li>
515 |   </ul>
516 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
517 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
518 |          <script>
519 |              document.addEventListener('DOMContentLoaded', function () {
520 |                  const hamburger = document.querySelector('.hamburger-icon');
521 |                  const navigation = document.querySelector('.navigation');
522 |                  let isOpen = false;
523 | 
524 | 
525 | 
526 | 
527 | 
528 | 
529 | 
530 | 
531 |                  hamburger.addEventListener('click', function () {
532 |                      // Toggle menu visibility
533 |                      isOpen = !isOpen;
534 |                      if (isOpen) {
535 |                          navigation.classList.add('show');
536 |                      } else {
537 |                          navigation.classList.remove('show');
538 |                      }
539 |                  });
540 | 
541 | 
542 | 
543 | 
544 | 
545 | 
546 | 
547 | 
548 |                  // Keep your existing navigation item click event listener
549 |                  let list = document.querySelectorAll('.navigation li');
550 |                  function activeLink() {
551 |                      list.forEach((item) => item.classList.remove('active'));
552 |                      this.classList.add('active');
553 |                  }
554 |                  list.forEach((item) => item.addEventListener('click', activeLink));
555 |              });
556 | 
557 | 
558 | 
559 | 
560 | 
561 | 
562 | 
563 | 
564 |          </script>
565 | 
566 | 
567 |   <form action="/submit" method="post">
568 |       <div class="dropdown-container">
569 |           <div>
570 |               <label for="country">Choose a Country:</label>
571 |               <select name="country" id="country">
572 |                   <option value="all">All</option>
573 |                   {% for country in countries %}
574 |                   <option value="{{ country }}">{{ country }}</option>
575 |                   {% endfor %}
576 |               </select>
577 |           </div>
578 |           <div>
579 |               <label for="sector">Choose a Sector:</label>
580 |               <select name="sector" id="sector">
581 |                   <option value="all">All</option>
582 |                   {% for sector in sectors %}
583 |                   <option value="{{ sector }}">{{ sector }}</option>
584 |                   {% endfor %}
585 |               </select>
586 |           </div>
587 |           <div>
588 |               <label for="industry">Choose an Industry:</label>
589 |               <select name="industry" id="industry">
590 |                   <option value="all">All</option>
591 |                   {% for industry in industries %}
592 |                   <option value="{{ industry }}">{{ industry }}</option>
593 |                   {% endfor %}
594 |               </select>
595 |           </div>
596 |           {% if not companies %}
597 |           <div>
598 |               <input type="submit" value="Submit" class="submit-button">
599 |           </div>
600 |           {% endif %}
601 |       </div>
602 |       {% if companies %}
603 |       <div class="company-container">
604 |           <label for="company">Choose a Company:</label>
605 |           <select name="company" id="company">
606 |               {% for company in companies %}
607 |               <option value="{{ company }}">{{ company }}</option>
608 |               {% endfor %}
609 |           </select>
610 |           <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
611 |              <button type="submit" id="submit" class="submit-button">Search</button>
612 |              <div id="loading-spinner" style="display: none;"></div>
613 |      </div>
614 |       </div>
615 |       {% endif %}
616 |       {% if selected_company %}
617 | 
618 |       <div class="report-container">
619 |           {% if report_url %}
620 |               <p>Latest ESG Report Link for {{selected_company}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
621 | 
622 | 
623 |           {% else %}
624 |               <p>No report found.</p>
625 |           {% endif %}
626 |       </div>
627 | 
628 |       <ul class="nav nav-tabs mt-4" id="resultTabs" role="tablist">
629 |           <li class="nav-item" role="presentation">
630 |               <button class="nav-link active" id="table-tab" data-bs-toggle="tab" data-bs-target="#table-content" type="button" role="tab">Extracted Table <i class="fa-solid fa-table"></i></button>
631 |           </li>
632 |           <li class="nav-item" role="presentation">
633 |               <button class="nav-link" id="chart-tab" data-bs-toggle="tab" data-bs-target="#chart-content" type="button" role="tab">Data Visualization <i class="fa-solid fa-chart-column"></i></button>
634 |           </li>
635 |       </ul>
636 |       <!-- Tab Content -->
637 |       <div class="tab-content mt-3" id="resultTabsContent">
638 |           <!-- Table Section -->
639 |           <div class="tab-pane fade show active" id="table-content" role="tabpanel">
640 |               {% if selected_company and emissions_data %}
641 |               <div class="selected-company">
642 |                   <a href="{{ url_for('download_table', company_name=selected_company) }}" class="btn btn-success mt-3">Download Table</a>
643 |                   <div>
644 |                       {{ emissions_data | safe }}
645 |                   </div>
646 |               {% else %}
647 |                   <p>No table data available.</p>
648 |               {% endif %}
649 |           </div>
650 |           </div>
651 | 
652 |         <!-- Data Visualization Section -->
653 |          <div class="tab-pane fade" id="chart-content">
654 |         <div class="chart-container">
655 |             <h3>Emissions Data Visualization</h3>
656 |             <canvas id="emissionsChart"></canvas>
657 |         </div>
658 |            {% endif %}
659 |     </div>
660 |          <div class="page-bottom">
661 |       </div>
662 |      </div>
663 |   </form>
664 | 
665 | 
666 |      <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
667 |      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
668 |     <!-- React and ReactDOM via CDN -->
669 |     <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
670 |     <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
671 | 
672 |     <!-- Material-UI Core (includes CircularProgress) -->
673 |     <script crossorigin src="https://unpkg.com/@mui/material@latest/umd/material-ui.production.min.js"></script>
674 | 
675 |     <script>
676 |     document.addEventListener("DOMContentLoaded", function () {
677 |          const { CircularProgress } = window.MaterialUI || {};
678 |          const spinnerContainer = document.getElementById("loading-spinner");
679 |          const submitButton = document.getElementById("submit");
680 |          const form = document.querySelector("form");
681 | 
682 |          let spinnerInitialized = false;
683 |          function initializeSpinner() {
684 |              if (!spinnerInitialized && CircularProgress) {
685 |                  const spinner = React.createElement(CircularProgress, { color: "success", size: 24 });
686 |                  ReactDOM.render(spinner, spinnerContainer);
687 |                  spinnerInitialized = true;
688 |              }
689 |          }
690 |          function showSpinner() {
691 |              submitButton.disabled = true;
692 |              submitButton.innerText = "Searching...";
693 |              initializeSpinner();
694 |              spinnerContainer.style.display = "inline-block"; // Show only when "Searching..."
695 |          }
696 | 
697 |          function hideSpinner() {
698 |              submitButton.disabled = false;
699 |              submitButton.innerText = "Search";
700 |              spinnerContainer.style.display = "none";
701 |          }
702 |          form.addEventListener("submit", function () {
703 |              showSpinner();
704 |          });
705 | 
706 |          //Reset spinner if user navigates away or cancels search
707 |          submitButton.addEventListener("click", function () {
708 |              if (submitButton.innerText === "Searching...") {
709 |                  hideSpinner();
710 |              }
711 |          });
712 |         });
713 |     </script>
714 |     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
715 | <script>
716 | document.addEventListener("DOMContentLoaded", function () {
717 |     function extractDataFromTable() {
718 |         const table = document.querySelector(".selected-company table");
719 |         if (!table) {
720 |             console.error(" No table found in .selected-company!");
721 |             return;
722 |         }
723 | 
724 |         const rows = table.querySelectorAll("tr");
725 |         if (rows.length < 2) {
726 |             console.error(" Table has no data rows.");
727 |             return;
728 |         }
729 | 
730 |         // Extract Headers & Year Columns
731 |         const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.innerText.trim());
732 |         let yearHeaders = headers.filter(h => /^\d{4}$/.test(h));
733 |         let yearIndexes = headers.map((h, i) => (yearHeaders.includes(h) ? i : -1)).filter(i => i !== -1);
734 | 
735 |         if (yearHeaders.length === 0) {
736 |             console.error(" No valid year columns found.");
737 |             return;
738 |         }
739 | 
740 |         console.log(" Extracted Year Headers:", yearHeaders);
741 | 
742 |         let emissionsData = {};
743 |         let dataFound = false;
744 | 
745 |         rows.forEach((row, rowIndex) => {
746 |             if (rowIndex === 0) return;
747 |             const cells = row.querySelectorAll("td");
748 | 
749 |             let metricName = cells[1]?.innerText.trim() || `Metric ${rowIndex}`; // Extract actual metric name from column 2
750 |             let values = yearIndexes.map(colIndex => {
751 |                 let value = parseFloat(cells[colIndex]?.innerText.replace(/,/g, "").trim()) || 0;
752 |                 if (value !== 0) dataFound = true;
753 |                 return value;
754 |             });
755 | 
756 |             emissionsData[metricName] = values;
757 |         });
758 | 
759 |         if (dataFound) {
760 |             console.log(" Emissions Data:", emissionsData);
761 |             setTimeout(() => renderHistogram(yearHeaders, emissionsData), 500);
762 |         } else {
763 |             console.warn(" No valid emissions data found.");
764 |         }
765 |     }
766 | 
767 |     function renderHistogram(labels, emissionsData) {
768 |         const canvas = document.getElementById("emissionsChart");
769 |         if (!canvas) {
770 |             console.error(" No canvas element found!");
771 |             return;
772 |         }
773 | 
774 |         const ctx = canvas.getContext("2d");
775 | 
776 |         if (window.myChart) {
777 |             window.myChart.destroy();
778 |         }
779 | 
780 |         const datasets = Object.keys(emissionsData).map((metric, index) => ({
781 |             label: metric, // Use metric names from column 2 as legend labels
782 |             data: emissionsData[metric],
783 |             backgroundColor: getRandomColor(index),
784 |             borderWidth: 1
785 |         }));
786 | 
787 |         window.myChart = new Chart(ctx, {
788 |             type: "bar",
789 |             data: { labels: labels, datasets: datasets },
790 |             options: {
791 |                 responsive: true,
792 |                 plugins: {
793 |                     legend: { position: "top" },
794 |                     title: { display: true, text: "Emissions Over the Years" }
795 |                 },
796 |                 scales: {
797 |                     x: { title: { display: true, text: "Year" } },
798 |                     y: { title: { display: true, text: "Emissions" }, beginAtZero: true }
799 |                 }
800 |             }
801 |         });
802 |     }
803 | 
804 |     function getRandomColor(index) {
805 |         const colors = ["rgba(255, 99, 132, 0.7)", "rgba(54, 162, 235, 0.7)", "rgba(255, 206, 86, 0.7)"];
806 |         return colors[index % colors.length];
807 |     }
808 | 
809 |     extractDataFromTable();
810 | });
811 | 
812 | </script>
813 | </body>
814 | </html>
815 | 
```

src/templates/firstpage.html
```
1 | 
2 | 
3 | 
4 | 
5 | <!DOCTYPE html>
6 | <html lang="en">
7 | <head>
8 | <meta charset="UTF-8">
9 | <meta name="viewport" content="width=device-width, initial-scale=1.0">
10 | <title>EmissiTrack</title>
11 | <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
12 |  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
13 | <style>
14 |    html, body {
15 |       width: 100vw;  /* Ensures full width of the viewport */
16 |       overflow-x: hidden; /* Prevents horizontal scroll issues */
17 |       margin: 0;
18 |       padding: 0;
19 |       font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
20 |       background-color: #1C1C1C;
21 |       color: #333333;
22 |     }
23 | 
24 | 
25 |     .footer {
26 |        display: flex; flex-direction: column;
27 |        justify-content: space-around;
28 |        align-items: center;
29 |        background-color: #1C1C1C;
30 |        color: #F5F5F5;
31 |        padding: 20px;
32 |        flex-wrap: wrap;
33 |        text-align: center;
34 |     }
35 | 
36 | 
37 |     .footer-section {
38 |        flex: 1;
39 |        min-width: 200px;
40 |        margin: 10px;
41 |     }
42 | 
43 | 
44 | 
45 |     .footer-section ul {
46 |        list-style: none;
47 |        padding: 0;
48 |        display: flex;
49 |        gap:15px;
50 |        justify-content: center;
51 |     }
52 | 
53 | 
54 |     .footer-section ul li {
55 |        margin: 5px 0;
56 |     }
57 | 
58 | 
59 |     .footer-section ul li a {
60 |        color: #F5F5F5;
61 |        text-decoration: none;
62 |     }
63 | 
64 | 
65 |     .footer-section ul li a:hover {
66 |        text-decoration: underline;
67 |     }
68 | 
69 | 
70 |     .social-icons a {
71 |        font-size: 24px;
72 |        color: white;
73 |        margin: 0 10px;
74 |        text-decoration: none;
75 |     }
76 | 
77 | 
78 |     .social-icons a:hover {
79 |        color: #606060;
80 |     }
81 | 
82 | 
83 |     #description {
84 |          font-weight:bold;
85 |     }
86 | 
87 | 
88 |      #learnMoreSection p {
89 |          margin-bottom: 50px; /* Adjust this value as needed */
90 |      }
91 | 
92 | 
93 |      #learnMoreBtn {
94 |          position:relative;
95 |          left: 50%; /* Adjust this value to move it more to the right */
96 |          top:200px;
97 |          width: auto; /* Adjust width automatically based on content */
98 |          font-size: 20px; /* Increase font size */
99 |          padding: 16px 32px;
100 |          font-size: 20px; /* Increase font size */
101 |          text-align: center; /* Center the text */
102 |          display: inline-flex; /* Ensure proper button behavior */
103 |          width: auto; /* Adjust width automatically based on content */
104 |          height: 50px; /* Adjust height automatically */
105 |          white-space: nowrap;
106 |          color:white;
107 |          font-weight: bold;
108 |          align-items: center; /* Centers vertically */
109 |          justify-content: center; /* Centers horizontally */
110 |          transform: translateX(-50%);
111 |          left: 51%;
112 |          background-color:#063800;
113 | 
114 |      }
115 | 
116 | 
117 |      #learnMoreSection {
118 |          color:white;
119 |      }
120 | 
121 | 
122 |    .btn {/* Keeps the button fixed in one position */
123 |        bottom: 120px;
124 |        padding: 16px 32px;
125 |        font-size: 16px;
126 |        color:   #2D2D2D ;
127 |        background-color:white  ;
128 |        border: none;
129 |        border-radius: 8px;
130 |        text-decoration: none;
131 |        cursor: pointer;
132 |        justify-content: center;
133 |        transition: background-color 0.3s ease;
134 |        display: inline-flex; /* Enables flexbox */
135 |   align-items: center; /* Centers text vertically */
136 |   justify-content: center; /* Centers text horizontally */
137 | 
138 | 
139 |    }
140 | 
141 |    .btn:hover {
142 |        background-color: #3B6633;
143 |    }
144 | 
145 | 
146 | 
147 | 
148 |    h3{
149 |           color:  white ;
150 |           font-size: 24px;
151 |           font-weight: bold;
152 |           margin-top: 0px;
153 |    }
154 | 
155 | 
156 | 
157 | 
158 |    @keyframes moveText {
159 |        0% {
160 |            transform: translateX(0);
161 |        }
162 |        100% {
163 |            transform: translateX(-100%);
164 |        }
165 |    }
166 | 
167 | 
168 |   .content-container {
169 |   display: flex;
170 |   justify-content: center; /* Centers elements horizontally */
171 |   align-items: center; /* Aligns elements vertically */
172 |   gap: 200px; /* Space between the two elements */
173 |   max-width: 1100px; /* Prevents excessive stretching */
174 |   margin: 250px auto 50px;  /* Centers everything on the page */
175 |   flex-wrap: wrap; /* Ensures responsiveness */
176 |   position: relative;
177 | }
178 | 
179 | 
180 | 
181 | /* Ensure Both Containers Have the Same Size */
182 | #imageContainer, .information_container {
183 |   width: 450px; /* Same width for both */
184 |   height: 440px; /* Same height for both */
185 |   display: flex;
186 |   align-items: center;
187 |   justify-content: center;
188 |   border-radius: 10px; /* Ensures uniform rounded corners */
189 |   box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3); /* Matches the box-shadow */
190 | }
191 | 
192 |    .information_container{
193 |     background-color: #063800;
194 |     box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
195 |     text-align: center;
196 |     color: white;
197 |     align-items: center;
198 |     border-radius: 10px;
199 |     padding: 20px;
200 |     display: block;
201 |        white-space: pre-line;
202 |        font-size: 23px;
203 |        font-weight: bold;
204 |    }
205 | 
206 | 
207 |    #container {
208 |        width: 100%;
209 |        text-align: right; /* Aligns text to the right */
210 |        position: absolute;
211 |        top: 150px;
212 |    }
213 | 
214 | 
215 |    #imageContainer {
216 |        text-align: center;
217 |    }
218 | 
219 | 
220 |    #dynamicImage {
221 |        width: 450px; /* Adjust size as needed */
222 |        height: 440px;
223 |        border-radius: 10px;
224 | 
225 | 
226 | 
227 | 
228 |    }
229 | 
230 | 
231 |    #dynamicText {
232 |     z-index: 15;
233 |        font-size: 24px;
234 |         font-family: ;
235 |        display: inline-block;
236 |        padding: 10px;
237 |        color: #063800;
238 |        position: relative;
239 |        white-space: nowrap; /* Prevent text from wrapping */
240 |        animation: moveText 45s linear infinite alternate;
241 |    }
242 | 
243 | 
244 |    #dynamicTextContainer {
245 |         z-index: 10;
246 |        display: inline-block;
247 |        background-color: white; /* White background box */
248 |        padding: 10px 20px; /* Adds padding inside the box */
249 |        border-radius: 8px; /* Rounds the corners */
250 |        position: relative;
251 |        width:100%;
252 |        height:60px;
253 |        top:0px;
254 | 
255 |    }
256 | 
257 |    .div1 {
258 |     z-index: 10; /* Ensures it appears above other elements */
259 |     position: relative; /* Required for z-index to work */
260 |        height: 160px;
261 |        width: 100%; /* Ensure it takes full width */
262 |        margin: 0;
263 |        background-color: #063800;
264 |        display: flex;
265 |        align-items: center; /* Centers vertically */
266 |        justify-content: center; /* Centers horizontally */
267 |        box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
268 |    }
269 |    .catchy-phrase {
270 |    color: white;
271 |    font-size: 20px;
272 |    margin-top: 5px; /* Adjust spacing between header and phrase */
273 | }
274 | 
275 | 
276 |     .hamburger-icon {
277 |         font-size: 30px;
278 |         color: white;
279 |         cursor: pointer;
280 |         position: absolute;
281 |         top: 20px;
282 |         left: 20px;
283 |     }
284 | 
285 |     .sidebar1 {
286 |         display: flex;
287 |         flex-direction: column;
288 |         align-items: center;
289 |         justify-content: center;
290 |         border: 1px solid #ccc;
291 |         border-radius: 8px;
292 |         margin-left: 50px;
293 |         float: left;
294 |         width: 250px;
295 |         height: 150px;
296 |         padding: 20px;
297 |         background-color: white;
298 |         color: white;
299 | 
300 |     }
301 |     .navigation {
302 |         position: fixed; /* Sticks to the side */
303 |         left: 0;
304 |         top: 0;
305 |         width: 100px;
306 |         height: 100vh; /* 100% of the viewport height */
307 |         background:  #063800;
308 |         box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25),
309 |                     inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2),
310 |                     inset -5px -5px 15px rgba(0,0,0,0.75);
311 |         display: flex;
312 |         justify-content: center;
313 |         align-items: center;
314 |         flex-direction: column;
315 |         gap: 10px;
316 |         transform: translateX(-100%);
317 |         transition: transform 0.3s ease;
318 | }
319 | 
320 |      .navigation.show {
321 |         transform: translateX(0);
322 |     }
323 | 
324 |     .navigation li {
325 |         position:relative;
326 |         list-style:none;
327 |         width:80px;
328 |         height: 80px;
329 |         display:flex;
330 |         justify-content:center;
331 |         margin: 0 5px;
332 | 
333 |     }
334 | 
335 |     .navigation li::before {
336 |         content: '';
337 |         position: absolute;
338 |         top:calc(50% - 2.5px);
339 |         left: 20px;
340 |         width:5px;
341 |         height: 5px;
342 |         border-radius:50%;
343 |         transition:0.5s;
344 | 
345 |     }
346 | 
347 |     .navigation li.active::before {
348 |         background:white;
349 |         box-shadow:0 0 5px white,
350 |         0 0 10px white,
351 |         0 0 20px white,
352 |         0 0 30px white,
353 |         0 0 40px white;
354 |     }
355 | 
356 |     .navigation li a {
357 |         display:flex;
358 |         justify-content:center;
359 |         align-items:center;
360 |         flex-direction:column;
361 |         text-decoration:none;
362 |     }
363 | 
364 |     .navigation li a .icon {
365 |         color: white;
366 |         transition: 0.5s;
367 |         transition-delay: 0.2s;
368 |         font-size: 1.5em; /* Adjust this value to your preference */
369 |     }
370 | 
371 |     .navigation li.active a .icon::before{
372 |         transform:scale(1);
373 | 
374 |     }
375 | 
376 |     .navigation li a .text{
377 |         position: absolute;
378 |         left:130px;
379 |         font-size:1.25em;
380 |         color:white;
381 |         visibility:hidden;
382 |         transition:0.5s;
383 | 
384 | 
385 |     }
386 | 
387 | 
388 |     .navigation li a .text::before {
389 |         content: '';
390 |         position: absolute;
391 |         top: 50%
392 |         left: -4px;
393 |         transform:translateY(-50%) rotate(45deg);
394 |         width:10px;
395 |         height:10px;
396 |     }
397 | 
398 |     .navigation li:hover a .text {
399 |         visibility: visible;
400 |     }
401 |     .logo {
402 |      z-index: 20;
403 |      max-height: 100px;
404 |      width: auto;
405 |      top: 30px;
406 |      left: 200px;
407 |      margin-right: 10px;
408 |     }
409 | 
410 |    *{
411 |          margin: 0;
412 |          padding: 0;
413 |          box-sizing: border-box;
414 |          font-family: sans-serif;
415 |      }
416 | 
417 | 
418 |      .main{
419 |          display: flex;
420 |          flex-direction: column;
421 |          align-items: center;
422 |          justify-content: center;
423 |          width: 100%;
424 |          margin-top: 90px;
425 |      }
426 | 
427 |      .full-boxer{
428 |          display: flex;
429 |          flex-wrap: wrap;
430 |          justify-content: center;
431 |          align-items: center;
432 |          width: 100%;
433 |      }
434 | 
435 | 
436 |      .box-top{
437 |          display: flex;
438 |          justify-content: space-between;
439 |          align-items: center;
440 |          margin-bottom: 20px;
441 |      }
442 | 
443 |      .comment-box:hover{
444 |          margin-top: 12px;
445 |      }
446 | 
447 |       .comments-container {
448 |      background-color: #414340;
449 |      padding: 30px;
450 |      border-radius: 10px;
451 |      box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
452 |      margin: 10px auto;
453 |      width: 80%;
454 |  }
455 |  .full-boxer {
456 |      display: flex;
457 |      flex-wrap: wrap;
458 |      justify-content: space-around;
459 |  }
460 |  .comment-box {
461 |      background: white;
462 |      padding: 20px;
463 |      margin: 15px;
464 |      border-radius: 8px;
465 |      cursor: pointer;
466 |      box-shadow: 3px 3px 25px rgba(0,0,0,0.3);
467 |      width: 22%;
468 | 
469 |  }
470 | 
471 | 
472 |      .Profile{
473 |          display: flex;
474 |          align-items: center;
475 |      }
476 | 
477 | 
478 |      .profile-image{
479 |          width: 70px;
480 |          height: 70px;
481 |          box-shadow: 2px 2px 30px rgba(0,0,0,0.3);
482 |          overflow: hidden;
483 |          border-radius: 50%;
484 |          margin-right: 10px;
485 |      }
486 | 
487 | 
488 |      .profile-image img{
489 |          width: 100%;
490 |          height: 100%;
491 |          object-fit: cover;
492 |          object-position: center;
493 |      }
494 | 
495 |      .Name{
496 |          display: flex;
497 |          flex-direction: column;
498 |          margin-left: 10px;
499 |      }
500 | 
501 | 
502 |      .Name strong{
503 |          color: black;
504 |          font-size: 18px;
505 |      }
506 | 
507 |      .Name span{
508 |          color: gray;
509 |          margin-top: 2px;
510 |      }
511 | 
512 |      .comment p{
513 |          color: black;
514 |      }
515 |      .padding-for-info {
516 |   max-width: 1100px;
517 |   padding: 0 40px;
518 |   text-align: center;
519 |   margin: 0 auto;
520 | 
521 | }
522 | 
523 |     .centered-link {
524 |     text-align: center;
525 |     margin-top: 20px;
526 | }
527 | 
528 | .centered-link a {
529 |     font-size: 18px;
530 |     color: white; /* Change to any preferred color */
531 |     text-decoration: none;
532 | 
533 | }
534 | 
535 | .centered-link a:hover {
536 |     color:white; /* Color on hover */
537 |     text-decoration: underline;
538 | }
539 | 
540 | </style>
541 | </head>
542 | <body>
543 | <div class="div1">
544 |    <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
545 |     <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
546 |    </div>
547 |  <div class="catchy-phrase">
548 |      <h2>Your Carbon Insights, Simplified</h2></div>
549 |  <a href="#learnMoreSection" class="btn" id="learnMoreBtn">Learn More  <i class="fa-solid fa-arrow-down"></i></a>
550 | <script>
551 |  document.getElementById("learnMoreBtn").addEventListener("click", function(event) {
552 |      event.preventDefault(); // Prevent default anchor behavior
553 |      document.getElementById("learnMoreSection").scrollIntoView({
554 |          behavior: "smooth"
555 |      });
556 |  });
557 | </script>
558 | <div class="centered-link">
559 |     <a href="emissions_map"> View the top 40 companies along with their ESG ratings.</a>
560 | </div>
561 | 
562 | 
563 | <div class="content-container">
564 |   <div id="imageContainer">
565 |       <img id="dynamicImage" src="{{ url_for('static', filename='images/image1.png') }}" alt="image1">
566 |   </div>
567 | 
568 | <div class="information_container">
569 | <h6 id="description">
570 |    EmissiTrack helps you effortlessly retrieve and analyze Scope 1 and Scope 2 carbon emissions data for listed companies using ISINs or company names. With real-time data sourcing from CSR reports, interactive filtering, and easy downloads, EmissiTrack empowers businesses and investors to make informed sustainability decisions.
571 | </h6>
572 | <br>
573 | <a href="/test" class="btn">Start Using for Free</a>
574 | </div>
575 | 
576 | 
577 | 
578 | 
579 | 
580 | 
581 | 
582 | 
583 | </div>
584 | <script>
585 |    document.addEventListener("DOMContentLoaded", function () {
586 |        const h6Element = document.getElementById("description");
587 |        const words = h6Element.innerText.split(" ");
588 |        let formattedText = "";
589 |        for (let i = 0; i < words.length; i++) {
590 |            formattedText += words[i] + " ";
591 |            if ((i + 1) % 6 === 0) {
592 |                formattedText += "<br>"; // Insert line break after every 6 words
593 |            }
594 |        }
595 |        h6Element.innerHTML = formattedText.trim();
596 |    });
597 | </script>
598 | <div id="container">
599 |    <div id="dynamicTextContainer">
600 |        <p id="dynamicText">Dynamically Filter Companies</p>
601 |    </div>
602 | </div>
603 | <script>
604 |    document.addEventListener("DOMContentLoaded", function () {
605 |        const wordsArray = [
606 |            "Retrieve Scope 1 and Scope 2 emissions data",
607 |            "Retrieve CSR Reports",
608 |            "Sustainability Reporting",
609 |            "ESG analysis"
610 |        ];
611 |        const dynamicText = document.getElementById("dynamicText");
612 |        let textContent = "";
613 |        // Create a long scrolling text by repeating words with spacing
614 |        for (let i = 0; i < wordsArray.length; i++) {
615 |            textContent += wordsArray[i] + " - ";
616 |        }
617 |        // Duplicate the text to create a seamless scrolling effect
618 |        dynamicText.innerHTML = textContent + textContent;
619 |    });
620 |    // Image Slideshow Logic
621 |    const images = ["image1.png", "image2.png", "image3.png"];
622 |    let imageIndex = 0;
623 |    const imgElement = document.getElementById("dynamicImage");
624 |    window.onload = function() {
625 |          document.getElementById("dynamicImage").src = "{{ url_for('static', filename='images/image1.png') }}";
626 |      };
627 |    function changeImage() {
628 |        imgElement.src = "{{ url_for('static', filename='images/') }}" + images[imageIndex];
629 |        imageIndex = (imageIndex + 1) % images.length;
630 |    }
631 |    setInterval(changeImage, 3000); // Change image every 3 seconds
632 | </script>
633 |  <section class="main">
634 |      <h4 style="color:white; margin-top:50px; font-weight:bold;">Learn more from our users</h4>
635 |      <div class="comments-container">
636 |      <div class="full-boxer">
637 |          <div class="comment-box">
638 |              <div class="box-top">
639 |                  <div class="Profile">
640 |                      <div class="profile-image">
641 |                          <img src="{{ url_for('static', filename='images/1.png') }}" alt="1">
642 |                      </div>
643 |                      <div class="Name">
644 |                          <strong>Ranidi Lochana</strong>
645 |                          <span>@Ranidi Lochana</span>
646 |                      </div>
647 |                  </div>
648 |              </div>
649 |              <div class="comment">
650 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
651 |                  <p>This tool is an excellent resource for academic research on corporate carbon footprints. The ability to retrieve and categorize emissions data dynamically, without spending hours on manual searches, is a huge time-saver. The accuracy and cleaning of the data are impressive, and the ability to export structured datasets makes it easy to conduct further analysis. Nice experience and efficient results, would recommend!</p>
652 |              </div>
653 |          </div>
654 |          <div class="comment-box">
655 |              <div class="box-top">
656 |                  <div class="Profile">
657 |                      <div class="profile-image">
658 |                          <img src="{{ url_for('static', filename='images/2.png') }}" alt="2">
659 |                      </div>
660 |                      <div class="Name">
661 |                          <strong>Senuda Dilwan</strong>
662 |                          <span>@senuda dilwan</span>
663 |                      </div>
664 |                  </div>
665 |              </div>
666 |              <div class="comment">
667 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
668 |                  <p>As someone responsible for reporting and benchmarking sustainability efforts, I find this tool incredibly valuable. It provides a centralized source of emissions data, reducing the hassle of manually tracking down reports from multiple sources. The user-friendly interface and downloadable CSV format are particularly helpful for integrating data into internal reports. This is the future of corporate carbon tracking!</p>
669 |              </div>
670 |          </div>
671 | 
672 |          <div class="comment-box">
673 |              <div class="box-top">
674 |                  <div class="Profile">
675 |                      <div class="profile-image">
676 |                          <img src="{{ url_for('static', filename='images/3.png') }}" alt="3">
677 |                      </div>
678 |                      <div class="Name">
679 |                          <strong>Rumali fernando</strong>
680 |                          <span>@Rumali fernando</span>
681 |                      </div>
682 |                  </div>
683 |              </div>
684 |              <div class="comment">
685 |                  <p>⭐️⭐️⭐️⭐️⭐️</p>
686 |                  <p>This platform is a game-changer for ESG research! Finding Scope 1 and Scope 2 emissions data used to be a tedious, manual process, requiring hours of combing through CSR reports. This tool simplifies everything—just input an ISIN or company name, and the latest emissions data is instantly retrieved, cleaned, and categorized. The visualization features are a great bonus, making trend analysis much easier. Highly recommend!</p>
687 | 
688 |              </div>
689 |          </div>
690 | 
691 |          <div class="comment-box">
692 |              <div class="box-top">
693 |                  <div class="Profile">
694 |                      <div class="profile-image">
695 |                          <img src="{{ url_for('static', filename='images/4.png') }}" alt="4">
696 |                      </div>
697 |                      <div class="Name">
698 |                          <strong>Midinu Thiranjana</strong>
699 |                          <span>@Midinu Thiranjana</span>
700 |                      </div>
701 |                  </div>
702 |              </div>
703 |              <div class="comment">
704 |                  <p>⭐️⭐️⭐️⭐️⭐</p>
705 |                  <p>A very useful tool for investment decision-making. Reliable emissions data is critical for evaluating companies from an ESG perspective, and this platform makes it easy to access. The filtering and download options allow for quick integration with our internal models. The chatbot offered by the pro account is very useful and enables me to find data more efficiently. </p>
706 | 
707 |              </div>
708 |          </div>
709 |      </div>
710 |      </div>
711 |  </section>
712 |  <section id="learnMoreSection">
713 |   <div class="padding-for-info">
714 |      <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack?</h2>
715 |      <p style="text-align:center;">A Smart, Scalable, and Dynamic Solution for Tracking Corporate Carbon Footprints.</p>
716 | 
717 | <p style="text-align:center;">The Carbon Emissions Tracker is a web-based platform designed to dynamically retrieve, categorize, and visualize corporate carbon emissions data for listed companies within the MSCI All World Index. This tool empowers users to access the latest Scope 1 (direct emissions) and Scope 2 (indirect emissions from purchased electricity) data from publicly available sources such as Corporate Social Responsibility (CSR) reports, government databases, and other sustainability disclosures.</p>
718 | 
719 | <p style="text-align:center;">In addition to emissions data, the platform features a real-time news feed with top headlines for each company, keeping users updated on sustainability-related developments. Users can also filter companies by sector, country, industry, and other key parameters to refine their searches and insights.</p>
720 |      <p style="text-align:center;">Emissions data can be visualized in interactive bar charts or structured in a detailed table format. </p>
721 |      <p style="text-align:center;">A premium membership unlocks access to an AI-powered chatbot that assists users with data retrieval, insights, and sustainability analysis.
722 | The chatbot can answer queries, provide company-specific emissions insights, suggest comparisons, and summarize trends.</p>
723 |      </div>
724 | 
725 |  </section>
726 |  <footer class="footer">
727 | 
728 | 
729 |    <div class="footer-section">
730 |        <ul>
731 |            <li><a href="#">About Us</a></li>
732 |            <li><a href="#">Contact</a></li>
733 |            <li><a href="#">Terms of Use</a></li>
734 |            <li><a href="#">Privacy Policy</a></li>
735 |        </ul>
736 |    </div>
737 | 
738 | 
739 |    <div class="footer-section">
740 |        <div class="social-icons">
741 |            <a href="#"><i class="fab fa-facebook"></i></a>
742 |            <a href="https://www.linkedin.com/in/budha/"><i class="fab fa-linkedin"></i></a>
743 |            <a href=""><i class="fas fa-envelope"></i></a>
744 |        </div>
745 |    </div>
746 | </footer>
747 | 
748 | 
749 | <section>
750 |    <p style="text-align:center;color:white">&copy; 2024 EmissiTrack</p>
751 | </section>
752 | </body>
753 | </html>
754 | 
755 | 
756 | 
757 | 
758 | 
759 | 
760 | 
761 | 
762 | 
763 | 
764 | 
765 | 
```

src/templates/index.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |     <meta charset="UTF-8">
5 |     <title>My ESG App</title>
6 |     <!-- Add Font Awesome for icons -->
7 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
8 |     <!-- Marked.js for client-side Markdown->HTML conversion -->
9 |     <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
10 |     <!-- Chart.js for the line chart -->
11 |     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
12 |     <!-- Optional: chartjs-plugin-annotation -->
13 |     <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@2"></script>
14 | 
15 |     <!-- Updated, more polished CSS -->
16 |     <style>
17 |       :root {
18 |         --primary-green: #1a4f1a;
19 |         --secondary-green: #2f8f2f;
20 |         --accent-green: #e8f5e9;
21 |         --text-dark: #2c3e50;
22 |       }
23 | 
24 | 
25 |       body {
26 |        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
27 |        background: linear-gradient(to bottom right, #f8fcf8, #e8f5e9);
28 |        margin: 0;
29 |        color: #2c3e50;
30 |      }
31 |      .content {
32 |       padding: 30px;
33 |     }
34 | 
35 | 
36 | 
37 | 
38 |     .logo-header-container {
39 |           z-index: 10;
40 |           position: relative;
41 |           height: 160px;
42 |           width: 100%;
43 |           background-color: #063800;
44 |           display: flex;
45 |           align-items: center; /* Align items vertically */
46 |           justify-content: center; /* Center items horizontally */
47 |           gap: 20px; /* Add spacing between logo and text */
48 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
49 |           text-align: center;
50 |         }
51 | 
52 | 
53 |     .logo {
54 |           max-height: 100px;
55 |           width: auto;
56 |         }
57 | 
58 | 
59 |     .div1 {
60 |           display: flex;
61 |           flex-direction: column; /* Stack heading and phrase */
62 |           align-items: center;
63 |           justify-content: center;
64 |         }
65 | 
66 |     .catchy-phrase {
67 |           color: white;
68 |           font-size: 20px;
69 |           margin-top: 5px; /* Adjust spacing between header and phrase */
70 |         }
71 | 
72 |     .hamburger-icon {
73 |               font-size: 30px;
74 |               color: white;
75 |               cursor: pointer;
76 |               position: absolute;
77 |               top: 20px;
78 |               left: 20px;
79 |               z-index: 100;
80 |           }
81 | 
82 | 
83 |     .report-container {
84 |               color: #1C1C1C;
85 |               display: flex;
86 |               padding: 10px;
87 |               gap: 30px;
88 |               align-items: center;
89 |               justify-content: center;
90 |               margin-bottom: 30px;
91 |           }
92 | 
93 |     .sidebar1 {
94 |               display: flex;
95 |               flex-direction: column;
96 |               align-items: center;
97 |               justify-content: center;
98 |               border: 1px solid #ccc;
99 |               border-radius: 8px;
100 |               margin-left: 50px;
101 |               float: left;
102 |               width: 250px;
103 |               height: 150px;
104 |               padding: 20px;
105 |               background-color: white;
106 |               color: white;
107 |               z-index: 1000;
108 | 
109 |           }
110 | 
111 | 
112 |     .navigation {
113 |       position: fixed; /* Sticks to the side */
114 |       left: 0;
115 |       top: 0;
116 |       width: 100px;
117 |       height: 100vh; /* 100% of the viewport height */
118 |       background:  #063800;
119 |       box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25),
120 |                   inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2),
121 |                   inset -5px -5px 15px rgba(0,0,0,0.75);
122 |       display: flex;
123 |       justify-content: center;
124 |       align-items: center;
125 |       flex-direction: column;
126 |       gap: 10px;
127 |       transform: translateX(-100%);
128 |       transition: transform 0.3s ease;
129 |     }
130 | 
131 | 
132 |    /* Class to toggle menu visibility */
133 |    .navigation.show {
134 |               transform: translateX(0);
135 |    }
136 | 
137 | 
138 | 
139 |    .navigation li {
140 |               position:relative;
141 |               list-style:none;
142 |               width:80px;
143 |               height: 80px;
144 |               display:flex;
145 |               justify-content:center;
146 |               margin: 0 5px;
147 |           }
148 | 
149 | 
150 |    .navigation li::before {
151 |               content: '';
152 |               position: absolute;
153 |               top:calc(50% - 2.5px);
154 |               left: 20px;
155 |               width:5px;
156 |               height: 5px;
157 |               border-radius:50%;
158 |               transition:0.5s;
159 | 
160 |           }
161 | 
162 | 
163 |    .navigation li.active::before {
164 |               background:white;
165 |               box-shadow:0 0 5px white,
166 |               0 0 10px white,
167 |               0 0 20px white,
168 |               0 0 30px white,
169 |               0 0 40px white;
170 |           }
171 | 
172 | 
173 | 
174 | 
175 |    .navigation li a {
176 |               display:flex;
177 |               justify-content:center;
178 |               align-items:center;
179 |               flex-direction:column;
180 |               text-decoration:none;
181 |           }
182 | 
183 | 
184 | 
185 | 
186 |    .navigation li a .icon {
187 |               color: white;
188 |               transition: 0.5s;
189 |               transition-delay: 0.2s;
190 |               font-size: 1.5em;
191 |           }
192 | 
193 | 
194 | 
195 | 
196 |    .navigation li.active a .icon::before{
197 |               transform:scale(1);
198 | 
199 |           }
200 | 
201 | 
202 | 
203 | 
204 |    .navigation li a .text{
205 |               position: absolute;
206 |               left:130px;
207 |               font-size:1.25em;
208 |               color:white;
209 |               visibility:hidden;
210 |               transition:0.5s;
211 |           }
212 | 
213 | 
214 | 
215 | 
216 |    .navigation li a .text::before {
217 |               content: '';
218 |               position: absolute;
219 |               top: 50%;
220 |               left: -4px;
221 |               transform:translateY(-50%) rotate(45deg);
222 |               width:10px;
223 |               height:10px;
224 |           }
225 | 
226 | 
227 | 
228 | 
229 |    .navigation li:hover a .text {
230 |               visibility: visible;
231 |           }
232 | 
233 | 
234 |    .logout {
235 |             z-index: 15;
236 |             position: absolute;
237 |             top: 20px;
238 |             right: 20px;
239 |             background-color: white;
240 |             color:  #063800;
241 |             border: none;
242 |             padding: 20px 35px;
243 |             border-radius: 4px;
244 |             font-size: 16px;
245 |             cursor: pointer;
246 |           }
247 | 
248 |    .logout:hover {
249 |              background-color: #145a32;
250 |             color: white;
251 |     }
252 | 
253 | 
254 |     h1 {
255 |         color: var(--primary-green);
256 |         margin-top: 0;
257 |         font-weight: 600;
258 |         margin-bottom: 25px;
259 |         font-size: 2.2em;
260 |         letter-spacing: -0.5px;
261 |       }
262 | 
263 | 
264 |     h2 {
265 |         color: var(--primary-green);
266 |         font-weight: 600;
267 |         font-size: 1.6em;
268 |         margin-bottom: 20px;
269 |         padding-bottom: 10px;
270 |         border-bottom: 2px solid #e0f0e0;
271 |       }
272 | 
273 | 
274 |     .column {
275 |         float: left;
276 |         width: 45%;
277 |         margin: 1%;
278 |         background: white;
279 |         border-radius: 12px;
280 |         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1);
281 |         padding: 25px;
282 |         box-sizing: border-box;
283 |         min-height: 400px;
284 |         transition: transform 0.3s ease, box-shadow 0.3s ease;
285 |       }
286 | 
287 | 
288 |     .column:hover {
289 |         transform: translateY(-5px);
290 |         box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
291 |       }
292 | 
293 | 
294 | 
295 |     #raw-markdown {
296 |         display: none;
297 |       }
298 | 
299 | 
300 |       #rendered-tables table {
301 |         border-collapse: collapse;
302 |         width: 100%;
303 |         margin: 20px 0;
304 |         border-radius: 8px;
305 |         overflow: hidden;
306 |         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
307 |       }
308 | 
309 | 
310 |       #rendered-tables th,
311 |       #rendered-tables td {
312 |         border: 1px solid #e0f0e0;
313 |         padding: 12px;
314 |         text-align: left;
315 |       }
316 | 
317 | 
318 |       #rendered-tables th {
319 |         background-color: var(--secondary-green);
320 |         color: white;
321 |         font-weight: 600;
322 |         text-transform: uppercase;
323 |         font-size: 0.9em;
324 |         letter-spacing: 0.5px;
325 |       }
326 | 
327 | 
328 |       /* Chart box wrapper */
329 |       .chart-box {
330 |         border: 1px solid #d4edd4;
331 |         background: linear-gradient(to bottom, #f9fff9, #ffffff);
332 |         border-radius: 12px;
333 |         padding: 0;
334 |         margin-bottom: 25px;
335 |         overflow: hidden;
336 |         box-shadow: 0 3px 6px rgba(0,0,0,0.05);
337 |       }
338 | 
339 | 
340 |       .chart-box h3 {
341 |         background: var(--primary-green);
342 |         color: white;
343 |         margin: 0;
344 |         padding: 15px;
345 |         font-size: 1.1em;
346 |         text-transform: uppercase;
347 |         letter-spacing: 0.5px;
348 |       }
349 | 
350 | 
351 |       /* RAG status styling */
352 |       #rag-status {
353 |         background: var(--accent-green);
354 |         padding: 10px 15px;
355 |         border-radius: 6px;
356 |         color: var(--primary-green);
357 |         font-weight: 600;
358 |         display: flex;
359 |         align-items: center;
360 |         gap: 10px;
361 |       }
362 | 
363 | 
364 |       #rag-status::before {
365 |         content: '';
366 |         width: 12px;
367 |         height: 12px;
368 |         border-radius: 50%;
369 |         background: var(--secondary-green);
370 |         display: inline-block;
371 |       }
372 | 
373 | 
374 |       /* Form styling */
375 |       form {
376 |         background: #fff;
377 |         padding: 20px;
378 |         border-radius: 8px;
379 |         box-shadow: 0 2px 10px rgba(0,0,0,0.05);
380 |         margin-bottom: 30px;
381 |       }
382 |       .search-container {
383 |        display: flex;
384 |        align-items: center;
385 |        justify-content: center;
386 |        gap: 10px;
387 |       }
388 | 
389 | 
390 |       .search-container label {
391 |        font-size: 1.2em;
392 |        color: #1C1C1C;;
393 |       }
394 |        #company_input {
395 |         width: 95%;
396 |         padding: 12px;
397 |         border: 2px solid #d4edd4;
398 |         border-radius: 6px;
399 |         margin-bottom: 15px;
400 |         transition: border-color 0.3s ease;
401 |         font-size: 1.2em;
402 |       }
403 | 
404 | 
405 |       #submit-btn {
406 |         background: linear-gradient(to right, var(--secondary-green), var(--primary-green));
407 |         padding: 12px 25px;
408 |         font-weight: 600;
409 |         text-transform: uppercase;
410 |         letter-spacing: 0.5px;
411 |         color: #fff;
412 |         border: none;
413 |         border-radius: 4px;
414 |         cursor: pointer;
415 |         transition: transform 0.2s ease;
416 |         font-size: 1.2em;
417 |       }
418 | 
419 | 
420 |       #submit-btn:hover {
421 |         transform: scale(1.02);
422 |       }
423 | 
424 | 
425 |       /* Chat form styling */
426 |       #question-form {
427 |         display: flex;
428 |         gap: 10px;
429 |         margin-top: 15px;
430 |       }
431 | 
432 | 
433 |       #question-input {
434 |         flex: 1;
435 |         padding: 12px;
436 |         border: 2px solid #d4edd4;
437 |         border-radius: 8px;
438 |         font-size: 1em;
439 |         transition: all 0.3s ease;
440 |       }
441 | 
442 | 
443 |       #question-input:focus {
444 |         outline: none;
445 |         border-color: #70c270;
446 |       }
447 | 
448 | 
449 |       #question-form button {
450 |         background: var(--secondary-green);
451 |         color: #fff;
452 |         border: none;
453 |         border-radius: 4px;
454 |         padding: 12px 20px;
455 |         font-weight: 600;
456 |         cursor: pointer;
457 |         transition: background 0.3s ease;
458 |       }
459 | 
460 | 
461 |       #question-form button:hover {
462 |         background-color: var(--primary-green);
463 |       }
464 | 
465 | 
466 |       /* Chat Q&A bubbles */
467 |       #chat-output {
468 |         margin-top: 15px;
469 |       }
470 | 
471 | 
472 |       #chat-output div {
473 |         background-color: #e9ffe9;
474 |         border: 1px solid #c7edc7;
475 |         margin-bottom: 10px;
476 |         padding: 10px;
477 |         border-radius: 4px;
478 |         white-space: normal;
479 |       }
480 | 
481 | 
482 |       #chat-output table {
483 |         border-collapse: collapse;
484 |         width: 100%;
485 |         margin: 10px 0;
486 |       }
487 | 
488 | 
489 |       #chat-output th,
490 |       #chat-output td {
491 |         border: 1px solid #d4edd4;
492 |         padding: 8px;
493 |         text-align: left;
494 |       }
495 | 
496 | 
497 |       #chat-output th {
498 |         background-color: #f1f9f1;
499 |       }
500 | 
501 | 
502 |       /* Loading spinner */
503 |       #loading-spinner {
504 |         display: none;
505 |         text-align: center;
506 |         margin: 30px 0;
507 |       }
508 | 
509 | 
510 |       .spinner {
511 |         width: 40px;
512 |         height: 40px;
513 |         margin: 0 auto;
514 |         border: 4px solid #f3f3f3;
515 |         border-top: 4px solid var(--secondary-green);
516 |         border-radius: 50%;
517 |         animation: spin 1s linear infinite;
518 |       }
519 | 
520 | 
521 |       @keyframes spin {
522 |         0% { transform: rotate(0deg); }
523 |         100% { transform: rotate(360deg); }
524 |       }
525 | 
526 | 
527 |       .clear { clear: both; }
528 |     </style>
529 | </head>
530 | <body>
531 | 
532 | 
533 |  <div class="logo-header-container">
534 |    <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
535 |    <div class="div1">
536 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
537 |        <p class="catchy-phrase">Advanced Search</p>
538 |    </div>
539 | </div>
540 | 
541 | 
542 | <div class="hamburger-icon">&#9776;</div>
543 |        <ul class="navigation">
544 |            <li class="active">
545 |                <a href="{{url_for('firstpage')}}">
546 |                    <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
547 |                    <span class="text">EmissiTrack</span>
548 |                </a>
549 |            </li>
550 |            <li>
551 |                <a href="{{url_for('advanced_search')}}">
552 |                    <span class="icon"> <ion-icon name="information-circle-outline"></ion-icon></span>
553 |                    <span class="text">Advanced Search</span>
554 |                </a>
555 |            </li>
556 |            <li>
557 |                <a href="{{url_for('home')}}">
558 |                    <span class="icon"> <ion-icon name="finger-print-outline"></ion-icon></span>
559 |                    <span class="text">Premium Page</span>
560 |                </a>
561 |            </li>
562 |            <li>
563 |                <a href="{{url_for('login')}}">
564 |                    <span class="icon"><ion-icon name="settings-outline"></ion-icon></span>
565 |                    <span class="text">Register/Login</span>
566 |                </a>
567 |            </li>
568 |            <li>
569 |                <a href="{{url_for('firstpage')}}">
570 |                    <span class="icon"><ion-icon name="log-out-outline"></ion-icon></span>
571 |                    <span class="text">Logout</span>
572 |                </a>
573 |            </li>
574 |        </ul>
575 |        <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
576 |            <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
577 |            <script>
578 |                document.addEventListener('DOMContentLoaded', function () {
579 |                    const hamburger = document.querySelector('.hamburger-icon');
580 |                    const navigation = document.querySelector('.navigation');
581 |                    let isOpen = false;
582 |                    hamburger.addEventListener('click', function () {
583 |                        // Toggle menu visibility
584 |                        isOpen = !isOpen;
585 |                        if (isOpen) {
586 |                            navigation.classList.add('show');
587 |                        } else {
588 |                            navigation.classList.remove('show');
589 |                        }
590 |                    });
591 |                    // Keep your existing navigation item click event listener
592 |                    let list = document.querySelectorAll('.navigation li');
593 |                    function activeLink() {
594 |                        list.forEach((item) => item.classList.remove('active'));
595 |                        this.classList.add('active');
596 |                    }
597 |                    list.forEach((item) => item.addEventListener('click', activeLink));
598 |                });
599 |            </script>
600 |  <div class="content">
601 |  <!-- Add search form at the top -->
602 |  <form method="POST" style="margin-bottom: 20px;">
603 |    <div class="search-container">
604 |    <label for="company_input">Enter Company, ISIN, or Ticker:</label>
605 |    <input type="text" id="company_input" name="company_name" required>
606 | 
607 | 
608 |    <label style="margin-left: 10px;"></label>
609 |    <label>
610 |      <input type="radio" name="idType" value="name" checked> Name
611 |    </label>
612 |    <label>
613 |      <input type="radio" name="idType" value="ticker"> Ticker
614 |    </label>
615 |    <label>
616 |      <input type="radio" name="idType" value="isin"> ISIN
617 |    </label>
618 |    <br><br>
619 |    <button type="submit" id="submit-btn">Search</button>
620 |  </div>
621 |  </form>
622 | 
623 | 
624 |  <!-- Updated loading spinner (initially hidden by CSS) -->
625 |  <div id="loading-spinner">
626 |    <div class="spinner"></div>
627 |    <p>Analyzing ESG Data...</p>
628 |  </div>
629 | 
630 | 
631 |  <!-- Wrap existing content in conditional -->
632 |  {% if company_name %}
633 |    <h1>
634 |      <i class="fas fa-leaf"></i>
635 |      ESG Insights: {{ company_name }}
636 |    </h1>
637 |  {% else %}
638 |    <h1>
639 |      <i class="fas fa-search"></i>
640 |      Discover ESG Analytics
641 |    </h1>
642 |  {% endif %}
643 | 
644 | 
645 |  {% if company_name %}
646 | 
647 | 
648 | 
649 | 
650 |  <div class="report-container">
651 |    {% if report_url %}
652 |        <p>Latest ESG Report Link for {{company_name}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
653 | 
654 | 
655 | 
656 | 
657 |    {% else %}
658 |        <p>No report found.</p>
659 |    {% endif %}
660 | </div>
661 | 
662 | 
663 |    <!-- Left column: LLM data (tables) -->
664 |    <div class="column">
665 |      <h2>GHG Emissions Tables (tCO2e) 🌱</h2>
666 | 
667 | 
668 |      <!-- Hidden raw markdown from the LLM -->
669 |      <div id="raw-markdown">{{ llm_markdown }}</div>
670 | 
671 | 
672 |      <!-- We'll display the rendered HTML tables here -->
673 |      <div id="rendered-tables"></div>
674 |    </div>
675 | 
676 | 
677 |    <!-- Right column: Chart + RAG chatbot -->
678 |    <div class="column">
679 |      <!-- Chart box above the chatbot -->
680 |      <div class="chart-box">
681 |        <h3>Emissions Over Time</h3>
682 |        <canvas id="keyTableChart" width="300" height="200"></canvas>
683 |      </div>
684 | 
685 | 
686 |      <h2>Chatbot 🌍</h2>
687 |      <div id="rag-status">Initializing RAG...</div>
688 | 
689 | 
690 |      <form id="question-form">
691 |        <input type="text" id="question-input" name="question" placeholder="Type your question..." />
692 |        <button type="submit">Ask</button>
693 |      </form>
694 | 
695 | 
696 |      <!-- Add this STOP button (it doesn't belong to the question-form) -->
697 |      <button type="button" id="stop-rag-btn" style="margin-left: 10px; background-color: #f44336; color: white; border: none; border-radius: 4px; padding: 7px 12px;">
698 |        Stop RAG
699 |      </button>
700 | 
701 | 
702 |      <div id="chat-output"></div>
703 |    </div>
704 | 
705 | 
706 |    <div class="clear"></div>
707 |  {% endif %}
708 | 
709 | 
710 |  <script>
711 |    // Immediately call /rag_init in the background
712 |    fetch("{{ url_for('rag_init') }}", { method: "POST" })
713 |      .then(resp => resp.json())
714 |      .then(data => {
715 |        console.log("RAG init response:", data);
716 |        // Show the user that something is happening
717 |        const ragStatusEl = document.getElementById("rag-status");
718 |        ragStatusEl.innerText = data.status; // e.g. "RAG initialization started"
719 | 
720 | 
721 |        // Now poll /rag_status every 5 seconds instead of 2
722 |        const checkInterval = setInterval(() => {
723 |          fetch("{{ url_for('rag_status') }}")
724 |            .then(r => r.json())
725 |            .then(rd => {
726 |              if (rd.initialized) {
727 |                ragStatusEl.innerText = "RAG is ready!";
728 |                clearInterval(checkInterval); // stop polling
729 |              } else {
730 |                ragStatusEl.innerText = "RAG is still initializing...";
731 |              }
732 |            })
733 |            .catch(err => {
734 |              console.error("Error checking RAG status:", err);
735 |              // If there's an error talking to /rag_status, you can handle it here
736 |            });
737 |        }, 5000); // Changed from 2000 to 5000 milliseconds
738 |      })
739 |      .catch(err => {
740 |        console.error("RAG init error:", err);
741 |        document.getElementById("rag-status").innerText = "Error initializing RAG";
742 |      });
743 | 
744 | 
745 |    window.addEventListener('DOMContentLoaded', () => {
746 |      let rawMarkdown = document.getElementById('raw-markdown')?.textContent || "";
747 | 
748 | 
749 |      // 1) Remove code fences
750 |      rawMarkdown = rawMarkdown.replaceAll("```markdown", "").replaceAll("```", "");
751 | 
752 | 
753 |      // 2) Parse the Key Table for the chart (long format)
754 |      const keyTableData = parseKeyTableFromMarkdown(rawMarkdown);
755 |      renderKeyTableChart(keyTableData);
756 | 
757 | 
758 |      // 3) Parse and pivot each of the five tables
759 |      const pivotedKey = pivotTableData(keyTableData, 'category', 'year', 'emissions');
760 | 
761 |      const scope1Data = parseBreakdownFromMarkdown(rawMarkdown, "Scope 1 Breakdown");
762 |      const pivotedScope1 = pivotTableData(scope1Data, 'subcategory', 'year', 'emissions');
763 | 
764 | 
765 |      const scope2MarketData = parseBreakdownFromMarkdown(rawMarkdown, "Scope 2 Market-based Breakdown");
766 |      const pivotedScope2M = pivotTableData(scope2MarketData, 'subcategory', 'year', 'emissions');
767 | 
768 | 
769 |      const scope2LocationData = parseBreakdownFromMarkdown(rawMarkdown, "Scope 2 Location-based Breakdown");
770 |      const pivotedScope2L = pivotTableData(scope2LocationData, 'subcategory', 'year', 'emissions');
771 | 
772 | 
773 |      const scope3Data = parseBreakdownFromMarkdown(rawMarkdown, "Scope 3 Breakdown");
774 |      const pivotedScope3 = pivotTableData(scope3Data, 'subcategory', 'year', 'emissions');
775 | 
776 | 
777 |      // 4) Build HTML tables
778 |      let html = "";
779 |      html += "<h3>Summary</h3>";
780 |      html += buildHtmlTable(pivotedKey, "Category");
781 | 
782 | 
783 |      html += "<h3>Scope 1 Breakdown</h3>";
784 |      html += buildHtmlTable(pivotedScope1, "Scope 1 Source / Subcategory");
785 | 
786 | 
787 |      html += "<h3>Scope 2 Market-based Breakdown</h3>";
788 |      html += buildHtmlTable(pivotedScope2M, "Region or Business Unit");
789 | 
790 | 
791 |      html += "<h3>Scope 2 Location-based Breakdown</h3>";
792 |      html += buildHtmlTable(pivotedScope2L, "Region or Business Unit");
793 | 
794 | 
795 |      html += "<h3>Scope 3 Breakdown</h3>";
796 |      html += buildHtmlTable(pivotedScope3, "Scope 3 Category");
797 | 
798 | 
799 |      document.getElementById('rendered-tables').innerHTML = html;
800 | 
801 | 
802 |      // Add chart annotations
803 |      Chart.register(ChartjsPluginAnnotation);
804 | 
805 | 
806 |      // Add smooth scroll to tables
807 |      document.querySelectorAll('#rendered-tables table').forEach(table => {
808 |        table.addEventListener('mouseover', () => {
809 |          table.style.transform = 'scale(1.02)';
810 |          table.style.transition = 'transform 0.3s ease';
811 |        });
812 |        table.addEventListener('mouseout', () => {
813 |          table.style.transform = 'scale(1)';
814 |        });
815 |      });
816 | 
817 | 
818 |      // Real-time chart resizing via ResizeObserver
819 |      const chartCanvas = document.getElementById('keyTableChart');
820 |      if (chartCanvas) {
821 |        const resizeObserver = new ResizeObserver(entries => {
822 |          entries.forEach(entry => {
823 |            const chart = Chart.getChart(chartCanvas);
824 |            if (chart) {
825 |              chart.resize();
826 |            }
827 |          });
828 |        });
829 |        resizeObserver.observe(chartCanvas.parentElement);
830 |      }
831 |    });
832 | 
833 | 
834 |    function pivotTableData(longData, rowField, colField, valField) {
835 |      const rowLabels = [...new Set(longData.map(d => d[rowField]))];
836 |      const colLabels = [...new Set(longData.map(d => d[colField]))].sort();
837 | 
838 | 
839 |      const lookup = {};
840 |      longData.forEach(item => {
841 |        const r = item[rowField];
842 |        const c = item[colField];
843 |        lookup[`${r}-${c}`] = item[valField];
844 |      });
845 | 
846 | 
847 |      const pivoted = rowLabels.map(rLabel => {
848 |        let rowObj = { rowLabel: rLabel };
849 |        colLabels.forEach(cLabel => {
850 |          rowObj[cLabel] = lookup[`${rLabel}-${cLabel}`] ?? null;
851 |        });
852 |        return rowObj;
853 |      });
854 | 
855 | 
856 |      return { rowLabels, colLabels, pivoted };
857 |    }
858 | 
859 | 
860 |    function buildHtmlTable(pivotResult, rowName = "Category") {
861 |      const { pivoted, colLabels } = pivotResult;
862 |      let html = '<table><thead><tr><th>' + rowName + '</th>';
863 |      colLabels.forEach(yr => {
864 |        html += `<th>${yr}</th>`;
865 |      });
866 |      html += '</tr></thead><tbody>';
867 | 
868 | 
869 |      pivoted.forEach(row => {
870 |        html += `<tr><td>${row.rowLabel}</td>`;
871 |        colLabels.forEach(yr => {
872 |          let val = row[yr] !== null ? row[yr] : '';
873 |          html += `<td>${val}</td>`;
874 |        });
875 |        html += '</tr>';
876 |      });
877 |      html += '</tbody></table>';
878 |      return html;
879 |    }
880 | 
881 | 
882 |    function parseBreakdownFromMarkdown(md, headingName) {
883 |      let lines = md.split('\n');
884 |      let foundHeading = false;
885 |      let result = [];
886 | 
887 | 
888 |      for (let i = 0; i < lines.length; i++) {
889 |        let line = lines[i].trim();
890 | 
891 | 
892 |        // Case-insensitive check for the heading name
893 |        if (line.toLowerCase().includes(headingName.toLowerCase())) {
894 |          foundHeading = true;
895 |          continue;
896 |        }
897 | 
898 | 
899 |        if (foundHeading) {
900 |          // If we see a new heading (# up to ######), we stop
901 |          if (line.match(/^#{1,6}\s/)) {
902 |            break;
903 |          }
904 | 
905 | 
906 |          if (line.startsWith("|") && line.endsWith("|")) {
907 |            if (line.includes("|---")) continue;
908 | 
909 | 
910 |            let cols = line.split("|").map(c => c.trim()).filter(Boolean);
911 |            if (cols.length < 3) continue;
912 |            let lower = cols.join(" ").toLowerCase();
913 |            if (lower.includes("year") && lower.includes("emissions")) {
914 |              continue;
915 |            }
916 | 
917 | 
918 |            let subcategory = cols[0];
919 |            let yearStr = cols[1].toUpperCase();
920 |            let match = yearStr.match(/\d{4}|\d{2}/);
921 |            let year = null;
922 |            if (match) {
923 |              let num = parseInt(match[0]);
924 |              if (num < 50) year = 2000 + num;
925 |              else if (num < 100) year = 1900 + num;
926 |              else year = num;
927 |            }
928 | 
929 | 
930 |            let eStr = cols[2].replace(/[^\d.-]/g,'');
931 |            let emissions = parseFloat(eStr);
932 |            if (isNaN(emissions)) emissions = 0;
933 | 
934 | 
935 |            result.push({ subcategory, year, emissions });
936 |          }
937 |        }
938 |      }
939 |      return result;
940 |    }
941 | 
942 | 
943 |    // Modified question form handler
944 |    document.getElementById("question-form")?.addEventListener("submit", function(e) {
945 |      e.preventDefault();
946 |      const questionInput = document.getElementById("question-input");
947 |      const question = questionInput.value.trim();
948 |      if (!question) return;
949 | 
950 | 
951 |      // Show immediate feedback
952 |      const outputDiv = document.getElementById("chat-output");
953 |      const waitingMsg = document.createElement("div");
954 |      waitingMsg.innerHTML = "<em>Processing your question, please wait...</em>";
955 |      outputDiv.appendChild(waitingMsg);
956 | 
957 | 
958 |      // Disable the ASK button so user knows it's "in progress"
959 |      const askButton = this.querySelector("button[type='submit']");
960 |      askButton.disabled = true;
961 | 
962 | 
963 |      const formData = new FormData();
964 |      formData.append("question", question);
965 | 
966 | 
967 |      fetch("{{ url_for('ask_question') }}", {
968 |        method: "POST",
969 |        body: formData
970 |      })
971 |        .then(resp => resp.json())
972 |        .then(data => {
973 |          // Remove the "waiting" message
974 |          outputDiv.removeChild(waitingMsg);
975 |          // Re-enable the ASK button
976 |          askButton.disabled = false;
977 | 
978 | 
979 |          let newQA = document.createElement("div");
980 |          // Clean out triple backticks
981 |          let cleanAnswer = data.answer.replaceAll("```markdown", "").replaceAll("```", "");
982 |          // Convert markdown to HTML
983 |          let htmlAnswer = marked.parse(cleanAnswer);
984 | 
985 | 
986 |          newQA.innerHTML = `
987 |            <b>Q:</b> ${question}<br>
988 |            <b>A:</b> ${htmlAnswer}
989 |          `;
990 |          outputDiv.appendChild(newQA);
991 |        })
992 |        .catch(err => {
993 |          console.error("Ask error:", err);
994 |          // Remove "waiting" message
995 |          outputDiv.removeChild(waitingMsg);
996 |          // Re-enable the button
997 |          askButton.disabled = false;
998 | 
999 | 
1000 |          const newQA = document.createElement("div");
1001 |          newQA.innerHTML = `
1002 |            <b>Q:</b> ${question}<br>
1003 |            <b>A:</b> Sorry, there was an error. Please try again.
1004 |          `;
1005 |          outputDiv.appendChild(newQA);
1006 |        });
1007 |    });
1008 | 
1009 | 
1010 |    function parseKeyTableFromMarkdown(md) {
1011 |      let lines = md.split('\n');
1012 |      let inKeyTable = false;
1013 |      let entries = [];
1014 | 
1015 | 
1016 |      for (let i = 0; i < lines.length; i++) {
1017 |        let line = lines[i].trim();
1018 | 
1019 | 
1020 |        // 1) Detect "Key Table" (case-insensitive)
1021 |        if (!inKeyTable && line.toLowerCase().includes("key table")) {
1022 |          inKeyTable = true;
1023 |          continue;
1024 |        }
1025 |        // 2) If we've found Key Table and see a new heading (# up to ######), we stop
1026 |        if (inKeyTable && line.match(/^#{1,6}\s/)) {
1027 |          break;
1028 |        }
1029 | 
1030 | 
1031 |        // 3) If inKeyTable, gather table rows
1032 |        if (inKeyTable && line.startsWith("|") && line.endsWith("|")) {
1033 |          // skip lines like "|---"
1034 |          if (line.includes("|---")) continue;
1035 | 
1036 | 
1037 |          // split columns
1038 |          let cols = line.split("|").map(c => c.trim()).filter(Boolean);
1039 |          if (cols.length < 3) continue; // not enough columns
1040 | 
1041 | 
1042 |          // skip header row
1043 |          let lower = cols.join(" ").toLowerCase();
1044 |          if (lower.includes("category") && lower.includes("year")) {
1045 |            continue;
1046 |          }
1047 | 
1048 | 
1049 |          // parse category
1050 |          let category = cols[0];
1051 | 
1052 | 
1053 |          // parse year
1054 |          let yearStr = cols[1].toUpperCase();
1055 |          let match = yearStr.match(/\d{4}|\d{2}/);
1056 |          let year = null;
1057 |          if (match) {
1058 |            let num = parseInt(match[0]);
1059 |            // Example logic for 2-digit years
1060 |            if (num < 50) year = 2000 + num;
1061 |            else if (num < 100) year = 1900 + num;
1062 |            else year = num;
1063 |          }
1064 |          if (!year) {
1065 |            continue;
1066 |          }
1067 | 
1068 | 
1069 |          // parse emissions
1070 |          let emissStr = cols[2];
1071 |          let cleaned = emissStr.replace(/[^\d.-]/g, '');
1072 |          let emissions = parseFloat(cleaned);
1073 |          if (isNaN(emissions)) emissions = 0;
1074 | 
1075 | 
1076 |          entries.push({ category, year, emissions });
1077 |        }
1078 |      }
1079 |      return entries;
1080 |    }
1081 | 
1082 | 
1083 |    function renderKeyTableChart(data) {
1084 |      if (!data || data.length === 0) {
1085 |        console.log("No Key Table data found to chart.");
1086 |        return;
1087 |      }
1088 | 
1089 | 
1090 |      let categories = {
1091 |        "Scope 1": [],
1092 |        "Scope 2 (Market-based)": [],
1093 |        "Scope 2 (Location-based)": []
1094 |      };
1095 | 
1096 | 
1097 |      data.forEach(entry => {
1098 |        if (categories.hasOwnProperty(entry.category) && entry.year && entry.emissions !== null) {
1099 |          categories[entry.category].push({ x: entry.year, y: entry.emissions });
1100 |        }
1101 |      });
1102 | 
1103 | 
1104 |      Object.keys(categories).forEach(cat => {
1105 |        categories[cat].sort((a,b) => a.x - b.x);
1106 |      });
1107 | 
1108 | 
1109 |      const chartDatasets = [];
1110 |      const colorMap = {
1111 |        "Scope 1": "#26c6da",
1112 |        "Scope 2 (Market-based)": "#ef5350",
1113 |        "Scope 2 (Location-based)": "#66bb6a"
1114 |      };
1115 | 
1116 | 
1117 |      for (let cat of Object.keys(categories)) {
1118 |        if (categories[cat].length > 0) {
1119 |          chartDatasets.push({
1120 |            label: cat,
1121 |            data: categories[cat],
1122 |            backgroundColor: colorMap[cat] || "#888",
1123 |            borderColor: colorMap[cat] || "#888",
1124 |            borderWidth: 1,
1125 |            borderRadius: 4
1126 |          });
1127 |        }
1128 |      }
1129 | 
1130 | 
1131 |      const ctx = document.getElementById('keyTableChart').getContext('2d');
1132 |      new Chart(ctx, {
1133 |        type: 'bar',
1134 |        data: { datasets: chartDatasets },
1135 |        options: {
1136 |          scales: {
1137 |            x: {
1138 |              type: 'linear',
1139 |              title: { display: true, text: 'Year' },
1140 |              ticks: {
1141 |                stepSize: 1,
1142 |                callback: function(value) {
1143 |                  return value;
1144 |                }
1145 |              }
1146 |            },
1147 |            y: {
1148 |              title: {
1149 |                display: true,
1150 |                text: 'Emissions (tCO2e)'
1151 |              }
1152 |            }
1153 |          },
1154 |          plugins: {
1155 |            title: {
1156 |              display: false
1157 |            }
1158 |          }
1159 |        }
1160 |      });
1161 |    }
1162 |    /* ================================================================ */
1163 | 
1164 | 
1165 |    document.addEventListener('DOMContentLoaded', function() {
1166 |      // STOP RAG button
1167 |      const stopButton = document.getElementById('stop-rag-btn');
1168 |      if (stopButton) {
1169 |        stopButton.addEventListener('click', function() {
1170 |          fetch("{{ url_for('reset_rag') }}", {
1171 |            method: "POST"
1172 |          })
1173 |          .then(resp => resp.json())
1174 |          .then(data => {
1175 |            console.log("Stop RAG response:", data);
1176 |            document.getElementById('rag-status').innerText = "RAG reset.";
1177 |          })
1178 |          .catch(err => console.error("Error stopping RAG:", err));
1179 |        });
1180 |      }
1181 |    });
1182 |  </script>
1183 |   </div>
1184 | </body>
1185 | </html>
1186 | 
```

src/templates/instructions.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Emissions Report</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |   <style>
11 |       body {
12 |            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
13 |            background-color: #F5F5F5;
14 |            color: #333333;
15 |            margin: 0;
16 |            padding: 0;
17 |        }
18 | 
19 | 
20 | 
21 | 
22 |       table, th, td {
23 |            border: 1px solid black;
24 |       }
25 | 
26 | 
27 | 
28 | 
29 |       .content {
30 |          margin-left: 130px; /* Pushes content right */
31 |          padding: 20px;
32 |       }
33 | 
34 | 
35 | 
36 | 
37 |       .div1 {
38 |        z-index: 10; /* Ensures it appears above other elements */
39 |        position: relative; /* Required for z-index to work */
40 |           height: 160px;
41 |           width: 100%; /* Ensure it takes full width */
42 |           margin: 0;
43 |           background-color: #063800;
44 |           display: flex;
45 |           align-items: center; /* Centers vertically */
46 |           justify-content: center; /* Centers horizontally */
47 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
48 |       }
49 |       .catchy-phrase {
50 |        z-index: 10;
51 |        position: absolute;
52 |        top: 120px;
53 |        transform: translate(-50%, -50%);
54 |        left: 50%;
55 |        color: white;
56 |        font-size: 20px;
57 | }
58 | 
59 | 
60 | 
61 | 
62 |       .navigation {
63 |           position: absolute;
64 |           left:0;
65 |           width:100px;
66 |           height:100%;
67 |           background:  #063800;
68 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
69 |           display:center;
70 |           justify-content:center;
71 |           align-items:center;
72 |           flex-direction:column;
73 |           gap:10px;
74 |           transform: translateX(-100%);
75 |           transition: transform 0.3s ease;
76 | 
77 | 
78 | 
79 | 
80 |       }
81 | 
82 | 
83 |       /* Class to toggle menu visibility */
84 |       .navigation.show {
85 |           transform: translateX(0);
86 |       }
87 | 
88 | 
89 | 
90 | 
91 |       .navigation li {
92 |           position:relative;
93 |           list-style:none;
94 |           width:80px;
95 |           height: 80px;
96 |           display:flex;
97 |           justify-content:center;
98 |           margin: 0 5px;
99 | 
100 |       }
101 | 
102 | 
103 | 
104 | 
105 |       .navigation li::before {
106 |           content: '';
107 |           position: absolute;
108 |           top:calc(50% - 2.5px);
109 |           left: 20px;
110 |           width:5px;
111 |           height: 5px;
112 |           border-radius:50%;
113 |           transition:0.5s;
114 |       }
115 | 
116 | 
117 | 
118 | 
119 |       .navigation li.active::before {
120 |           background:white;
121 |           box-shadow:0 0 5px white,
122 |           0 0 10px white,
123 |           0 0 20px white,
124 |           0 0 30px white,
125 |           0 0 40px white;
126 |       }
127 | 
128 | 
129 | 
130 | 
131 |       .navigation li a {
132 |           display:flex;
133 |           justify-content:center;
134 |           align-items:center;
135 |           flex-direction:column;
136 |           text-decoration:none;
137 |       }
138 | 
139 | 
140 | 
141 | 
142 |       .navigation li a .icon {
143 |           color: white;
144 |           transition: 0.5s;
145 |           transition-delay: 0.2s;
146 |           font-size: 1.5em;
147 |       }
148 | 
149 | 
150 |       .navigation li.active a .icon::before{
151 |           transform:scale(1);
152 |       }
153 | 
154 | 
155 |       .navigation li a .text{
156 |           position: absolute;
157 |           left:130px;
158 |           font-size:1.25em;
159 |           color:white;
160 |           visibility:hidden;
161 |           transition:0.5s;
162 | 
163 |       }
164 | 
165 | 
166 |       .navigation li:hover a .text {
167 |           visibility: visible;
168 |       }
169 | 
170 | 
171 |       .hamburger-icon {
172 |           font-size: 30px;
173 |          color: white;
174 |          cursor: pointer;
175 |          position: absolute;
176 |          top: 20px;
177 |          left: 20px;
178 |          z-index: 100;
179 |          align-items: center;
180 |       }
181 | 
182 | 
183 | 
184 | 
185 |       .sidebar1 {
186 |           display: flex;
187 |          flex-direction: column;
188 |          align-items: center;
189 |          justify-content: center;
190 |          border: 1px solid #ccc;
191 |          border-radius: 8px;
192 |          margin-left: 50px;
193 |          margin-top: 40px;
194 |          float: left;
195 |          width: 250px;
196 |          height: 150px;
197 |          padding: 20px;
198 |          background-color: white;
199 |          color: white;
200 |          z-index: 1000;
201 |       }
202 | 
203 | 
204 | 
205 | 
206 |       .dropbtn {
207 |         background-color: white;
208 |            color:  #063800;
209 |            padding: 16px;
210 |            font-size: 16px;
211 |            border: none;
212 |           cursor: pointer;
213 |       }
214 | 
215 | 
216 | 
217 | 
218 |       /* The container <div> - needed to position the dropdown content */
219 |        .dropdown {
220 |        z-index: 15;
221 |         position: absolute;
222 |          top: 20px; /* Distance from the top */
223 |          right: 20px;
224 |            display: inline-block;
225 |            border: 1px solid white;
226 |            background-color: white;
227 |            border-radius: 12px;
228 |            padding: 4px 7px;
229 |              font-size: 16px;
230 |              cursor: pointer;
231 |              align-items: center;
232 |       }
233 | 
234 | 
235 | 
236 | 
237 |       /* Dropdown Content (Hidden by Default) */
238 |       .dropdown-content {
239 |            display: none;
240 |            padding: 5px 15px;
241 |            position: absolute;
242 |            font-size: 16px;
243 |            background-color:white;
244 |            min-width: 100px;
245 |            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
246 |            z-index: 1;
247 |       }
248 | 
249 | 
250 | 
251 | 
252 |       /* Links inside the dropdown */
253 |       .dropdown-content a {
254 |         color: black;
255 |         padding: 12px 16px;
256 |         text-decoration: none;
257 |         display: block;
258 |       }
259 | 
260 | 
261 | 
262 | 
263 |       /* Change color of dropdown links on hover */
264 |       .dropdown-content a:hover {background-color: #2e8b563d;}
265 | 
266 | 
267 | 
268 | 
269 |       /* Show the dropdown menu on hover */
270 |       .dropdown:hover .dropdown-content {display: block;}
271 | 
272 | 
273 | 
274 | 
275 |       /* Change the background color of the dropdown button when the dropdown content is shown */
276 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
277 | 
278 | 
279 | 
280 | 
281 |       .progress-bar {
282 |           background-color: #045000!important;/* This is the green color you used for other elements */
283 |       }
284 | 
285 | 
286 | 
287 | 
288 |       .selected-company {
289 |            background-color: white;
290 |            padding: 20px;
291 |            margin: 20px auto;
292 |            align-items: center;
293 |            justify-content: center;
294 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
295 |            border: 2px solid black;
296 |            display: inline-block;
297 |            width: 90%; /* Adjust width for better layout */
298 |            max-width: 1400px;
299 |         }
300 | 
301 | 
302 |         /* Table Styling */
303 |         .selected-company table {
304 |            width: 100%;
305 |            border-collapse: collapse;
306 |         }
307 | 
308 | 
309 |         .selected-company th, .selected-company td {
310 |            border: 1px solid black;
311 |            padding: 8px;
312 |            text-align: center;
313 |         }
314 | 
315 | 
316 |         .selected-company th {
317 |            background-color: #063800;
318 |            color: white;
319 |         }
320 | 
321 | 
322 |         /* Style the Download Button */
323 |         .selected-company a.btn-success {
324 |            display: block;
325 |            margin: 10px auto;
326 |            text-align: center;
327 |            background-color: #063800;
328 |            color: white;
329 |            padding: 10px 15px;
330 |            font-size: 16px;
331 |            border-radius: 5px;
332 |            text-decoration: none;
333 |            transition: background-color 0.3s ease;
334 |         }
335 | 
336 | 
337 |         .selected-company a.btn-success:hover {
338 |            background-color: #1E6B47;
339 |         }
340 | 
341 | 
342 |     .esg-container {
343 |              background-color: white;
344 |              display: flex;
345 |              padding: 10px;
346 |              gap: 30px;
347 |              align-items: center;
348 |              justify-content: center;
349 |              margin-bottom: 30px;
350 |          }
351 | 
352 | 
353 | 
354 |       .list-group-item {
355 |          width:1400px;
356 |          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
357 |          border: 2px solid black; padding: 5px; display: inline-block;
358 |          background-color: white;
359 |          padding: 20px;
360 |          margin-left:20px;
361 |          align-items: center;
362 |          justify-content: center;
363 |       }
364 | 
365 | 
366 | 
367 | 
368 |       .dropdown-container {
369 |          background-color: #F5F5F5;
370 |          display: flex;
371 |          padding: 10px;
372 |          gap: 30px;
373 |          align-items: center;
374 |          justify-content: center;
375 |          margin-bottom: 30px;
376 |      }
377 |      .dropdown-container label{
378 |        color: #1C1C1C;
379 |      }
380 | 
381 | 
382 | 
383 | 
384 |      .nav-tabs .nav-link {
385 |           background-color: #063800 !important;
386 |           color: white !important; /* Ensure text is readable */
387 |           border: none !important; /* Optional: remove default border */
388 |       }
389 | 
390 | 
391 | 
392 | 
393 | 
394 | 
395 |       .nav-tabs .nav-link.active {
396 |           background-color: #045000 !important; /* Slightly darker shade for active tab */
397 |           color: white !important;
398 |       }
399 | 
400 | 
401 | 
402 | 
403 |       .submit-button {
404 |          background-color: #063800;
405 |          color: #FFFFFF;
406 |          border: none;
407 |          padding: 10px 20px;
408 |          border-radius: 4px;
409 |          font-size: 16px;
410 |          cursor: pointer;
411 |      }
412 |      .submit-button:hover {
413 |          background-color: #1E6B47;
414 |      }
415 | 
416 | 
417 | 
418 |      .report-container{
419 |        background-color: #F5F5F5;
420 |        color: #1C1C1C;
421 |        display: flex;
422 |        padding: 10px;
423 |        gap: 30px;
424 |        align-items: center;
425 |        justify-content: center;
426 |        margin-bottom: 30px;
427 |      }
428 | 
429 | 
430 |       #loading-spinner {
431 |           display: none;
432 |           width: 24px;
433 |           height: 24px;
434 |           border: 4px solid rgba(46, 139, 87, 0.3);
435 |           border-top: 4px solid #2E8B57;
436 |           border-radius: 50%;
437 |           animation: spin 1s linear infinite;
438 |       }
439 | 
440 | 
441 | 
442 | 
443 |       @keyframes spin {
444 |           0% { transform: rotate(0deg); }
445 |           100% { transform: rotate(360deg); }
446 |       }
447 | 
448 | 
449 | 
450 | 
451 |       .news-image {
452 |           width: 100px;  /* Set width */
453 |           height: 80px;  /* Set height */
454 |           object-fit: cover;  /* Crop image to fit */
455 |           border-radius: 5px;
456 |           box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
457 |       }
458 |       .nav-tabs {
459 |        border-bottom: none !important;
460 |        margin-bottom: 0 !important;
461 |        padding-bottom: 0 !important;
462 |     }
463 | 
464 | 
465 | 
466 |     .tab-content {
467 |        color:#F5F5F5;
468 |        background-color: #1C1C1C !important; /* Match the surrounding area */
469 |        margin-top: -1px !important; /* Fixes any white gap */
470 |        border-radius: 0 0 8px 8px;
471 |        border: none !important;
472 |     }
473 | 
474 | 
475 |     /* Ensure each tab-pane also has the correct background */
476 |     .tab-pane {
477 |        background-color: #1C1C1C !important;
478 |        margin: 0 !important;
479 |        border: none !important;
480 |     }
481 | 
482 | 
483 |     /* If a card or container inside tab-content has a background, override it */
484 |     .tab-pane > div {
485 |        background-color: #1C1C1C !important;
486 |        border: none !important;
487 |        margin: 0 !important;
488 |        padding: 20px;
489 |     }
490 |     .page-bottom {
491 |        background-color: #1C1C1C !important;
492 |        padding: 50px 0; /* Adds spacing */
493 |        min-height: 1000px; /* Adjust as needed */
494 |     }
495 | 
496 | 
497 |     .logo {
498 |            z-index: 20;
499 |        max-height: 100px; /* Adjusts within the header */
500 |        width: auto; /* Maintains aspect ratio */
501 |        position: absolute;
502 |        top: 30px; /* Aligns with the hamburger icon */
503 |        left: 500px; /* Pushes it to the right of the hamburger icon */
504 |     }
505 |     .padding-for-info {
506 |        max-width: 1100px; /* Limits width for readability */
507 |        padding: 0 40px; /* Left & right padding */
508 |        text-align: center;
509 |        margin: 0 auto; /* Ensures centering */
510 |     }
511 | 
512 |   </style>
513 |   <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
514 |   integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
515 |   crossorigin="anonymous"></script>
516 | </head>
517 | <body>
518 |    <div class="div1">
519 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
520 |       </div>
521 |       <div class="catchy-phrase"> User Guide </div>
522 |   <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
523 |       <div class="hamburger-icon">&#9776;</div>
524 |       <ul class="navigation">
525 |        <li class="active">
526 |            <a href="{{url_for('test')}}">
527 |                <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
528 |            </a>
529 |        </li>
530 |        <li>
531 |            <a href="#">
532 |                <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
533 |            </a>
534 |        </li>
535 |        <li>
536 |            <a href="{{url_for('advanced_search')}}">
537 |                <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
538 |            </a>
539 |        </li>
540 |        <li>
541 |            <a href="{{url_for('register')}}">
542 |                <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
543 |            </a>
544 |        </li>
545 |        <li class="active">
546 |            <a href=/firstpage>
547 |                <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
548 |            </a>
549 |        </li>
550 |    </ul>
551 |       <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
552 |           <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
553 |           <script>
554 |               document.addEventListener('DOMContentLoaded', function () {
555 |                   const hamburger = document.querySelector('.hamburger-icon');
556 |                   const navigation = document.querySelector('.navigation');
557 |                   let isOpen = false;
558 |                   hamburger.addEventListener('click', function () {
559 |                       // Toggle menu visibility
560 |                       isOpen = !isOpen;
561 |                       if (isOpen) {
562 |                           navigation.classList.add('show');
563 |                       } else {
564 |                           navigation.classList.remove('show');
565 |                       }
566 |                   });
567 | 
568 |                   // Keep your existing navigation item click event listener
569 |                   let list = document.querySelectorAll('.navigation li');
570 |                   function activeLink() {
571 |                       list.forEach((item) => item.classList.remove('active'));
572 |                       this.classList.add('active');
573 |                   }
574 |                   list.forEach((item) => item.addEventListener('click', activeLink));
575 |               });
576 |           </script>
577 | <br>
578 | <h1 style="text-align:center;">How does EmissiTrack work? </h1>
579 | <div class="padding-for-info">
580 | <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack?</h2>
581 |       <p style="text-align:center;">A Smart, Scalable, and Dynamic Solution for Tracking Corporate Carbon Footprints.</p>
582 | 
583 | 
584 | 
585 | 
586 |       <p style="text-align:center;">The Carbon Emissions Tracker is a web-based platform designed to dynamically retrieve, categorize, and visualize corporate carbon emissions data for listed companies within the MSCI All World Index. This tool empowers users to access the latest Scope 1 (direct emissions) and Scope 2 (indirect emissions from purchased electricity) data from publicly available sources such as Corporate Social Responsibility (CSR) reports, government databases, and other sustainability disclosures.</p>
587 | 
588 | 
589 | 
590 | 
591 |       <p style="text-align:center;">In addition to emissions data, the platform features a real-time news feed with top headlines for each company, keeping users updated on sustainability-related developments. Users can also filter companies by sector, country, industry, and other key parameters to refine their searches and insights.</p>
592 |           <p style="text-align:center;">Emissions data can be visualized either in interactive bar charts or structured in a detailed table format. </p>
593 | 
594 | 
595 | 
596 | 
597 |           <h2 style="text-align:center; margin-top:50px; font-weight:bold;">What is EmissiTrack Pro?</h2>
598 | 
599 |          <p> EmissiTrack Pro is a web-based platform that helps you quickly and accurately view a company’s greenhouse gas (GHG) emissions.<p></p> Under the hood, it uses Docling to extract raw GHG emission tables (Scope 1, Scope 2, etc.) from a company’s ESG PDFs. Once you search by name, ticker, or ISIN, EmissiTrack Pro retrieves the relevant PDF reports, processes the relevant tables with Docling, and uses an LLM for accurate data extraction and unit conversions. It then displays the extracted figures in a clear, interactive layout on the premium page, where a bar chart lets you visualise year-over-year changes at a glance. </p>
600 |          <p> Meanwhile, the system also creates a separate Chatbot using the full sustainability report parsed in chunks by PyMuPDF4LLM, powered by a vector-embedding and retrieval flow that references the same underlying text and tables for in-depth Q&A. The Chatbot runs in parallel by indexing the parsed data into vector storage and retrieving details on demand. If you wish to halt loading—perhaps to search for a different company—you can click “Stop RAG” to interrupt the Chatbot’s background retrieval process before starting fresh.<p></p> This dual approach—Docling for accurate table extraction and an LLM-based retriever for chat—ensures maximum accuracy in capturing raw numbers while still providing a dynamic conversational interface for deeper insight into sustainability reports.</p>
601 | 
602 | 
603 | </div>
604 |       <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
605 |       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
606 | 
607 | </body>
608 | </html>
609 | 
610 | 
611 | 
```

src/templates/instructionspremium.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |   <meta charset="UTF-8">
5 |   <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |   <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |   <title>Emissions Report</title>
8 |   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |   <style>
11 |       body {
12 |            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
13 |            background-color: #F5F5F5;
14 |            color: #333333;
15 |            margin: 0;
16 |            padding: 0;
17 |        }
18 | 
19 | 
20 |       table, th, td {
21 |            border: 1px solid black;
22 |       }
23 | 
24 | 
25 | 
26 | 
27 |       .content {
28 |          margin-left: 130px; /* Pushes content right */
29 |          padding: 20px;
30 | 
31 |       }
32 | 
33 | 
34 |       .div1 {
35 |        z-index: 10; /* Ensures it appears above other elements */
36 |        position: relative; /* Required for z-index to work */
37 |           height: 160px;
38 |           width: 100%; /* Ensure it takes full width */
39 |           margin: 0;
40 |           background-color: #063800;
41 |           display: flex;
42 |           align-items: center; /* Centers vertically */
43 |           justify-content: center; /* Centers horizontally */
44 |           box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
45 |       }
46 |       .catchy-phrase {
47 |        z-index: 10;
48 |        position: absolute;
49 |        top: 120px;
50 |        transform: translate(-50%, -50%);
51 |        left: 50%;
52 |        color: white;
53 |        font-size: 20px;
54 | }
55 | 
56 | 
57 | 
58 | 
59 |       .navigation {
60 |           position: absolute;
61 |           left:0;
62 |           width:100px;
63 |           height:100%;
64 |           background:  #063800;
65 |           box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
66 |           display:center;
67 |           justify-content:center;
68 |           align-items:center;
69 |           flex-direction:column;
70 |           gap:10px;
71 |           transform: translateX(-100%);
72 |           transition: transform 0.3s ease;
73 | 
74 | 
75 | 
76 | 
77 |       }
78 | 
79 | 
80 |       .navigation.show {
81 |           transform: translateX(0);
82 |       }
83 | 
84 | 
85 | 
86 | 
87 |       .navigation li {
88 |           position:relative;
89 |           list-style:none;
90 |           width:80px;
91 |           height: 80px;
92 |           display:flex;
93 |           justify-content:center;
94 |           margin: 0 5px;
95 | 
96 |       }
97 | 
98 |       .navigation li::before {
99 |           content: '';
100 |           position: absolute;
101 |           top:calc(50% - 2.5px);
102 |           left: 20px;
103 |           width:5px;
104 |           height: 5px;
105 |           border-radius:50%;
106 |           transition:0.5s;
107 | 
108 |       }
109 | 
110 | 
111 | 
112 | 
113 |       .navigation li.active::before {
114 |           background:white;
115 |           box-shadow:0 0 5px white,
116 |           0 0 10px white,
117 |           0 0 20px white,
118 |           0 0 30px white,
119 |           0 0 40px white;
120 |       }
121 | 
122 | 
123 |       .navigation li a {
124 |           display:flex;
125 |           justify-content:center;
126 |           align-items:center;
127 |           flex-direction:column;
128 |           text-decoration:none;
129 |       }
130 | 
131 | 
132 | 
133 | 
134 |       .navigation li a .icon {
135 |           color: white;
136 |           transition: 0.5s;
137 |           transition-delay: 0.2s;
138 |           font-size: 1.5em;
139 |       }
140 | 
141 | 
142 |       .navigation li.active a .icon::before{
143 |           transform:scale(1);
144 | 
145 |       }
146 | 
147 | 
148 | 
149 | 
150 |       .navigation li a .text{
151 |           position: absolute;
152 |           left:130px;
153 |           font-size:1.25em;
154 |           color:white;
155 |           visibility:hidden;
156 |           transition:0.5s;
157 | 
158 |       }
159 | 
160 | 
161 |       .navigation li:hover a .text {
162 |           visibility: visible;
163 |       }
164 | 
165 | 
166 |       .hamburger-icon {
167 |           font-size: 30px;
168 |          color: white;
169 |          cursor: pointer;
170 |          position: absolute;
171 |          top: 20px;
172 |          left: 20px;
173 |          z-index: 100;
174 |          align-items: center;
175 |       }
176 | 
177 | 
178 | 
179 | 
180 |       .sidebar1 {
181 |           display: flex;
182 |          flex-direction: column;
183 |          align-items: center;
184 |          justify-content: center;
185 |          border: 1px solid #ccc;
186 |          border-radius: 8px;
187 |          margin-left: 50px;
188 |          margin-top: 40px;
189 |          float: left;
190 |          width: 250px;
191 |          height: 150px;
192 |          padding: 20px;
193 |          background-color: white;
194 |          color: white;
195 |          z-index: 1000;
196 |       }
197 | 
198 | 
199 | 
200 | 
201 |       .dropbtn {
202 |         background-color: white;
203 |            color:  #063800;
204 |            padding: 16px;
205 |            font-size: 16px;
206 |            border: none;
207 |           cursor: pointer;
208 |       }
209 | 
210 | 
211 |        .dropdown {
212 |        z-index: 15;
213 |         position: absolute;
214 |          top: 20px; /* Distance from the top */
215 |          right: 20px;
216 |            display: inline-block;
217 |            border: 1px solid white;
218 |            background-color: white;
219 |            border-radius: 12px;
220 |            padding: 4px 7px;
221 |              font-size: 16px;
222 |              cursor: pointer;
223 |              align-items: center;
224 |       }
225 | 
226 | 
227 | 
228 | 
229 |       .dropdown-content {
230 |            display: none;
231 |            padding: 5px 15px;
232 |            position: absolute;
233 |            font-size: 16px;
234 |            background-color:white;
235 |            min-width: 100px;
236 |            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
237 |            z-index: 1;
238 |       }
239 | 
240 |       .dropdown-content a {
241 |         color: black;
242 |         padding: 12px 16px;
243 |         text-decoration: none;
244 |         display: block;
245 |       }
246 | 
247 | 
248 |       /* Change color of dropdown links on hover */
249 |       .dropdown-content a:hover {background-color: #2e8b563d;}
250 | 
251 | 
252 |       /* Show the dropdown menu on hover */
253 |       .dropdown:hover .dropdown-content {display: block;}
254 | 
255 |       /* Change the background color of the dropdown button when the dropdown content is shown */
256 |       .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
257 | 
258 | 
259 | 
260 | 
261 |       .progress-bar {
262 |           background-color: #045000!important;/* This is the green color you used for other elements */
263 |       }
264 | 
265 | 
266 |       .selected-company {
267 |            background-color: white;
268 |            padding: 20px;
269 |            margin: 20px auto;
270 |            align-items: center;
271 |            justify-content: center;
272 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
273 |            border: 2px solid black;
274 |            display: inline-block;
275 |            width: 90%; /* Adjust width for better layout */
276 |            max-width: 1400px;
277 |         }
278 | 
279 | 
280 |     /* Table Styling */
281 |     .selected-company table {
282 |        width: 100%;
283 |        border-collapse: collapse;
284 |     }
285 | 
286 | 
287 |     .selected-company th, .selected-company td {
288 |        border: 1px solid black;
289 |        padding: 8px;
290 |        text-align: center;
291 |     }
292 | 
293 | 
294 |     .selected-company th {
295 |        background-color: #063800;
296 |        color: white;
297 |     }
298 | 
299 | 
300 |     /* Style the Download Button */
301 |     .selected-company a.btn-success {
302 |        display: block;
303 |        margin: 10px auto;
304 |        text-align: center;
305 |        background-color: #063800;
306 |        color: white;
307 |        padding: 10px 15px;
308 |        font-size: 16px;
309 |        border-radius: 5px;
310 |        text-decoration: none;
311 |        transition: background-color 0.3s ease;
312 |     }
313 | 
314 | 
315 |     .selected-company a.btn-success:hover {
316 |        background-color: #1E6B47;
317 |     }
318 | 
319 | 
320 |     .esg-container {
321 |              background-color: white;
322 |              display: flex;
323 |              padding: 10px;
324 |              gap: 30px;
325 |              align-items: center;
326 |              justify-content: center;
327 |              margin-bottom: 30px;
328 |          }
329 | 
330 | 
331 |       .list-group-item {
332 |          width:1400px;
333 |          box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
334 |          border: 2px solid black; padding: 5px; display: inline-block;
335 |          background-color: white;
336 |          padding: 20px;
337 |          margin-left:20px;
338 |          align-items: center;
339 |          justify-content: center;
340 |       }
341 | 
342 | 
343 | 
344 | 
345 |       .dropdown-container {
346 |          background-color: #F5F5F5;
347 |          display: flex;
348 |          padding: 10px;
349 |          gap: 30px;
350 |          align-items: center;
351 |          justify-content: center;
352 |          margin-bottom: 30px;
353 |      }
354 |      .dropdown-container label{
355 |        color: #1C1C1C;
356 |      }
357 | 
358 | 
359 | 
360 | 
361 |      .nav-tabs .nav-link {
362 |           background-color: #063800 !important;
363 |           color: white !important; /* Ensure text is readable */
364 |           border: none !important; /* Optional: remove default border */
365 |       }
366 | 
367 | 
368 | 
369 | 
370 | 
371 | 
372 |       .nav-tabs .nav-link.active {
373 |           background-color: #045000 !important; /* Slightly darker shade for active tab */
374 |           color: white !important;
375 |       }
376 | 
377 | 
378 | 
379 | 
380 |       .submit-button {
381 |          background-color: #063800;
382 |          color: #FFFFFF;
383 |          border: none;
384 |          padding: 10px 20px;
385 |          border-radius: 4px;
386 |          font-size: 16px;
387 |          cursor: pointer;
388 |      }
389 |      .submit-button:hover {
390 |          background-color: #1E6B47;
391 |      }
392 | 
393 | 
394 | 
395 | 
396 |      .report-container{
397 |        background-color: #F5F5F5;
398 |        color: #1C1C1C;
399 |        display: flex;
400 |        padding: 10px;
401 |        gap: 30px;
402 |        align-items: center;
403 |        justify-content: center;
404 |        margin-bottom: 30px;
405 |      }
406 | 
407 | 
408 | 
409 | 
410 |       #loading-spinner {
411 |           display: none;
412 |           width: 24px;
413 |           height: 24px;
414 |           border: 4px solid rgba(46, 139, 87, 0.3);
415 |           border-top: 4px solid #2E8B57;
416 |           border-radius: 50%;
417 |           animation: spin 1s linear infinite;
418 |       }
419 | 
420 | 
421 | 
422 | 
423 |       @keyframes spin {
424 |           0% { transform: rotate(0deg); }
425 |           100% { transform: rotate(360deg); }
426 |       }
427 | 
428 | 
429 | 
430 | 
431 |       .news-image {
432 |           width: 100px;  /* Set width */
433 |           height: 80px;  /* Set height */
434 |           object-fit: cover;  /* Crop image to fit */
435 |           border-radius: 5px;
436 |           box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
437 |       }
438 |       .nav-tabs {
439 |            border-bottom: none !important;
440 |            margin-bottom: 0 !important;
441 |            padding-bottom: 0 !important;
442 |         }
443 | 
444 | 
445 |         /* Ensure tab content blends perfectly with the background */
446 |         .tab-content {
447 |            color:#F5F5F5;
448 |            background-color: #1C1C1C !important; /* Match the surrounding area */
449 |            margin-top: -1px !important; /* Fixes any white gap */
450 |            border-radius: 0 0 8px 8px;
451 |            border: none !important;
452 |         }
453 | 
454 | 
455 |         /* Ensure each tab-pane also has the correct background */
456 |         .tab-pane {
457 |            background-color: #1C1C1C !important;
458 |            margin: 0 !important;
459 |            border: none !important;
460 |         }
461 | 
462 | 
463 |         /* If a card or container inside tab-content has a background, override it */
464 |         .tab-pane > div {
465 |            background-color: #1C1C1C !important;
466 |            border: none !important;
467 |            margin: 0 !important;
468 |            padding: 20px;
469 |         }
470 |         .page-bottom {
471 |            background-color: #1C1C1C !important;
472 |            padding: 50px 0; /* Adds spacing */
473 |            min-height: 1000px; /* Adjust as needed */
474 |         }
475 | 
476 | 
477 |         .logo {
478 |                z-index: 20;
479 |            max-height: 100px; /* Adjusts within the header */
480 |            width: auto; /* Maintains aspect ratio */
481 |            position: absolute;
482 |            top: 30px; /* Aligns with the hamburger icon */
483 |            left: 500px; /* Pushes it to the right of the hamburger icon */
484 |         }
485 |         .padding-for-info {
486 |            max-width: 1100px; /* Limits width for readability */
487 |            padding: 0 40px; /* Left & right padding */
488 |            text-align: center;
489 |            margin: 0 auto; /* Ensures centering */
490 |         }
491 |   </style>
492 |   <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
493 |   integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
494 |   crossorigin="anonymous"></script>
495 | 
496 | 
497 | 
498 | 
499 | </head>
500 | <body>
501 |    <div class="div1">
502 |        <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
503 |       </div>
504 |       <div class="catchy-phrase"> Instructions </div>
505 |   <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
506 |       <div class="hamburger-icon">&#9776;</div>
507 |       <ul class="navigation">
508 |        <li class="active">
509 |            <a href="{{url_for('test')}}">
510 |                <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
511 |            </a>
512 |        </li>
513 |        <li>
514 |            <a href="#">
515 |                <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
516 |            </a>
517 |        </li>
518 |        <li>
519 |            <a href="{{url_for('advanced_search')}}">
520 |                <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
521 |            </a>
522 |        </li>
523 |        <li>
524 |            <a href="{{url_for('register')}}">
525 |                <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
526 |            </a>
527 |        </li>
528 |        <li class="active">
529 |            <a href=/firstpage>
530 |                <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
531 |            </a>
532 |        </li>
533 |    </ul>
534 |       <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
535 |           <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
536 |           <script>
537 |               document.addEventListener('DOMContentLoaded', function () {
538 |                   const hamburger = document.querySelector('.hamburger-icon');
539 |                   const navigation = document.querySelector('.navigation');
540 |                   let isOpen = false;
541 | 
542 |                   hamburger.addEventListener('click', function () {
543 |                       // Toggle menu visibility
544 |                       isOpen = !isOpen;
545 |                       if (isOpen) {
546 |                           navigation.classList.add('show');
547 |                       } else {
548 |                           navigation.classList.remove('show');
549 |                       }
550 |                   });
551 | 
552 |                   // Keep your existing navigation item click event listener
553 |                   let list = document.querySelectorAll('.navigation li');
554 |                   function activeLink() {
555 |                       list.forEach((item) => item.classList.remove('active'));
556 |                       this.classList.add('active');
557 |                   }
558 |                   list.forEach((item) => item.addEventListener('click', activeLink));
559 |               });
560 | 
561 |           </script>
562 | 
563 | <div class="padding-for-info">
564 | 
565 | 
566 |    <h2 style="text-align:center; margin-top:50px; font-weight:bold;">How to use EmissiTrack Pro?</h2>
567 |    <p style="text-align:center;"> <strong> Step 1: Searching for a Company </strong></p>
568 |    <p style="text-align:center;">In the text box at the top, type the name (e.g., “Amazon”), the ticker symbol (e.g., “AMZN”), or the ISIN (unique identifier) of the company you want to research.</p>
569 | 
570 | 
571 | 
572 | 
573 |    <p style="text-align:center;"><strong>  Step 2: Viewing GHG Emissions Tables </strong></p>
574 | <p style="text-align:center;">After searching, you’ll see GHG Emissions Tables on the left.
575 | • This includes “Key Table,” which lists the company’s Scope 1, Scope 2 (market-based), and Scope 2 (location-based) emissions by year.
576 | • There may also be additional breakdown tables (Scope 1 detail, Scope 2 detail, etc.).
577 | </p>
578 |    <p style="text-align:center;"> Tip: If you see “null,” that means no data was reported for that category/year.</p>
579 | 
580 | 
581 | 
582 | 
583 | <p style="text-align:center;"> <strong> Step 3: Checking the Emissions Chart </strong></p>
584 |    <p style="text-align:center;">No data for the Key Table was found, or the system couldn’t parse the year numbers.
585 | • If this happens, try searching a different way (e.g., exact company name or ticker).
586 | </p>
587 |    <p style="text-align:center;"> <strong> Step 4: RAG Chatbot </strong></p>
588 |    <p style="text-align:center;">It automatically initializes (you’ll see “RAG initialization started”).
589 | • Once it’s ready, you can type questions like “How do these emissions compare to last year?” or “What are the biggest drivers for Scope 3?”
590 | • Click Ask to see an AI-generated response based on the PDF data that was retrieved.</p>
591 | <p style="text-align:center;"> Stop RAG button:  If the background data build is taking too long or you want to cancel it, click Stop RAG.</p>
592 | 
593 | 
594 | 
595 | 
596 | </div>
597 |           <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
598 |       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
599 | 
600 | 
601 |    </body>
602 |    </html>
603 | 
604 | 
```

src/templates/login.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |    <meta charset="UTF-8">
5 |    <title>login1</title>
6 |    <style>
7 |        body {
8 |            font-family: 'Inter', sans-serif;
9 |            background-color: #F5F5F5;
10 |            display: flex;
11 |            justify-content: center;
12 |            align-items: center;
13 |            height: 100vh;
14 |            margin: 0;
15 |        }
16 |        .logo {
17 |    z-index: 20;
18 |    max-height: 175px; /* Adjusts within the header */
19 |    width: auto; /* Maintains aspect ratio */
20 |    position: absolute;
21 |    top: 150px; /* Aligns with the hamburger icon */
22 |    left: 627px; /* Pushes it to the right of the hamburger icon */
23 | }
24 |        .container {
25 |            display: flex;
26 |        }
27 | 
28 | 
29 |        .box {
30 |            background-color: #063800;
31 |            width: 50%;
32 |            height: 700px;
33 |            box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
34 |            border-radius: 10px;
35 |            padding: 30px;
36 |        }
37 | 
38 | 
39 |        .content {
40 |            text-align: center;
41 |            padding-top: 160px;
42 |        }
43 | 
44 | 
45 |        .welcome-text {
46 |            text-align: center;
47 |            color: white;
48 |            font-size: 36px;
49 |        }
50 | 
51 | 
52 |        form {
53 |            text-align: center;
54 |        }
55 | 
56 | 
57 |        ul {
58 |            list-style-type: none;
59 |            margin: 0;
60 |            padding: 0;
61 |        }
62 | 
63 | 
64 |        .login-btn {
65 |            background-color: #FFFFFF;
66 |            color: #063800;
67 |            border: none;
68 |            padding: 10px 20px;
69 |            border-radius: 4px;
70 |            font-size: 16px;
71 |            cursor: pointer;
72 |        }
73 | 
74 | 
75 |        .login-btn:hover {
76 |            background-color: #ffffff9a;
77 |        }
78 | 
79 | 
80 |        .input-field {
81 |    border: 1px solid #ccc;
82 |    border-radius: 6px;
83 |    padding: 12px;
84 |    font-size: 16px;
85 |    width: 95%;
86 |    transition: all 0.3s ease-in-out;
87 | }
88 | .input-field:focus {
89 |    border-color: #063800;
90 |    box-shadow: 0 0 8px rgba(6, 56, 0, 0.3);
91 |    outline: none;
92 | }
93 | 
94 | 
95 | 
96 | 
97 |        .input-field::placeholder {
98 |    font-size: 18px;  /* For placeholder text */
99 | }
100 |        .forgot-password {
101 |            font-size: 14px;
102 |            color: #063800;
103 |            text-decoration: none;
104 |        }
105 | 
106 | 
107 |        .forgot-password:hover {
108 |            text-decoration: underline;
109 |        }
110 | 
111 | 
112 |        footer {
113 |            text-align: center;
114 |            margin-top: 20px;
115 |            font-size: 14px;
116 |        }
117 | 
118 | 
119 |        footer a {
120 |            color: #F5F5F5;
121 |            text-decoration: none;
122 |        }
123 | 
124 | 
125 |        footer a:hover {
126 |            text-decoration: underline;
127 |        }
128 |    </style>
129 | </head>
130 | <body>
131 | 
132 | 
133 |    <div class="box">
134 |        <h1 class="welcome-text">Welcome Back to EmissiTrack Pro!</h1>
135 |        <img src="{{ url_for('static', filename='images/missiTrack2.png') }}" alt="Logo" class="logo">
136 |        <div class="content">
137 |            <h2 style="color:white;">Sign in to access your Account</h2>
138 |            <form method="POST" action="/login">
139 |                <br>
140 |                <input type="email" id="email" name="email" required class="input-field" placeholder="Enter your email">
141 |                <br>
142 |                <br>
143 |                <input type="password" id="password" name="password" required class="input-field" placeholder="Enter your password">
144 |                <br>
145 |                <br>
146 |                <button type="submit" class="login-btn">Login</button>
147 |            </form>
148 |            <br>
149 |            <a href="#" class="forgot-password">Forgot Password?</a>
150 |            <br>
151 |            <br>
152 |            <footer>
153 |            <a href="{{url_for('register')}}" style="color:white;">Don't have an account? Sign up</a>
154 |        </footer>
155 |            <br>
156 |            <br>
157 |            <footer>
158 |                <p style="color: #F5F5F5;">Look at our <a href="#">Privacy Policy</a> for more information.</p>
159 |            </footer>
160 |        </div>
161 |    </div>
162 | 
163 | 
164 | 
165 | 
166 | </body>
167 | </html>
```

src/templates/maps.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |  <meta charset="UTF-8">
5 |     <style>
6 |         body {
7 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
8 |           background-color: #1C1C1C;
9 |           color: #1C1C1C;
10 |           margin: 0;
11 |           padding: 0;
12 |       }
13 | 
14 |           .logo-header-container {
15 |    z-index: 10;
16 |    position: relative;
17 |    height: 160px;
18 |    width: 100%;
19 |    background-color: #063800;
20 |    display: flex;
21 |    align-items: center; /* Align items vertically */
22 |    justify-content: center; /* Center items horizontally */
23 |    gap: 20px; /* Add spacing between logo and text */
24 |    text-align: center;
25 | }
26 | 
27 | 
28 | .logo {
29 |    max-height: 100px;
30 |    width: auto;
31 | }
32 | 
33 | 
34 | .div1 {
35 |    display: flex;
36 |    flex-direction: column; /* Stack heading and phrase */
37 |    align-items: center;
38 |    justify-content: center;
39 | }
40 | 
41 | 
42 | .catchy-phrase {
43 |    color: white;
44 |    font-size: 20px;
45 |    margin-top: 5px; /* Adjust spacing between header and phrase */
46 | }
47 |         .padding-for-info {
48 |    max-width: 1100px; /* Limits width for readability */
49 |    padding: 40px; /* Left & right padding */
50 |    text-align: center;
51 |    margin: 0 auto; /* Ensures centering */
52 | }
53 | 
54 | 
55 | 
56 | 
57 | 
58 |      .navigation li:hover a .text {
59 |          visibility: visible;
60 |      }
61 | 
62 | 
63 |      .hamburger-icon {
64 |          font-size: 30px;
65 |         color: white;
66 |         cursor: pointer;
67 |         position: absolute;
68 |         top: 20px;
69 |         left: 20px;
70 |         z-index: 100;
71 |         align-items: center;
72 |      }
73 | 
74 | 
75 |      .sidebar1 {
76 |          display: flex;
77 |         flex-direction: column;
78 |         align-items: center;
79 |         justify-content: center;
80 |         border: 1px solid #ccc;
81 |         border-radius: 8px;
82 |         margin-left: 50px;
83 |         margin-top: 40px;
84 |         float: left;
85 |         width: 250px;
86 |         height: 150px;
87 |         padding: 20px;
88 |         background-color: white;
89 |         color: white;
90 |         z-index: 1000;
91 |      }
92 | 
93 | 
94 |      .navigation {
95 |          position: absolute;
96 |          left:0;
97 |          width:100px;
98 |          height:100%;
99 |          background:  #063800!important;
100 |          box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
101 |          display:center;
102 |          justify-content:center;
103 |          align-items:center;
104 |          flex-direction:column;
105 |          gap:10px;
106 |          transform: translateX(-100%);
107 |          transition: transform 0.3s ease;
108 | 
109 |      }
110 | 
111 |      .navigation.show {
112 |          transform: translateX(0);
113 |      }
114 | 
115 |      .navigation li {
116 |          position:relative;
117 |          list-style:none;
118 |          width:80px;
119 |          height: 80px;
120 |          display:flex;
121 |          justify-content:center;
122 |          margin: 0 5px;
123 | 
124 |      }
125 | 
126 | 
127 |      .navigation li::before {
128 |          content: '';
129 |          position: absolute;
130 |          top:calc(50% - 2.5px);
131 |          left: 20px;
132 |          width:5px;
133 |          height: 5px;
134 |          border-radius:50%;
135 |          transition:0.5s;
136 | 
137 |      }
138 | 
139 | 
140 |      .navigation li.active::before {
141 |          background:white;
142 |          box-shadow:0 0 5px white,
143 |          0 0 10px white,
144 |          0 0 20px white,
145 |          0 0 30px white,
146 |          0 0 40px white;
147 |      }
148 | 
149 |      .navigation li a {
150 |          display:flex;
151 |          justify-content:center;
152 |          align-items:center;
153 |          flex-direction:column;
154 |          text-decoration:none;
155 |      }
156 | 
157 | 
158 |      .navigation li a .icon {
159 |          color: white;
160 |          transition: 0.5s;
161 |          transition-delay: 0.2s;
162 |          font-size: 1.5em; /* Adjust this value to your preference */
163 |      }
164 | 
165 |      .navigation li.active a .icon::before{
166 |          transform:scale(1);
167 | 
168 | 
169 |      }
170 |      .navigation li a .text{
171 |          position: absolute;
172 |          left:130px;
173 |          font-size:1.25em;
174 |          color:white;
175 |          visibility:hidden;
176 |          transition:0.5s;
177 | 
178 |      }
179 | 
180 |     </style>
181 |     <title>Emissions Map</title>
182 | </head>
183 | <body>
184 |        <div class="logo-header-container">
185 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
186 |        <div class="div1">
187 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
188 |            <p class="catchy-phrase">Company Emissions Map</p>
189 |        </div>
190 |        </div>
191 |        <div class="hamburger-icon">&#9776;</div>
192 |      <ul class="navigation">
193 |       <li class="active">
194 |           <a href="{{url_for('test')}}">
195 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
196 |           </a>
197 |       </li>
198 |       <li>
199 |           <a href="{{url_for('instructions')}}">
200 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
201 |           </a>
202 |       </li>
203 |       <li>
204 |           <a href="{{url_for('advanced_search')}}">
205 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
206 |           </a>
207 |       </li>
208 |       <li>
209 |           <a href="{{url_for('register')}}">
210 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
211 |           </a>
212 |       </li>
213 |       <li class="active">
214 |           <a href=/firstpage>
215 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
216 |           </a>
217 |       </li>
218 |   </ul>
219 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
220 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
221 |          <script>
222 |              document.addEventListener('DOMContentLoaded', function () {
223 |                  const hamburger = document.querySelector('.hamburger-icon');
224 |                  const navigation = document.querySelector('.navigation');
225 |                  let isOpen = false;
226 |                  hamburger.addEventListener('click', function () {
227 |                      // Toggle menu visibility
228 |                      isOpen = !isOpen;
229 |                      if (isOpen) {
230 |                          navigation.classList.add('show');
231 |                      } else {
232 |                          navigation.classList.remove('show');
233 |                      }
234 |                  });
235 |                  // Keep your existing navigation item click event listener
236 |                  let list = document.querySelectorAll('.navigation li');
237 |                  function activeLink() {
238 |                      list.forEach((item) => item.classList.remove('active'));
239 |                      this.classList.add('active');
240 |                  }
241 |                  list.forEach((item) => item.addEventListener('click', activeLink));
242 |              });
243 |          </script>
244 |    </div>
245 |        <div class="padding-for-info">
246 |            <h3 style="color:white;">Top 40 Companies and their ESG Ratings</h3>
247 |     <iframe src="{{ url_for('serve_emissions_map') }}" width="90%" height="700px"></iframe>
248 |            </div>
249 | </body>
250 | </html>
```

src/templates/register.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |    <meta charset="UTF-8">
5 |    <title>Financial Markets</title>
6 |    <style>
7 |        body {
8 |            font-family: 'Inter', sans-serif;
9 |            background-color: #F5F5F5;
10 |            display: flex;
11 |            justify-content: center;
12 |            align-items: center;
13 |            height: 100vh;
14 |            margin: 0;
15 |        }
16 |        .instructions{
17 |            background-color: #F5F5F5;
18 |            color:#063800;
19 |            width: 47%;
20 |            height: 700px;
21 |        }
22 |        .container {
23 |            display: flex;
24 |        }
25 |        .logo-container {
26 |    display: flex;
27 |    justify-content: center;
28 |    margin-top: -70px;
29 | }
30 | .logo {
31 |    max-height: 160px;
32 |    width: auto;
33 | }
34 | 
35 | 
36 |        .box {
37 |            background-color: #063800;
38 |            width: 30%;
39 |            height: 700px;
40 |            box-shadow: 0px 16px 32px rgba(0, 0, 0, 0.5);
41 |            border-radius: 10px;
42 |            padding: 30px;
43 |        }
44 | 
45 | 
46 |        .content {
47 |            text-align: center;
48 |            padding-top:130px;
49 |            padding-left:20px;
50 |            padding-right:20px;
51 |            align-items: center;
52 |        }
53 | 
54 | 
55 | 
56 | 
57 | 
58 | 
59 |        form {
60 |            text-align: center;
61 |        }
62 | 
63 | 
64 |        .essay1 {
65 |            font-size: 14px;
66 |            padding-right: 120px
67 |        }
68 | 
69 | 
70 |        .box2 {
71 |            width: 400px;
72 |            padding: 1px;
73 |            border: 4px solid #ccc;
74 |            border-radius: 4px;
75 |            background-color: #fff;
76 |            color: #333;
77 |            font-size: 16px;
78 |            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
79 |        }
80 | 
81 | 
82 | 
83 | 
84 |        .input-field {
85 |    border: 1px solid #ccc;
86 |    border-radius: 6px;
87 |    padding: 12px;
88 |    font-size: 16px;
89 |    width: 95%;
90 |    transition: all 0.3s ease-in-out;
91 | }
92 | .input-field:focus {
93 |    border-color: #063800;
94 |    box-shadow: 0 0 8px rgba(6, 56, 0, 0.3);
95 |    outline: none;
96 | }
97 |        .input-field::placeholder {
98 |    font-size: 18px;  /* For placeholder text */
99 | }
100 |        .register-btn {
101 |            background-color: #FFFFFF;
102 |            color: #215839;
103 |            border: none;
104 |            padding: 10px 20px;
105 |            border-radius: 4px;
106 |            font-size: 16px;
107 |            cursor: pointer;
108 |        }
109 |        .register-btn:hover {
110 |            background-color: #ffffffa1;
111 |        }
112 |        footer {
113 |            text-align: center;
114 |            margin-top: 20px;
115 |            font-size: 14px;
116 |        }
117 | 
118 | 
119 |        footer a {
120 |            color: #F5F5F5;
121 |            text-decoration: none;
122 |        }
123 | 
124 | 
125 |        footer a:hover {
126 |            text-decoration: underline;
127 |        }
128 | 
129 |    </style>
130 | </head>
131 | <body>
132 |    <div class="instructions">
133 |        <h1 > Welcome to EmissiTrack Pro</h1>
134 |        <h2 >User Instructions:</h2>
135 |         <p > <b>1.</b> In the text field at the top, type the company name, ticker, or ISIN. </p>
136 |        <br>
137 |            <p> <b>2.</b> Choose the matching “Search Type” radio button.</p>
138 |            <br>
139 |                <p>   <b>3.</b> Click “Go.”</p>
140 |                <br>
141 |                    <p>   <b>4.</b> View the left column for the extracted emissions tables.</p>
142 |                    <br>
143 |                        <p>   <b>5.</b> Check the right column for the emissions chart and the chatbot.</p>
144 |                        <br>
145 |                            <p>   <b>6.</b> (Optional) Type a question for the chatbot and click “Ask.”</p>
146 |                            <br>
147 |                                <p>  <b>7.</b> (Optional) If you need to cancel the data retrieval process, click Stop RAG.</p>
148 |                                <br>
149 |                                    <h4>  That’s it! The page is meant to help you quickly find, visualize, and chat about greenhouse gas emissions data from the company’s sustainability reports.</h4>
150 |    </div>
151 | 
152 | 
153 |      <div class="box">
154 |          <div class="content">
155 |            <div class="logo-container">
156 |                <img src="{{ url_for('static', filename='images/missiTrack2.png') }}" alt="EmissiTrack Logo" class="logo">
157 |            </div>
158 | 
159 |              <h2 style="color:white;"> Register to access EmissiTrack Pro </h2>
160 |              <form method="POST" action="">
161 |                <br>
162 |                <input type="text" id="first_name" name="first_name" required class="input-field" placeholder="First Name"> <br>
163 |                <br>
164 |                <input type="text" id="last_name" name="last_name" required class="input-field" placeholder="Last Name"> <br>
165 |                <br>
166 |                <input type="email" id="email" name="email" required class="input-field" placeholder="Email Address"> <br>
167 |                <br>
168 |                <input type="password" id="password" name="Password" required class="input-field" placeholder="Password"> <br>
169 |                <br>
170 |                  <button type="submit" class="register-btn">Register</button>
171 |              </form>
172 |              <footer>
173 |              <p><a href="{{url_for('login')}}" style="color:white;">Already have an account, log in!</a></p>
174 |            </footer>
175 |              <footer>
176 |                <p style="color: #F5F5F5;">By continuing, you agree to our <a href="#">Terms of Service</a> and acknowledge that you've read our <a href="#">Privacy Policy</a>.</p>
177 |            </footer>
178 |          </div>
179 |      </div>
180 |  </div>
181 | </body>
182 | </html>
```

src/templates/test.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |  <meta charset="UTF-8">
5 |  <meta http-equiv="X-UA-Compatible" content="IE=edge">
6 |  <meta name="viewport" content="width=device-width, initial-scale=1.0">
7 |  <title>Emissions Report</title>
8 |  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
9 |  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
10 |    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
11 |  <style>
12 |      body {
13 |           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
14 |           background-color: #F5F5F5;
15 |           color: #333333;
16 |           margin: 0;
17 |           padding: 0;
18 |       }
19 | 
20 | 
21 |      table, th, td {
22 |           border: 1px solid black;
23 |      }
24 | 
25 | 
26 |      .content {
27 |         margin-left: 130px; /* Pushes content right */
28 |         padding: 20px;
29 | 
30 |      }
31 | 
32 | 
33 |      .navigation {
34 |          position: absolute;
35 |          left:0;
36 |          width:100px;
37 |          height:100%;
38 |          background:  #063800;
39 |          box-shadow: 25px 25px 75px rgba(0,0,0,0.25), 10px 10px 70px rgba(0,0,0,0.25), inset 5px 5px 10px rgba(0,0,0,0.5), inset 5px 5px 20px rgba(255,255,255,0.2) , inset -5px -5px 15px rgba(0,0,0,0.75);
40 |          display:center;
41 |          justify-content:center;
42 |          align-items:center;
43 |          flex-direction:column;
44 |          gap:10px;
45 |          transform: translateX(-100%);
46 |          transition: transform 0.3s ease;
47 | 
48 | 
49 |      }
50 | 
51 | 
52 |      /* Class to toggle menu visibility */
53 |      .navigation.show {
54 |          transform: translateX(0);
55 |      }
56 | 
57 |      .navigation li {
58 |          position:relative;
59 |          list-style:none;
60 |          width:80px;
61 |          height: 80px;
62 |          display:flex;
63 |          justify-content:center;
64 |          margin: 0 5px;
65 | 
66 |      }
67 | 
68 |      .navigation li::before {
69 |          content: '';
70 |          position: absolute;
71 |          top:calc(50% - 2.5px);
72 |          left: 20px;
73 |          width:5px;
74 |          height: 5px;
75 |          border-radius:50%;
76 |          transition:0.5s;
77 |      }
78 | 
79 | 
80 |      .navigation li.active::before {
81 |          background:white;
82 |          box-shadow:0 0 5px white,
83 |          0 0 10px white,
84 |          0 0 20px white,
85 |          0 0 30px white,
86 |          0 0 40px white;
87 |      }
88 | 
89 | 
90 |      .navigation li a {
91 |          display:flex;
92 |          justify-content:center;
93 |          align-items:center;
94 |          flex-direction:column;
95 |          text-decoration:none;
96 |      }
97 | 
98 | 
99 |      .navigation li a .icon {
100 |          color: white;
101 |          transition: 0.5s;
102 |          transition-delay: 0.2s;
103 |          font-size: 1.5em;
104 |      }
105 | 
106 |      .navigation li.active a .icon::before{
107 |          transform:scale(1);
108 | 
109 |      }
110 | 
111 | 
112 |      .navigation li a .text{
113 |          position: absolute;
114 |          left:130px;
115 |          font-size:1.25em;
116 |          color:white;
117 |          visibility:hidden;
118 |          transition:0.5s;
119 | 
120 | 
121 |      }
122 | 
123 | 
124 |      .logo-header-container {
125 |    z-index: 10;
126 |    position: relative;
127 |    height: 160px;
128 |    width: 100%;
129 |    background-color: #063800;
130 |    display: flex;
131 |    align-items: center; /* Align items vertically */
132 |    justify-content: center; /* Center items horizontally */
133 |    gap: 20px; /* Add spacing between logo and text */
134 |    box-shadow: 0px 4px 15px rgba(20, 80, 20, 0.6);
135 |    text-align: center;
136 | }
137 | 
138 | 
139 | .logo {
140 |    max-height: 100px;
141 |    width: auto;
142 | }
143 | 
144 | 
145 | .div1 {
146 |    display: flex;
147 |    flex-direction: column; /* Stack heading and phrase */
148 |    align-items: center;
149 |    justify-content: center;
150 | }
151 | 
152 | 
153 | .catchy-phrase {
154 |    color: white;
155 |    font-size: 20px;
156 |    margin-top: 5px; /* Adjust spacing between header and phrase */
157 | }
158 | 
159 | 
160 |      .navigation li:hover a .text {
161 |          visibility: visible;
162 |      }
163 | 
164 | 
165 |      /* Hamburger Icon Styles */
166 |      .hamburger-icon {
167 |          font-size: 30px;
168 |         color: white;
169 |         cursor: pointer;
170 |         position: absolute;
171 |         top: 20px;
172 |         left: 20px;
173 |         z-index: 100;
174 |         align-items: center;
175 |      }
176 | 
177 | 
178 | 
179 | 
180 | 
181 | 
182 | 
183 | 
184 |      .sidebar1 {
185 |          display: flex;
186 |         flex-direction: column;
187 |         align-items: center;
188 |         justify-content: center;
189 |         border: 1px solid #ccc;
190 |         border-radius: 8px;
191 |         margin-left: 50px;
192 |         margin-top: 40px;
193 |         float: left;
194 |         width: 250px;
195 |         height: 150px;
196 |         padding: 20px;
197 |         background-color: white;
198 |         color: white;
199 |         z-index: 1000;
200 |      }
201 | 
202 | 
203 | 
204 | 
205 | 
206 | 
207 | 
208 | 
209 |      .dropbtn {
210 |        background-color: white;
211 |           color:  #063800;
212 |           padding: 16px;
213 |           font-size: 16px;
214 |           border: none;
215 |          cursor: pointer;
216 |      }
217 | 
218 | 
219 | 
220 | 
221 | 
222 | 
223 | 
224 | 
225 |      /* The container <div> - needed to position the dropdown content */
226 |       .dropdown {
227 |       z-index: 15;
228 |        position: absolute;
229 |         top: 20px; /* Distance from the top */
230 |         right: 20px;
231 |           display: inline-block;
232 |           border: 1px solid white;
233 |           background-color: white;
234 |           border-radius: 12px;
235 |           padding: 4px 7px;
236 |             font-size: 16px;
237 |             cursor: pointer;
238 |             align-items: center;
239 |      }
240 | 
241 | 
242 |      /* Dropdown Content (Hidden by Default) */
243 |      .dropdown-content {
244 |           display: none;
245 |           padding: 5px 15px;
246 |           position: absolute;
247 |           font-size: 16px;
248 |           background-color:white;
249 |           min-width: 100px;
250 |           box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
251 |           z-index: 1;
252 |      }
253 | 
254 | 
255 | 
256 | 
257 | 
258 | 
259 | 
260 | 
261 |      /* Links inside the dropdown */
262 |      .dropdown-content a {
263 |        color: black;
264 |        padding: 12px 16px;
265 |        text-decoration: none;
266 |        display: block;
267 |      }
268 | 
269 | 
270 |      /* Change color of dropdown links on hover */
271 |      .dropdown-content a:hover {background-color: #2e8b563d;}
272 | 
273 | 
274 |      /* Show the dropdown menu on hover */
275 |      .dropdown:hover .dropdown-content {display: block;}
276 | 
277 | 
278 |      /* Change the background color of the dropdown button when the dropdown content is shown */
279 |      .dropdown:hover .dropbtn {background-color: rgba(255, 255, 255, 0.607);}
280 | 
281 |      .progress-bar {
282 |          background-color: #045000!important;/* This is the green color you used for other elements */
283 |      }
284 | 
285 | 
286 |      .selected-company {
287 |       background-color: white;
288 |       padding: 20px;
289 |       margin: 20px auto;
290 |       align-items: center;
291 |       justify-content: center;
292 |       box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
293 |       border: 2px solid black;
294 |       display: inline-block;
295 |       width: 90%; /* Adjust width for better layout */
296 |       max-width: 1400px;
297 |     }
298 | 
299 | 
300 | 
301 | 
302 | /* Table Styling */
303 | .selected-company table {
304 |   width: 100%;
305 |   border-collapse: collapse;
306 | }
307 | 
308 | 
309 | 
310 | 
311 | .selected-company th, .selected-company td {
312 |   border: 1px solid black;
313 |   padding: 8px;
314 |   text-align: center;
315 | }
316 | 
317 | 
318 | 
319 | 
320 | .selected-company th {
321 |   background-color: #063800;
322 |   color: white;
323 | }
324 | 
325 | 
326 | 
327 | 
328 | /* Style the Download Button */
329 | .selected-company a.btn-success {
330 |   display: block;
331 |   margin: 10px auto;
332 |   text-align: center;
333 |   background-color: #063800;
334 |   color: white;
335 |   padding: 10px 15px;
336 |   font-size: 16px;
337 |   border-radius: 5px;
338 |   text-decoration: none;
339 |   transition: background-color 0.3s ease;
340 | }
341 | 
342 | 
343 | 
344 | 
345 | .selected-company a.btn-success:hover {
346 |   background-color: #1E6B47;
347 | }
348 | 
349 | 
350 | 
351 | 
352 | .esg-container {
353 |         background-color: white;
354 |         display: flex;
355 |         padding: 10px;
356 |         gap: 30px;
357 |         align-items: center;
358 |         justify-content: center;
359 |         margin-bottom: 30px;
360 |     }
361 | 
362 | 
363 |      .list-group-item {
364 |         width:1400px;
365 |         box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
366 |         border: 2px solid black; padding: 5px; display: inline-block;
367 |         background-color: white;
368 |         padding: 20px;
369 |         margin-left:20px;
370 |         align-items: center;
371 |         justify-content: center;
372 |      }
373 | 
374 | 
375 |      .dropdown-container {
376 |         background-color: #F5F5F5;
377 |         display: flex;
378 |         padding: 10px;
379 |         gap: 30px;
380 |         align-items: center;
381 |         justify-content: center;
382 |         margin-bottom: 30px;
383 |     }
384 |     .dropdown-container label{
385 |       color: #1C1C1C;
386 |     }
387 | 
388 | 
389 |     .nav-tabs .nav-link {
390 |          background-color: #063800 !important;
391 |          color: white !important; /* Ensure text is readable */
392 |          border: none !important; /* Optional: remove default border */
393 |      }
394 | 
395 |      .nav-tabs .nav-link.active {
396 |          background-color: #045000 !important; /* Slightly darker shade for active tab */
397 |          color: white !important;
398 |      }
399 | 
400 |      .submit-button {
401 |         background-color: #063800;
402 |         color: #FFFFFF;
403 |         border: none;
404 |         padding: 10px 20px;
405 |         border-radius: 4px;
406 |         font-size: 16px;
407 |         cursor: pointer;
408 |     }
409 |     .submit-button:hover {
410 |         background-color: #1E6B47;
411 |     }
412 | 
413 |     .report-container{
414 |       background-color: #F5F5F5;
415 |       color: #1C1C1C;
416 |       display: flex;
417 |       padding: 10px;
418 |       gap: 30px;
419 |       align-items: center;
420 |       justify-content: center;
421 |       margin-bottom: 30px;
422 |     }
423 | 
424 | 
425 |      #loading-spinner {
426 |          display: none;
427 |          width: 24px;
428 |          height: 24px;
429 |          border: 4px solid rgba(46, 139, 87, 0.3);
430 |          border-top: 4px solid #2E8B57;
431 |          border-radius: 50%;
432 |          animation: spin 1s linear infinite;
433 |      }
434 | 
435 | 
436 |      @keyframes spin {
437 |          0% { transform: rotate(0deg); }
438 |          100% { transform: rotate(360deg); }
439 |      }
440 | 
441 | 
442 |      .news-image {
443 |          width: 100px;  /* Set width */
444 |          height: 80px;  /* Set height */
445 |          object-fit: cover;  /* Crop image to fit */
446 |          border-radius: 5px;
447 |          box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
448 |      }
449 |      .nav-tabs {
450 |   border-bottom: none !important;
451 |   margin-bottom: 0 !important;
452 |   padding-bottom: 0 !important;
453 | }
454 | 
455 | 
456 | 
457 | 
458 | /* Ensure tab content blends perfectly with the background */
459 | .tab-content {
460 |   color:#F5F5F5;
461 |   background-color: #1C1C1C !important; /* Match the surrounding area */
462 |   margin-top: -1px !important; /* Fixes any white gap */
463 |   border-radius: 0 0 8px 8px;
464 |   border: none !important;
465 | }
466 | 
467 | 
468 | 
469 | 
470 | /* Ensure each tab-pane also has the correct background */
471 | .tab-pane {
472 |   background-color: #1C1C1C !important;
473 |   margin: 0 !important;
474 |   border: none !important;
475 | }
476 | 
477 | 
478 | 
479 | 
480 | /* If a card or container inside tab-content has a background, override it */
481 | .tab-pane > div {
482 |   background-color: #1C1C1C !important;
483 |   border: none !important;
484 |   margin: 0 !important;
485 |   padding: 20px;
486 | }
487 | .page-bottom {
488 |   background-color: #1C1C1C !important;
489 |   padding: 50px 0; /* Adds spacing */
490 |   min-height: 1000px; /* Adjust as needed */
491 | }
492 | 
493 |      .chart-container {
494 |            width: 100%;
495 |            max-width: 800px;
496 |            margin: 20px auto;
497 |        }
498 | 
499 | 
500 |  </style>
501 |  <script src="https://cdn.socket.io/4.5.3/socket.io.min.js"
502 |  integrity="sha384-WPFUvHkB1aHA5TDSZi6xtDgkF0wXJcIIxXhC6h8OT8EH3fC5PWro5pWJ1THjcfEi"
503 |  crossorigin="anonymous"></script>
504 | 
505 | </head>
506 | <body>
507 |    <div class="logo-header-container">
508 |        <img src="{{ url_for('static', filename='images/missiTrack.png') }}" alt="Logo" class="logo">
509 |        <div class="div1">
510 |            <h1 style="color:white; text-align:center;"> EmissiTrack</h1>
511 |            <p class="catchy-phrase">Home</p>
512 |        </div>
513 |    </div>
514 |  <div class="dropdown">
515 |          <button class="dropbtn">My Premium Profile</button>
516 |          <div class="dropdown-content">
517 |              <a href="{{url_for('register')}}">Create an account</a>
518 |              <a href="{{url_for('login')}}">Login</a>
519 |          </div>
520 |  </div>
521 | 
522 |      <div class="hamburger-icon">&#9776;</div>
523 |      <ul class="navigation">
524 |       <li class="active">
525 |           <a href="{{url_for('test')}}">
526 |               <span class="icon"> <ion-icon name="home-outline"></ion-icon></span>
527 |           </a>
528 |       </li>
529 |       <li>
530 |           <a href="{{url_for('instructions')}}">
531 |               <span class="icon"> <ion-icon name="help-circle-outline"></ion-icon></span>
532 |           </a>
533 |       </li>
534 |       <li>
535 |           <a href="{{url_for('advanced_search')}}">
536 |               <span class="icon"> <ion-icon name="funnel-outline"></ion-icon></span> <!-- ✅ Corrected -->
537 |           </a>
538 |       </li>
539 |       <li>
540 |           <a href="{{url_for('register')}}">
541 |               <span class="icon"><ion-icon name="person-add-outline"></ion-icon></span> <!-- ✅ Corrected -->
542 |           </a>
543 |       </li>
544 |       <li class="active">
545 |           <a href=/firstpage>
546 |               <span class="icon"> <ion-icon name="grid-outline"></ion-icon></span> <!-- ✅ First Page Icon -->
547 |           </a>
548 |       </li>
549 |   </ul>
550 |      <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
551 |          <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
552 |          <script>
553 |              document.addEventListener('DOMContentLoaded', function () {
554 |                  const hamburger = document.querySelector('.hamburger-icon');
555 |                  const navigation = document.querySelector('.navigation');
556 |                  let isOpen = false;
557 | 
558 |                  hamburger.addEventListener('click', function () {
559 |                      // Toggle menu visibility
560 |                      isOpen = !isOpen;
561 |                      if (isOpen) {
562 |                          navigation.classList.add('show');
563 |                      } else {
564 |                          navigation.classList.remove('show');
565 |                      }
566 |                  });
567 | 
568 |                  // Keep your existing navigation item click event listener
569 |                  let list = document.querySelectorAll('.navigation li');
570 |                  function activeLink() {
571 |                      list.forEach((item) => item.classList.remove('active'));
572 |                      this.classList.add('active');
573 |                  }
574 |                  list.forEach((item) => item.addEventListener('click', activeLink));
575 |              });
576 | 
577 |          </script>
578 | 
579 |  <!-- Form to enter company name -->
580 |  <form method="post" class="mb-4">
581 |      <div class="dropdown-container">
582 |      <label for="company_name" class="form-label">Enter Company Identifier:</label>
583 |      <input type="text" id="company_name" name="company_name" class="form-control" style="width:850px;" required>
584 | 
585 |      <div class="form-check mt-2">
586 |          <input class="form-check-input" type="radio" id="company" name="idType" value="name" checked>
587 |          <label class="form-check-label" for="company">Company</label>
588 |      </div>
589 |      <div class="form-check">
590 |          <input class="form-check-input" type="radio" id="ticker" name="idType" value="ticker">
591 |          <label class="form-check-label" for="ticker">Ticker</label>
592 |      </div>
593 |      <div class="form-check">
594 |          <input class="form-check-input" type="radio" id="isin" name="idType" value="isin">
595 |          <label class="form-check-label" for="isin">ISIN</label>
596 |      </div>
597 |      </div>
598 |      <!-- Submit Button and Spinner Container -->
599 |      <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 10px;">
600 |          <button type="submit" id="submit" class="submit-button">Search</button>
601 |          <div id="loading-spinner" style="display: none;"></div>
602 |      </div>
603 | 
604 |  </form>
605 |  <div id="resultContainer" style="display: none;"></div>
606 |  {% if company_name %}
607 |  <div class="report-container">
608 |      {% if report_url %}
609 |          <p>Latest ESG Report Link for {{company_name}}: <a href="{{ report_url }}" target="_blank">{{ report_url }}</a></p>
610 | 
611 | 
612 | 
613 | 
614 |      {% else %}
615 |          <p>No report found.</p>
616 |      {% endif %}
617 |  </div>
618 | 
619 | 
620 | 
621 | 
622 | 
623 | 
624 | 
625 | 
626 | 
627 | 
628 | 
629 | 
630 | 
631 | 
632 | 
633 | 
634 | 
635 | 
636 | 
637 | 
638 | 
639 | 
640 | 
641 | 
642 |      <!-- Tab Navigation -->
643 |      <ul class="nav nav-tabs mt-4" id="resultTabs" role="tablist">
644 |          <li class="nav-item" role="presentation">
645 |              <button class="nav-link active" id="table-tab" data-bs-toggle="tab" data-bs-target="#table-content" type="button" role="tab">Extracted Table <i class="fa-solid fa-table"></i></button>
646 |          </li>
647 |          <li class="nav-item" role="presentation">
648 |              <button class="nav-link" id="news-tab" data-bs-toggle="tab" data-bs-target="#news-content" type="button" role="tab">Latest News <i class="fa-solid fa-newspaper"></i></button>
649 |          </li>
650 |          <li class="nav-item" role="presentation">
651 |              <button class="nav-link" id="chart-tab" data-bs-toggle="tab" data-bs-target="#chart-content" type="button" role="tab">Data Visualization <i class="fa-solid fa-chart-column"></i></button>
652 |          </li>
653 |      </ul>
654 | 
655 |      <!-- Tab Content -->
656 |          <div class="tab-content mt-3" id="resultTabsContent">
657 |           <!-- Table Section -->
658 |           <div class="tab-pane fade show active" id="table-content" role="tabpanel">
659 |               {% if company_name and table_html %}
660 |               <div class="selected-company">
661 |                   <a href="{{ url_for('download_table', company_name=company_name) }}" class="btn btn-success mt-3">Download Table</a>
662 |                   <div>
663 |                       {{ table_html | safe }}
664 |                   </div>
665 |               {% else %}
666 |                   <p>No table data available.</p>
667 |               {% endif %}
668 |           </div>
669 |           </div>
670 | 
671 |          <!-- News Section -->
672 |          <div class="tab-pane fade" id="news-content" role="tabpanel">
673 |           <br>
674 |           <h3>Top Headlines for {{ company_name }}</h3>
675 |           {% if news_data %}
676 |               <div class="container-fluid"> <!-- Fluid container to match background -->
677 |                   <div class="row">
678 |                       {% for news in news_data %}
679 |                           <div class="col-md-6 mb-4"> <!-- Two columns per row -->
680 |                               <div class="card border-0 shadow-sm bg-transparent"> <!-- Transparent background -->
681 |                                   <div class="card-body d-flex align-items-center">
682 |                                       <img src="{{ news.image }}" alt="News Image" class="news-image me-3"
683 |                                            onerror="this.style.display='none';" style="width: 100px; height: auto;">
684 |                                       <div>
685 |                                           <strong style="color: white;">{{ news.title }}</strong> <!-- News Title -->
686 |                                           <br>
687 |                                           <small style="color: white;">Source: {{ news.publisher }}</small> <!-- Publisher Name -->
688 |                                           <br>
689 |                                           <a href="{{ news.link }}" target="_blank" class="btn btn-primary btn-sm mt-2">Read More</a> <!-- Read More Button -->
690 |                                       </div>
691 |                                   </div>
692 |                               </div>
693 |                           </div>
694 |                       {% endfor %}
695 |                   </div>
696 |               </div>
697 |           {% else %}
698 |               <p>No news available for this company.</p>
699 |           {% endif %}
700 |       </div>
701 | 
702 |           <!-- Histogram Visualization Section -->
703 |        <div class="tab-pane fade" id="chart-content">
704 |     <div class="chart-container">
705 |         <h3>Emissions Data Visualization</h3>
706 |         <canvas id="emissionsChart"></canvas>
707 |     </div>
708 |        {% endif %}
709 | </div>
710 | 
711 |          <div class="page-bottom">
712 |       </div>
713 | 
714 |      </div>
715 | 
716 |      <!-- Bootstrap JS (Ensure Bootstrap's JavaScript is included) -->
717 |      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
718 | 
719 |     <!-- React and ReactDOM via CDN -->
720 |     <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
721 |     <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
722 |     <!-- Material-UI Core (includes CircularProgress) -->
723 |     <script crossorigin src="https://unpkg.com/@mui/material@latest/umd/material-ui.production.min.js"></script>
724 | 
725 |     <script>
726 |     document.addEventListener("DOMContentLoaded", function () {
727 |      const { CircularProgress } = window.MaterialUI || {};
728 |      const spinnerContainer = document.getElementById("loading-spinner");
729 |      const submitButton = document.getElementById("submit");
730 |      const form = document.querySelector("form");
731 | 
732 |      let spinnerInitialized = false;
733 |      function initializeSpinner() {
734 |          if (!spinnerInitialized && CircularProgress) {
735 |              const spinner = React.createElement(CircularProgress, { color: "success", size: 24 });
736 |              ReactDOM.render(spinner, spinnerContainer);
737 |              spinnerInitialized = true;
738 |          }
739 |      }
740 | 
741 |      function showSpinner() {
742 |          submitButton.disabled = true;
743 |          submitButton.innerText = "Searching...";
744 |          initializeSpinner();
745 |          spinnerContainer.style.display = "inline-block"; // Show only when "Searching..."
746 |      }
747 | 
748 |      function hideSpinner() {
749 |          submitButton.disabled = false;
750 |          submitButton.innerText = "Search";
751 |          spinnerContainer.style.display = "none";
752 |      }
753 | 
754 |      form.addEventListener("submit", function () {
755 |          showSpinner();
756 |      });
757 | 
758 |      //  Reset spinner if user navigates away or cancels search
759 |      submitButton.addEventListener("click", function () {
760 |          if (submitButton.innerText === "Searching...") {
761 |              hideSpinner();
762 |          }
763 |      });
764 |     });
765 | 
766 |     </script>
767 |    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
768 | <script>
769 | document.addEventListener("DOMContentLoaded", function () {
770 |     function extractDataFromTable() {
771 |         const table = document.querySelector(".selected-company table");
772 |         if (!table) {
773 |             console.error(" No table found in .selected-company!");
774 |             return;
775 |         }
776 | 
777 |         const rows = table.querySelectorAll("tr");
778 |         if (rows.length < 2) {
779 |             console.error(" Table has no data rows.");
780 |             return;
781 |         }
782 | 
783 |         // Extract Headers & Year Columns
784 |         const headers = Array.from(rows[0].querySelectorAll("th")).map(th => th.innerText.trim());
785 |         let yearHeaders = headers.filter(h => /^\d{4}$/.test(h));
786 |         let yearIndexes = headers.map((h, i) => (yearHeaders.includes(h) ? i : -1)).filter(i => i !== -1);
787 | 
788 |         if (yearHeaders.length === 0) {
789 |             console.error(" No valid year columns found.");
790 |             return;
791 |         }
792 | 
793 |         console.log(" Extracted Year Headers:", yearHeaders);
794 | 
795 |         let emissionsData = {};
796 |         let dataFound = false;
797 | 
798 |         rows.forEach((row, rowIndex) => {
799 |             if (rowIndex === 0) return;
800 |             const cells = row.querySelectorAll("td");
801 | 
802 |             let metricName = cells[1]?.innerText.trim() || `Metric ${rowIndex}`; // Extract actual metric name from column 2
803 |             let values = yearIndexes.map(colIndex => {
804 |                 let value = parseFloat(cells[colIndex]?.innerText.replace(/,/g, "").trim()) || 0;
805 |                 if (value !== 0) dataFound = true;
806 |                 return value;
807 |             });
808 | 
809 |             emissionsData[metricName] = values;
810 |         });
811 | 
812 |         if (dataFound) {
813 |             console.log(" Emissions Data:", emissionsData);
814 |             setTimeout(() => renderHistogram(yearHeaders, emissionsData), 500);
815 |         } else {
816 |             console.warn("No valid emissions data found.");
817 |         }
818 |     }
819 | 
820 |     function renderHistogram(labels, emissionsData) {
821 |         const canvas = document.getElementById("emissionsChart");
822 |         if (!canvas) {
823 |             console.error(" No canvas element found!");
824 |             return;
825 |         }
826 | 
827 |         const ctx = canvas.getContext("2d");
828 | 
829 |         if (window.myChart) {
830 |             window.myChart.destroy();
831 |         }
832 | 
833 |         const datasets = Object.keys(emissionsData).map((metric, index) => ({
834 |             label: metric, // Use metric names from column 2 as legend labels
835 |             data: emissionsData[metric],
836 |             backgroundColor: getRandomColor(index),
837 |             borderWidth: 1
838 |         }));
839 | 
840 |         window.myChart = new Chart(ctx, {
841 |             type: "bar",
842 |             data: { labels: labels, datasets: datasets },
843 |             options: {
844 |                 responsive: true,
845 |                 plugins: {
846 |                     legend: { position: "top" },
847 |                     title: { display: true, text: "Emissions Over the Years" }
848 |                 },
849 |                 scales: {
850 |                     x: { title: { display: true, text: "Year" } },
851 |                     y: { title: { display: true, text: "Emissions" }, beginAtZero: true }
852 |                 }
853 |             }
854 |         });
855 |     }
856 | 
857 |     function getRandomColor(index) {
858 |         const colors = ["rgba(255, 99, 132, 0.7)", "rgba(54, 162, 235, 0.7)", "rgba(255, 206, 86, 0.7)"];
859 |         return colors[index % colors.length];
860 |     }
861 | 
862 |     extractDataFromTable();
863 | });
864 | </script>
865 | 
866 | 
867 | </body>
868 | </html>
869 | 
870 | 
871 | 
```

src/utils/__init__.py
```
```

src/utils/data.py
```
1 | import os
2 | import sys
3 | import urllib
4 | from io import BytesIO
5 | from typing import List
6 | 
7 | import pandas as pd
8 | import requests
9 | from dotenv import load_dotenv
10 | from loguru import logger
11 | 
12 | load_dotenv()
13 | 
14 | sys.path.append(os.getenv("ROOT_DIR"))
15 | 
16 | # URL to the CSV file (ACWI ETF holdings)
17 | MSCI_FUND_URL = "https://www.blackrock.com/ca/investors/en/products/239697/ishares-msci-world-index-etf/1515395013957.ajax?fileType=xls&fileName=iShares-MSCI-World-Index-ETF_fund&dataType=fund"
18 | 
19 | 
20 | def get_msci_index_df(write=False):
21 |     """
22 |     # TODO - add functionality for data refresh every 2 months
23 |     Function to fetch the MSCI ACWI ETF holdings data and return a filtered DataFrame.
24 | 
25 |     Args:
26 |         write (bool): Whether to write the CSV file to disk (default: False)
27 | 
28 |     Returns:
29 |         pd.DataFrame: DataFrame containing the MSCI ACWI ETF holdings data
30 |     """
31 |     headers = {
32 |         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
33 |     }
34 | 
35 |     # if file already downloaded read directly from disk
36 |     if os.path.exists(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv'):
37 |         # Load the CSV file from disk
38 |         df = pd.read_csv(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', header=9)
39 |     else:
40 |         response = requests.get(MSCI_FUND_URL, headers=headers)
41 |         # Save the CSV file to disk (optional)
42 |         if write:
43 |             with open(f'{os.getenv("ROOT_DIR")}/data/ACWI_holdings.csv', "wb") as f:
44 |                 f.write(response.content)
45 |         # Load the content into a Pandas DataFrame (headers are on row 10 (0-indexed: row 9))
46 |         file_content = BytesIO(response.content)
47 |         df = pd.read_csv(file_content, header=9)
48 |     # Filter the rows where the 'Asset Class' column is equal to 'Equity'
49 |     df_filtered = df[df["Asset Class"] == "Equity"]
50 |     # Select the first two columns (Ticker and Name)
51 |     df_filtered = df_filtered[["Ticker", "Name"]]
52 |     return df_filtered
53 | 
54 | 
55 | def download_pdf_from_urls(urls: List[str], root_path: str):
56 |     """
57 |     Function to download a PDF file from a URL. Breaks on the first successful download.
58 | 
59 |     Args:
60 |         urls (List[str]): List of URLs to try to download in pdf format.
61 |     """
62 |     for url in urls:
63 |         try:
64 |             # isolate PDF filename from URL
65 |             pdf_file_name = (
66 |                 os.path.basename(url) + ".pdf"
67 |                 if not url.endswith(".pdf")
68 |                 else os.path.basename(url)
69 |             )
70 |             with urllib.request.urlopen(url, timeout=10):
71 |                 urllib.request.urlretrieve(url, os.path.join(root_path, pdf_file_name))
72 |             return os.path.join(root_path, pdf_file_name)
73 |         except Exception as e:
74 |             logger.error(f"Uh oh! Could not download {url}: {e}")
75 |             continue
```

src/utils/data_models.py
```
1 | """
2 | Stores enums and data models
3 | """
4 | 
5 | from enum import Enum
6 | 
7 | from pydantic import BaseModel, Field
8 | 
9 | 
10 | class SearchKeyWords(Enum):
11 |     ESG = "esg"
12 |     CSR = "csr"
13 |     SUSTAINABILITY = "sustainability"
14 |     EMISSION = "emission"
15 |     ENVIRONMENT = "environment"
16 |     SCOPE_1 = "scope 1"
17 |     SCOPE_2 = "scope 2"
18 |     SCOPE = "scope"
19 |     SUSTAINABLE = "sustainable"
20 |     IMPACT = "impact"
21 |     REPORT = "report"
22 |     FACT_SHEET = "fact sheet"
23 | 
24 | 
25 | class RegexPatterns(Enum):
26 |     SCOPE1 = r"\b(scope\s*1|scope\s*i|scope\s*one)\b"
27 |     SCOPE2 = r"\b(scope\s*2|scope\s*ii|scope\s*two)\b"
28 |     YEAR_1 = r"\b(?:FY|FISCAL\s*YEAR)?\s*(\d{2}|20\d{2}|[-–]\d{2})"
29 |     YEAR_2 = r"\b(\d{2}|20\d{2}|[-–]\d{2})"
30 |     UNITS_1 = r"\b(?:\d+(?:,\d{3})*(?:\.\d+)?|million|billion|thousand)"
31 |     UNITS_2 = r"\s*(?:tco2e|tco2-e|co2e|co₂e|co2-eq|co₂-eq|mtco2e|mtco₂e|ktco2e|ktco₂e|mt|kt|tons?|tonnes?|metric\s*tons?)"
32 | 
33 | 
34 | class TableParsers(Enum):
35 |     DOCLING = "docling"
36 |     TABULA = "tabula"
37 | 
38 | 
39 | class PDFParsers(Enum):
40 |     LLAMA_PARSE = "llama"
41 | 
42 | 
43 | class Company(BaseModel):
44 |     ticker: str = Field(..., title="Ticker Symbol")
45 |     name: str = Field(..., title="Company Name")
46 |     isin: str = Field(..., title="Company ISIN")
```

src/utils/llm_table_data_filtering.py
```
1 | import os
2 | 
3 | import pandas as pd
4 | from dotenv import load_dotenv
5 | 
6 | load_dotenv()
7 | 
8 | 
9 | try:
10 |     from openai import OpenAI
11 | except ImportError:
12 |     print("OpenAI client is not installed. Please install with: pip install openai")
13 |     OpenAI = None
14 | 
15 | 
16 | # Both keys are available. Uncomment the one you want to use below.
17 | OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
18 | DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
19 | 
20 | 
21 | def filter_tables(directory_path, parser):
22 |     """
23 |     Gather all CSVs in directory_path/parser.value, convert them to markdown,
24 |     send them to the LLM, store the LLM's markdown output, and return as a DataFrame.
25 |     """
26 | 
27 |     # 1) Collect all CSVs into one markdown string
28 |     combined_markdown = ""
29 |     parser_subfolder = os.path.join(directory_path, parser.value)
30 | 
31 |     # If the parser subfolder doesn't exist or is empty, handle gracefully
32 |     if not os.path.isdir(parser_subfolder):
33 |         print(f"No directory found for parser: {parser_subfolder}")
34 |         return pd.DataFrame()
35 | 
36 |     for filename in os.listdir(parser_subfolder):
37 |         if filename.endswith(".csv"):
38 |             file_path = os.path.join(parser_subfolder, filename)
39 |             try:
40 |                 df = pd.read_csv(file_path)
41 |                 # Convert df to markdown
42 |                 md = df.to_markdown(index=False, tablefmt="pipe")
43 |                 # Optionally label by file
44 |                 combined_markdown += f"\n\n#### File: {filename}\n\n"
45 |                 combined_markdown += md
46 |                 combined_markdown += "\n\n"
47 |             except Exception as e:
48 |                 print(f"Error reading CSV {file_path}: {e}")
49 | 
50 |     if not combined_markdown.strip():
51 |         print("No CSV data found to send to the LLM.")
52 |         return pd.DataFrame()
53 | 
54 |     # 2) Send markdown content to LLM
55 |     llm_output = _send_to_deepseek(combined_markdown)
56 |     if not llm_output:
57 |         print("No response from LLM or an error occurred.")
58 |         return pd.DataFrame()
59 | 
60 |     # 3) Save the LLM's markdown output directly as .md file
61 |     output_path = os.path.join(directory_path, "esg_data_llm.md")
62 |     with open(output_path, "w", encoding="utf-8") as f:
63 |         f.write(llm_output)
64 |     print(f"LLM output saved to: {output_path}")
65 | 
66 |     # 4) Return DataFrame for compatibility with existing code
67 |     return pd.DataFrame({"LLM_Output": [llm_output]})
68 | 
69 | 
70 | def _send_to_deepseek(markdown_content: str) -> str | None:
71 |     """Sends markdown content to the LLM (either OpenAI or DeepSeek) for processing."""
72 |     # ---------------------------------------------------------------------
73 |     # To use OpenAI, uncomment the following block:
74 |     if not OPENAI_API_KEY:
75 |         print("OpenAI API key missing.")
76 |         return None
77 |     client = OpenAI(api_key=OPENAI_API_KEY)
78 |     # model="gpt-4o" will be used below.
79 |     # ---------------------------------------------------------------------
80 | 
81 |     # ---------------------------------------------------------------------
82 |     # To use DeepSeek, comment out the above block and uncomment this one:
83 |     # if not DEEPSEEK_API_KEY:
84 |     #     print("DeepSeek API key missing.")
85 |     #     return None
86 |     # client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
87 |     # ---------------------------------------------------------------------
88 | 
89 |     try:
90 |         response = client.chat.completions.create(
91 |             # -----------------------------------------------------------------
92 |             # To use OpenAI, uncomment the following line:
93 |             model="gpt-4o",
94 |             # To use DeepSeek, comment out the above line and uncomment this one:
95 |             # model="deepseek-chat",
96 |             # -----------------------------------------------------------------
97 |             messages=[
98 |                 {
99 |                     "role": "system",
100 |                     "content": "You are a sustainability data extraction specialist. Return ONLY valid markdown tables.",
101 |                 },
102 |                 {"role": "user", "content": _build_llm_prompt(markdown_content)},
103 |             ],
104 |             temperature=1,
105 |             max_tokens=4000,
106 |         )
107 |         return response.choices[0].message.content.strip()
108 |     except Exception as e:
109 |         print(f"API error: {str(e)}")
110 |         return None
111 | 
112 | 
113 | def _build_llm_prompt(markdown_data: str) -> str:
114 |     return f"""
115 | You are given sustainability report tables as markdown below:
116 | {markdown_data}
117 | 
118 | 
119 | 
120 | 
121 | Please perform the following steps:
122 | 
123 | 
124 | 
125 | 
126 | 1. Identify the table(s) with the most complete year-by-year data for
127 |  Scope 1, Scope 2 (market-based), and Scope 2 (location-based)
128 |  from the provided markdown.
129 |  - Use judgment to select tables with the most complete and likely
130 |    accurate data across all years.
131 |  - Prioritize completeness and consistency.
132 |  - For Scope 2, include both market-based and location-based data if
133 |    available, and explicitly note which is which.
134 |  - Convert all values to tCO2e and keep units consistent across years.
135 |  - Use null for years where data is missing or unavailable.
136 | 
137 | 
138 | 
139 | 
140 | 2. Create a **"Key Table"** in Markdown with columns for:
141 |  | Category | Year | Emissions (tCO2e) |
142 |  The rows should be:
143 |    - Scope 1
144 |    - Scope 2 (Market-based)
145 |    - Scope 2 (Location-based)
146 |  Include data for as many years as can be found (e.g., 2020, 2021, 2022, 2023).
147 |  Convert all values to tCO2e. Use null for years where data is missing.
148 | 
149 | 
150 | 
151 | 
152 | 3. Create four additional Markdown tables (breakdown tables) if
153 |  information is available; otherwise, return them with "No Data" or "N/A":
154 |  - **Scope 1 Breakdown**:
155 |    | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
156 |  - **Scope 2 Market-based Breakdown**:
157 |    | Region or Business Unit | Year | Emissions (tCO2e) |
158 |  - **Scope 2 Location-based Breakdown**:
159 |    | Region or Business Unit | Year | Emissions (tCO2e) |
160 |  - **Scope 3 Breakdown**:
161 |    | Scope 3 Category | Year | Emissions (tCO2e) |
162 |    Always include a "Total Scope 3" row.
163 | 
164 | 
165 | 
166 | 
167 | 4. Return exactly **these five Markdown tables** in this order with titles:
168 |  A) Key Table
169 |  B) Scope 1 Breakdown
170 |  C) Scope 2 Market-based Breakdown
171 |  D) Scope 2 Location-based Breakdown
172 |  E) Scope 3 Breakdown (with Total)
173 | 
174 | 
175 | 
176 | 
177 | 5. Provide **no additional commentary**, just the five tables in Markdown format.
178 | """
```

src/utils/rag_utils.py
```
1 | import hashlib
2 | import json
3 | import logging
4 | import os
5 | import shutil  # added for cache removal
6 | from threading import Event
7 | 
8 | import pymupdf4llm
9 | from langchain.prompts import ChatPromptTemplate
10 | from langchain.retrievers.multi_vector import MultiVectorRetriever
11 | from langchain.schema import Document, StrOutputParser
12 | from langchain.storage import InMemoryStore
13 | from langchain.text_splitter import MarkdownTextSplitter
14 | from langchain_community.embeddings import HuggingFaceEmbeddings
15 | from langchain_community.vectorstores import FAISS
16 | from langchain_core.runnables import RunnableLambda, RunnablePassthrough
17 | from langchain_openai import ChatOpenAI
18 | 
19 | logger = logging.getLogger(__name__)
20 | 
21 | 
22 | # ===========================
23 | # Environment Variables
24 | # ===========================
25 | OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
26 | DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
27 | 
28 | 
29 | # ===========================
30 | # Global RAG variables
31 | # ===========================
32 | rag_chain = None
33 | rag_initialized = False
34 | pdf_path_global = None
35 | stop_rag_event = Event()
36 | 
37 | 
38 | def _pdf_md5(pdf_path: str) -> str:
39 |     """Compute an MD5 hash of the entire PDF file contents."""
40 |     md5 = hashlib.md5()
41 |     with open(pdf_path, "rb") as f:
42 |         md5.update(f.read())
43 |     return md5.hexdigest()
44 | 
45 | 
46 | def _rag_cache_dir(pdf_path: str) -> str:
47 |     """Get the base 'rag_cache' folder next to the PDF."""
48 |     return os.path.join(os.path.dirname(pdf_path), "rag_cache")
49 | 
50 | 
51 | def chunk_with_tables(pdf_path):
52 |     """Convert PDF to markdown with table preservation. Skips on error or stop event."""
53 |     if stop_rag_event.is_set():
54 |         logger.info(
55 |             "Stop RAG event triggered before chunking. Exiting chunk_with_tables early."
56 |         )
57 |         return []
58 | 
59 |     try:
60 |         md_text = pymupdf4llm.to_markdown(pdf_path, write_images=False)
61 |     except Exception as e:
62 |         logger.error(f"Cannot parse PDF text: {e}")
63 |         return []
64 | 
65 |     if stop_rag_event.is_set():
66 |         logger.info("Stop RAG event triggered after PDF->markdown. Exiting.")
67 |         return []
68 | 
69 |     splitter = MarkdownTextSplitter(chunk_size=5000, chunk_overlap=400)
70 |     chunks = splitter.split_text(md_text)
71 | 
72 |     if stop_rag_event.is_set():
73 |         logger.info("Stop RAG event triggered after splitting text. Exiting.")
74 |         return []
75 | 
76 |     return chunks
77 | 
78 | 
79 | def build_rag_system(pdf_path):
80 |     """
81 |     Build the RAG pipeline using the unfiltered PDF, checking for a cached
82 |     FAISS vector store + docstore so we can skip chunking/summarizing if already done.
83 |     """
84 |     if stop_rag_event.is_set():
85 |         logger.info("Stop RAG event triggered at start of build_rag_system.")
86 |         return None
87 | 
88 |     # 1) Attempt to load from disk cache
89 |     pdf_hash = _pdf_md5(pdf_path)
90 |     cache_folder = os.path.join(_rag_cache_dir(pdf_path), pdf_hash)
91 |     vectorstore_dir = os.path.join(cache_folder, "vectorstore")
92 |     docstore_json = os.path.join(cache_folder, "docstore.json")
93 | 
94 |     if os.path.isdir(vectorstore_dir) and os.path.isfile(docstore_json):
95 |         logger.info(
96 |             f"[RAG Cache] Found existing cache for hash={pdf_hash}. Attempting to load."
97 |         )
98 |         if stop_rag_event.is_set():
99 |             logger.info(
100 |                 "Stop event was set before loading cache. Exiting build_rag_system."
101 |             )
102 |             return None
103 |         try:
104 |             embedder = HuggingFaceEmbeddings(
105 |                 model_name="nomic-ai/nomic-embed-text-v1.5",
106 |                 model_kwargs={"device": "cpu", "trust_remote_code": True},
107 |             )
108 |             # Load the FAISS index with dangerous deserialization allowed.
109 |             vectorstore = FAISS.load_local(
110 |                 vectorstore_dir,
111 |                 embeddings=embedder,
112 |                 allow_dangerous_deserialization=True,
113 |             )
114 |             # Load docstore from JSON
115 |             with open(docstore_json, "r", encoding="utf-8") as f:
116 |                 stored_docs = json.load(f)  # list of [doc_id, doc_content]
117 |             docstore = InMemoryStore()
118 |             for doc_id, content in stored_docs:
119 |                 docstore.mset(
120 |                     [
121 |                         (
122 |                             doc_id,
123 |                             Document(page_content=content, metadata={"doc_id": doc_id}),
124 |                         )
125 |                     ]
126 |                 )
127 |             retriever = MultiVectorRetriever(
128 |                 vectorstore=vectorstore,
129 |                 docstore=docstore,
130 |                 id_key="doc_id",
131 |                 search_kwargs={"k": 3},
132 |             )
133 |             logger.info("[RAG Cache] Successfully loaded RAG cache!")
134 |             return retriever
135 | 
136 |         except Exception as e:
137 |             logger.warning(
138 |                 f"[RAG Cache] Failed to load from cache: {e}. Removing cache folder and proceeding with normal pipeline."
139 |             )
140 |             try:
141 |                 shutil.rmtree(cache_folder)
142 |             except Exception as re:
143 |                 logger.error(f"Failed to remove cache folder {cache_folder}: {re}")
144 | 
145 |     # 2) No valid cache found; proceed with chunking & summarizing.
146 |     chunks = chunk_with_tables(pdf_path)
147 |     if stop_rag_event.is_set() or not chunks:
148 |         logger.info(
149 |             "Stop RAG event triggered or no chunks found. Exiting build_rag_system."
150 |         )
151 |         return None
152 | 
153 |     summarize_prompt = ChatPromptTemplate.from_template(
154 |         """
155 | Create a concise summary of this text chunk from a sustainability report
156 | optimized for retrieval purposes.
157 | Focus on:
158 | - Key numerical data and metrics
159 | - Table and figure descriptions
160 | - Technical terms and definitions
161 | Original text: {chunk}
162 | Summary:"""
163 |     )
164 | 
165 |     # ===================================================================
166 |     # To switch to DeepSeek, comment out the OpenAI lines and uncomment
167 |     # the DeepSeek lines below:
168 |     #
169 |     summarizer = (
170 |         {"chunk": RunnablePassthrough()}
171 |         | summarize_prompt
172 |         | ChatOpenAI(
173 |             # --- OPENAI (default) ---
174 |             openai_api_key=OPENAI_API_KEY,
175 |             model="gpt-4o-mini",
176 |             # ------------------------
177 |             # --- DEEPSEEK (comment out the above lines, then uncomment below) ---
178 |             # openai_api_key=DEEPSEEK_API_KEY,
179 |             # base_url="https://api.deepseek.com",
180 |             # model="deepseek-chat",
181 |             # -------------------------------------------------------
182 |             temperature=0.2,
183 |         )
184 |         | StrOutputParser()
185 |     )
186 |     # ===================================================================
187 | 
188 |     if stop_rag_event.is_set():
189 |         logger.info("Stop RAG event triggered before summarizing. Exiting.")
190 |         return None
191 | 
192 |     summaries = summarizer.batch(chunks)
193 |     if stop_rag_event.is_set() or not summaries:
194 |         logger.info("Stop event was set after summarizing. Exiting.")
195 |         return None
196 | 
197 |     summary_docs = [
198 |         Document(page_content=s, metadata={"doc_id": str(i)})
199 |         for i, s in enumerate(summaries)
200 |     ]
201 |     original_docs = [
202 |         Document(page_content=c, metadata={"doc_id": str(i)})
203 |         for i, c in enumerate(chunks)
204 |     ]
205 | 
206 |     embedder = HuggingFaceEmbeddings(
207 |         model_name="nomic-ai/nomic-embed-text-v1.5",
208 |         model_kwargs={"device": "cpu", "trust_remote_code": True},
209 |     )
210 | 
211 |     if stop_rag_event.is_set():
212 |         logger.info("Stop RAG event triggered before embedding. Exiting.")
213 |         return None
214 | 
215 |     vectorstore = FAISS.from_documents(summary_docs, embedder)
216 |     docstore = InMemoryStore()
217 |     docstore.mset([(str(i), original_docs[i]) for i in range(len(original_docs))])
218 | 
219 |     # 3) Save new cache if not stopped
220 |     if not stop_rag_event.is_set():
221 |         try:
222 |             os.makedirs(cache_folder, exist_ok=True)
223 |             vectorstore.save_local(vectorstore_dir)
224 |             # Save docstore to JSON
225 |             doc_data = []
226 |             for i, c in enumerate(chunks):
227 |                 doc_data.append((str(i), c))
228 |             with open(docstore_json, "w", encoding="utf-8") as f:
229 |                 json.dump(doc_data, f, indent=2)
230 |             logger.info(f"[RAG Cache] Saved new RAG cache to {cache_folder}")
231 |         except Exception as e:
232 |             logger.error(f"[RAG Cache] Failed to save cache: {e}")
233 | 
234 |     retriever = MultiVectorRetriever(
235 |         vectorstore=vectorstore,
236 |         docstore=docstore,
237 |         id_key="doc_id",
238 |         search_kwargs={"k": 3},
239 |     )
240 | 
241 |     return retriever
242 | 
243 | 
244 | def build_final_system(pdf_path):
245 |     """
246 |     Wrap the retriever in a final prompt chain that answers user queries.
247 |     """
248 |     if stop_rag_event.is_set():
249 |         logging.info("Stop RAG event triggered at start of build_final_system.")
250 |         return None
251 | 
252 |     retriever = build_rag_system(pdf_path)
253 |     if stop_rag_event.is_set() or retriever is None:
254 |         logging.info(
255 |             "Stop RAG event triggered or retriever is None. Exiting build_final_system."
256 |         )
257 |         return None
258 | 
259 |     prompt = ChatPromptTemplate.from_template(
260 |         """
261 | Analyze this parsed text and poorly formatted markdown tables from a sustainability report:
262 | {context}
263 | 
264 | 
265 | Respond as a sustainability report assistant providing relevant information in detail.
266 | Create your own tables if applicable. If data is not available, say "Data not available".
267 | 
268 | 
269 | Question: {input}
270 | """
271 |     )
272 | 
273 |     if stop_rag_event.is_set():
274 |         logging.info(
275 |             "Stop RAG event triggered before returning final pipeline. Exiting build_final_system."
276 |         )
277 |         return None
278 | 
279 |     # ===================================================================
280 |     # To switch to DeepSeek, comment out the OpenAI lines and uncomment
281 |     # the DeepSeek lines below:
282 |     #
283 |     final_pipeline = (
284 |         {
285 |             "context": retriever
286 |             | RunnableLambda(lambda docs: "\n\n".join(d.page_content for d in docs)),
287 |             "input": RunnablePassthrough(),
288 |         }
289 |         | prompt
290 |         | ChatOpenAI(
291 |             # --- OPENAI ---
292 |             openai_api_key=OPENAI_API_KEY,
293 |             model="gpt-4o",
294 |             # ------------------------
295 |             # --- DEEPSEEK ---
296 |             # openai_api_key=DEEPSEEK_API_KEY,
297 |             # base_url="https://api.deepseek.com",
298 |             # model="deepseek-chat",
299 |             # -------------------------------------------------------
300 |             temperature=0.2,
301 |         )
302 |         | StrOutputParser()
303 |     )
304 | 
305 |     return final_pipeline
```

src/utils/standardize_table.py
```
1 | import os
2 | import re
3 | 
4 | import dotenv
5 | import numpy as np
6 | import pandas as pd
7 | 
8 | 
9 | def save_raw_data(df, output_path):
10 |     """
11 |     Save the raw data to a specified file path in CSV format.
12 |     """
13 |     df.to_csv(output_path, index=False)
14 |     print(f"Raw data saved at: {output_path}")
15 | 
16 | 
17 | def standardize_emissions_table(raw_data):
18 | 
19 |     renamed_columns = {}
20 |     for col in raw_data.columns:
21 |         clean_col = re.sub(r"[^a-zA-Z0-9 ]", " ", col).strip()
22 |         clean_col = " ".join(clean_col.split())  # Remove double spaces
23 |         match = re.search(r"(?:FY|fy|Year)?\D*(\d{4}|\d{2})", clean_col)
24 |         if match:
25 |             year = match.group(1)
26 |             if len(year) == 2:
27 |                 year = f"20{year}" if int(year) >= 10 else f"19{year}"
28 |             renamed_columns[col] = year
29 | 
30 |     raw_data = raw_data.rename(columns=renamed_columns)
31 |     financial_years = [
32 |         year for year in renamed_columns.values() if re.match(r"\b20\d{2}\b", year)
33 |     ]
34 | 
35 |     # Define regex patterns for Scope 1, Scope 2 Market, and Scope 2 Location
36 |     scope_1_pattern = r"scope\s*1"
37 |     scope_2_market_pattern = r"scope\s*2.*market"
38 |     scope_2_location_pattern = r"scope\s*2.*location"
39 |     scope_2_general_pattern = r"\bscope\s*2\b"
40 | 
41 |     # Identify the parameter column
42 |     parameter_col_index = None
43 |     for idx in range(len(raw_data.columns)):
44 |         if (
45 |             raw_data.iloc[:, idx]
46 |             .astype(str)
47 |             .str.contains(scope_1_pattern, case=False, regex=True)
48 |             .any()
49 |         ):
50 |             parameter_col_index = idx
51 |             break
52 | 
53 |     # Keep only relevant columns (years + parameter column)
54 |     if parameter_col_index is not None:
55 |         parameter_col_name = raw_data.columns[parameter_col_index]
56 |         columns_to_keep = (
57 |             [parameter_col_name]
58 |             + financial_years
59 |             + (["Units"] if "Units" in raw_data.columns else [])
60 |         )
61 | 
62 |     else:
63 |         columns_to_keep = financial_years
64 | 
65 |     filtered_data = raw_data[columns_to_keep]
66 |     filtered_data = filtered_data.rename(columns={filtered_data.columns[0]: "Metric"})
67 | 
68 |     # Save a copy of the filtered table
69 |     standardized_data = filtered_data.copy()
70 | 
71 |     # Keep rows matching Scope 1, Scope 2 Market, or Scope 2 Location
72 |     filtered_rows = standardized_data[
73 |         standardized_data.iloc[:, 0]
74 |         .astype(str)
75 |         .str.contains(
76 |             f"({scope_1_pattern}|{scope_2_market_pattern}|{scope_2_location_pattern})",
77 |             case=False,
78 |             regex=True,
79 |         )
80 |     ]
81 | 
82 |     # If no Scope 2 Market or Location rows exist, add rows matching Scope 2 General
83 |     if (
84 |         not filtered_rows.iloc[:, 0]
85 |         .astype(str)
86 |         .str.contains(scope_2_market_pattern, case=False, regex=True)
87 |         .any()
88 |         and not filtered_rows.iloc[:, 0]
89 |         .astype(str)
90 |         .str.contains(scope_2_location_pattern, case=False, regex=True)
91 |         .any()
92 |     ):
93 |         additional_rows = standardized_data[
94 |             standardized_data.iloc[:, 0]
95 |             .astype(str)
96 |             .str.contains(scope_2_general_pattern, case=False, regex=True)
97 |         ]
98 |         filtered_rows = pd.concat([filtered_rows, additional_rows], axis=0)
99 | 
100 |     # Function to clean the 'Metric' column by removing numbers except for 1 and 2 and commas
101 |     def clean_scope_metric(x):
102 |         # Convert to string
103 |         x = str(x)
104 | 
105 |         # Initialize a result list to accumulate the filtered characters
106 |         result = []
107 | 
108 |         # Flag to indicate when to stop removing characters
109 |         stop_removal = False
110 | 
111 |         # Start iterating from the end of the string
112 |         for char in reversed(x):
113 |             # If we encounter '1', '2', '(', ')', or any alphabet, stop removing
114 |             if char in ["1", "2", "(", ")"] or char.isalpha():
115 |                 stop_removal = True
116 | 
117 |             if stop_removal:
118 |                 result.append(char)
119 |             else:
120 |                 # Skip digits except 1 and 2, commas, and spaces
121 |                 if char.isdigit() and char not in ["1", "2"]:
122 |                     continue
123 |                 elif char == "," or char == " ":
124 |                     continue
125 |                 # Append allowed characters
126 |                 result.append(char)
127 | 
128 |         # Reverse the result list to get the original order and join it to form the final string
129 |         cleaned_x = "".join(reversed(result))
130 | 
131 |         return cleaned_x
132 | 
133 |     # Apply the cleaning function to the 'Metric' column in filtered_rows
134 |     filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)
135 | 
136 |     # Apply the cleaning function to the 'Metric' column in filtered_rows
137 |     filtered_rows["Metric"] = filtered_rows["Metric"].apply(clean_scope_metric)
138 | 
139 |     filtered_rows = filtered_rows.loc[:, ~filtered_rows.T.duplicated()]
140 |     filtered_rows.replace("", np.nan, inplace=True)
141 | 
142 |     # Drop rows where all values are NaN
143 |     filtered_rows = filtered_rows.dropna(how="any")
144 |     return filtered_rows
145 | 
146 | 
147 | def clean_header(headers):
148 |     """
149 |     Clean the header by removing any columns that match 'untitled' or 'Unnamed' (case-insensitive)
150 |     after the first valid one.
151 |     """
152 |     # Define the regex pattern to match 'untitled' or 'Unnamed' (case-insensitive)
153 |     invalid_pattern = re.compile(r"untitled|Unnamed", re.IGNORECASE)
154 | 
155 |     # Find the first valid header (non-"untitled" or "Unnamed" columns)
156 |     first_valid_header_index = next(
157 |         (i for i, header in enumerate(headers) if not invalid_pattern.search(header)),
158 |         None,
159 |     )
160 | 
161 |     if first_valid_header_index is not None:
162 |         # Remove all "untitled" or "Unnamed" columns after the first valid header
163 |         new_headers = headers[: first_valid_header_index + 1] + [
164 |             header
165 |             for header in headers[first_valid_header_index + 1 :]  # noqa: E203
166 |             if not invalid_pattern.search(header)
167 |         ]
168 |     else:
169 |         # If no valid header found, keep only the first and remove others
170 |         new_headers = headers[:1] + [
171 |             header for header in headers[1:] if not invalid_pattern.search(header)
172 |         ]
173 | 
174 |     return new_headers
175 | 
176 | 
177 | def clean_rows(df):
178 |     """
179 |     Clean rows by removing NaN values and shifting the data to the left.
180 |     """
181 |     cleaned_rows = []
182 |     for _, row in df.iterrows():
183 |         # Remove NaN values and shift the data to the left
184 |         cleaned_row = row.dropna().values.tolist()
185 |         cleaned_rows.append(cleaned_row)
186 |     return cleaned_rows
187 | 
188 | 
189 | def merge_rows_with_headers(cleaned_rows, headers):
190 |     """
191 |     Merge cleaned rows back into a DataFrame, filling with NA where necessary.
192 |     """
193 |     max_len = max(len(row) for row in cleaned_rows)
194 |     # Adjust each row to match the length of the header, filling missing values with NaN
195 |     adjusted_rows = [row + [np.nan] * (max_len - len(row)) for row in cleaned_rows]
196 | 
197 |     # Ensure all rows are aligned to the headers length
198 |     return pd.DataFrame(adjusted_rows, columns=headers)
199 | 
200 | 
201 | def process_dataframe(df):
202 |     """
203 |     Process the raw CSV file and clean up the data based on specified requirements.
204 |     """
205 | 
206 |     # Clean the header by removing "Untitled" columns after the first valid one
207 |     cleaned_headers = clean_header(df.columns.tolist())
208 | 
209 |     # Clean the rows by removing NaN values and shifting to the left
210 |     cleaned_rows = clean_rows(df)
211 | 
212 |     # Merge cleaned rows back into a DataFrame, aligning with the cleaned header
213 |     cleaned_df = merge_rows_with_headers(cleaned_rows, cleaned_headers)
214 | 
215 |     return cleaned_df
216 | 
217 | 
218 | def standardize_table(data):
219 |     try:
220 |         cleaned_data = process_dataframe(data)
221 |         print(cleaned_data.head())
222 |     except Exception as e:
223 |         print(f"Table clearing failed: {e}")
224 |         return None
225 | 
226 |     try:
227 |         standardized_table = standardize_emissions_table(
228 |             cleaned_data
229 |         )  # Pass the cleaned data
230 |         return standardized_table
231 | 
232 |     except Exception as e:
233 |         print(f"Standardization failed: {e}")
234 |         return cleaned_data
235 | 
236 | 
237 | if __name__ == "__main__":
238 |     dotenv.load_dotenv()
239 |     OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
240 |     file_path = os.path.join(OUTPUT_DIR, "BANK_OF_AMERICA_CORP", "esg_data.csv")
241 |     df = pd.read_csv(file_path)
242 |     try:
243 |         df = standardize_table(df)
244 |         print(df.head())
245 |         output_path = os.path.join(OUTPUT_DIR, "std_esg_data.csv")
246 |         save_raw_data(df, output_path)
247 |     except Exception as e:
248 |         print(f"Table clearing failed: {e}")
```

src/utils/units.py
```
1 | import os
2 | import re
3 | 
4 | import dotenv
5 | import pandas as pd
6 | 
7 | from src.utils.data_models import TableParsers
8 | 
9 | 
10 | def extract_units(value):
11 |     match = re.search(
12 |         r"\b(t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*o\s*f\s*C\s*O\s*2\s*e|C\s*O\s*2\s*e|t\s*C\s*O\s*2\s*e|M\s*T\s*C\s*O\s*2\s*e|k\s*g\s*C\s*O\s*2\s*e|k\s*t\s*C\s*O\s*2\s*e|g\s*C\s*O\s*2\s*e|h\s*u\s*n\s*d\s*r\s*e\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|t\s*h\s*o\s*u\s*s\s*a\s*n\s*d\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|b\s*i\s*l\s*l\s*i\s*o\s*n\s*s\s*o\s*f\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|m\s*e\s*t\s*r\s*i\s*c\s*t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*s\s*C\s*O\s*2\s*e|t\s*o\s*n\s*n\s*e\s*s\s*C\s*O\s*2\s*e|\srevenue\s)\b",
13 |         str(value),
14 |         re.IGNORECASE,
15 |     )
16 | 
17 |     return match.group(0) if match else None
18 | 
19 | 
20 | def get_units_raw_input(df: pd.DataFrame):
21 |     updated_df = df.copy()
22 | 
23 |     updated_df["Units"] = None
24 |     first_unit = None
25 |     for idx, row in df.iterrows():
26 |         extracted_units = extract_units(pd.DataFrame(row).to_string())
27 |         updated_df.iloc[idx]["Units"] = extracted_units
28 | 
29 |         if first_unit is None and extract_units is not None:
30 |             first_unit = extracted_units
31 | 
32 |     updated_df["Units"] = updated_df["Units"].apply(
33 |         lambda x: first_unit if x is None else x
34 |     )
35 | 
36 |     return updated_df
37 | 
38 | 
39 | def infer_emissions_unit(max, min):
40 |     """
41 |     Infer the unit of measurement based on the numerical value.
42 |     """
43 |     if max < 7:
44 |         return "Inferred: CO₂e per FTE"  # Emissions per Full-Time Employee
45 |     elif min > 2 and max < 100:
46 |         return "Inferred: MMT CO₂e"  # Million Metric Tons
47 |     elif min > 10 and max < 500:
48 |         return "Inferred: thousand MT CO₂e"  # Thousand Metric Tons
49 |     return "Inferred: MT CO₂e"  # Metric Tons
50 | 
51 | 
52 | def clean_numeric_values(row):
53 |     # Now apply the cleaning to all columns, including the first one (Metric)
54 |     numeric_values = pd.to_numeric(
55 |         row.astype(str).str.replace(
56 |             r"(?<=\d),(?=\d{3}\b)", "", regex=True
57 |         ),  # Remove commas only for thousands
58 |         errors="coerce",  # Ignore non-numeric values, treat them as NaN
59 |     ).dropna()
60 |     return numeric_values
61 | 
62 | 
63 | def infer_units_for_rows(filtered_rows):
64 |     """
65 |     Infer emissions unit for each row based on numerical values.
66 |     """
67 |     unit_inferences = []
68 |     for idx, row in filtered_rows.iterrows():
69 |         try:
70 |             # If the row already has a valid unit, keep it
71 |             if row["Units"] not in ["", None, "Unknown"]:
72 |                 unit_inferences.append(row["Units"])
73 |                 continue
74 |         except Exception:
75 |             unit_inferences.append(None)
76 | 
77 |         # Extract numerical values from the row (excluding the first column 'Metric')
78 |         numeric_values = clean_numeric_values(row)
79 | 
80 |         if numeric_values.empty:
81 |             unit_inferences.append(None)  # No valid numerical data
82 |         else:
83 |             # Infer unit based on the maximum value in the row
84 |             inferred_unit = infer_emissions_unit(
85 |                 numeric_values.max(), numeric_values.min()
86 |             )
87 |             unit_inferences.append(inferred_unit)
88 | 
89 |     try:
90 |         # Add the inferred units as a new column
91 |         filtered_rows["Units"] = unit_inferences
92 |     except ValueError:
93 |         filtered_rows["Units"] = unit_inferences[0]
94 |     return filtered_rows
95 | 
96 | 
97 | if __name__ == "__main__":
98 |     dotenv.load_dotenv()
99 |     OUTPUT_DIR = os.getenv("ROOT_OUTPUT_PATH")
100 |     df = pd.read_csv(
101 |         os.path.join(
102 |             OUTPUT_DIR,
103 |             "NVIDA",
104 |             TableParsers.DOCLING.value,
105 |             "FY2024-NVIDIA-Corporate-Sustainability-Report-table-2.csv",
106 |         )
107 |     )
108 |     get_units_raw_input(df)
```

data/cache/BE0003470755/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "BE0003470755",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "BE0003470755",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/BE0003470755"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://am.oddo-bhf.com/france/en/distributor__ifa/DownloadSingleDocumentML?Langue=GB&IDsarray=15909&IdSeqArray=2876354",
13 |         "1": "https://www.solvay.com/sites/g/files/srpend616/files/2022-04/Solvay%202021%20Annual%20Integrated%20Report.pdf",
14 |         "2": "https://iasj.org/wp-content/uploads/investor-guide-to-carbon-footprinting.pdf",
15 |         "3": "https://www.solvay.com/sites/g/files/srpend221/files/2020-08/First%20Half%202020%20presentation_0.pdf",
16 |         "4": "https://www.solvay.com/sites/g/files/srpend616/files/2019-10/20190731%20-%20Solvay%20second%20quarter%20%26%20first%20half%20year%202019%20results%20presentation%20to%20analysts%20%26%20investors.pdf"
17 |     }
18 | }
```

data/cache/IE00BLP1HW54/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "IE00BLP1HW54",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "IE00BLP1HW54",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/iman/Desktop/UCL 2024:26/IFTE0001-IntroToFM/esg-data-retrieval/data/cache/IE00BLP1HW54"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://veganetf.com/wp-content/uploads/2024/09/ESS-Beyond-Fund-Advisors-Voting-Table.pdf",
13 |         "1": "https://www.westpac.co.nz/assets/Personal/investments/documents/Westpac-Active-Series-full-portfolio-holdings/Moderate-trust/Active-Series-Moderate-Trust-Full-Portfolio-Holdings-Report-31-March-2023.pdf",
14 |         "2": "https://api.schroders.com/document-store/AUF-Schroder-Global-Core-Fund-VR-AUEN.pdf",
15 |         "3": "https://inversis.lu/corporative-site-lux/dam/jcr:bcf8cab2-8805-4085-a522-7c71d35c25bd/BA3-Strategic-Investment_FS_-31.12.22_signed-by-MAB-1.pdf",
16 |         "4": "https://bankone.mu/private/wp-content/files/sites/2/2024/09/Newsletter-2409.pdf"
17 |     }
18 | }
```

data/cache/MICROSOFT_CORP/esg_data.csv
```
1 | ,Metric,2020,2021,2022,2023,Units
2 | 0,Scope 1,0.8,0.7,0.7,0.7,Inferred: CO₂e per FTE
3 | 1,Scope 2 (location-based),30.3,29.8,32.2,38.1,Inferred: MT CO₂e
4 | 2,Scope 2 (market-based),3.2,2.6,1.5,1.9,Inferred: CO₂e per FTE
5 | 3,Scope 1,"118,100","123,704","139,413","144,960",Inferred: MT CO₂e
6 | 7,Subtotal emissions (Scope 1 + 2 market-based),"574,219","553,109","427,442","538,094",Inferred: MT CO₂e
7 | 8,Scope 1 + 2 1,"574,219","553,109","427,442","538,094",Inferred: MT CO₂e
```

data/cache/MICROSOFT_CORP/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "US5949181045",
4 |         "idType": "isin",
5 |         "isin": "US5949181045",
6 |         "name": "MICROSOFT CORP",
7 |         "ticker": "MSFT",
8 |         "description": "MSFT",
9 |         "output_path": "/Users/iman/Desktop/UCL 2024:26/IFTE0001-IntroToFM/esg-data-retrieval/data/cache/MICROSOFT_CORP"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2024-Environmental-Sustainability-Report-Data-Fact.pdf",
13 |         "1": "https://info.microsoft.com/rs/157-GQE-382/images/EN-Microsoft-Cloud-Sustainability.pdf",
14 |         "2": "https://download.microsoft.com/download/5/9/4/5946a7a0-3fef-4374-878c-e5d60e7211c1/Nov2024MCfSTS-D4S3-UnlockESGMetricsMicrosoftFabric.pdf",
15 |         "3": "https://news.microsoft.com/wp-content/uploads/prod/sites/42/2023/05/2022-Environmental-Sustainability-Report.pdf",
16 |         "4": "https://datacenters.microsoft.com/globe/pdfs/sustainability/factsheets/Taiwan%20(Taiwan%20North).pdf"
17 |     }
18 | }
```

data/cache/NVIDIA/esg_data_llm.md
```
1 | ### Key Table
2 | 
3 | | Category                   | Year | Emissions (tCO2e) |
4 | |----------------------------|------|-------------------|
5 | | Scope 1                    | 2024 | 14,390            |
6 | | Scope 1                    | 2023 | 12,346            |
7 | | Scope 1                    | 2022 | 4,612             |
8 | | Scope 2 (Market-based)     | 2024 | 40,555            |
9 | | Scope 2 (Market-based)     | 2023 | 60,671            |
10 | | Scope 2 (Market-based)     | 2022 | 78,210            |
11 | | Scope 2 (Location-based)   | 2024 | 178,087           |
12 | | Scope 2 (Location-based)   | 2023 | 142,909           |
13 | | Scope 2 (Location-based)   | 2022 | 133,569           |
14 | 
15 | ### Scope 1 Breakdown
16 | 
17 | | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
18 | |------------------------------|------|-------------------|
19 | | N/A                          | 2024 | N/A               |
20 | 
21 | ### Scope 2 Market-based Breakdown
22 | 
23 | | Region or Business Unit | Year | Emissions (tCO2e) |
24 | |-------------------------|------|-------------------|
25 | | N/A                     | 2024 | N/A               |
26 | 
27 | ### Scope 2 Location-based Breakdown
28 | 
29 | | Region or Business Unit | Year | Emissions (tCO2e) |
30 | |-------------------------|------|-------------------|
31 | | N/A                     | 2024 | N/A               |
32 | 
33 | ### Scope 3 Breakdown
34 | 
35 | | Scope 3 Category                            | Year | Emissions (tCO2e) |
36 | |---------------------------------------------|------|-------------------|
37 | | Category 1: Purchased goods and services    | 2024 | 3,216,144         |
38 | | Category 1: Purchased goods and services    | 2023 | 2,975,189         |
39 | | Category 1: Purchased goods and services    | 2022 | 2,506,722         |
40 | | Category 2: Capital goods                   | 2024 | 200,483           |
41 | | Category 2: Capital goods                   | 2023 | 353,280           |
42 | | Category 2: Capital goods                   | 2022 | 62,586            |
43 | | Category 3: Fuel and energy-related         | 2024 | 61,590            |
44 | | Category 3: Fuel and energy-related         | 2023 | 67,805            |
45 | | Category 3: Fuel and energy-related         | 2022 | 50,631            |
46 | | Category 4: Upstream transportation         | 2024 | 72,562            |
47 | | Category 4: Upstream transportation         | 2023 | 60,572            |
48 | | Category 4: Upstream transportation         | 2022 | 37,910            |
49 | | Category 5: Waste generated in operations   | 2024 | 617               |
50 | | Category 5: Waste generated in operations   | 2023 | 579               |
51 | | Category 5: Waste generated in operations   | 2022 | 291               |
52 | | Category 6: Business travel                 | 2024 | 17,132            |
53 | | Category 6: Business travel                 | 2023 | 8,633             |
54 | | Category 6: Business travel                 | 2022 | 576               |
55 | | Category 7: Employee commuting              | 2024 | 23,019            |
56 | | Category 7: Employee commuting              | 2023 | 14,990            |
57 | | Category 7: Employee commuting              | 2022 | 21,189            |
58 | | Category 8: Upstream leased assets          | 2024 | 45,931            |
59 | | Category 8: Upstream leased assets          | 2023 | 32,952            |
60 | | Category 8: Upstream leased assets          | 2022 | 21,572            |
61 | | Total Scope 3                               | 2024 | 3,637,478         |
62 | | Total Scope 3                               | 2023 | 3,514,000         |
63 | | Total Scope 3                               | 2022 | 2,701,477         |
```

data/cache/NVIDIA/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "Nvidia",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "Nvidia",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/NVIDIA"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://images.nvidia.com/aem-dam/Solutions/documents/FY2024-NVIDIA-Corporate-Sustainability-Report.pdf",
13 |         "1": "https://s201.q4cdn.com/141608511/files/doc_financials/2024/ar/NVIDIA-2024-Annual-Report.pdf",
14 |         "2": "https://s201.q4cdn.com/141608511/files/doc_financials/2023/ar/2023-Annual-Report-1.pdf",
15 |         "3": "https://images.nvidia.com/aem-dam/Solutions/documents/FY2021-NVIDIA-CSR-Social-Responsibility.pdf",
16 |         "4": "https://images.nvidia.com/aem-dam/Solutions/documents/FY2023-NVIDIA-Corporate-Responsibility-Report-1.pdf"
17 |     }
18 | }
```

data/cache/NETFLIX/esg_data_llm.md
```
1 | ### A) Key Table
2 | 
3 | | Category                | Year | Emissions (tCO2e) |
4 | |-------------------------|------|-------------------|
5 | | Scope 1                 | 2019 | 51,487            |
6 | | Scope 1                 | 2020 | 30,883            |
7 | | Scope 1                 | 2021 | 62,815            |
8 | | Scope 1                 | 2022 | 59,388            |
9 | | Scope 2 (Market-based)  | 2019 | 565               |
10 | | Scope 2 (Market-based)  | 2020 | 141               |
11 | | Scope 2 (Market-based)  | 2021 | 0                 |
12 | | Scope 2 (Market-based)  | 2022 | 0                 |
13 | | Scope 2 (Location-based)| 2019 | 26,594            |
14 | | Scope 2 (Location-based)| 2020 | 28,585            |
15 | | Scope 2 (Location-based)| 2021 | 42,291            |
16 | | Scope 2 (Location-based)| 2022 | 41,411            |
17 | 
18 | ### B) Scope 1 Breakdown
19 | 
20 | | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
21 | |------------------------------|------|-------------------|
22 | | No Data                      | N/A  | N/A               |
23 | 
24 | ### C) Scope 2 Market-based Breakdown
25 | 
26 | | Region or Business Unit | Year | Emissions (tCO2e) |
27 | |-------------------------|------|-------------------|
28 | | No Data                 | N/A  | N/A               |
29 | 
30 | ### D) Scope 2 Location-based Breakdown
31 | 
32 | | Region or Business Unit | Year | Emissions (tCO2e) |
33 | |-------------------------|------|-------------------|
34 | | No Data                 | N/A  | N/A               |
35 | 
36 | ### E) Scope 3 Breakdown
37 | 
38 | | Scope 3 Category | Year | Emissions (tCO2e) |
39 | |------------------|------|-------------------|
40 | | Total Scope 3    | 2019 | 1,192,659         |
41 | | Total Scope 3    | 2020 | 1,020,541         |
42 | | Total Scope 3    | 2021 | 1,466,497         |
43 | | Total Scope 3    | 2022 | 1,086,833         |
```

data/cache/NETFLIX/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "netflix",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "netflix",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/NETFLIX"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://downloads.ctfassets.net/4cd45et68cgf/7rnC6zK537cM8zAGrXA90E/3c654a2d0023a4dac26a20b2fff39855/Netflix_2022-ESG-Report-FINAL.pdf",
13 |         "1": "http://q4live.s22.clientfiles.s3-website-us-east-1.amazonaws.com/959853165/files/doc_financials/2024/q2/FINAL-Q2-24-Shareholder-Letter.pdf",
14 |         "2": "https://www.responsibilityreports.com/HostedData/ResponsibilityReportArchive/n/NASDAQ_NFLX_2021.pdf",
15 |         "3": "http://q4live.s22.clientfiles.s3-website-us-east-1.amazonaws.com/959853165/files/doc_financials/2022/ar/netflix-inc-2023-proxy-statement.pdf",
16 |         "4": "https://www.hermes-investment.com/uploads/2023/12/2a388bae653f2c2d70cb6d5ada8663c5/eos-netflix-case-study-11-2023.pdf"
17 |     }
18 | }
```

data/cache/SOLVAY_SA/esg_data.csv
```
1 | ,Metric,2022,2021,2020,2019,2018,Units
2 | 0,Scope 1,9.2,9.6,8.9,10.6,10.4,Inferred: MT CO₂e
3 | 1,Scope 2 - gross market-based,1.1,1.4,1.2,1.4,1.9,Inferred: CO₂e per FTE
4 | 2,Total Scope 1+2,10.3,11.0,10.1,12.0,12.3,Inferred: MMT CO₂e
```

data/cache/SOLVAY_SA/esg_data_llm.md
```
1 | ### Key Table
2 | 
3 | | Category                  | Year | Emissions (tCO2e) |
4 | |---------------------------|------|-------------------|
5 | | Scope 1                   | 2022 | 9,200,000         |
6 | | Scope 1                   | 2021 | 9,600,000         |
7 | | Scope 1                   | 2020 | 8,900,000         |
8 | | Scope 1                   | 2019 | 10,600,000        |
9 | | Scope 1                   | 2018 | 10,400,000        |
10 | | Scope 2 (Market-based)    | 2022 | 1,100,000         |
11 | | Scope 2 (Market-based)    | 2021 | 1,400,000         |
12 | | Scope 2 (Market-based)    | 2020 | 1,200,000         |
13 | | Scope 2 (Market-based)    | 2019 | 1,400,000         |
14 | | Scope 2 (Market-based)    | 2018 | 1,900,000         |
15 | | Scope 2 (Location-based)  | 2022 | 1,500,000         |
16 | | Scope 2 (Location-based)  | 2021 | 1,600,000         |
17 | | Scope 2 (Location-based)  | 2020 | 1,400,000         |
18 | | Scope 2 (Location-based)  | 2019 | null              |
19 | | Scope 2 (Location-based)  | 2018 | null              |
20 | 
21 | ### Scope 1 Breakdown
22 | 
23 | | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
24 | |------------------------------|------|-------------------|
25 | | No Data                      |      |                   |
26 | 
27 | ### Scope 2 Market-based Breakdown
28 | 
29 | | Region or Business Unit      | Year | Emissions (tCO2e) |
30 | |------------------------------|------|-------------------|
31 | | Electricity purchased        | 2022 | 300,000           |
32 | | Electricity purchased        | 2021 | 700,000           |
33 | | Electricity purchased        | 2020 | 700,000           |
34 | | Steam purchased              | 2022 | 700,000           |
35 | | Steam purchased              | 2021 | 700,000           |
36 | | Steam purchased              | 2020 | 500,000           |
37 | 
38 | ### Scope 2 Location-based Breakdown
39 | 
40 | | Region or Business Unit       | Year | Emissions (tCO2e) |
41 | |-------------------------------|------|-------------------|
42 | | Electricity purchased         | 2022 | 800,000           |
43 | | Electricity purchased         | 2021 | 900,000           |
44 | | Electricity purchased         | 2020 | 900,000           |
45 | | Steam purchased               | 2022 | 700,000           |
46 | | Steam purchased               | 2021 | 700,000           |
47 | | Steam purchased               | 2020 | 500,000           |
48 | 
49 | ### Scope 3 Breakdown
50 | 
51 | | Scope 3 Category                              | Year | Emissions (tCO2e) |
52 | |-----------------------------------------------|------|-------------------|
53 | | Purchased goods and services                  | 2022 | 5,400,000         |
54 | | Capital goods                                 | 2022 | 2,500,000         |
55 | | Fuel- and energy-related activities           | 2022 | 1,300,000         |
56 | | Business travel                               | 2022 | 5,000             |
57 | | Employee commuting                            | 2022 | 30,000            |
58 | | Downstream transportation and distribution    | 2022 | 700,000           |
59 | | Processing of sold products                   | 2022 | 3,400,000         |
60 | | Use of sold products                          | 2022 | 5,100,000         |
61 | | End-of-life treatment of sold products        | 2022 | 5,300,000         |
62 | | Investments                                   | 2022 | 400,000           |
63 | | Total Scope 3                                 | 2022 | 24,200,000        |
```

data/cache/SOLVAY_SA/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "BE0003470755",
4 |         "idType": "isin",
5 |         "isin": "BE0003470755",
6 |         "name": "SOLVAY SA",
7 |         "ticker": "SA",
8 |         "description": "SA",
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/SOLVAY_SA"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://corporate.dow.com/documents/science-sustainability/919-00037-01-2023-dow-thailand-esg-report.pdf",
13 |         "1": "https://www.solvay.com/sites/g/files/srpend616/files/2023-05/solvay-2022-annual-integrated-report.pdf",
14 |         "2": "https://www.solvay.com/sites/g/files/srpend616/files/2024-03/2023Q4_Financialreport_EN.pdf",
15 |         "3": "https://www.solvay.com/sites/g/files/srpend616/files/2024-11/2024Q3_Financialreport_EN_final.pdf",
16 |         "4": "https://www.esma.europa.eu/sites/default/files/2023-10/ESMA32-1283113657-1041_Report_-_Disclosures_of_Climate_Related_Matters_in_the_Financial_Statements.pdf"
17 |     }
18 | }
```

data/cache/US5949181045/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "US5949181045",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "US5949181045",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/iman/Desktop/UCL 2024:26/IFTE0001-IntroToFM/esg-data-retrieval/data/cache/US5949181045"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://prod-epi.lgim.com/landg-assets/lgim/_document-library/esg/engagement-report-q4-2023.pdf",
13 |         "1": "https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE2EWBx",
14 |         "2": "https://www.quoniam.com/wp-content/uploads/2023/06/2022_Engagement-ReportDE_Quoniam_Funds_Selection_SICAV.pdf",
15 |         "3": "https://bankone.mu/wp-content/files/2025/01/Newsletter-14.01.2025.pdf",
16 |         "4": "https://www.pancretabank.gr/media/m2sddghr/incometric-semi-annual-report-00000000-0000-2023-06-30-sr-en-0000_http-nio-8080-exec-11062108234023427.pdf"
17 |     }
18 | }
```

data/cache/WELLS_FARGO/esg_data_llm.md
```
1 | ### A) Key Table
2 | 
3 | | Category                | Year | Emissions (tCO2e) |
4 | |-------------------------|------|-------------------|
5 | | Scope 1                 | 2019 | 86,602            |
6 | | Scope 1                 | 2020 | 78,087            |
7 | | Scope 1                 | 2021 | 73,319            |
8 | | Scope 1                 | 2022 | 77,476            |
9 | | Scope 2 (Market-based)  | 2019 | 4,988             |
10 | | Scope 2 (Market-based)  | 2020 | 3,614             |
11 | | Scope 2 (Market-based)  | 2021 | 1,792             |
12 | | Scope 2 (Market-based)  | 2022 | 4,424             |
13 | | Scope 2 (Location-based)| 2019 | 771,327           |
14 | | Scope 2 (Location-based)| 2020 | 694,011           |
15 | | Scope 2 (Location-based)| 2021 | 569,633           |
16 | | Scope 2 (Location-based)| 2022 | 593,495           |
17 | 
18 | ### B) Scope 1 Breakdown
19 | 
20 | | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
21 | |------------------------------|------|-------------------|
22 | | No Data                      | N/A  | N/A               |
23 | 
24 | ### C) Scope 2 Market-based Breakdown
25 | 
26 | | Region or Business Unit | Year | Emissions (tCO2e) |
27 | |-------------------------|------|-------------------|
28 | | No Data                 | N/A  | N/A               |
29 | 
30 | ### D) Scope 2 Location-based Breakdown
31 | 
32 | | Region or Business Unit | Year | Emissions (tCO2e) |
33 | |-------------------------|------|-------------------|
34 | | No Data                 | N/A  | N/A               |
35 | 
36 | ### E) Scope 3 Breakdown
37 | 
38 | | Scope 3 Category                                                             | Year | Emissions (tCO2e) |
39 | |------------------------------------------------------------------------------|------|-------------------|
40 | | Category 1: Purchased goods and services                                     | 2020 | 1,639,281         |
41 | | Category 1: Purchased goods and services                                     | 2021 | 1,429,619         |
42 | | Category 1: Purchased goods and services                                     | 2022 | 1,300,698         |
43 | | Category 2: Capital goods                                                    | 2020 | 358,268           |
44 | | Category 2: Capital goods                                                    | 2021 | 348,249           |
45 | | Category 2: Capital goods                                                    | 2022 | 293,289           |
46 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2)| 2020 | 123,970           |
47 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2)| 2021 | 121,357           |
48 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2)| 2022 | 123,938           |
49 | | Category 5: Waste generated in operations                                    | 2020 | 7,622             |
50 | | Category 5: Waste generated in operations                                    | 2021 | 13,058            |
51 | | Category 5: Waste generated in operations                                    | 2022 | 12,730            |
52 | | Category 6: Employee business travel (air travel only)                       | 2020 | 14,111            |
53 | | Category 6: Employee business travel (air travel only)                       | 2021 | 4,795             |
54 | | Category 6: Employee business travel (air travel only)                       | 2022 | 27,403            |
55 | | Category 7: Employee commuting (excluding remote work)                       | 2020 | 313,757           |
56 | | Category 7: Employee commuting (excluding remote work)                       | 2021 | 218,795           |
57 | | Category 7: Employee commuting (excluding remote work)                       | 2022 | 289,051           |
58 | | Total Scope 3                                                                | 2020 | 2,457,009         |
59 | | Total Scope 3                                                                | 2021 | 2,135,873         |
60 | | Total Scope 3                                                                | 2022 | 2,047,109         |
```

data/cache/WELLS_FARGO/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "wells fargo",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "wells fargo",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/WELLS_FARGO"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://www.wellsfargo.com/assets/pdf/about/corporate/2022-sustainability-and-governance-report.pdf",
13 |         "1": "https://www08.wellsfargomedia.com/assets/pdf/about/corporate-responsibility/sustainability-and-governance-report.pdf",
14 |         "2": "https://www08.wellsfargomedia.com/assets/pdf/about/investor-relations/annual-reports/2024-proxy-statement.pdf",
15 |         "3": "https://www.wellsfargo.com/assets/pdf/about/corporate-responsibility/inclusive-communities-climate-bond-report.pdf",
16 |         "4": "https://www.wellsfargo.com/assets/pdf/about/investor-relations/annual-reports/2021-proxy-statement.pdf"
17 |     }
18 | }
```

data/cache/WELLS_FARGO_&_CO/esg_data.csv
```
1 | Metric,2019,2020,2021,2022,Units
2 | Scope 1,86602,78087,73319,77476,MTCO2e
3 | Scope 2 (market-based),4988,3614,1792,4424,MTCO2e
4 | Scope 2 (location-based),771327,694011,569633,593495,MTCO2e
```

data/cache/WELLS_FARGO_&_CO/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "US9497461015",
4 |         "idType": "isin",
5 |         "isin": "US9497461015",
6 |         "name": "WELLS FARGO & CO",
7 |         "ticker": "WFC",
8 |         "description": "WFC",
9 |         "output_path": "/workspaces/esg-data-retrieval/data/cache/WELLS_FARGO_&_CO"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://www.wellsfargo.com/assets/pdf/about/corporate/2022-sustainability-and-governance-report.pdf",
13 |         "1": "https://www08.wellsfargomedia.com/assets/pdf/about/corporate-responsibility/sustainability-and-governance-report.pdf",
14 |         "2": "https://www08.wellsfargomedia.com/assets/pdf/about/investor-relations/annual-reports/2024-proxy-statement.pdf",
15 |         "3": "https://www.wellsfargo.com/assets/pdf/about/investor-relations/annual-reports/2021-proxy-statement.pdf",
16 |         "4": "https://www.ssga.com/library-content/products/fund-docs/etfs/emea/1-GENERIC-EN-AR-IRISH-SPDR-I.pdf"
17 |     }
18 | }
```

data/cache/WELLS_FAROG/esg_data_llm.md
```
1 | ### A) Key Table
2 | 
3 | | Category                | Year | Emissions (tCO2e) |
4 | |-------------------------|------|-------------------|
5 | | Scope 1                 | 2019 | 86,602            |
6 | | Scope 1                 | 2020 | 78,087            |
7 | | Scope 1                 | 2021 | 73,319            |
8 | | Scope 1                 | 2022 | 77,476            |
9 | | Scope 2 (Market-based)  | 2019 | 4,988             |
10 | | Scope 2 (Market-based)  | 2020 | 3,614             |
11 | | Scope 2 (Market-based)  | 2021 | 1,792             |
12 | | Scope 2 (Market-based)  | 2022 | 4,424             |
13 | | Scope 2 (Location-based)| 2019 | 771,327           |
14 | | Scope 2 (Location-based)| 2020 | 694,011           |
15 | | Scope 2 (Location-based)| 2021 | 569,633           |
16 | | Scope 2 (Location-based)| 2022 | 593,495           |
17 | 
18 | ### B) Scope 1 Breakdown
19 | 
20 | | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
21 | |------------------------------|------|-------------------|
22 | | N/A                          | N/A  | N/A               |
23 | 
24 | ### C) Scope 2 Market-based Breakdown
25 | 
26 | | Region or Business Unit | Year | Emissions (tCO2e) |
27 | |-------------------------|------|-------------------|
28 | | N/A                     | N/A  | N/A               |
29 | 
30 | ### D) Scope 2 Location-based Breakdown
31 | 
32 | | Region or Business Unit | Year | Emissions (tCO2e) |
33 | |-------------------------|------|-------------------|
34 | | N/A                     | N/A  | N/A               |
35 | 
36 | ### E) Scope 3 Breakdown
37 | 
38 | | Scope 3 Category                                                         | Year | Emissions (tCO2e) |
39 | |--------------------------------------------------------------------------|------|-------------------|
40 | | Category 1: Purchased goods and services                                 | 2020 | 1,639,281         |
41 | | Category 1: Purchased goods and services                                 | 2021 | 1,429,619         |
42 | | Category 1: Purchased goods and services                                 | 2022 | 1,300,698         |
43 | | Category 2: Capital goods                                                | 2020 | 358,268           |
44 | | Category 2: Capital goods                                                | 2021 | 348,249           |
45 | | Category 2: Capital goods                                                | 2022 | 293,289           |
46 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2) | 2020 | 123,970        |
47 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2) | 2021 | 121,357        |
48 | | Category 3: Fuel and energy-related activities (not included in Scope 1 or 2) | 2022 | 123,938        |
49 | | Category 5: Waste generated in operations                                | 2020 | 7,622             |
50 | | Category 5: Waste generated in operations                                | 2021 | 13,058            |
51 | | Category 5: Waste generated in operations                                | 2022 | 12,730            |
52 | | Category 6: Employee business travel (air travel only)                   | 2020 | 14,111            |
53 | | Category 6: Employee business travel (air travel only)                   | 2021 | 4,795             |
54 | | Category 6: Employee business travel (air travel only)                   | 2022 | 27,403            |
55 | | Category 7: Employee commuting (excluding remote work)                   | 2020 | 313,757           |
56 | | Category 7: Employee commuting (excluding remote work)                   | 2021 | 218,795           |
57 | | Category 7: Employee commuting (excluding remote work)                   | 2022 | 289,051           |
58 | | Total Scope 3                                                            | 2020 | 2,456,009         |
59 | | Total Scope 3                                                            | 2021 | 2,135,873         |
60 | | Total Scope 3                                                            | 2022 | 2,047,109         |
```

data/cache/WELLS_FAROG/profile.json
```
1 | {
2 |     "company": {
3 |         "identifier": "wells farog",
4 |         "idType": "name",
5 |         "isin": null,
6 |         "name": "wells farog",
7 |         "ticker": null,
8 |         "description": null,
9 |         "output_path": "/Users/neilanderson/Documents/GitHub/esg-data-retrieval/data/cache/WELLS_FAROG"
10 |     },
11 |     "esg_reports": {
12 |         "0": "https://www.wellsfargo.com/assets/pdf/about/corporate/2022-sustainability-and-governance-report.pdf",
13 |         "1": "https://www08.wellsfargomedia.com/assets/pdf/about/corporate-responsibility/sustainability-and-governance-report.pdf",
14 |         "2": "https://www08.wellsfargomedia.com/assets/pdf/about/investor-relations/annual-reports/2024-proxy-statement.pdf",
15 |         "3": "https://www.wellsfargo.com/assets/pdf/about/corporate-responsibility/inclusive-communities-climate-bond-report.pdf",
16 |         "4": "https://www.spartannash.com/wp-content/uploads/2023/10/SpartanNash_ESG_2022_FINAL.pdf"
17 |     }
18 | }
```

tests/src/find/__init__.py
```
```

tests/src/find/test_company_profile.py
```
1 | from src.find.company_profile import CompanyProfile
2 | 
3 | 
4 | class TestIsValidISIN:
5 | 
6 |     def test_with_valid_isin(self):
7 |         ISIN = "GB00BNC5T391"
8 |         result = CompanyProfile.is_valid_isin(ISIN)
9 |         assert result is True
10 | 
11 |     def test_with_invalid_isin(self):
12 |         ISIN = "apple"
13 |         result = CompanyProfile.is_valid_isin(ISIN)
14 |         assert result is False
```

tests/src/find/test_esg_reports.py
```
1 | from datetime import datetime
2 | 
3 | from src.find.esg_reports import ESGReports, SearchResult
4 | 
5 | 
6 | class TestScoreSearch:
7 | 
8 |     def test_score_search_zero(self):
9 |         search = SearchResult(
10 |             company_name="apple",
11 |             url="amazon.com",
12 |             title="macbook pro",
13 |             description="product details",
14 |         )
15 |         score = search.score_search()
16 |         assert score == 0
17 | 
18 |     def test_score_search_nonzero(self):
19 |         current_year = str(datetime.now().year)
20 |         search = SearchResult(
21 |             company_name="Nvidia",
22 |             url="www.nvidia.com",
23 |             title=f"Nvidia ESG Report {current_year}",
24 |             description="latest esg figures",
25 |         )
26 |         score = search.score_search()
27 |         assert score == 5
28 | 
29 | 
30 | class TestSortResults:
31 | 
32 |     def test_sort_results(self):
33 |         current_year = str(datetime.now().year)
34 |         company_name = "Apple"
35 |         search_results = [
36 |             {"title": "Amazon Report", "link": "www.amazon.com", "snippet": "report"},
37 |             {
38 |                 "title": f"Apple Sustainability Report {current_year}",
39 |                 "link": "www.apple.com",
40 |                 "snippet": "ESG figures",
41 |             },
42 |             {
43 |                 "title": "2023 ESG report",
44 |                 "link": "www.apple-store.com",
45 |                 "snippet": "Sustainability report for Apple",
46 |             },
47 |         ]
48 |         sorted_results = ESGReports._sort_search_reults(
49 |             company_name=company_name, search_results=search_results
50 |         )
51 |         assert sorted_results[0] == search_results[1]
52 |         assert sorted_results[1] == search_results[2]
53 |         assert sorted_results[2] == search_results[0]
```

src/static/images/emissions_map.html
```
1 | <!DOCTYPE html>
2 | <html>
3 | <head>
4 |     
5 |     <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
6 |     
7 |         <script>
8 |             L_NO_TOUCH = false;
9 |             L_DISABLE_3D = false;
10 |         </script>
11 |     
12 |     <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
13 |     <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
14 |     <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
15 |     <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
16 |     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
17 |     <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
18 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
19 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
20 |     <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
21 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
22 |     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
23 |     <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
24 |     
25 |             <meta name="viewport" content="width=device-width,
26 |                 initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
27 |             <style>
28 |                 #map_28748e7bd156afca3a16a7fad43c62fe {
29 |                     position: relative;
30 |                     width: 100.0%;
31 |                     height: 100.0%;
32 |                     left: 0.0%;
33 |                     top: 0.0%;
34 |                 }
35 |                 .leaflet-container { font-size: 1rem; }
36 |             </style>
37 |         
38 | </head>
39 | <body>
40 |     
41 |     
42 |             <div class="folium-map" id="map_28748e7bd156afca3a16a7fad43c62fe" ></div>
43 |         
44 | </body>
45 | <script>
46 |     
47 |     
48 |             var map_28748e7bd156afca3a16a7fad43c62fe = L.map(
49 |                 "map_28748e7bd156afca3a16a7fad43c62fe",
50 |                 {
51 |                     center: [20.0, 0.0],
52 |                     crs: L.CRS.EPSG3857,
53 |                     ...{
54 |   "zoom": 2,
55 |   "zoomControl": true,
56 |   "preferCanvas": false,
57 | }
58 | 
59 |                 }
60 |             );
61 | 
62 |             
63 | 
64 |         
65 |     
66 |             var tile_layer_72cfa08a165107c1cb094a1caf0a8597 = L.tileLayer(
67 |                 "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
68 |                 {
69 |   "minZoom": 0,
70 |   "maxZoom": 19,
71 |   "maxNativeZoom": 19,
72 |   "noWrap": false,
73 |   "attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors",
74 |   "subdomains": "abc",
75 |   "detectRetina": false,
76 |   "tms": false,
77 |   "opacity": 1,
78 | }
79 | 
80 |             );
81 |         
82 |     
83 |             tile_layer_72cfa08a165107c1cb094a1caf0a8597.addTo(map_28748e7bd156afca3a16a7fad43c62fe);
84 |         
85 |     
86 |             var circle_marker_64914ac016ac7073d9c3e13320b5acb0 = L.circleMarker(
87 |                 [48.06666666666667, -122.0],
88 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0168, "stroke": true, "weight": 3}
89 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
90 |         
91 |     
92 |         var popup_9e2a71f35897978c2dc3751cbfa40b80 = L.popup({
93 |   "maxWidth": "100%",
94 | });
95 | 
96 |         
97 |             
98 |                 var html_b66b19c481dc19271a05d38ec8269376 = $(`<div id="html_b66b19c481dc19271a05d38ec8269376" style="width: 100.0%; height: 100.0%;">Apple - 16.8 CO2</div>`)[0];
99 |                 popup_9e2a71f35897978c2dc3751cbfa40b80.setContent(html_b66b19c481dc19271a05d38ec8269376);
100 |             
101 |         
102 | 
103 |         circle_marker_64914ac016ac7073d9c3e13320b5acb0.bindPopup(popup_9e2a71f35897978c2dc3751cbfa40b80)
104 |         ;
105 | 
106 |         
107 |     
108 |     
109 |             var circle_marker_3eb0a02e0002afc2ee89d4be2aa7667c = L.circleMarker(
110 |                 [48.06666666666667, -121.78333333333333],
111 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0154, "stroke": true, "weight": 3}
112 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
113 |         
114 |     
115 |         var popup_4333922652221e4bd3c139694688ab52 = L.popup({
116 |   "maxWidth": "100%",
117 | });
118 | 
119 |         
120 |             
121 |                 var html_0c91f92c61122ec41c8dd1cd05cf3f8e = $(`<div id="html_0c91f92c61122ec41c8dd1cd05cf3f8e" style="width: 100.0%; height: 100.0%;">Microsoft - 15.4 CO2</div>`)[0];
122 |                 popup_4333922652221e4bd3c139694688ab52.setContent(html_0c91f92c61122ec41c8dd1cd05cf3f8e);
123 |             
124 |         
125 | 
126 |         circle_marker_3eb0a02e0002afc2ee89d4be2aa7667c.bindPopup(popup_4333922652221e4bd3c139694688ab52)
127 |         ;
128 | 
129 |         
130 |     
131 |     
132 |             var circle_marker_11a01ce12d2672567afd8ecbddf67842 = L.circleMarker(
133 |                 [37.7, -121.86666666666666],
134 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0249, "stroke": true, "weight": 3}
135 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
136 |         
137 |     
138 |         var popup_e808644f3710bb679dcf2258aa0f9caa = L.popup({
139 |   "maxWidth": "100%",
140 | });
141 | 
142 |         
143 |             
144 |                 var html_f7d626037641282734d19db38e41981f = $(`<div id="html_f7d626037641282734d19db38e41981f" style="width: 100.0%; height: 100.0%;">Alphabet - 24.9 CO2</div>`)[0];
145 |                 popup_e808644f3710bb679dcf2258aa0f9caa.setContent(html_f7d626037641282734d19db38e41981f);
146 |             
147 |         
148 | 
149 |         circle_marker_11a01ce12d2672567afd8ecbddf67842.bindPopup(popup_e808644f3710bb679dcf2258aa0f9caa)
150 |         ;
151 | 
152 |         
153 |     
154 |     
155 |             var circle_marker_a8b16ae5869115b545eab894d0f1ef80 = L.circleMarker(
156 |                 [18.466666666666665, 42.88333333333333],
157 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.047, "stroke": true, "weight": 3}
158 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
159 |         
160 |     
161 |         var popup_a66932cb678652700bf8b9e00cce5b74 = L.popup({
162 |   "maxWidth": "100%",
163 | });
164 | 
165 |         
166 |             
167 |                 var html_76928a2b3b998a5ace132383eaa2eb8f = $(`<div id="html_76928a2b3b998a5ace132383eaa2eb8f" style="width: 100.0%; height: 100.0%;">Saudi Aramco - 47.0 CO2</div>`)[0];
168 |                 popup_a66932cb678652700bf8b9e00cce5b74.setContent(html_76928a2b3b998a5ace132383eaa2eb8f);
169 |             
170 |         
171 | 
172 |         circle_marker_a8b16ae5869115b545eab894d0f1ef80.bindPopup(popup_a66932cb678652700bf8b9e00cce5b74)
173 |         ;
174 | 
175 |         
176 |     
177 |     
178 |             var circle_marker_5f13314c63e1c3c55fe7639730dd4401 = L.circleMarker(
179 |                 [37.61666666666667, -119.4],
180 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0122, "stroke": true, "weight": 3}
181 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
182 |         
183 |     
184 |         var popup_3f02147392a63fd6b1fc2636578f334a = L.popup({
185 |   "maxWidth": "100%",
186 | });
187 | 
188 |         
189 |             
190 |                 var html_10dc1c013bd59ea741803d09c53facb4 = $(`<div id="html_10dc1c013bd59ea741803d09c53facb4" style="width: 100.0%; height: 100.0%;">Nvidia - 12.2 CO2</div>`)[0];
191 |                 popup_3f02147392a63fd6b1fc2636578f334a.setContent(html_10dc1c013bd59ea741803d09c53facb4);
192 |             
193 |         
194 | 
195 |         circle_marker_5f13314c63e1c3c55fe7639730dd4401.bindPopup(popup_3f02147392a63fd6b1fc2636578f334a)
196 |         ;
197 | 
198 |         
199 |     
200 |     
201 |             var circle_marker_c69a962f7ba2a611ad4b1c942175f6c6 = L.circleMarker(
202 |                 [48.016666666666666, -121.43333333333334],
203 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0261, "stroke": true, "weight": 3}
204 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
205 |         
206 |     
207 |         var popup_012bb4db1cf4a42af708bacacf6c552c = L.popup({
208 |   "maxWidth": "100%",
209 | });
210 | 
211 |         
212 |             
213 |                 var html_48731b4e40c90083994029fae32faef1 = $(`<div id="html_48731b4e40c90083994029fae32faef1" style="width: 100.0%; height: 100.0%;">Amazon  - 26.1 CO2</div>`)[0];
214 |                 popup_012bb4db1cf4a42af708bacacf6c552c.setContent(html_48731b4e40c90083994029fae32faef1);
215 |             
216 |         
217 | 
218 |         circle_marker_c69a962f7ba2a611ad4b1c942175f6c6.bindPopup(popup_012bb4db1cf4a42af708bacacf6c552c)
219 |         ;
220 | 
221 |         
222 |     
223 |     
224 |             var circle_marker_6fc1147b06f4261819481ca4c740ab4a = L.circleMarker(
225 |                 [25.266666666666666, 120.0],
226 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0137, "stroke": true, "weight": 3}
227 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
228 |         
229 |     
230 |         var popup_8564a82e9b445b9aba8fd338bd4429bb = L.popup({
231 |   "maxWidth": "100%",
232 | });
233 | 
234 |         
235 |             
236 |                 var html_839d0d3c36a32e60c7c42fb868c38307 = $(`<div id="html_839d0d3c36a32e60c7c42fb868c38307" style="width: 100.0%; height: 100.0%;">Taiwan Semiconductor Company - 13.7 CO2</div>`)[0];
237 |                 popup_8564a82e9b445b9aba8fd338bd4429bb.setContent(html_839d0d3c36a32e60c7c42fb868c38307);
238 |             
239 |         
240 | 
241 |         circle_marker_6fc1147b06f4261819481ca4c740ab4a.bindPopup(popup_8564a82e9b445b9aba8fd338bd4429bb)
242 |         ;
243 | 
244 |         
245 |     
246 |     
247 |             var circle_marker_b4af2e1260d1add04da22a498b324ed4 = L.circleMarker(
248 |                 [30.033333333333335, 120.31666666666666],
249 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.01323, "stroke": true, "weight": 3}
250 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
251 |         
252 |     
253 |         var popup_93c61c0f24950aae6fc5910c924ca715 = L.popup({
254 |   "maxWidth": "100%",
255 | });
256 | 
257 |         
258 |             
259 |                 var html_638812fbb5bab5a9f9b4fa67134e4f87 = $(`<div id="html_638812fbb5bab5a9f9b4fa67134e4f87" style="width: 100.0%; height: 100.0%;">Alibaba - 13.23 CO2</div>`)[0];
260 |                 popup_93c61c0f24950aae6fc5910c924ca715.setContent(html_638812fbb5bab5a9f9b4fa67134e4f87);
261 |             
262 |         
263 | 
264 |         circle_marker_b4af2e1260d1add04da22a498b324ed4.bindPopup(popup_93c61c0f24950aae6fc5910c924ca715)
265 |         ;
266 | 
267 |         
268 |     
269 |     
270 |             var circle_marker_7cb59119f791d16cde2f7b58c773a0e1 = L.circleMarker(
271 |                 [51.85, 0.03333333333333333],
272 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0242, "stroke": true, "weight": 3}
273 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
274 |         
275 |     
276 |         var popup_d6be0fc069588e484265b8621d0364c2 = L.popup({
277 |   "maxWidth": "100%",
278 | });
279 | 
280 |         
281 |             
282 |                 var html_daa5ac16fb0f473b25f7d4fe218b1588 = $(`<div id="html_daa5ac16fb0f473b25f7d4fe218b1588" style="width: 100.0%; height: 100.0%;">HSBC - 24.2 CO2</div>`)[0];
283 |                 popup_d6be0fc069588e484265b8621d0364c2.setContent(html_daa5ac16fb0f473b25f7d4fe218b1588);
284 |             
285 |         
286 | 
287 |         circle_marker_7cb59119f791d16cde2f7b58c773a0e1.bindPopup(popup_d6be0fc069588e484265b8621d0364c2)
288 |         ;
289 | 
290 |         
291 |     
292 |     
293 |             var circle_marker_0a389d78d0cf42074c400b81d3c26577 = L.circleMarker(
294 |                 [38.3, -121.31666666666666],
295 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0154, "stroke": true, "weight": 3}
296 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
297 |         
298 |     
299 |         var popup_a6796347335801764e1b31db1873a26d = L.popup({
300 |   "maxWidth": "100%",
301 | });
302 | 
303 |         
304 |             
305 |                 var html_8b01fa5efdb8d067cda2500c658df691 = $(`<div id="html_8b01fa5efdb8d067cda2500c658df691" style="width: 100.0%; height: 100.0%;">Visa - 15.4 CO2</div>`)[0];
306 |                 popup_a6796347335801764e1b31db1873a26d.setContent(html_8b01fa5efdb8d067cda2500c658df691);
307 |             
308 |         
309 | 
310 |         circle_marker_0a389d78d0cf42074c400b81d3c26577.bindPopup(popup_a6796347335801764e1b31db1873a26d)
311 |         ;
312 | 
313 |         
314 |     
315 |     
316 |             var circle_marker_d2c6eaca981dd25b4fa2327e959cf7a3 = L.circleMarker(
317 |                 [37.75, -121.7],
318 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0327, "stroke": true, "weight": 3}
319 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
320 |         
321 |     
322 |         var popup_476233fe2b4cc4a4a9ed03a164bcc8f6 = L.popup({
323 |   "maxWidth": "100%",
324 | });
325 | 
326 |         
327 |             
328 |                 var html_c51b1e712ac450aae2161f9400b43cac = $(`<div id="html_c51b1e712ac450aae2161f9400b43cac" style="width: 100.0%; height: 100.0%;">Meta - 32.7 CO2</div>`)[0];
329 |                 popup_476233fe2b4cc4a4a9ed03a164bcc8f6.setContent(html_c51b1e712ac450aae2161f9400b43cac);
330 |             
331 |         
332 | 
333 |         circle_marker_d2c6eaca981dd25b4fa2327e959cf7a3.bindPopup(popup_476233fe2b4cc4a4a9ed03a164bcc8f6)
334 |         ;
335 | 
336 |         
337 |     
338 |     
339 |             var circle_marker_4ab322a1a83d27265bfca7b6be2ca8be = L.circleMarker(
340 |                 [30.366666666666667, -95.96666666666667],
341 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0247, "stroke": true, "weight": 3}
342 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
343 |         
344 |     
345 |         var popup_eb851943b34cf228c4a29e3307d8076b = L.popup({
346 |   "maxWidth": "100%",
347 | });
348 | 
349 |         
350 |             
351 |                 var html_96ae983299429eb20aa0271bfffc6c6d = $(`<div id="html_96ae983299429eb20aa0271bfffc6c6d" style="width: 100.0%; height: 100.0%;">Tesla  - 24.7 CO2</div>`)[0];
352 |                 popup_eb851943b34cf228c4a29e3307d8076b.setContent(html_96ae983299429eb20aa0271bfffc6c6d);
353 |             
354 |         
355 | 
356 |         circle_marker_4ab322a1a83d27265bfca7b6be2ca8be.bindPopup(popup_eb851943b34cf228c4a29e3307d8076b)
357 |         ;
358 | 
359 |         
360 |     
361 |     
362 |             var circle_marker_369b054545937e169fd60928e7905c24 = L.circleMarker(
363 |                 [37.56666666666667, -119.51666666666667],
364 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0192, "stroke": true, "weight": 3}
365 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
366 |         
367 |     
368 |         var popup_7f5bcee6a59e5aaa10234346c01838c4 = L.popup({
369 |   "maxWidth": "100%",
370 | });
371 | 
372 |         
373 |             
374 |                 var html_4023ebef175922873418aebc30452b3f = $(`<div id="html_4023ebef175922873418aebc30452b3f" style="width: 100.0%; height: 100.0%;">Broadcom - 19.2 CO2</div>`)[0];
375 |                 popup_7f5bcee6a59e5aaa10234346c01838c4.setContent(html_4023ebef175922873418aebc30452b3f);
376 |             
377 |         
378 | 
379 |         circle_marker_369b054545937e169fd60928e7905c24.bindPopup(popup_7f5bcee6a59e5aaa10234346c01838c4)
380 |         ;
381 | 
382 |         
383 |     
384 |     
385 |             var circle_marker_65ba241cb17fcf0e54a014af30f84bcf = L.circleMarker(
386 |                 [40.28333333333333, -85.73333333333333],
387 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0236, "stroke": true, "weight": 3}
388 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
389 |         
390 |     
391 |         var popup_487fbcb90f10712bcf8824bd0b20581b = L.popup({
392 |   "maxWidth": "100%",
393 | });
394 | 
395 |         
396 |             
397 |                 var html_c1f2d0881d368944a6d9c552091f3d63 = $(`<div id="html_c1f2d0881d368944a6d9c552091f3d63" style="width: 100.0%; height: 100.0%;">Eli Lilly - 23.6 CO2</div>`)[0];
398 |                 popup_487fbcb90f10712bcf8824bd0b20581b.setContent(html_c1f2d0881d368944a6d9c552091f3d63);
399 |             
400 |         
401 | 
402 |         circle_marker_65ba241cb17fcf0e54a014af30f84bcf.bindPopup(popup_487fbcb90f10712bcf8824bd0b20581b)
403 |         ;
404 | 
405 |         
406 |     
407 |     
408 |             var circle_marker_3db646b9255ce2c99b2903ba3d6fbce6 = L.circleMarker(
409 |                 [41.43333333333333, -93.45],
410 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0262, "stroke": true, "weight": 3}
411 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
412 |         
413 |     
414 |         var popup_5d8208d47170733ae5e69bc7faf68860 = L.popup({
415 |   "maxWidth": "100%",
416 | });
417 | 
418 |         
419 |             
420 |                 var html_52dad4f302d1cec05062bb4c0dc37f03 = $(`<div id="html_52dad4f302d1cec05062bb4c0dc37f03" style="width: 100.0%; height: 100.0%;">Berkshire Hathaway - 26.2 CO2</div>`)[0];
421 |                 popup_5d8208d47170733ae5e69bc7faf68860.setContent(html_52dad4f302d1cec05062bb4c0dc37f03);
422 |             
423 |         
424 | 
425 |         circle_marker_3db646b9255ce2c99b2903ba3d6fbce6.bindPopup(popup_5d8208d47170733ae5e69bc7faf68860)
426 |         ;
427 | 
428 |         
429 |     
430 |     
431 |             var circle_marker_b6bed7e6e8eb3e78e66a8c9f12d55b2b = L.circleMarker(
432 |                 [36.61666666666667, -93.65],
433 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.025, "stroke": true, "weight": 3}
434 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
435 |         
436 |     
437 |         var popup_96028b6850f4c486a615d443be058755 = L.popup({
438 |   "maxWidth": "100%",
439 | });
440 | 
441 |         
442 |             
443 |                 var html_1401ad6f14d8b335c0b55de626b3d1d7 = $(`<div id="html_1401ad6f14d8b335c0b55de626b3d1d7" style="width: 100.0%; height: 100.0%;">Walmart - 25.0 CO2</div>`)[0];
444 |                 popup_96028b6850f4c486a615d443be058755.setContent(html_1401ad6f14d8b335c0b55de626b3d1d7);
445 |             
446 |         
447 | 
448 |         circle_marker_b6bed7e6e8eb3e78e66a8c9f12d55b2b.bindPopup(popup_96028b6850f4c486a615d443be058755)
449 |         ;
450 | 
451 |         
452 |     
453 |     
454 |             var circle_marker_2fa07e6aa5fe396475e669afb0b4409e = L.circleMarker(
455 |                 [22.883333333333333, 114.55],
456 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0188, "stroke": true, "weight": 3}
457 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
458 |         
459 |     
460 |         var popup_59eec27a30a39607cc0d0fffb1529dd7 = L.popup({
461 |   "maxWidth": "100%",
462 | });
463 | 
464 |         
465 |             
466 |                 var html_992b016cf52de55d845d334d57b5ba23 = $(`<div id="html_992b016cf52de55d845d334d57b5ba23" style="width: 100.0%; height: 100.0%;">Tencent - 18.8 CO2</div>`)[0];
467 |                 popup_59eec27a30a39607cc0d0fffb1529dd7.setContent(html_992b016cf52de55d845d334d57b5ba23);
468 |             
469 |         
470 | 
471 |         circle_marker_2fa07e6aa5fe396475e669afb0b4409e.bindPopup(popup_59eec27a30a39607cc0d0fffb1529dd7)
472 |         ;
473 | 
474 |         
475 |     
476 |     
477 |             var circle_marker_76d9460c3cf78356d97eb2cad4463f6b = L.circleMarker(
478 |                 [37.88333333333333, -121.55],
479 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0149, "stroke": true, "weight": 3}
480 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
481 |         
482 |     
483 |         var popup_a84dcb9b89434afa69fb80db0f69700a = L.popup({
484 |   "maxWidth": "100%",
485 | });
486 | 
487 |         
488 |             
489 |                 var html_b72dc3c384be95d429d15d0c98dd02ef = $(`<div id="html_b72dc3c384be95d429d15d0c98dd02ef" style="width: 100.0%; height: 100.0%;">Oracle - 14.9 CO2</div>`)[0];
490 |                 popup_a84dcb9b89434afa69fb80db0f69700a.setContent(html_b72dc3c384be95d429d15d0c98dd02ef);
491 |             
492 |         
493 | 
494 |         circle_marker_76d9460c3cf78356d97eb2cad4463f6b.bindPopup(popup_a84dcb9b89434afa69fb80db0f69700a)
495 |         ;
496 | 
497 |         
498 |     
499 |     
500 |             var circle_marker_8972d3da70614618fb9949829aac7379 = L.circleMarker(
501 |                 [30.116666666666667, -94.3],
502 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0437, "stroke": true, "weight": 3}
503 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
504 |         
505 |     
506 |         var popup_d9b27a6edc65142a945f10ca5c9f98e7 = L.popup({
507 |   "maxWidth": "100%",
508 | });
509 | 
510 |         
511 |             
512 |                 var html_8c8bb491c9ba70c9ae10529cd8377c97 = $(`<div id="html_8c8bb491c9ba70c9ae10529cd8377c97" style="width: 100.0%; height: 100.0%;">Exxon Mobil  - 43.7 CO2</div>`)[0];
513 |                 popup_d9b27a6edc65142a945f10ca5c9f98e7.setContent(html_8c8bb491c9ba70c9ae10529cd8377c97);
514 |             
515 |         
516 | 
517 |         circle_marker_8972d3da70614618fb9949829aac7379.bindPopup(popup_d9b27a6edc65142a945f10ca5c9f98e7)
518 |         ;
519 | 
520 |         
521 |     
522 |     
523 |             var circle_marker_d01caa22e9de5d143e73345041a08051 = L.circleMarker(
524 |                 [34.45, -83.43333333333334],
525 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0126, "stroke": true, "weight": 3}
526 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
527 |         
528 |     
529 |         var popup_b1debb8de00ec5fd9efbee974ecc269e = L.popup({
530 |   "maxWidth": "100%",
531 | });
532 | 
533 |         
534 |             
535 |                 var html_bad1c540c9a74cfde1e2dc60196960f6 = $(`<div id="html_bad1c540c9a74cfde1e2dc60196960f6" style="width: 100.0%; height: 100.0%;">Home Depot - 12.6 CO2</div>`)[0];
536 |                 popup_b1debb8de00ec5fd9efbee974ecc269e.setContent(html_bad1c540c9a74cfde1e2dc60196960f6);
537 |             
538 |         
539 | 
540 |         circle_marker_d01caa22e9de5d143e73345041a08051.bindPopup(popup_b1debb8de00ec5fd9efbee974ecc269e)
541 |         ;
542 | 
543 |         
544 |     
545 |     
546 |             var circle_marker_ac97d03a1436f8f4c7f22827f202cd78 = L.circleMarker(
547 |                 [38.28333333333333, -121.3],
548 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0344, "stroke": true, "weight": 3}
549 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
550 |         
551 |     
552 |         var popup_94b8bd533b568891e909a175166d982e = L.popup({
553 |   "maxWidth": "100%",
554 | });
555 | 
556 |         
557 |             
558 |                 var html_fbffed55c86069255c5e2b1a9aef4e48 = $(`<div id="html_fbffed55c86069255c5e2b1a9aef4e48" style="width: 100.0%; height: 100.0%;">Wells Fargo - 34.4 CO2</div>`)[0];
559 |                 popup_94b8bd533b568891e909a175166d982e.setContent(html_fbffed55c86069255c5e2b1a9aef4e48);
560 |             
561 |         
562 | 
563 |         circle_marker_ac97d03a1436f8f4c7f22827f202cd78.bindPopup(popup_94b8bd533b568891e909a175166d982e)
564 |         ;
565 | 
566 |         
567 |     
568 |     
569 |             var circle_marker_3d7bb00c3b9f49a1250ada2e438dbc48 = L.circleMarker(
570 |                 [37.4, -119.4],
571 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0156, "stroke": true, "weight": 3}
572 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
573 |         
574 |     
575 |         var popup_39e21b21438e43abafc0077898de66ab = L.popup({
576 |   "maxWidth": "100%",
577 | });
578 | 
579 |         
580 |             
581 |                 var html_7e740bb149c44a6c9d32849ab0d81e58 = $(`<div id="html_7e740bb149c44a6c9d32849ab0d81e58" style="width: 100.0%; height: 100.0%;">Netflix  - 15.6 CO2</div>`)[0];
582 |                 popup_39e21b21438e43abafc0077898de66ab.setContent(html_7e740bb149c44a6c9d32849ab0d81e58);
583 |             
584 |         
585 | 
586 |         circle_marker_3d7bb00c3b9f49a1250ada2e438dbc48.bindPopup(popup_39e21b21438e43abafc0077898de66ab)
587 |         ;
588 | 
589 |         
590 |     
591 |     
592 |             var circle_marker_3c2fdfe43d952d1cf8d2c9a5800b4b03 = L.circleMarker(
593 |                 [37.833333333333336, 127.05],
594 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.015, "stroke": true, "weight": 3}
595 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
596 |         
597 |     
598 |         var popup_369566de65e9e115ec09218696189d4a = L.popup({
599 |   "maxWidth": "100%",
600 | });
601 | 
602 |         
603 |             
604 |                 var html_d95fa9400c5c92ab9d7bab81c20df69b = $(`<div id="html_d95fa9400c5c92ab9d7bab81c20df69b" style="width: 100.0%; height: 100.0%;">Samsung - 15.0 CO2</div>`)[0];
605 |                 popup_369566de65e9e115ec09218696189d4a.setContent(html_d95fa9400c5c92ab9d7bab81c20df69b);
606 |             
607 |         
608 | 
609 |         circle_marker_3c2fdfe43d952d1cf8d2c9a5800b4b03.bindPopup(popup_369566de65e9e115ec09218696189d4a)
610 |         ;
611 | 
612 |         
613 |     
614 |     
615 |             var circle_marker_b6bf365483868414fcefe6c6d55b4967 = L.circleMarker(
616 |                 [41.266666666666666, -71.36666666666666],
617 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0243, "stroke": true, "weight": 3}
618 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
619 |         
620 |     
621 |         var popup_c93c6b55cfc3bb27110db87a71150e13 = L.popup({
622 |   "maxWidth": "100%",
623 | });
624 | 
625 |         
626 |             
627 |                 var html_3b449678ed9b86b032e55e23b9032d14 = $(`<div id="html_3b449678ed9b86b032e55e23b9032d14" style="width: 100.0%; height: 100.0%;">Bank of America - 24.3 CO2</div>`)[0];
628 |                 popup_c93c6b55cfc3bb27110db87a71150e13.setContent(html_3b449678ed9b86b032e55e23b9032d14);
629 |             
630 |         
631 | 
632 |         circle_marker_b6bf365483868414fcefe6c6d55b4967.bindPopup(popup_c93c6b55cfc3bb27110db87a71150e13)
633 |         ;
634 | 
635 |         
636 |     
637 |     
638 |             var circle_marker_8330d1be19652a8d2b499c81c7773e4e = L.circleMarker(
639 |                 [41.266666666666666, 7.983333333333333],
640 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0238, "stroke": true, "weight": 3}
641 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
642 |         
643 |     
644 |         var popup_3e5b377d409f5fd2a620006eeb4d8585 = L.popup({
645 |   "maxWidth": "100%",
646 | });
647 | 
648 |         
649 |             
650 |                 var html_8081e7233a0c0a69baafbf4e8b8e0df7 = $(`<div id="html_8081e7233a0c0a69baafbf4e8b8e0df7" style="width: 100.0%; height: 100.0%;">Roche  - 23.8 CO2</div>`)[0];
651 |                 popup_3e5b377d409f5fd2a620006eeb4d8585.setContent(html_8081e7233a0c0a69baafbf4e8b8e0df7);
652 |             
653 |         
654 | 
655 |         circle_marker_8330d1be19652a8d2b499c81c7773e4e.bindPopup(popup_3e5b377d409f5fd2a620006eeb4d8585)
656 |         ;
657 | 
658 |         
659 |     
660 |     
661 |             var circle_marker_7bc5200ecdc1decf14552a5c1adb8858 = L.circleMarker(
662 |                 [34.25, -83.35],
663 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0242, "stroke": true, "weight": 3}
664 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
665 |         
666 |     
667 |         var popup_7ae58c45f83e9b7de4db5b19cf57d53a = L.popup({
668 |   "maxWidth": "100%",
669 | });
670 | 
671 |         
672 |             
673 |                 var html_8fdb9162fc22706766a74c4e38956773 = $(`<div id="html_8fdb9162fc22706766a74c4e38956773" style="width: 100.0%; height: 100.0%;">Coca Cola  - 24.2 CO2</div>`)[0];
674 |                 popup_7ae58c45f83e9b7de4db5b19cf57d53a.setContent(html_8fdb9162fc22706766a74c4e38956773);
675 |             
676 |         
677 | 
678 |         circle_marker_7bc5200ecdc1decf14552a5c1adb8858.bindPopup(popup_7ae58c45f83e9b7de4db5b19cf57d53a)
679 |         ;
680 | 
681 |         
682 |     
683 |     
684 |             var circle_marker_fd608d5c763ccc0e58fa903d826ad7cc = L.circleMarker(
685 |                 [51.68333333333333, 5.683333333333334],
686 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0085, "stroke": true, "weight": 3}
687 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
688 |         
689 |     
690 |         var popup_5e092e691977e7e928c9493b12dc91df = L.popup({
691 |   "maxWidth": "100%",
692 | });
693 | 
694 |         
695 |             
696 |                 var html_8ee7d47f0575b2b90d4b309818b4c74d = $(`<div id="html_8ee7d47f0575b2b90d4b309818b4c74d" style="width: 100.0%; height: 100.0%;">ASML - 8.5 CO2</div>`)[0];
697 |                 popup_5e092e691977e7e928c9493b12dc91df.setContent(html_8ee7d47f0575b2b90d4b309818b4c74d);
698 |             
699 |         
700 | 
701 |         circle_marker_fd608d5c763ccc0e58fa903d826ad7cc.bindPopup(popup_5e092e691977e7e928c9493b12dc91df)
702 |         ;
703 | 
704 |         
705 |     
706 |     
707 |             var circle_marker_a7d59023d540ac014185e37610b9ab38 = L.circleMarker(
708 |                 [49.483333333333334, 9.066666666666666],
709 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0144, "stroke": true, "weight": 3}
710 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
711 |         
712 |     
713 |         var popup_8479f9fcfb1a6eed2963a072458a62cc = L.popup({
714 |   "maxWidth": "100%",
715 | });
716 | 
717 |         
718 |             
719 |                 var html_75245c2d1b5f261efe5cea256615da1e = $(`<div id="html_75245c2d1b5f261efe5cea256615da1e" style="width: 100.0%; height: 100.0%;">SAP - 14.4 CO2</div>`)[0];
720 |                 popup_8479f9fcfb1a6eed2963a072458a62cc.setContent(html_75245c2d1b5f261efe5cea256615da1e);
721 |             
722 |         
723 | 
724 |         circle_marker_a7d59023d540ac014185e37610b9ab38.bindPopup(popup_8479f9fcfb1a6eed2963a072458a62cc)
725 |         ;
726 | 
727 |         
728 |     
729 |     
730 |             var circle_marker_1ced2bc656cfb8fe6ae163817cf0660c = L.circleMarker(
731 |                 [49.45, 2.5166666666666666],
732 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0139, "stroke": true, "weight": 3}
733 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
734 |         
735 |     
736 |         var popup_786e4e9b10506f16f427e04290f90a21 = L.popup({
737 |   "maxWidth": "100%",
738 | });
739 | 
740 |         
741 |             
742 |                 var html_cab10576333cae39b89f782781b610ab = $(`<div id="html_cab10576333cae39b89f782781b610ab" style="width: 100.0%; height: 100.0%;">LVMH - 13.9 CO2</div>`)[0];
743 |                 popup_786e4e9b10506f16f427e04290f90a21.setContent(html_cab10576333cae39b89f782781b610ab);
744 |             
745 |         
746 | 
747 |         circle_marker_1ced2bc656cfb8fe6ae163817cf0660c.bindPopup(popup_786e4e9b10506f16f427e04290f90a21)
748 |         ;
749 | 
750 |         
751 |     
752 |     
753 |             var circle_marker_1fcef5620c2182d7e7e8b2f5a55d8c6e = L.circleMarker(
754 |                 [56.266666666666666, 12.766666666666667],
755 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0232, "stroke": true, "weight": 3}
756 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
757 |         
758 |     
759 |         var popup_83b4d312d46c077bac8c49bec4a0a1ed = L.popup({
760 |   "maxWidth": "100%",
761 | });
762 | 
763 |         
764 |             
765 |                 var html_767d10e78c22d1f59cf44b19f35208cd = $(`<div id="html_767d10e78c22d1f59cf44b19f35208cd" style="width: 100.0%; height: 100.0%;">Novo Nordisk  - 23.2 CO2</div>`)[0];
766 |                 popup_83b4d312d46c077bac8c49bec4a0a1ed.setContent(html_767d10e78c22d1f59cf44b19f35208cd);
767 |             
768 |         
769 | 
770 |         circle_marker_1fcef5620c2182d7e7e8b2f5a55d8c6e.bindPopup(popup_83b4d312d46c077bac8c49bec4a0a1ed)
771 |         ;
772 | 
773 |         
774 |     
775 |     
776 |             var circle_marker_408bdf1c258dfc6543d1db737445b9d7 = L.circleMarker(
777 |                 [39.166666666666664, -83.15],
778 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0249, "stroke": true, "weight": 3}
779 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
780 |         
781 |     
782 |         var popup_37ff4bdc108e5cb55d10db440558c739 = L.popup({
783 |   "maxWidth": "100%",
784 | });
785 | 
786 |         
787 |             
788 |                 var html_c818e05b2ce26696f487b492c6e17c74 = $(`<div id="html_c818e05b2ce26696f487b492c6e17c74" style="width: 100.0%; height: 100.0%;">Procter & Gamble  - 24.9 CO2</div>`)[0];
789 |                 popup_37ff4bdc108e5cb55d10db440558c739.setContent(html_c818e05b2ce26696f487b492c6e17c74);
790 |             
791 |         
792 | 
793 |         circle_marker_408bdf1c258dfc6543d1db737445b9d7.bindPopup(popup_37ff4bdc108e5cb55d10db440558c739)
794 |         ;
795 | 
796 |         
797 |     
798 |     
799 |             var circle_marker_4a2c0524e66ddd8a6f2709b101bccaf8 = L.circleMarker(
800 |                 [47.916666666666664, -121.91666666666667],
801 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0291, "stroke": true, "weight": 3}
802 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
803 |         
804 |     
805 |         var popup_96f2bf35fe4afa5a697803bd130775c6 = L.popup({
806 |   "maxWidth": "100%",
807 | });
808 | 
809 |         
810 |             
811 |                 var html_e54aaf92261eab7a4eb2382afc50a70d = $(`<div id="html_e54aaf92261eab7a4eb2382afc50a70d" style="width: 100.0%; height: 100.0%;">Costco  - 29.1 CO2</div>`)[0];
812 |                 popup_96f2bf35fe4afa5a697803bd130775c6.setContent(html_e54aaf92261eab7a4eb2382afc50a70d);
813 |             
814 |         
815 | 
816 |         circle_marker_4a2c0524e66ddd8a6f2709b101bccaf8.bindPopup(popup_96f2bf35fe4afa5a697803bd130775c6)
817 |         ;
818 | 
819 |         
820 |     
821 |     
822 |             var circle_marker_a7cc2fb257663b0b4dd60a91f55607a7 = L.circleMarker(
823 |                 [41.05, -71.8],
824 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0161, "stroke": true, "weight": 3}
825 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
826 |         
827 |     
828 |         var popup_aab0bbd5f277014cc076deb901ba0746 = L.popup({
829 |   "maxWidth": "100%",
830 | });
831 | 
832 |         
833 |             
834 |                 var html_368649caaad2b3b9f6919977016ca042 = $(`<div id="html_368649caaad2b3b9f6919977016ca042" style="width: 100.0%; height: 100.0%;">Mastercard - 16.1 CO2</div>`)[0];
835 |                 popup_aab0bbd5f277014cc076deb901ba0746.setContent(html_368649caaad2b3b9f6919977016ca042);
836 |             
837 |         
838 | 
839 |         circle_marker_a7cc2fb257663b0b4dd60a91f55607a7.bindPopup(popup_aab0bbd5f277014cc076deb901ba0746)
840 |         ;
841 | 
842 |         
843 |     
844 |     
845 |             var circle_marker_a8350b8107f54477c068477064cd9d42 = L.circleMarker(
846 |                 [38.31666666666667, -121.33333333333333],
847 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0152, "stroke": true, "weight": 3}
848 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
849 |         
850 |     
851 |         var popup_4003c6eb668ed8e34b1350be494213fc = L.popup({
852 |   "maxWidth": "100%",
853 | });
854 | 
855 |         
856 |             
857 |                 var html_9b47d40d552b12abda9d8f1f511a9a1a = $(`<div id="html_9b47d40d552b12abda9d8f1f511a9a1a" style="width: 100.0%; height: 100.0%;">Salesforce - 15.2 CO2</div>`)[0];
858 |                 popup_4003c6eb668ed8e34b1350be494213fc.setContent(html_9b47d40d552b12abda9d8f1f511a9a1a);
859 |             
860 |         
861 | 
862 |         circle_marker_a8350b8107f54477c068477064cd9d42.bindPopup(popup_4003c6eb668ed8e34b1350be494213fc)
863 |         ;
864 | 
865 |         
866 |     
867 |     
868 |             var circle_marker_7fd894a68426804c63993a8490cc1830 = L.circleMarker(
869 |                 [41.266666666666666, -71.4],
870 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0273, "stroke": true, "weight": 3}
871 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
872 |         
873 |     
874 |         var popup_7c919e88496979412a786d567cc0857d = L.popup({
875 |   "maxWidth": "100%",
876 | });
877 | 
878 |         
879 |             
880 |                 var html_9ab9742a92d3e05ab7e819deb49bf805 = $(`<div id="html_9ab9742a92d3e05ab7e819deb49bf805" style="width: 100.0%; height: 100.0%;">JP Morgan Chase - 27.3 CO2</div>`)[0];
881 |                 popup_7c919e88496979412a786d567cc0857d.setContent(html_9ab9742a92d3e05ab7e819deb49bf805);
882 |             
883 |         
884 | 
885 |         circle_marker_7fd894a68426804c63993a8490cc1830.bindPopup(popup_7c919e88496979412a786d567cc0857d)
886 |         ;
887 | 
888 |         
889 |     
890 |     
891 |             var circle_marker_8e77b36c56cce57b7dec41e3f039c3d7 = L.circleMarker(
892 |                 [45.5, -92.33333333333333],
893 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0166, "stroke": true, "weight": 3}
894 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
895 |         
896 |     
897 |         var popup_3cf657954374f17d1465fcdbcc30766a = L.popup({
898 |   "maxWidth": "100%",
899 | });
900 | 
901 |         
902 |             
903 |                 var html_d35401bec638e8a5467209b07811a9f8 = $(`<div id="html_d35401bec638e8a5467209b07811a9f8" style="width: 100.0%; height: 100.0%;">UnitedHealth - 16.6 CO2</div>`)[0];
904 |                 popup_3cf657954374f17d1465fcdbcc30766a.setContent(html_d35401bec638e8a5467209b07811a9f8);
905 |             
906 |         
907 | 
908 |         circle_marker_8e77b36c56cce57b7dec41e3f039c3d7.bindPopup(popup_3cf657954374f17d1465fcdbcc30766a)
909 |         ;
910 | 
911 |         
912 |     
913 |     
914 |             var circle_marker_d818ee2b447f5f6abbace6fd824223aa = L.circleMarker(
915 |                 [40.81666666666667, -73.25],
916 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0201, "stroke": true, "weight": 3}
917 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
918 |         
919 |     
920 |         var popup_fda2f84d36e13e9b9eb69e8448c05f00 = L.popup({
921 |   "maxWidth": "100%",
922 | });
923 | 
924 |         
925 |             
926 |                 var html_c9c4534c4d2ed381f5f77955bc0a7c11 = $(`<div id="html_c9c4534c4d2ed381f5f77955bc0a7c11" style="width: 100.0%; height: 100.0%;">Johnson&Johnson  - 20.1 CO2</div>`)[0];
927 |                 popup_fda2f84d36e13e9b9eb69e8448c05f00.setContent(html_c9c4534c4d2ed381f5f77955bc0a7c11);
928 |             
929 |         
930 | 
931 |         circle_marker_d818ee2b447f5f6abbace6fd824223aa.bindPopup(popup_fda2f84d36e13e9b9eb69e8448c05f00)
932 |         ;
933 | 
934 |         
935 |     
936 |     
937 |             var circle_marker_af9a11974cc4a371478a61b50858c69c = L.circleMarker(
938 |                 [42.56666666666667, -85.61666666666666],
939 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0261, "stroke": true, "weight": 3}
940 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
941 |         
942 |     
943 |         var popup_a968587c88b86d35b2a9db10e2cb5155 = L.popup({
944 |   "maxWidth": "100%",
945 | });
946 | 
947 |         
948 |             
949 |                 var html_948af71d94a26bf023d47454f7e14d1c = $(`<div id="html_948af71d94a26bf023d47454f7e14d1c" style="width: 100.0%; height: 100.0%;">AbbVie - 26.1 CO2</div>`)[0];
950 |                 popup_a968587c88b86d35b2a9db10e2cb5155.setContent(html_948af71d94a26bf023d47454f7e14d1c);
951 |             
952 |         
953 | 
954 |         circle_marker_af9a11974cc4a371478a61b50858c69c.bindPopup(popup_a968587c88b86d35b2a9db10e2cb5155)
955 |         ;
956 | 
957 |         
958 |     
959 |     
960 |             var circle_marker_2615d9659958a5e52a408ae4bc10ca42 = L.circleMarker(
961 |                 [49.45, 2.5166666666666666],
962 |                 {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.7, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 5.0166, "stroke": true, "weight": 3}
963 |             ).addTo(map_28748e7bd156afca3a16a7fad43c62fe);
964 |         
965 |     
966 |         var popup_ca1bd868535a5f1ef8ed26373f328717 = L.popup({
967 |   "maxWidth": "100%",
968 | });
969 | 
970 |         
971 |             
972 |                 var html_1e2eebae5b0f1870e12226e184856a97 = $(`<div id="html_1e2eebae5b0f1870e12226e184856a97" style="width: 100.0%; height: 100.0%;">Hermes - 16.6 CO2</div>`)[0];
973 |                 popup_ca1bd868535a5f1ef8ed26373f328717.setContent(html_1e2eebae5b0f1870e12226e184856a97);
974 |             
975 |         
976 | 
977 |         circle_marker_2615d9659958a5e52a408ae4bc10ca42.bindPopup(popup_ca1bd868535a5f1ef8ed26373f328717)
978 |         ;
979 | 
980 |         
981 |     
982 | </script>
983 | </html>
```

data/cache/BE0003470755/docling/investor-guide-to-carbon-footprinting-table-1.csv
```
1 | ,,Upstream Scope 3,Downstream Scope 3
2 | 0,Sectors for which Scope 3 is likely to be material,"Consumer goods, utilities, industrials; energy; materials, chemicals","Sold product for oilandgas, automobiles; technology; apparel, chemicals Financed emissions: financials"
```

data/cache/NVIDIA/docling/FY2024-NVIDIA-Corporate-Sustainability-Report-table-1.csv
```
1 | ,0,1,2,3,4,5,6
2 | 0,Message From,Introduction,Climate and,"People, Diversity",Product Value,Responsible,Sustainability
3 | 1,Our CEO,,Efficiency,and Inclusion,Chain,Business,Indicators
```

data/cache/NVIDIA/docling/FY2024-NVIDIA-Corporate-Sustainability-Report-table-2.csv
```
1 | ,Metric,FY24,FY23,FY22,Reference Indicator
2 | 0,GHG Emissions 1  (MT CO 2 e),GHG Emissions 1  (MT CO 2 e),GHG Emissions 1  (MT CO 2 e),GHG Emissions 1  (MT CO 2 e),GHG Emissions 1  (MT CO 2 e)
3 | 1,Scope 1,"14,390","12,346","4,612",GRI 305-1 UNGC E6
4 | 2,"Scope 2, market-based","40,555","60,671","78,210",GRI 305-2 UNGC E6
5 | 3,"Scope 1 and 2, market-based","54,945","73,017","82,822",
6 | 4,"Scope 2, location-based","178,087","142,909","133,569",GRI 305-2 UNGC E6
7 | 5,Scope 3,"3,637,478","3,514,000","2,701,477",GRI 305-3
8 | 6,Category 1: Purchased goods and services 2,"3,216,144","2,975,189","2,506,722","UNGC E6, E6.1"
9 | 7,Category 2: Capital goods 2,"200,483","353,280","62,586",
10 | 8,Category 3: Fuel-and energy-related activities,"61,590","67,805","50,631",
11 | 9,Category 4: Upstream transportation and distribution,"72,562","60,572","37,910",
12 | 10,Category 5: Waste generated in operations 3,617,579,291,
13 | 11,Category 6: Business travel 2,"17,132","8,633",576,
14 | 12,Category 7: Employee commuting,"23,019","14,990","21,189",
15 | 13,Category 8: Upstream leased assets,"45,931","32,952","21,572",
16 | 14,External assurance,Report of Independent Accountants  for select metrics for FY23 and FY24.,Report of Independent Accountants  for select metrics for FY23 and FY24.,Report of Independent Accountants  for select metrics for FY23 and FY24.,GRI 2-5 UNGC G13
17 | 15,GHG emissions intensity (Scope 1 and 2 MT CO2e/$M revenue),0.9 2.7,3.1,,GRI 305-4
```

data/cache/NETFLIX/docling/Netflix_2022-ESG-Report-FINAL-table-1.csv
```
1 | ,,2019 MTCO2e,2020 MTCO2e,2021 MTCO2e,2022 MTCO2e
2 | 0,SCOPE 1,"51,487","30,883","62,815","59,388"
3 | 1,SCOPE 2 (market-based),565,141,0,0
4 | 2,SCOPE 2 (location-based),"26,594","28,585","42,291","41,411"
5 | 3,SCOPE 2 (target-based),"26,317","29,356","31,937","23,622"
6 | 4,SCOPE 1+2 (market-based),"52,052","31,024","62,815","59,388"
7 | 5,SCOPE 1+2 (target-based),"77,804","60,239","94,752","83,010"
8 | 6,SCOPE 3 (market-based),"1,192,659","1,020,541","1,466,497","1,086,833"
9 | 7,TOTAL (market-based),"1,244,711","1,051,564","1,529,312","1,146,221"
10 | 8,CARBON CREDITS,"(35,506)","(54,107)","(1,529,312)","(1,146,221)"
```

data/cache/NETFLIX/docling/Netflix_2022-ESG-Report-FINAL-table-2.csv
```
1 | ,Introduction,Environment,Social,Governance,Appendix,,
2 | 0,About This Report,ESG Data Tables,SASB Index,TCFD Index,Resources,GHG Inventory Methodology,Carbon Credit Project Screening Criteria
```

data/cache/NETFLIX/docling/Netflix_2022-ESG-Report-FINAL-table-3.csv
```
1 | ,Data Point,2019,2020,2021,2022
2 | 0,Paid Memberships,167 million,204 million,222 million,231 million
3 | 1,Employees,"8,600","9,400","11,300","12,800"
4 | 2,Revenue (USD Millions),"20,156","24,996","26,698","31,616"
```

data/cache/NETFLIX/docling/Netflix_2022-ESG-Report-FINAL-table-4.csv
```
1 | ,Data Point,2019,2020,2021,2022
2 | 0,Electricity (MWH),"81,136","94,285","156,555","156,967"
3 | 1,Global Renewable Electricity (%),100,100,100,100
4 | 2,Scope 1 Emissions (Metric Tons C02-e),"51,487","30,883","62,815","59,388"
5 | 3,"Scope 2 Emissions, Market-Based (Metrics Tons C02-e)",565,141,0,0
6 | 4,"Scope 2 Emissions, Location-Based (Metric Tons C02-e)","26,594","28,585","42,291","41,411"
7 | 5,"Scope 2 Emissions, Target-Based (Metric Tons C02-e)","26,317","29,356","31,937","23,622"
8 | 6,Scope 1 + Scope 2 (Market-Based) Emissions (Metric Tons C02-e),"52,052","31,024","62,815","59,388"
9 | 7,Scope 1 + Scope 2 (Target-Based) Emissions (Metric Tons C02-e),"77,804","60,239","94,752","83,010"
10 | 8,Scope 3 Emissions (Metric Tons C02-e),"1,192,659","1,020,541","1,466,497","1,086,833"
11 | 9,Total GHG Emissions: Scope 1 + Scope 2 (Market-Based) +  Scope 3 (Metric Tons C02-e),"1,244,711","1,051,564","1,529,312","1,146,221"
12 | 10,Carbon Credits,"(36,506)","(54,107)","(1,529,312)","(1,146,221)"
```

data/cache/NETFLIX/docling/Netflix_2022-ESG-Report-FINAL-table-5.csv
```
1 | ,Introduction,Environment,Social,Governance,Appendix,,
2 | 0,About This Report,ESG Data Tables,SASB Index,TCFD Index,Resources,GHG Inventory Methodology,Carbon Credit Project Screening Criteria
```

data/cache/SOLVAY_SA/docling/solvay-2022-annual-integrated-report-table-1.csv
```
1 | ,Category,Objective,Key initiatives delivered as part of the objective,Achievement
2 | 0,,Solvay 2030 vision: 5%,"Execute Power of Two companies. Definition of a management office (PMO), a clear roadmap for day  1, working in a constructive and collaborative manner with a strong focus on  people engagement Extra achievements: ·  Built a powerful and compelling equity story to create two strong separate  Companies ·  Excellent key stakeholder engagement - in internal and external - to achieve  decision support ·  Highly complex split, managed at pace to achieve ambitious timelines ·  zero-based redesign with effective new Organisation Design, cost management  and communication ·  M&A: created and negotiated portfolio opportunities with high multiples while  closing significant deals Target: ·  Deployment of Value Creation Plans for the segments in alignment with  G.R.O.W. strategy",10%
3 | 1,Strategy,GROW 2.0 Continue refining  and delivering the  G.R.O.W strategy 5%,"Extra achievements: ·  €300mn investment to extend leadership position in global lithium-ion battery  market  ·  First licensing agreement for Solvay for Hydrogen Peroxides (H2O2) in China for  500 kilotons of caprolactam facility  ·  Beat previous records for: Underlying EBITDA, cost reduction (85% of objective  achieved within 15 months); ROCE; balance sheet improvement and leverage  ratio.  ·  Deployment of Pricing and Contract Management ·  Acceleration of R&I capability building with open innovation and a focus on  circularity ·  Rollout of Star Factory program* and two flagship pilots in place and global  launch with ~100 site leader ·  Acceleration of technological growth platforms, with the launch of the fourth  Platform focused on Renewable Materials and Biotechnology  ·  Launched Scope 3 roadmap while delivering ~2x Paris Agreement on Scope 1  and Scope 2 since 2019 Target: ·  Further deploy the drive for excellence while leading with our Purpose ·  Further leverage assessment and pursue organization upskilling (30% execu- tive-level hired) Extra achievement:",10%
4 | 2,Organization,GROW 2.0 Continue refining  and delivering the  G.R.O.W strategy 5%,"·  Advancing our Commitment to Diversity, Equity and Inclusion** ·  Enhancing Solvay's reputation with employees and broader society through  Solvay One Planet, Solvay Cares, Solvay One Dignity, Solvay Solidarity Fund,  Employee Share program and other initiatives ·  Chair World Business Council for Sustainable Development (WBCSD) ·  ERT Board, government engagement ·  12 podcasts: 'The power of the AND is the future' available on the Solvay web- site and Podcast Apps Target:",10%
5 | 3,,Define the human  capital strategy for  the two new entities  5%,"·  Preparing two independent high-performing organizations with dedicated lead- ership, competencies and mandates  Extra achievement: ·  Best in class launch of the the two NewCos - Essential and Special ·  Benchmark practice in the Organisation Design of the two new Companies ·  Engaging with all leaders (head of businesses and head of functions): 73% en-",
```

data/cache/SOLVAY_SA/docling/solvay-2022-annual-integrated-report-table-2.csv
```
1 | ,Dimension of One Planet,,Min.,Target,,Max.,Result
2 | 0,Climate,GreenHouse Gas (GHG)  emissions (current scope Mt),11.3Mt Min.,11Mt Target,10.7Mt Max.,10.4Mt,200%
3 | 1,,% of sustainable solutions  in sales(constant rules),50.3% Min.,51.6% Target,53.2% Max.,54.8%,200%
4 | 2,,Water Water de-risking plans,No site with  mitigation plan Min.,5 top critical sites (water risk) with mitigation plan  to exit the Risk Zone Target,7,15 sites with  mitigation plan Max.,120%
5 | 3,Resources,,,,,,
6 | 4,,Industrial wastes without  valorization (kt),+9kt  versus 2021 result Min.,+0kt  versus 2021 result Target,56.45Kt,-5kt  versus 2021 result Max.,120%
7 | 5,,Increase the share of  revenue in Circular Business,Min. 8%,Target 9%,9.30%,Max. 10%,130%
8 | 6,Better Life,,,,,,
9 | 7,,Diversity number of initiatives,Proportional to 7  Initiatives implemented,7 Initiatives  implemented,"8,5",9 Initiatives+External  outstanding recognitions,140%
10 | 8,,included % of women manager,included % of women manager,,26.5%,,
11 | 9,Total One Planet Score,Total One Planet Score,Total One Planet Score,Total One Planet Score,Total One Planet Score,Total One Planet Score,137%
```

data/cache/SOLVAY_SA/docling/solvay-2022-annual-integrated-report-table-3.csv
```
1 | ,,Units,2022,2021,2020,2019,2018
2 | 0,PRIORITY TOPICS,PRIORITY TOPICS,PRIORITY TOPICS,PRIORITY TOPICS,PRIORITY TOPICS,PRIORITY TOPICS,PRIORITY TOPICS
3 | 1,Greenhouse gas emissions,Greenhouse gas emissions,Greenhouse gas emissions,Greenhouse gas emissions,Greenhouse gas emissions,Greenhouse gas emissions,Greenhouse gas emissions
4 | 2,Scope 1,Mt CO 2  eq.,9.2,9.6,8.9,10.6,10.4
5 | 3,Scope 2 - gross market-based,Mt CO 2  eq.,1.1,1.4,1.2,1.4,1.9
6 | 4,Total Scope 1+2,Mt CO 2  eq.,10.3,11.0,10.1,12.0,12.3
7 | 5,Scope 3,Mt CO 2  eq.,24.2,25.8,28.8,32.6,34.2
8 | 6,Total scopes 1+2+3,Mt CO 2  eq.,34.5,36.8,38.9,44.6,46.5
9 | 7,Biodiversity,Biodiversity,Biodiversity,Biodiversity,Biodiversity,Biodiversity,Biodiversity
10 | 8,Species potentially affected,Number,88,93,107,116,122
11 | 9,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS,HIGH MATERIALITY TOPICS
12 | 10,Energy,Energy,Energy,Energy,Energy,Energy,Energy
13 | 11,Fuel consumption for energy production,PJ,98,105,99,107,93
14 | 12,Energy purchased,PJ,29,33,34,38,45
15 | 13,Energy sold,PJ,26,33,31,32,23
16 | 14,Primary energy consumption,PJ,101,106,103,113,115
17 | 15,Solid fuels,PJ,28,27,27,32,33
```

data/cache/SOLVAY_SA/docling/solvay-2022-annual-integrated-report-table-4.csv
```
1 | ,0,1,2
2 | 0,Theme,Planet: Core metrics and disclosures,
3 | 1,Climate change,"Greenhouse gas (GHG) emissions  For all relevant greenhouse gasses (e.g. carbon dioxide, methane, nitrous oxide, F-gasses, etc.),  report in metric tons of carbon dioxide equivalent (tCO 2 e) GHG 