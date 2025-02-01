from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, Response, send_from_directory
from src.scripts.retrieve_emissions_data import get_emissions_data
from loguru import logger
from src.find.company_profile import CompanyProfile
from src.find.esg_reports import ESGReports
from io import BytesIO
import os
import threading
import folium
import src.utils.rag_utils as rag_utils

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
from flask_socketio import SocketIO
from asyncio import sleep
from threading import Event

# LLM-based table extraction
from src.scripts.retrieve_emissions_data_pro import get_emissions_data_pro
from src.utils.data_models import TableParsers

# Globals for RAG
rag_chain = None
rag_initialized = False
pdf_path_global = None

import csv
import re
import yfinance as yf
import pandas as pd

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allows cross-origin requests

for rule in app.url_map.iter_rules():
    print(rule)

# Get the absolute path of the correct static folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
STATIC_FOLDER = os.path.join(BASE_DIR, "static", "images")

# Ensure the correct static/images directory exists
os.makedirs(STATIC_FOLDER, exist_ok=True)


def dms_to_decimal(dms):
    match = re.match(r"(-?\d+)°(\d+)?", dms)  # Support negative values
    if match:
        degrees = int(match.group(1))  # Handle negative degrees
        minutes = int(match.group(2)) if match.group(2) else 0
        return degrees + (minutes / 60)
    return None  # Return None if format is incorrect


df = pd.read_csv("src/emissimap3.csv")
# Ensure required columns exist
print(df.head())
df["Latitude"] = df["Latitude"].apply(dms_to_decimal)
df["Longitude"] = df["Longitude"].apply(dms_to_decimal)
print(df)

# Create a base map
m = folium.Map(location=[20, 0], zoom_start=2)


# Define a color scale based on emissions level
def get_color(emissions):
    if emissions < 1000:
        return "green"
    elif 1000 <= emissions < 5000:
        return "orange"
    else:
        return "red"


# Add markers for each company
for _, row in df.iterrows():
    print(f"Adding marker: {row['Company']} ({row['Latitude']}, {row['Longitude']}) - {row['Emissions']} CO2")

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5 + (row["Emissions"] / 1000),
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.7,
        popup=f"{row['Company']} - {row['Emissions']} CO2",
    ).add_to(m)

# Save map to an HTML file
map_path = os.path.join(STATIC_FOLDER, "emissions_map.html")
m.save(map_path)

print(f"Map saved as {map_path}")


@app.route("/static/images/emissions_map.html")
def serve_emissions_map():
    return send_from_directory("static/images", "emissions_map.html")


@app.route("/emissions_map")
def emissions_map():
    return render_template("maps.html")


@app.route("/firstpage")
def firstpage():
    return render_template("firstpage.html")


@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


@app.route("/instructionspremium")
def instructionspremium():
    return render_template("instructionspremium.html")


def normalize_name(name):
    """Normalize company name for better matching."""
    name = name.strip().upper()

    # Remove common suffixes
    name = re.sub(r"[.,'’]", "", name)  # Remove punctuation
    name = re.sub(r"\b(INC|LTD|CO|CORPORATION|CORP|LLC|GROUP|HOLDINGS|PLC)\b", "", name)  # Remove suffixes
    name = re.sub(r"\s+", " ", name).strip()  # Remove extra spaces

    print(f"[DEBUG] Normalized name: '{name}'")  # Debugging output
    return name


@app.route("/get_news", methods=['POST'])
def get_news_route():
    company_name = request.form.get("company_name")
    if not company_name:
        return jsonify({"error": "Please enter a company name."}), 400

    news_data = get_news(company_name)

    print(f"News data for {company_name}: {news_data}")

    return jsonify({
        "company_name": company_name,
        "news_data": news_data,
    })


def format_news(raw_news):
    """Helper function to format news data correctly, including images."""
    if not raw_news or not isinstance(raw_news, list):
        print("[ERROR] News data is empty or not a list")
        return []

    news_data = []
    for article in raw_news:
        try:
            content = article.get("content", {})
            if not isinstance(content, dict):
                print(f"[ERROR] Invalid content format: {content}")
                continue

            title = content.get("title", "No title available")
            publisher = content.get("provider", {}).get("displayName", "Unknown source")

            # Extract the news link
            link_data = content.get("clickThroughUrl") or content.get("canonicalUrl")
            link = link_data.get("url") if isinstance(link_data, dict) else "#"

            # Extract the image URL
            image_url = content.get("thumbnail", {}).get("resolutions", [{}])[0].get("url", "")

            news_data.append({
                "title": title,
                "publisher": publisher,
                "link": link,
                "image": image_url  # Add image URL
            })
        except Exception as e:
            print(f"[ERROR] Error formatting news article: {e}")

    return news_data


