#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:

A = 10
B = 3
C = 7
if A <= B <= C:
    print(A, B, C)
elif A <= C <= B:
    print(A, C, B)
elif B <= A <= C:
    print(B, A, C)
elif B <= C <= A:
    print(B, C, A)
elif C <= A <= B:
    print(C, A, B)
else:
    print(C, B, A)


# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
A = 2
B = 10
C = 7
if A <= B <= C:
    print(A, B, C)
elif A <= C <= B:
    print(A, C, B)
elif B <= A <= C:
    print(B, A, C)
elif B <= C <= A:
    print(B, C, A)
elif C <= A <= B:
    print(C, A, B)
else:
    print(C, B, A)


# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10
