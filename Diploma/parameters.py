#Мужчины: BMR = 88.36 + (13.4 x вес, кг) + (4.8 х рост, см) — (5.7 х возраст, лет)
#Женщины: BMR = 447.6 + (9.2 x вес, кг) + (3.1 х рост, cм) — (4.3 х возраст, лет)

import math

gender = print(input('введите пол'))
w = print(int(input('введите вес')))
h = print(int(input('введите рост')))
a = print(int(input('введите возраст')))

if gender == 'male':
    print(lambda w,h,a: 88 + w * 14 + h * 5 - 6 * a)
elif gender == 'female':
    print(lambda w,h,a: 447 + w * 9 + h * 3 - 4 * a)