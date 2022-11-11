# todo: Реализовать класс "Игровой персонаж".
# Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, Раса, Тип персонажа, урон.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом

#недоделано

from random import randint as rand
class Person:
    def __init__(self, name, ovo, species, type):
        self.id = rand(0, 100)
        self.name = name
        self.ovo = ovo
        self.max_h = rand(5, 20)* ovo
        self.h = self.max_h
        self.loss = rand(1, 4) * ovo
        self.species = species
        self.type = type

    def dead(self, loss):
        self.h -= loss

    def __del__(self):
        if self.h <= 0:
            self.help = 0
            print(f'{self.name} game over')
    def __sub__(self, other):
        print(f"{self.name} deals {self.loss} damage by {other.name}")
        other.dead(self.loss)
        if other.h > 0:
            print(f"У {other.name} keep {other.h} health from {other.max_h}")
            print(f"{other.name} deals {other.loss} damage by {self.name}")
            self.dead(other.loss)
            print(f"У {self.name} keep {self.h} health from {self.max_h}")

    def __repr__(self):
        return f'''{self.name} {self.ovo}''' #уровня

class Battle:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        print(f" battle between {player_1.__repr__()} vs {player_2.__repr__()}")

        def battle(self):
            while self.player_1.h > 0 and self.player_2.h > 0:
                player_1 - player_2


player_1 = Person('ivan', 1, 'europoid', 'killer')
player_2 = Person('vova', 1, 'europoid', 'tsar')

fight = Battle(player_1, player_2)
fight.battle()