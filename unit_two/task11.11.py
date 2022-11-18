# 1. Поймите для чего служит данный паттерн
# 2. Ознакомьтесь со схемой паттерна в графической натации OMT
# 3. Установите по натации взаимодействие классов, объектов и поведения
# 4. Сравните натацию с кодом представленным в этом листинге
# 5. Проанализируйте работу кода
# 6. Переименуйте систему классов согласно контексту задачи
#
# Задача:
# Создайте на базе кода решение которое конструирует объект состоящий из разных частей:
# Пример:
# Объект компьютер состоит из устройств:
# 1. Процессора
# 2. Оперативной памяти
# 3. Материнской платы
# 4. Жесткого диска

#Для каждого компьютера может быть различный тип устройств.

import abc

class Director:

    def __init__(self):
        self._builder = None


    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_processor()
        self._builder._build_part_ram()
        self._builder._build_part_mainboard()
        self._builder._build_part_harddrive()

        return self._builder.buld()


class Builder(metaclass=abc.ABCMeta):

    def __init__(self):
        self.product = Product1()

    def __init__(self):
        self.product = Product2()

    @abc.abstractmethod
    def _build_part_processor(self):
        pass

    @abc.abstractmethod
    def _build_part_ram(self):
        pass

    @abc.abstractmethod
    def _build_part_mainboard(self):
        pass

    @abc.abstractmethod
    def _build_part_harddrive(self):
        pass


class ConcreteBuilder(Builder):

    def _build_part_processor(self):
        self.product.processor = "Intel 7"
        self.product.processor = 'AMD'
        return self

    def _build_part_ram(self):
        self.product.ram = "DIMM"
        self.product.ram = 'DDR'
        return self

    def _build_part_mainboard(self):
        self.product.mainboard = "ATX"
        self.product.mainboard = 'MINI - ITX'
        return self

    def _build_part_harddrive(self):
        self.product.harddrive = "SSD"
        self.product.harddrive = "HDD"
        return self

    def buld(self):
        return self.product

class Product1:

    def __init__(self):
        self.processor = None
        self.ram = None
        self.mainboard = None
        self.harddrive = None

    def __repr__(self):
        return (f"Для того, чтобы произвести компьютер необходимо произвести {self.processor} {self.ram} {self.mainboard} {self.harddrive}")

class Product2:

    def __init__(self):
        self.processor = None
        self.ram = None
        self.mainboard = None
        self.harddrive = None

    def __repr__(self):
        return (f"Для того, чтобы произвести компьютер необходимо произвести {self.processor} {self.ram} {self.mainboard} {self.harddrive}")


def main():
    print('Процесс производства компьютера:')
    concrete_builder = ConcreteBuilder()
    director = Director()
    product = director.construct(concrete_builder)
    product = concrete_builder.product
    print(product)

if __name__ == "__main__":
    main()
