# Напишите программу, которая определит позицию второго вхождения строки в списке, либо сообщит, что её нет.

some_list = ['asd', 'qwe', 'zxc', 'rty', 'fgh', 'asd', 'zxcasd']

a = input('Введите искомое: ')

count_1 = 0
count_2 = 0
b = False
for line in some_list:
    count_1 += 1
    if a == line:
        count_2 += 1

        if count_2 == 2:
            b = True
            print(f'{count_1} ')
            break

if not b:
    print('Нет совпадений')
