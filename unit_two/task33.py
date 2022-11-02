# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:

#  1. пользователь ввел некорректное значение в заданном диапазоне

user = int(input('введите значение от 0 до 10'))

class TrueVallue(Exception):

    def __init__(self):
        super().__init__()

try:
    if 10 < user or user < 0:
        raise TrueVallue()
except TrueVallue as e:
    print(e, 'значение должно быть в диапазоне от 0 до 10')
else:
    print('значение корректно')
finally:
    print()

 2. результат запроса вернул 0 строк

import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="task",
        user="postgres",
        password="4511")

cur = conn.cursor()
class EmptyString(Exception):

     def __init__(self):
         super().__init__()
try:
   SQL_LINE = f"""SELECT name
                from task
               where id = 8"""
   cur.execute(SQL_LINE)

   records = cur.fetchall()
   if not records:
       raise EmptyString()

except EmptyString as e:
     print(e, 'имени с заданным id не существует')
else:
    for row in records:
        print(row)

finally:
     print()


 3. Произошел разрыв соединения с сервером

import psycopg2
class ConnectionError(Exception):

    def __init__(self):
        super().__init__()
try:
    conn = psycopg2.connect(
        host="localhost",
        database="task",
        user="postgres",
        password="4511")
    raise ConnectionError()
except ConnectionError as e:
    print(e, 'произошел разрыв соединения с сервером')
else:
    print(conn, 'соединение установлено')
finally:
    print()