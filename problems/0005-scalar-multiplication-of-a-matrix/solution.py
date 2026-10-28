# Cell 1
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    m = len(matrix)
    n = len(matrix[0])

    result = []

    for x in range(m):
        row = []
        for y in range(n):
            row.append(matrix[x][y] * scalar)
        result.append(row)
        
    return result