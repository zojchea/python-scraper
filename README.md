# 🕸️ Python Scraper – Newegg Product Data Collection

This project is a Python-based web scraper that collects product information from [Newegg](https://www.newegg.com/) using BeautifulSoup and `requests`. It extracts key product details and exports them to a CSV file.

---

## 🚀 Features

- Scrapes product title, description, pricing, rating, seller, and main image
- Dynamically configured via `scraper_config.json`
- Built-in polite delays to avoid rate-limiting
- Retry logic for failed requests
- TQDM progress bar
- Clean project structure with unit tests

---

## 📁 Project Structure
<pre>
python-scraper/
│
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Dependencies list
├── scraper_config.json         # Scraper settings (target URL, delay, etc.)
│
├── exported_data/              # Output CSV files go here
│
├── logs/                       # Logs from the scraper
│   └── scraper_errors.log
│
├── src/                        # Main source code
│   ├── __init__.py
│   ├── config.py               # Loads and parses scraper_config.json
│   ├── export.py               # CSV export logic
│   ├── main.py                 # Entry point to run the scraper
│   ├── product_scraper.py      # Functions for scraping product data
│   └── utils.py                # Utility functions (e.g., polite_delay)
│
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_scraper.py         # Tests for product scraping logic
│   └── test_utils.py           # Tests for delay utility
│
└── venv/                       # (Local virtual environment – ignored by Git)
</pre>



## ⚙️ Configuration (`scraper_config.json`)

```json
{
  "base_url": "https://www.newegg.com/",
  "search_query": "graphics+card",
  "max_products": 500,
  "output_file": "exported_data/newegg_products_{datetime}.csv",
  "user_agent": "Mozilla/5.0 (...) Chrome/113.0.0.0 Safari/537.36",
  "delay_between_requests": 1.5
}
```

- `max_products`: Number of products to scrape
- `output_file`: Path with optional `{datetime}` placeholder
- `delay_between_requests`: Seconds to wait between requests
- `user_agent`: User agent to mimic real browser


---

## 🛠 Installation

```bash
git clone https://github.com/zojchea/python-scraper.git
cd python-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Running the Scraper

```bash
python src/main.py
```

The output will be saved in `exported_data/` as a timestamped `.csv` file.

---

## 🧪 Running Tests

Run all tests using:

```bash
pytest tests/
```

---

## ⚠️ Important Note on Limitations

This scraper is implemented using `requests` and `BeautifulSoup`, which works for fetching public product data from Newegg under normal conditions. However, Newegg uses Cloudflare protection that may trigger a CAPTCHA challenge after several requests or depending on network behavior.

When this happens, the page content returned by requests is no longer the actual product page, but a Cloudflare challenge or CAPTCHA screen. This will cause the scraper to fail in collecting real product data.

The proper workaround in such cases involves using:

- `Selenium` with a real browser, which can render JavaScript and solve Cloudflare challenges.

- Rotating proxies or residential IPs to avoid rate-limiting and detection.

During development, I tested multiple free proxy options, but none were stable, fast, or reliable enough to maintain consistent scraping. All either timed out or failed HTTPS handshakes.

For production-grade scraping, integrating paid proxy services (such as ScraperAPI or Smartproxy) or browser automation tools (such as undetected-chromedriver) is highly recommended.

---

## ✨ Author

**Zojche Atanasova**  
[GitHub @zojchea](https://github.com/zojchea)

---
