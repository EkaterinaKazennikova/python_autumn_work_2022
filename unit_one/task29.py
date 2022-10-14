#todo. Транспонирование матрицы, transpose(matrix)
# level:hight
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.

matrix = [[1, 2, 3], [4, 5, 6]]
result = [[0, 0, 0], [0, 0, 0]]
def transpose(matrix):
    result = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    return result
print(transpose(matrix))

