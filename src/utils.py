import time
import random


def polite_delay(min_seconds=1.5, max_seconds=3.0):
    time.sleep(random.uniform(min_seconds, max_seconds))
