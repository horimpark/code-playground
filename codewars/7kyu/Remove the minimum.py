import numpy as np

def remove_smallest(numbers):
    if not numbers:
        return []
    min_idx = np.argmin(numbers)
    return [n for i, n in enumerate(numbers) if i != min_idx]