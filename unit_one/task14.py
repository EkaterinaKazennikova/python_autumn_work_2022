#todo: Дан массив размера N.Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
#import ast

array = [2, 2, 5, 22, 5, 5, 6, 7, 31, 22, 5, 2, 2]

number_indexes = {}
index = 0
for number in array:
    number_indexes[number] = []

for number in array:
    number_indexes[number].append(index)
    index += 1

index_distances = {}
distances = {}
for number, indexes in number_indexes.items():
    distances[number] = {}
    for index in range(len(indexes) - 1):
        distance = indexes[index+1] - indexes[index]
        distances[number][indexes[index+1], indexes[index]] = distance

print(array)
print(number_indexes)
print(distances)


#Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
#Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
#Для числа 17 нет минимального растояния т.к элемент в массиве один.
