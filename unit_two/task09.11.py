#todo:
# 1. Задокументировать все классы и методы для дендера __doc__


class Person(object):
     instance = None
     def __new__(cls, *args, **kwargs):
         if not cls.instance:
             cls.instance = object.__new__(cls)
         return cls.instance
     def __init__(self):
         self.__name = 'Peter I'

class Person(object):
    ''' Класс Test для демонстрации '''

    def show(self):
        ''' This is Show Function DocString '''
        pass

obj_one = Person()
obj_two = Person()
print( obj_one is obj_two )


print(obj_one.__doc__)
print(obj_two.__doc__)
print(obj_one.show.__doc__)
print(obj_two.show.__doc__)

#2. Переписать Singlton на дандер __new__
import psycopg2

class DB(object):
    __conn = None

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance


    def __init__(self):
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
            if not DB.__conn:
                DB()
            return DB.__conn
            pass

new_conn = DB()
two_conn = DB()
print(new_conn is two_conn)
print(new_conn)
print(two_conn)


# 3. Ограничить атрибуты для класса Person только (age, name, phone) через __slots__

class Person(object):

    __slots__= ['age', 'name', 'phone']

    def __init__(self, age, name, phone):
        self.age = age
        self.name = name
        self.phone = phone

person = Person('30', 'peter', '9215465874')
print(person)


# 4. Создать итератор для класса Person в котором итерируем атрибуты экземпляра.
# Итерацию объекта осуществляем через цикл for


class Person(object):


     def __init__(self, name):
          self.name = name
          self.counter = 0

     def __next__(self):
         if self.counter < 5:
             self.counter += 1
         return self.name

         else:
             raise StopIteration

     def __iter__(self):
         return self

person = Person('peter')
myiter = iter(person)
for i in myiter:
    print(i)
