import numpy as np
def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here

    reference_counts_normalised = np.array(reference_counts)/sum(reference_counts)
    production_counts_normalised = np.array(production_counts)/sum(production_counts)
    tvd = 1/2 * np.sum(np.abs(reference_counts_normalised - production_counts_normalised))
    drift_detected = True if tvd > threshold else False
    return ({'score' : tvd, 'drift_detected' : drift_detected})