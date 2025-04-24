import unittest
from unittest.mock import patch, MagicMock

from src import product_scraper


class TestProductScraper(unittest.TestCase):

    @patch("src.product_scraper.requests.get")
    def test_get_product_links(self, mock_get):
        mock_html = """
        <html><body>
        <a class="item-title" href="https://www.newegg.com/p/1">Product 1</a>
        </body></html>
        """
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        links = product_scraper.get_product_links(max_products=1)
        self.assertIn("https://www.newegg.com/p/1", links)
