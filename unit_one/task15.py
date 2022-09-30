# Написать игру "Поле чудес"
import random

answers = ["оператор", "функция", "класс"]
questions = [
        "Наименьшая автономная часть языка программирования",
        "Выделенный блок кода, выполняющий определенную операцию",
        "модель для создания объектов определённого типа, описывающая их структуру "
    ]

index = random.randrange(0, len(answers))

question = questions[index]
answer = answers[index].upper()

print('Вопрос:', question)
print('▮'*len(answer))

max_penalty_points = 10
penalty_points = 0
guessed_letters = []
while penalty_points < max_penalty_points:
    print('Введите букву: ')
    try_letter = answer = answers[index].upper()

    if try_letter in answer:
        print('Есть такая буква!')
        guessed_letters.append(try_letter)
        masked_word = answer
        for letter in answer:
            if letter not in guessed_letters:
                masked_word = masked_word.replace(letter, '▮')
        print(masked_word)
        if masked_word == answer:
            print('Угадано! У вас штрафных баллов: ', penalty_points)
            break

    else:
        penalty_points += 1
        print('нет такой буквы, штрафных баллов: ', penalty_points)
        if penalty_points == max_penalty_points:
            print('Вы проиграли!')



#Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
#words = ["оператор", "конструкция", "объект"]
#desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
#Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
#Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
#в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
#либо победы.

#Пример вывода:

#"Это слово обозначает наименьшую автономную часть языка программирования"

#▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

#Введите букву: O

#O  ▒  ▒  ▒  ▒  ▒  O  ▒


#Введите букву: Я

#Нет такой буквы.
#У вас осталось 9 попыток !
#Введите букву:
