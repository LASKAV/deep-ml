# Cell 1
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    if len(a) != len(b):
        print("Vectors have different lengths")
        return -1 
        
    c = []
    for i in range(len(a)):
         sum_element = a[i] + b[i]
         c.append(sum_element)
         
    return c