#todo: Сделать рефакторинг кода задачи task1  22 лекции .
#  1. Реализовать из класса DB синглтон. Экземляр класса(подключение) должно быть единственным.
#  2. Реализовать  фабрику которая создает модели различных производителей


import psycopg2
class DB:
    __conn = None
    #'''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     #(атрибуты доступа к БД) . Метод возвращает соединение.'''
    def __init__(self):
    # В констукторе инициализируем атрибуты доступа к БД
        if DB.__conn is None:
            DB.__conn = psycopg2.connect(
            host = 'localhost',
            database = 'tour_agency',
            user = 'postgres',
            password = '4511')

        else:
            raise Exception
        pass
    @staticmethod
    def get_connect():
        # Метод возвращает соединение к БД
        if not DB.__conn:
            DB()
        return DB.__conn
        pass

base = DB()
print(base.get_connect())
print(base)
base_err = DB()


import psycopg2
from abc import ABC, abstractmethod


class AbsClass(ABC):
    @abstractmethod
    def get_connect(self):
        pass


class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     (атрибуты доступа к БД) . Метод возвращает соединение.'''
    __conn = None

    def __init__(self):
        # В конструкторе инициализируем атрибуты доступа к БД
        if DB.__conn is None:
            DB.__conn = psycopg2.connect(
                host='localhost',
                database='tour_agency',
                user='postgres',
                password='4511')

        else:
            raise Exception("We can not create another class")

    @staticmethod
    def get_connect():
        # Метод возвращает соединение к БД
        if not DB.__conn:
            DB()
        return DB.__conn


connection = DB()
print(connection.get_connect())
print(connection)
connection_1 = DB()

# 3. Реализовать для класса Car абстрактный класс который содержит
# aбстрактные методы sold, discount

from abs import ABS, abstractmethod


from abc import ABC, abstractmethod
class AbsCar(ABC):
    @abstractmethod
    def sold(self):
        pass
    @abstractmethod
    def discount(self):
        pass

class Car(AbsCar):
    def init(self, brand, model):
        self.brand = brand
        self.model = model
        """Инициализируйте атрибуты brand и model"""
    @classmethod
    def make_lada(cls):
        return cls('Z', 'Урал')
        "реализуйте метод для создания  автомобиля Lada"

    @classmethod
    def make_mercedes(cls):
        "реализуйте метод для создания  автомобиля Mercedes"
        return cls('ZZ', 'Урал1')

    @classmethod
    def make_toyota(cls):
        return cls('ZZZ', 'Урал2')
        "реализуйте метод для создания создания Toyota"

    def repr(self):
        return (f"brand {self.brand}")
        "Реализуйте логику дандера"
    def sold(self):
        """Автомобиль продан"""
        print(f"Автомобиль {self.brand} {self.model} продан ")

    def discount(self):
        """Скидка на автомобиль"""
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

print(Car.make_toyota())
element = Car.make_toyota()
element.sold()






