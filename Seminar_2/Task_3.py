# Задача 3. Напишите программу, в которой пользователь будет задавать 2 строки, а программа определять кол-во вхождений одной строки в другую.

string1 = input('Введите строку 1: ')
string2 = input('Введите строку 2: ')
print(string1.count(string2) or string2.count(string1))
