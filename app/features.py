from typing import List
import numpy as np

def featurize(raw: List[float]) -> np.ndarray:
    # Example: normalize simple numeric inputs
    x = np.array(raw, dtype=float)
    # Clip to a reasonable range and return
    x = np.clip(x, -5, 5)
    return x
