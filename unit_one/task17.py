#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
prices.values()
def compute_bill(prices):
    return prices.values()
print(sum(prices.values()))