"""
Product Scraper Module for Newegg

This module handles the web scraping logic for collecting product information
from Newegg based on a search query. It uses BeautifulSoup to parse HTML and
`requests` to handle HTTP requests.

Functions:
- get_product_links(max_products): Collects product URLs from paginated search results.
- parse_product_page(url, retries): Extracts product details from an individual product page.
- scrape_all_products(): Scrapes multiple products and returns the full dataset.
"""

from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import logging

import config
from utils import polite_delay


logging.basicConfig(filename="../logs/scraper_errors.log", level=logging.ERROR)

BASE_URL = config.BASE_URL
SEARCH_URL = config.SEARCH_URL_TEMPLATE
HEADERS = config.HEADERS

FIELDS = [
    "product_title",
    "product_description",
    "product_final_pricing",
    "product_rating",
    "seller_name",
    "main_image_url"
]


def get_product_links(max_products=config.MAX_PRODUCTS):
    product_links = set()
    page = 1

    while len(product_links) < max_products:
        print(f"Fetching product list page {page}...")

        try:
            response = requests.get(SEARCH_URL.format(page), headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for a_tag in soup.select("a.item-title"):
                if len(product_links) >= max_products:
                    break
                product_links.add(a_tag.get("href"))

        except requests.RequestException as e:
            logging.error(f"Failed to fetch page {page}: {e}")
            print(f"Failed to fetch page {page}: {e}")

        polite_delay()
        page += 1

    return list(product_links)


def parse_product_page(url, retries=3):
    for attempt in range(retries):

        try:
            print(f"Scraping product: {url}")
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find("h1", class_="product-title").get_text(strip=True)

            description_tag = soup.find("div", class_="product-bullets")
            description = description_tag.get_text(strip=True) if description_tag else "N/A"

            price_tag = soup.select_one("li.price-current")
            final_price = price_tag.get_text(strip=True) if price_tag else "N/A"

            rating_tag = soup.select_one(".rating .rating-views")
            rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

            seller_tag = soup.select_one(".product-seller strong")
            seller = seller_tag.get_text(strip=True) if seller_tag else "N/A"

            image_tag = soup.select_one(".product-view .swiper-slide img")
            image_url = image_tag.get("src") if image_tag else "N/A"

            return {
                "product_title": title,
                "product_description": description,
                "product_final_pricing": final_price,
                "product_rating": rating,
                "seller_name": seller,
                "main_image_url": image_url
            }

        except Exception as e:
            logging.error(f"[{attempt + 1}/{retries}] Error scraping {url}: {e}")
            polite_delay(2, 4)

    print(f"Failed to scrape product after {retries} attempts: {url}")
    return None


def scrape_all_products():
    links = get_product_links()
    data = []

    for link in tqdm(links, desc="Scraping products"):
        product_data = parse_product_page(link)
        if product_data:
            data.append(product_data)
        polite_delay(1, 2)

    return data
