#   Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#   Пример:
#   - 45 -> 101101
#   - 3 -> 11
#   - 2 -> 10

first_number = int(input('Введите число: '))
a = str(first_number)

second_number = ''

while first_number > 0:
    second_number = str(first_number % 2) + second_number
    first_number = first_number // 2

print(f'Десятичное число {a} стало двоичным: {second_number}')
