"""
Main entry point for the Newegg product scraping application.

This script:
1. Ensures the output directory exists.
2. Executes the scraping process to collect product data.
3. Exports the data to a CSV file defined in the configuration.
"""

import os
import config

from product_scraper import scrape_all_products
from export import save_to_csv


if __name__ == "__main__":
    os.makedirs(os.path.dirname(config.OUTPUT_FILE), exist_ok=True)

    print("Starting scraping process...")
    scraped_data = scrape_all_products()
    print(f"Finished scraping. Total products collected: {len(scraped_data)}")

    print("Saving to CSV...")
    save_to_csv(scraped_data)
    print("Export complete.")
