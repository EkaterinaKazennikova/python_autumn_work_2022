# todo:Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07

# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

from random import randint as rand
from time import time, strftime

def decor_stat(func):
    def wrapper(*a, **kwargs):
        f = open("debug.log", "x")
        wrapper.count += 1
        res = func(*args, **kwargs)
        f.write(
            "{0} Была вызвана: {1} раз. Последний вызов {2}.\n".format(func.__name__, wrapper.count, strftime("%c")))
        return res

    wrapper.count = 0
    return wrapper
@decor_stat
def field_gen(rows=5, kolumns=5):
    res = [[rand(0, 1) for _ in range(kolumns)] for _ in range(rows)]
    return res
@decor_stat
def count_ship(field):
    digit = [digits for row in field for digits in row]
    return digit.count(1)