TICKER_CSV_PATH = "src/company_names_tickers_news.csv"


# Function to load tickers from CSV file
def load_ticker_map(csv_path):
    ticker_map = {}
    isin_map = {}

    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            headers = [header.strip().upper() for header in reader.fieldnames]

            if not headers or "COMPANY NAME" not in headers or "SYMBOL" not in headers or "ISIN NUMBER" not in headers:
                print(f"[ERROR] CSV file is missing required headers: {headers}")
                return {}, {}

            for row in reader:
                company = normalize_name(row["Company Name"])  # Normalize before storing
                ticker = row["Symbol"].strip().upper()
                isin = row["ISIN Number"].strip().upper()

                if company and ticker:
                    ticker_map[company] = ticker
                if isin and ticker:
                    isin_map[isin] = ticker

        print(f"[DEBUG] Ticker map loaded with {len(ticker_map)} entries")
        print(f"[DEBUG] ISIN map loaded with {len(isin_map)} entries")

    except Exception as e:
        print(f"[ERROR] Failed to load ticker map: {e}")

    return ticker_map, isin_map


# Load at startup
MANUAL_TICKER_MAP, MANUAL_ISIN_MAP = load_ticker_map(TICKER_CSV_PATH)


def get_ticker(identifier):
    """Retrieve the stock ticker symbol for a given company name or ISIN."""
    identifier = normalize_name(identifier)  # Normalize user input

    print(f"[DEBUG] Normalized identifier: '{identifier}'")

    # First, check if it's an ISIN
    if identifier in MANUAL_ISIN_MAP:
        print(f"[DEBUG] Found ticker in ISIN map: {MANUAL_ISIN_MAP[identifier]}")
        return MANUAL_ISIN_MAP[identifier]

    # Second, check if it's an exact company name match
    if identifier in MANUAL_TICKER_MAP:
        print(f"[DEBUG] Found ticker in company map: {MANUAL_TICKER_MAP[identifier]}")
        return MANUAL_TICKER_MAP[identifier]

    # Third, try to find a close match in the manual map
    for stored_name, ticker in MANUAL_TICKER_MAP.items():
        if identifier in stored_name or stored_name in identifier:
            print(f"[DEBUG] Found ticker by fuzzy match: {stored_name} -> {ticker}")
            return ticker

    print(f"[DEBUG] {identifier} not found in manual maps, searching Yahoo Finance...")

    # If no match, try to query Yahoo Finance
    try:
        search_results = yf.Ticker(identifier)
        if search_results.history(period="1d").empty:
            print(f"[DEBUG] No historical data found for: {identifier}")
            return None

        print(f"[DEBUG] Found ticker dynamically: {search_results.ticker}")
        return search_results.ticker
    except Exception as e:
        print(f"[ERROR] Error retrieving ticker: {e}")
        return None


def get_news(company_name):
    try:
        ticker_symbol = get_ticker(company_name)
        if not ticker_symbol:
            print(f"[DEBUG] No ticker found for {company_name}")
            return []

        ticker = yf.Ticker(ticker_symbol)
        raw_news = ticker.news

        if not isinstance(raw_news, list):  # Ensure raw_news is a list before processing
            print(f"[ERROR] Unexpected news format for {ticker_symbol}: {type(raw_news)}")
            return []

        print(f"[DEBUG] Raw news data for {ticker_symbol}: {raw_news}")

        return format_news(raw_news)

    except Exception as e:
        print(f"[ERROR] Error retrieving news: {e}")
        return []


print(get_news("Apple"))


