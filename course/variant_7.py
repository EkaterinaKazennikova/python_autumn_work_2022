#БД «Туристическое бюро»
#Описание предметной области. БД создается для информационного
#обслуживания сотрудников фирмы. Фирма оказывает услуги в туристическом
#бизнесе. Клиентам предлагаются путевки в разные страны, города. Путевки
#отличаются содержанием программы (отдых, экскурсии, туризм и т.д.), имеется
#возможность выбора путевки по цене (в зависимости от места проживания, все
#включено и т.д.). Для постоянных клиентов и детей до 12 лет имеются скидки.
#Готовые запросы:
#1. Выдавать список стран;
#2. Выдавать список городов;
#3. Покупать путевку в выбранное место с расчетом ее стоимости;
#4. Показывать весь ассортимент путевок в данное место;
#5. Выбирать путевку по содержанию, по цене и т.д.
#6. Показывать список самых популярных путевок (по месту пребывания, по
#содержанию, в целом).

import psycopg2
class ConnectionError(Exception):
    def __init__(self):
        super().__init__()
try:
    conn = psycopg2.connect(
        host="localhost",
        database="tour_agency",
        user="postgres",
        password="4511")
    raise ConnectionError()
except ConnectionError as e:
    print(e, 'произошел разрыв соединения с сервером')
else:
    print(conn, 'соединение установлено')
finally:
    print()

cur = conn.cursor()

filter_country = input('вывести список всех стран и курортов. Нажмите enter')
SQL_COUNTRY = f'''SELECT id, country, city
                FROM filter'''
cur.execute(SQL_COUNTRY)
records = cur.fetchall()
for row in records:
    print(row)

choice_country = input('введите номер выбранной страны и курорта')

SQL_ALL_CITY = f'''SELECT id, city
                FROM filter
                  WHERE  id = {choice_country}'''
cur.execute(SQL_ALL_CITY)
records = cur.fetchall()
for row in records:
    print('выбранная страна и курорт', row)

SQL_CHOICE = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
	               FROM filter f
                     WHERE  id = {choice_country}'''
cur.execute(SQL_CHOICE)
records = cur.fetchall()
for row in records:
    print('выбранная поездка', row)
    choice_customer = ()
    print('хотите купить- введите 1, хотите продолжит поиск- введите 2')
    choice_customer = input()
    choice_customer = int(choice_customer)
    if choice_customer == 1:
        print('поздравляю с выбором тура')
    else:
        print('вернуться к выбору всех доступных поездкок, нажмите enter')
        SQL_ALL_TOURS_IN_COUNTRY = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
	                                      FROM filter'''
        cur.execute(SQL_ALL_TOURS_IN_COUNTRY)
        records = cur.fetchall()
        for row in records:
            print(row)

            print('введите промежуток длительности поздки от 7 и до 14 дней')
            chose_duration1 = int(input())
            chose_duration2 = int(input())

            SQL_DURATION = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
	                             FROM filter
	                                where duration BETWEEN {chose_duration1} and {chose_duration2}'''
            cur.execute(SQL_DURATION)
            records = cur.fetchall()
            for row in records:
                print(row)

            print('введите диапазон сумму поездки от 700 до 5000 $')
            chose_price1 = int(input())
            chose_price2 = int(input())

            SQL_PRICE = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
	                           FROM filter
	                                where price BETWEEN {chose_price1} and {chose_price2}'''
            cur.execute(SQL_PRICE)
            records = cur.fetchall()
            for row in records:
                print(row)
                choice_1 = input('введите номер выбранной страны и курорта')
                SQL_FINISH = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
	                                FROM filter f
                                       WHERE  id = {choice_1} '''
                cur.execute(SQL_FINISH)
                records = cur.fetchall()
                for row in records:
                    print('выбранный тур', row)
                    choice_finish = ()
                    print('хотите купить- введите 1, хотите продолжит поиск- введите 2')
                    choice_finish = input()
                    choice_finish = int(choice_finish)
                    if choice_finish == 1:
                        print('поздравляю с выбором тура')

                    else:
                        print('вернуться к выбору всех доступных поездкок, нажмите enter')
                        SQL_ALL_TOURS_IN_COUNTRY = f'''SELECT id, country, city, duration, nutrition, hotel, included, price
                    	                                      FROM filter'''
                        cur.execute(SQL_ALL_TOURS_IN_COUNTRY)
                        records = cur.fetchall()
                        for row in records:
                            print(row)


conn.close()