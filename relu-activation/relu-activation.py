import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.array(x, dtype = float, ndmin = 1)
    return np.maximum(x, 0)