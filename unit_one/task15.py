# Написать игру "Поле чудес"
import random
from typing import List
def pole_chudes():
    answers = ["оператор", "функция", "класс"]
    questions = [
        "Наименьшая автономная часть языка программирования",
        "Выделенный блок кода, выполняющий определенную операцию",
        "модель для создания объектов определённого типа, описывающая их структуру "
    ]

    index = random.randrange(0, len(answers))

    question = questions[index]
    answer = answers[index]

    print('Вопрос:', question)
    print('▮'*len(answer))

    max_penalty_points = 10
    penalty_points = 0
    guessed_letters = []
    while penalty_points < max_penalty_points:
        print('Введите букву: ')
        try_letter = str(input())

        if try_letter in answer:
            print('Есть такая буква!')
            guessed_letters.append(try_letter)
        else:
            penalty_points += 1
            print('нет такой буквы, штрафных баллов: ', penalty_points)


def mask_word(word: str, guessed_letters: List[str]):
    masked_word = word
    for letter in word:
        masked_word.replace(letter, '▮')
import random
words = ["оператор", "конструкция", "объект"]
desc = ["Это слово обозначает наименьшую автономную часть языка программирования", "..", ".."]
index = random.randrange(0, len(desc))
print('вопрос:', question[index])
answer = answer[index]
print('|'*len(question))
print('введите букву')
answer_user= input()
start_ansewer = []
scores = 0
for i in range(len(answer)) and scores <= 10:
    star_answer.append("*")
    print('ведите следующую букву')
else:
    scores +=1
    print('нет такой буквы, у вас осталось', (10- score), 'попыток')

Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
либо победы.

Пример вывода:

"Это слово обозначает наименьшую автономную часть языка программирования"

▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

Введите букву: O

O  ▒  ▒  ▒  ▒  ▒  O  ▒


Введите букву: Я

Нет такой буквы.
У вас осталось 9 попыток !
Введите букву:
