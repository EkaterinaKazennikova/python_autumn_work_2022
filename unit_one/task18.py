#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.

не сделано
import random
#def combination():
    #rolls = []
    #for i in range(1, 36):
        #total = random.randint(1, 6) + random.randint(1, 6)
        #rolls.append(total)
    #return rolls
#summ = combination()
count = 36
def combination():
    while count < 36:
        result1 = random.randint(1, 6)
        result2 = random.randint(1, 6)
        return (result1, result2)
total = combination()
print((f"1 кость = total[0] | 2 кость = total[1]"), "сумма", total[0] + total[1])

    #result1 = random.randint(1, 6)
    #result2 = random.randint(1, 6)
    #return (result1, result2)
    #total = 0
    #for i in range(36):
        #total += random.randint(1, 6)
        #return(total)
#res1 = result1
#res2 = result2
#total = combination()
#print((f"1 кость = {total[0]} | 2 кость = {total[1]}"), "сумма", total)


#import random
#def combination():
    #result1 = random.randint(1, 6)
    #result2 = random.randint(1, 6)
    #return (result1, result2)
#total = combination()
#print((f"1 кость = {total[0]} | 2 кость = {total[1]}"), "сумма", total[0] + total[1])