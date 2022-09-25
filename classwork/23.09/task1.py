# todo: База данных пользователя.
# Задан массив объектов пользователя


db = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
input_age = input(print('ведите возраст:'))
result = []
input_name = input(print('ведите возраст:'))
input_group = input(print('введите группу:'))
for user in db:
    if user['age'] > input_age:
    result.append(user)
for user in db:
    if user('login') [0] == input_name:
    result.append(user)
for user in db:
    if user['group'] == input_group:
    db.sort(user)
    result.append(user)
print(login, age, group)

Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
1. По возрасту
2. По первой букве
3. По группе

тип сортировки: 1

#Затем сообщение для ввода
Ввидите критерии поиска: 16

Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"




