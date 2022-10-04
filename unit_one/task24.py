#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. Не числа не изменять.

#Пример.
#Input	                            #Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

#import string, re
#num = input()
#num_index = list(num)
#letters = string.ascii_letters
#for num.index() in enumerate(letters.index()):
#    char = f'{chr(num + 97)}'
#print(char)

import string
alphabet = string.ascii_uppercase
numbers = input().split()
letters = [alphabet[int(number)-1] for number in numbers]
print(letters, sep='')