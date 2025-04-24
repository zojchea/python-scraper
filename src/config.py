import os
import json
from datetime import datetime

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scraper_config.json"))

with open(CONFIG_PATH, "r") as f:
    CONFIG = json.load(f)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

BASE_URL = CONFIG["base_url"]
SEARCH_QUERY = CONFIG["search_query"]
MAX_PRODUCTS = CONFIG["max_products"]
USER_AGENT = CONFIG["user_agent"]
DELAY = CONFIG["delay_between_requests"]

OUTPUT_FILE = CONFIG.get("output_file", "../exported_data/newegg_products_{datetime}.csv").replace("{datetime}", timestamp)

SEARCH_URL_TEMPLATE = f"{BASE_URL}p/pl?d={SEARCH_QUERY}&page={{}}"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1"
}