@app.route("/download_table")
def download_table():
    """Generate and serve the emissions data as a CSV file for download."""
    company_name = request.args.get("company_name")
    parser = TableParsers.DOCLING

    if not company_name:
        return "Company name is required!", 400

    data = get_emissions_data(company_name, idType="name", parser=parser)

    if not isinstance(data, pd.DataFrame) or data.empty:
        return "No data available for download.", 404

    csv_buffer = BytesIO()
    data.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(csv_buffer, mimetype="text/csv", as_attachment=True, download_name=f"{company_name}_emissions.csv")


stop_rag_event = Event()


################################################################
# 1) Tables on the left
################################################################
@app.route("/index", methods=["GET", "POST"])
def home():
    """
    Updated route to handle form submissions for a new company,
    re-run LLM extraction, and pass data to index.html for the
    chatbot, chart, and extracted tables.
    """
    company_name = None
    report_url = None
    llm_markdown = ""
    pdf_path = None

    if request.method == "POST":
        # Force-stop any old RAG job
        rag_utils.stop_rag_event.set()

        # Clear out old chain
        rag_utils.rag_chain = None
        rag_utils.rag_initialized = False

        # Normal "search" logic
        company_name = request.form.get("company_name", "").strip()
        selected_id_type = request.form.get("idType", "name")

        if company_name:
            parser = TableParsers.DOCLING
            df, pdf_path = get_emissions_data_pro(company_name, selected_id_type, parser)
            if not df.empty and "LLM_Output" in df.columns:
                llm_markdown = df["LLM_Output"].iloc[0]
            else:
                llm_markdown = "No emissions data found for this company."

            # Store the PDF path in rag_utils
            rag_utils.pdf_path_global = pdf_path

            esg_reports = ESGReports(CompanyProfile(company_name, selected_id_type))
            print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging

            # Extract the first available report URL
            if esg_reports.urls:
                report_url = next(iter(esg_reports.urls.values()))  # Get first URL dynamically

            print(f"DEBUG: Selected Report URL -> {report_url}")

    return render_template(
        "index.html",
        company_name=company_name,
        report_url=report_url,
        llm_markdown=llm_markdown
    )


################################################################
# 3) RAG Endpoints
################################################################
@app.route("/rag_init", methods=["POST"])
def rag_init():
    """
    Trigger RAG building in a background thread so it doesn't block.
    """
    if rag_utils.rag_chain is not None or rag_utils.rag_initialized:
        return jsonify({"status": "RAG already initialized"})

    if not rag_utils.pdf_path_global or not os.path.isfile(rag_utils.pdf_path_global):
        return jsonify({"status": "No valid original PDF to build RAG from."})

    # Clear the stop event
    rag_utils.stop_rag_event.clear()

    def init_rag_in_background(path):
        logging.info("Starting RAG initialization in background...")
        try:
            if rag_utils.stop_rag_event.is_set():
                logging.info("Stop event was set before starting RAG initialization")
                return
            chain = rag_utils.build_final_system(path)
            if rag_utils.stop_rag_event.is_set() or chain is None:
                logging.info("Stop event was set during RAG initialization or chain creation failed")
                return
            rag_utils.rag_chain = chain
            rag_utils.rag_initialized = True
            logging.info("RAG system successfully initialized.")
        except Exception as e:
            logging.error(f"Failed to build RAG: {e}")
            rag_utils.rag_chain = None
            rag_utils.rag_initialized = False

    thread = threading.Thread(target=init_rag_in_background, args=(rag_utils.pdf_path_global,))
    thread.start()

    return jsonify({"status": "RAG initialization started"})


@app.route("/ask", methods=["POST"])
def ask_question():
    """
    POST route for user queries to the RAG.
    """
    question = request.form.get("question", "")
    if not question:
        return jsonify({"answer": "No question provided."})

    if not rag_utils.rag_chain or not rag_utils.rag_initialized:
        return jsonify({"answer": "RAG is not initialized yet. Please wait."})

    try:
        answer = rag_utils.rag_chain.invoke(question)
        return jsonify({"answer": answer})
    except Exception as e:
        logging.error(f"Error in RAG QA: {e}")
        return jsonify({"answer": f"Error: {str(e)}"})


@app.route("/reset_rag", methods=["POST"])
def reset_rag():
    rag_utils.stop_rag_event.set()
    rag_utils.rag_chain = None
    rag_utils.rag_initialized = False
    return jsonify({"status": "RAG reset"})


df = pd.read_csv('src/company_names_tickers.csv')

