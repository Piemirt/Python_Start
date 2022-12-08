#  Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#  Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

list = []
for i in range(5):
    list.append(int(input(f"Введите число {i+1}: ")))
print(list)
max = list[0]
for i in list:
    if max < i:
        max = i
print(f"Максимальное число: {max}")
