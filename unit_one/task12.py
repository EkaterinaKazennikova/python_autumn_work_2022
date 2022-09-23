#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


m = float(input())
def unit(num):
    match num:
        case 1:
            print(m, 'кг')
        case 2:
            print(m / 1000000, 'кг')
        case 3:
            print(m / 1000, 'кг')
        case 4:
            print(m * 1000, 'кг')
        case 5:
            print(m * 100, 'кг')

# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
>4

#Введите  массу тела
>1

Ответ: 1000 кг

