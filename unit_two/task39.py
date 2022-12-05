# todo: Написать юнит-тест на функцию matrix.
from random import randint as rdi
import unittest

game_field = []

def get_row(number_of_count=5):
    row = []
    func = lambda: rdi(0, 1)
    for i in range(number_of_count):
        row.append(func)
    result = []
    for l in row:
        result.append(l())
    return result


def matrix(amount_row=5):
    global game_field
    for i in range(amount_row):
        game_field.append(get_row())
    return game_field

class TestMatrix(unittest.TestCase):
    def test_matrix(self):
        self.assertEqual(matrix(5), game_field)

    def test_value(self):
        self.assertRaises(ValueError, 0)


game_field = matrix()