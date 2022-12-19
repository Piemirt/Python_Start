#   Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#   Пример:
#   - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))

right_list = []
n1 = 0
n2 = 1

for i in range(n + 1):
    right_list.append(n1)
    x = n1 + n2
    n1 = n2
    n2 = x

left_list = []
for i in range(len(right_list) - 1, 0, -1):
    left_list.append(right_list[i] * (-1) ** (i + 1))

print(left_list + right_list)
