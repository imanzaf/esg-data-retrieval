import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()


try:
    from openai import OpenAI
except ImportError:
    print("OpenAI client is not installed. Please install with: pip install openai")
    OpenAI = None


# Both keys are available. Uncomment the one you want to use below.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")


def filter_tables(directory_path, parser):
    """
    Gather all CSVs in directory_path/parser.value, convert them to markdown,
    send them to the LLM, store the LLM's markdown output, and return as a DataFrame.
    """

    # 1) Collect all CSVs into one markdown string
    combined_markdown = ""
    parser_subfolder = os.path.join(directory_path, parser.value)

    # If the parser subfolder doesn't exist or is empty, handle gracefully
    if not os.path.isdir(parser_subfolder):
        print(f"No directory found for parser: {parser_subfolder}")
        return pd.DataFrame()

    for filename in os.listdir(parser_subfolder):
        if filename.endswith(".csv"):
            file_path = os.path.join(parser_subfolder, filename)
            try:
                df = pd.read_csv(file_path)
                # Convert df to markdown
                md = df.to_markdown(index=False, tablefmt="pipe")
                # Optionally label by file
                combined_markdown += f"\n\n#### File: {filename}\n\n"
                combined_markdown += md
                combined_markdown += "\n\n"
            except Exception as e:
                print(f"Error reading CSV {file_path}: {e}")

    if not combined_markdown.strip():
        print("No CSV data found to send to the LLM.")
        return pd.DataFrame()

    # 2) Send markdown content to LLM
    llm_output = _send_to_deepseek(combined_markdown)
    if not llm_output:
        print("No response from LLM or an error occurred.")
        return pd.DataFrame()

    # 3) Save the LLM's markdown output directly as .md file
    output_path = os.path.join(directory_path, "esg_data_llm.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(llm_output)
    print(f"LLM output saved to: {output_path}")

    # 4) Return DataFrame for compatibility with existing code
    return pd.DataFrame({"LLM_Output": [llm_output]})


def _send_to_deepseek(markdown_content: str) -> str | None:
    """Sends markdown content to the LLM (either OpenAI or DeepSeek) for processing."""
    # ---------------------------------------------------------------------
    # To use OpenAI, uncomment the following block:
    if not OPENAI_API_KEY:
        print("OpenAI API key missing.")
        return None
    client = OpenAI(api_key=OPENAI_API_KEY)
    # model="gpt-4o" will be used below.
    # ---------------------------------------------------------------------

    # ---------------------------------------------------------------------
    # To use DeepSeek, comment out the above block and uncomment this one:
    # if not DEEPSEEK_API_KEY:
    #     print("DeepSeek API key missing.")
    #     return None
    # client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
    # ---------------------------------------------------------------------

    try:
        response = client.chat.completions.create(
            # -----------------------------------------------------------------
            # To use OpenAI, uncomment the following line:
            model="gpt-4o",
            # To use DeepSeek, comment out the above line and uncomment this one:
            # model="deepseek-chat",
            # -----------------------------------------------------------------
            messages=[
                {
                    "role": "system",
                    "content": "You are a sustainability data extraction specialist. Return ONLY valid markdown tables.",
                },
                {"role": "user", "content": _build_llm_prompt(markdown_content)},
            ],
            temperature=1,
            max_tokens=4000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"API error: {str(e)}")
        return None


def _build_llm_prompt(markdown_data: str) -> str:
    return f"""
You are given sustainability report tables as markdown below:
{markdown_data}




Please perform the following steps:




1. Identify the table(s) with the most complete year-by-year data for
 Scope 1, Scope 2 (market-based), and Scope 2 (location-based)
 from the provided markdown.
 - Use judgment to select tables with the most complete and likely
   accurate data across all years.
 - Prioritize completeness and consistency.
 - For Scope 2, include both market-based and location-based data if
   available, and explicitly note which is which.
 - Convert all values to tCO2e and keep units consistent across years.
 - Use null for years where data is missing or unavailable.




2. Create a **"Key Table"** in Markdown with columns for:
 | Category | Year | Emissions (tCO2e) |
 The rows should be:
   - Scope 1
   - Scope 2 (Market-based)
   - Scope 2 (Location-based)
 Include data for as many years as can be found (e.g., 2020, 2021, 2022, 2023).
 Convert all values to tCO2e. Use null for years where data is missing.




3. Create four additional Markdown tables (breakdown tables) if
 information is available; otherwise, return them with "No Data" or "N/A":
 - **Scope 1 Breakdown**:
   | Scope 1 Source / Subcategory | Year | Emissions (tCO2e) |
 - **Scope 2 Market-based Breakdown**:
   | Region or Business Unit | Year | Emissions (tCO2e) |
 - **Scope 2 Location-based Breakdown**:
   | Region or Business Unit | Year | Emissions (tCO2e) |
 - **Scope 3 Breakdown**:
   | Scope 3 Category | Year | Emissions (tCO2e) |
   Always include a "Total Scope 3" row.




4. Return exactly **these five Markdown tables** in this order with titles:
 A) Key Table
 B) Scope 1 Breakdown
 C) Scope 2 Market-based Breakdown
 D) Scope 2 Location-based Breakdown
 E) Scope 3 Breakdown (with Total)




5. Provide **no additional commentary**, just the five tables in Markdown format.
"""
