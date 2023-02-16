# Задача 2. Для натурального n создать словарь "индекс-значение", состоящий из элементов последовательности 3n+1
# Пример:           для n = 6: {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

n = int(input('Введите натуральное число: '))
d = dict()
for i in range(1, n + 1):
    d[i] = 3 * i + 1
for k, v in d.items():
    print(f'{k}:{v}', end=', ')
