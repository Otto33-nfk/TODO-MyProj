import re

# Задание 1: Среднее соседей
def neighbor_average(matrix):
    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            total, count = 0, 0
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    total += matrix[ni][nj]
                    count += 1
            new_matrix[i][j] = total / count if count else 0
    return new_matrix

# Задание 2: Нормализация текста
def normalize_text(text):
    text = re.sub(r'\s+', ' ', text.strip())
    text = re.sub(r'([!?.])\1+', r'\1', text)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    normalized = []
    for sent in sentences:
        if sent:
            sent = sent[0].upper() + sent[1:].lower()
        normalized.append(sent)
    return ' '.join(normalized)

# Примеры
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(neighbor_average(matrix))

example = "привет!!!  КАК дела??  я  нормально."
print(normalize_text(example))  # "Привет! Как дела? Я нормально."
