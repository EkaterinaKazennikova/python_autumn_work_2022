# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.

#недоделано
import random

game_field = []
row_one = [(lambda i : random.randint(0, 1))(i) for i in range(0,5)]
row_two = [(lambda i : random.randint(0, 1))(i) for i in range(0,5)]
row_three = [(lambda i : random.randint(0, 1))(i) for i in range(0,5)]
row_four = [(lambda i : random.randint(0, 1))(i) for i in range(0,5)]
row_five = [(lambda i : random.randint(0, 1))(i) for i in range(0,5)]
game_field.append(row_one)
game_field.append(row_two)
game_field.append(row_three)
game_field.append(row_four)
game_field.append(row_five)

#print((row_one, '\n', row_two, '\n', row_three, '\n', row_four,'\n', row_five) * len(game_field))
print('▮'* len(game_field))

print("Начнем игру в Морской бой!, введите координаты")

user_row = int(input())
user_col = int(input())
ship = game_field.index(1)


if user_row == ship and user_col == ship:
    print("Ты потопил корабль!, введите следующие координаты")
    user_row = int(input())
    user_col = int(input())

elif (user_row < 0 or user_row > 5) or (user_col < 0 or user_col > 5):
    print("Таких координат нет")

elif:
    print("Эти координаты вы уже называли.")

else:
    print("Мимо!")
    game_field[user_row][user_col] = "X"



from random import randint as rdi
game_field = []
LIVE = 1
import sys

def init():
    matrix()

def menu():
    out = f"1. Новая игра\n2. Продолжить игру\n3. Сохранить игру\n4.Загрузить игру"
    print(out)
    num = int(input("Раздел:"))
    if num == 1:
        init()
        game()
    else:
        sys.exit(0)

def get_row(number_of_count = 5):
    row = []
    func = lambda: rdi(0, 1)
    for i in range(number_of_count):
        row.append(func)
    result = []
    for l in row:
        result.append(l())
    return result

def matrix(amount_row = 5):
    global game_field
    for i in range(amount_row):
        game_field.append(get_row())
    return game_field

def get_position():
    long = input("Введите координату x:")
    lot = input("Введите координату y:")
    return (int(long),int(lot))

def minus_live():
    global LIVE
    LIVE -= 1

def game():
    global game_field

    while LIVE:
        i, j = get_position()
        if game_field[i][j] == 1:
            game_field[i][j]  = -1
            print("Попал")
        else:
            minus_live()
    else:
        print("Ваша песенка спета!")




#menu()
keys = ["name", "age"]
values = ["Peter", 12]
lst = [{k: !} for k in keys for _ in values]
print(lst)

i_val
str_name
ft_pi


#i = 0  # вхождение в первый массив
#j = 3  # вхождение в 4-ый элемент текущего массива
# доступ к элементам двухмерного массива
#print(game_field[i][j])