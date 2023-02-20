# Реализуйте алгоритм перемешивания списка.

import random

list = []
for i in range(5):
    list.append(int(input(f'Введите число {i+1}: ')))
print(list)
random.shuffle(list)
print(f'Перемешанный список: {list}')
