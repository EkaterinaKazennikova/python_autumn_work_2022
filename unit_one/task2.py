#Преобразуйте переменную age и foo в число 
age = "23"
print(int(age))
print(type(age))

foo = "23abc"                  #? нельзя преобразовать строку с числом и буквами
print(type(int(foo)))

#Преобразуйте переменную age в Boolean
age = 123abc                   #? должны быть кавычки?
print(bool(age))

#Преобразуйте переменную flag в Boolean
flag = 1
print(bool(flag))

#Преобразуйте значение  в Boolean
str_one = "Privet"
bool_value = bool(str_one)
print(bool_value)
str_two = ""
bool_value = bool(str_two)
print(bool_value)

#Преобразуйте значение 0 и 1  в Boolean
value1 = 0
print(bool(value1))
value2 = 1
print(bool(value2))
