import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    counter = Counter(x)
    max_freq = max(counter.values())

    mode = [k for k,v in counter.items() if v == max_freq]
    mode = float(min(mode))
    return mean, median, mode