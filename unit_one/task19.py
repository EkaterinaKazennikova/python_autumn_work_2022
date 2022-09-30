#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm


#Каждое значение из списка должно находится на отдельной строке.

import csv
FILE = "algoritm.csv"
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
id = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
f = open("algoritm.csv", "wt", encoding='utf-8', newline="")
writer = csv.writer(f)
writer.writerows(zip(id, algoritm))




