# Cell 1
import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    match norm_type:
        case 'l1':
            print(f"l1: {arr}")
            return np.linalg.norm(arr.ravel(), ord=1)
        case 'l2':
            print(f"l2: {arr}")
            return np.linalg.norm(arr)
        case 'linf':
            print(f"linf: {arr}")
            return np.linalg.norm(arr.ravel(), ord=np.inf)
        case 'frobenius':
            print(f"frobenius: {arr}")
            if arr.ndim != 2: 
                raise ValueError(...)
            return np.linalg.norm(arr, ord='fro')
        case _:
            return "Unknown Vector Norms"