#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.


from itertools import combinations
num = [1, 2, 3, 4, 5, 6]
dice1 = combinations(num, 2)
dice2 = combinations(num, 2)
for i in list(dice1):
    for j in list(dice2):
	    print ('сумма', sum(i + j), 'комбинация пар: кость 1',[i], 'кость2', [j])


