import sys
import psycopg2
from configparser import ConfigParser

def config(filename='databese.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

params = config()

conn = psycopg2.connect(
    host="localhost",
    database="task",
    user="postgres",
    password="4511")

print(conn)

cur = conn.cursor()

id_student=input('ведите id студента')

SQL_GET_TASK_BY_STUDENT = f"""SELECT s.surname , t."name"n , t.condition
                                 FROM students s , students_task st , task t
                              WHERE s.id = st.id_students
                                 AND st.id_task = t.id
                                 AND s.id = {id_student}"""

cur.execute(SQL_GET_TASK_BY_STUDENT)

records = cur.fetchall()
for row in records:
    print(row)


conn(close)

