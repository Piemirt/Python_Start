# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt, в одной строке одно число.

import random
n = int(input('Введите число N: '))
mult = 1
someList = [random.randint(-n, n) for _ in range(n)]
print(someList)

with open('d:\Python\Python_Start\Seminar_2\HW_Task_4.txt', 'w+', encoding='utf-8') as file:
    count = random.randint(1, n)
    for _ in range(count):
        file.write(f'{random.randint(0, n - 1)}' + '\n')
    file.seek(0, 0)
    indexList = file.read().splitlines()
    for i in indexList:
        mult = mult * someList[int(i)]
print(mult)

# Отдельно чтение и запись --->>>
# with open('file.txt', 'w', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')

# with open('file.txt', 'r', encoding='utf-8') as file:
#     indexList = file.read().splitlines()
#     for i in indexList:
#         mult = mult * someList[int(i)]
# print(mult)
