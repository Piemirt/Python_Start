# Напишите программу, которая принимает на вход число N и выдаёт набор произведений чисел от 1 до N.
# Пример:           - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
product = 1
some_list = []
for i in range(1, n + 1):
    product = product * i
    some_list.append(product)
print(some_list)
