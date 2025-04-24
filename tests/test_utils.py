from src.utils import polite_delay
import time


def test_polite_delay_duration():
    start = time.time()
    polite_delay(0.5, 0.6)
    end = time.time()
    assert 0.5 <= (end - start) <= 0.7
