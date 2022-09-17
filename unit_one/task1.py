age = "23"
age = int(age)
print(type(int(age)))

foo = "23abc"
print(type(int(foo)))

age = "123abc"
print(bool(age))

flag = 1
print(bool(flag))

str_one = "Privet"
bool_value = bool(str_one)
print(bool_value)
str_two = ""
bool_value = bool(str_two)
print(bool_value)

value1 = 0
print(bool(value1))
value2 = 1
print(bool(value2))


age = 36.6
temperature = float(25)
age, temperature = temperature, age
print(int(age))
print(temperature)
