# Задание 1: Элементы между позициями
def elements_between(matrix, pos1, pos2):
    rows, cols = len(matrix), len(matrix[0])
    def to_linear(r, c):
        return r * cols + c

    idx1 = to_linear(*pos1)
    idx2 = to_linear(*pos2)

    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)

    result = []
    for i in range(rows):
        for j in range(cols):
            linear = to_linear(i, j)
            if start <= linear < end:
                result.append(matrix[i][j])
    return result

# Задание 2: Локальные максимумы
def local_maxima(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for i in range(rows):
        for j in range(cols):
            val = matrix[i][j]
            is_max = True
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] >= val:
                        is_max = False
                        break
            if is_max:
                result.append(val)
    return result

# Примеры!!!
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(elements_between(matrix, (0, 1), (2, 0)))  # [3, 4, 5, 6]

matrix2 = [[1, 3, 2], [4, 9, 5], [7, 6, 8]]
print(local_maxima(matrix2))  # [9, 8]
