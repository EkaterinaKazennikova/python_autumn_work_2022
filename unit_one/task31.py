# todo:Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07

# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime
import time
#недоделано

from datetime import  datetime

start = datetime.now()
def decor_stat(func):
    def wrapper(*a, **kwargs):
        wrapper.count += 1
        return func(*a, **kwargs)
        #count_calls = 0
        #start_time = time.perf_counter_ns()
        #end_time = start_time + time.perf_counter_ns()
        #result = func()
        #print(datetime.datetime.now(), end_time)
        #return result

         #if i in range():
         #  count_calls += 1
         #retern counnt_calls
    wrapper.count = 0
    return wrapper()

def stat():
    render = 0
    for i in range(1000):
        render += 1

    return render
wp = decor_stat(stat)
print(wp())


