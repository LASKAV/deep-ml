import numpy as np

def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    a_arr = np.array(a)
    b_arr = np.array(b)

    if a_arr.shape[1] != b_arr.shape[0]:
        return -1

    return (a_arr @ b_arr).tolist()