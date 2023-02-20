# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.

a = int(input('Введите число: '))

with open('d:\Python\Python_Start\Seminar_3\Task_1.txt', 'w', encoding='utf-8') as file:
    for _ in range(a):
        file.write(input() + '\n')

c = input('Введите искомое: ')

with open('d:\Python\Python_Start\Seminar_3\Task_1.txt', 'r', encoding='utf-8') as file:
    strings = file.read().splitlines()
    count = 0
    b = False
    for line in strings:
        count += 1
        if c in line:
            b = True
            print(f'Да, в строке {count}')
    if not b:
        print('Нет')
