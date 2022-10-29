# todo:Прочитать главу 6 (стр. 119) книги SQL Полное Руководство.
#Написать на модели данный ПО "Авторизации" запросы:


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="task",
    user="postgres",
    password="4511")

print(conn)

cur = conn.cursor()

#1. Простой запрос
#список студентов,  и их задачи

SQL = f"""SELECT s.surname , t."name"n , t.condition
              FROM students s , students_task st , task t
           WHERE s.id = st.id_students
              AND st.id_task = t.id"""
                            

cur.execute(SQL)

print(conn)

#2. Вычисляемый столбец
#студенты решившие задачу 1


SQL_TASK = f"""SELECT s.surname , t.name 
                   from students s , students_task st , task t
               where s.id = st.id_students
                   and t.id = st.id_task
	               and t.id = 1"""
cur.execute(SQL_TASK)

print(conn)

#3. Выборка всех столбцов

SQL_ALL = f"""SELECT s.surname , t.name , t.condition
                 from students s , students_task st , task t
             where s.id = st.id_students
                 and t.id = st.id_task"""

cur.execute(SQL_ALL)

print(conn)

#4. Повторяющиеся строки (DISTINCT)

SQL_DISTINCT = f"""SELECT DISTINCT s.surname
                    from students s"""

cur.execute(SQL_DISTINCT)

print(conn)

#5. Отбор строк (WHERE) с оператором ставнения

SQL_WHERE = f"""SELECT id_students , id_task
                 from students_task
                where id_task <> 1"""

cur.execute(SQL_WHERE)

print(conn)

# 6. Выборка одной строки


SQL_LINE = f"""SELECT name
                from task
               where id = 1"""

cur.execute(SQL_LINE)

print(conn)

# 7. Проверка на принадлежность диапазону (BETWEEN)

SQL_BETWEEN = f"""SELECT ID , name , condition
                     from task
                   where id BETWEEN 2 AND 4"""


cur.execute(SQL_BETWEEN)

print(conn)

# 8. Проверка наличия во множестве (IN)

SQL_IN = f"""SELECT ID , name , condition
               from task
              where ID IN (2 , 4)"""

cur.execute(SQL_IN)

print(conn)

# 9. Проверка на соответствие шаблону (LIKE)
SQL_LIKE = f"""SELECT id, surname
                  FROM students
                    WHERE surname LIKE 'stud%'"""

cur.execute(SQL_LIKE)

records = cur.fetchall()

print(conn)

#10. Проверка на равенство NULL (is NULL)
SQL_NULL = f"""SELECT id
                 from task
            where ID IS NOT NULL"""
cur.execute(SQL_NULL)

print(conn)

#11. Сопоставление условия отбора (AND, OR и NOT)

SQL_OR = f"""SELECT surname
               from students
              where id < 9
                or id < 3"""
cur.execute(SQL_OR)

print(conn)

#12. Сортировка результатов запроса (ORDER ВУ)

SQL_ORDER_BY = f"""SELECT id_students , id_task
	                  FROM students_task
	                order by id_task"""

cur.execute(SQL_ORDER_BY)

print(conn)

#13. Объединение результов нескольких запросов (UNION)

SQL_UNION = f"""SELECT surname
                  from students
                where id > 3
                union
                select name
                   from task
                where id >5"""
cur.execute(SQL_UNION)

print(conn)

