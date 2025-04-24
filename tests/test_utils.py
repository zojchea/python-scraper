"""
Unit tests for utility functions in the Newegg scraper project.

This test ensures that polite_delay introduces a delay
within a specified range to mimic human browsing behavior.
"""

from src.utils import polite_delay
import time


def test_polite_delay_duration():
    start = time.time()
    polite_delay(0.5, 0.6)
    end = time.time()
    assert 0.5 <= (end - start) <= 0.7