unique_countries = sorted(df['Country'].dropna().astype(str).unique().tolist())
unique_sectors = sorted(df['Sector'].dropna().astype(str).unique().tolist())
unique_industries = sorted(df['Industry'].dropna().astype(str).unique().tolist())


@app.route("/advanced_search")
def advanced_search():
    return render_template(
        "advanced_search.html",
        countries=unique_countries,
        sectors=unique_sectors,
        industries=unique_industries,
        companies=[],
        selected_company=None,
        emissions_data=None,
        report_url=None
    )


@app.route("/submit", methods=["POST"])
def submit():
    # Retrieve form data
    sector = request.form["sector"]
    country = request.form["country"]
    industry = request.form["industry"]
    selected_company = request.form.get("company")  # Get the selected company

    filtered_df = df
    if sector != "all":
        filtered_df = filtered_df[filtered_df['Sector'] == sector]
    if country != "all":
        filtered_df = filtered_df[filtered_df['Country'] == country]
    if industry != "all":
        filtered_df = filtered_df[filtered_df['Industry'] == industry]

    selected_companies = filtered_df['Company Name'].drop_duplicates().tolist()

    report_url = None
    emissions_data = None
    if selected_company:
        try:
            parser = TableParsers.DOCLING
            emissions_data = get_emissions_data(selected_company, idType="name", parser=parser)

            esg_reports = ESGReports(CompanyProfile(selected_company, idType="name"))
            print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging

            # Extract the first available report URL
            if esg_reports.urls:
                report_url = next(iter(esg_reports.urls.values()))  # Get first URL dynamically

            print(f"DEBUG: Selected Report URL -> {report_url}")
        except Exception as e:
            print(f"Error retrieving emissions data for {selected_company}: {e}")
            emissions_data = None

    return render_template(
        "advanced_search.html",
        companies=selected_companies,
        countries=unique_countries,
        sectors=unique_sectors,
        industries=unique_industries,
        selected_company=selected_company,
        report_url=report_url,
        emissions_data=emissions_data.to_html() if emissions_data is not None else None
    )


@app.route("/test", methods=["GET", "POST"])
def test():
    table_html = ""
    report_url = None
    company_name = ""
    news_data = []

    if request.method == "POST":
        company_name = request.form.get("company_name")  # get the text input
        parser = TableParsers.DOCLING

        # NEW: get the radio button value (defaults to 'name' if none chosen)
        selected_id_type = request.form.get("idType", "name")

        if company_name:
            # Pass user's choice of 'name', 'ticker', or 'isin'
            data = get_emissions_data(company_name, idType=selected_id_type, parser=parser)

            if isinstance(data, pd.DataFrame):
                table_html = data.to_html()

            esg_reports = ESGReports(CompanyProfile(company_name, selected_id_type))
            print(f"DEBUG: ESGReports URLs -> {esg_reports.urls}")  # Debugging

            # Extract the first available report URL
            if esg_reports.urls:
                report_url = next(iter(esg_reports.urls.values()))  # Get first URL dynamically

            print(f"DEBUG: Selected Report URL -> {report_url}")

    news_data = get_news(company_name)

    return render_template(
        "test.html",
        table_html=table_html,
        report_url=report_url,
        company_name=company_name,
        news_data=news_data
    )


@app.route("/progress/<socketid>", methods=["POST"])
def progress(socketid):
    def background_task():
        for x in range(1, 6):  # Updates from 20% to 100%
            socketio.emit("update_progress", {"progress": x * 20}, room=socketid)
            socketio.sleep(5)  # Wait 5 seconds before sending the next update

        # Emit event when progress reaches 100%
        socketio.emit("progress_complete", room=socketid)

    socketio.start_background_task(background_task)
    return Response(status=204)


@app.route("/register")
def register():
    return render_template("register.html")


VALID_USERS = {
    "test@example.com": "password123"
}


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check credentials
        if email in VALID_USERS and VALID_USERS[email] == password:
            return redirect(url_for("home"))  # Redirects to the index page

        return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


@app.route("/rag_status", methods=["GET"])
def rag_status():
    """
    Returns whether the RAG system is initialized yet.
    The front end can poll this to update the UI.
    """
    return jsonify({"initialized": rag_utils.rag_initialized})


if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
