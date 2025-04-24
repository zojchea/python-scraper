"""
CSV Export Utility

This module provides a single function to export scraped product data
into a CSV file with predefined field names. The output filename is
determined by the config or can be passed as a parameter.
"""

import csv
import config


def save_to_csv(data, filename=None):
    filename = filename or config.OUTPUT_FILE
    fieldnames = [
        "product_title",
        "product_description",
        "product_final_pricing",
        "product_rating",
        "seller_name",
        "main_image_url"
    ]

    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
