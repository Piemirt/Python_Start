# Обход всех цифр числа и все операции, что можно с ним сделать, с помощью цикла while

n = int(input('Введи число: '))

quantity = 0
quantity_even = 0
quantity_odd = 0
sum = 0
product = 1
max_digit = 0
min_digit = 9

while n > 0:
    last = n % 10
    quantity += 1
    if last % 2 == 0:
        quantity_even += 1
    if last % 2 == 1:
        quantity_odd += 1
    sum += last
    product *= last
    if last > max_digit:
        max_digit = last
    if last < min_digit:
        min_digit = last
    n //= 10

print('Всего цифр в числе: ', quantity)
print('Всего чётных цифр в числе: ', quantity_even)
print('Всего нечётных цифр в числе: ', quantity_odd)
print('Сумма всех цифр в числе: ', sum)
print('Произведение всех цифр в числе: ', product)
print('Максимальная цифра в числе: ', max_digit)
print('Минимальная цифра в числе: ', min_digit)
