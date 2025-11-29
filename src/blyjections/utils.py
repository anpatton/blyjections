import numpy as np

def repeat_last_element(vector, repeats=None):
    """
    Takes an input vector and returns it with the last element repeated N times.
    
    Args:
        vector (list/array): Input vector
        repeats: Number of times to repeat the last element
    
    Returns:
        New array with last element repeated N times
    """
    if repeats is None
        raise ValueError("Provide number of repeats")

    vector = np.array(vector)
    last_element = vector[-1]
    repeated_elements = np.full(repeats, last_element)
    repeated_vector = np.concatenate([vector, repeated_elements])
    return repeated_vector