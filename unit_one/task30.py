#todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

matrix = [[1, 2, 3], [4, 5, 6]]
def msum(matrix):
    summed = [sum(i) for i in matrix]
    return summed
print(sum(msum(matrix)))




