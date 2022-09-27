#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.

def mask_word(word: str, guessed_letters: list[str]):
    masked_word = word
    for letter in word:
        masked_word.replace(letter, '▮')
import random
words = ["оператор", "конструкция", "объект"]
desc = [
        "Наименьшая автономная часть языка программирования",
        "Выделенный блок кода, выполняющий определенную операцию",
        "модель для создания объектов определённого типа, описывающая их структуру "
    ]
index = random.randrange(0, len(desc))
print('вопрос:', desc[index])
answer = words[index]
print('|'*len(desc))
print('введите букву')
answer_user= input()
start_answer = []
scores = 0

for i in range(len(answer)) and scores <= 10:
    star_answer.append("*")
    print('ведите следующую букву')
else:
    scores +=1
    print('нет такой буквы, у вас осталось', (10- scores), 'попыток')