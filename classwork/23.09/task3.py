#todo 3.1: Получите заданное количество N (например, 20) различных
# случайных целых чисел в диапазоне от 0 до N-1. Найдите их
# сумму.

import random
res = [random.randrange(1, 20) for i in range(20)]
print(str(res))
res = sum([random.randrange(1, 20) for i in range(20)])
print('сумма случайных чисел диапазона', str(res))

#todo 3.2:  Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф, ис-
# пользуя метод перебора с помощью нескольких операторов
# цикла for.

import random
cod = [random.randrange(1, 9) for i in range(3)]
print(str(cod))
user_cod = []
for i in cod:
    user_cod.append(i)
print(user_cod)