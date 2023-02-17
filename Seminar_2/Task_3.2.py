# Задача 3. Напишите программу, в которой пользователь будет задавать 2 строки, а программа определять кол-во вхождений одной строки в другую.

string1 = input('Введите строку 1: ')
string2 = input('Введите строку 2: ')
count = 0
index = 0
while index < len(string1):
    if string1[index: index + len(string2)] == string2:
        count += 1
        index += len(string2)
    else:
        index += 1
print(count)
