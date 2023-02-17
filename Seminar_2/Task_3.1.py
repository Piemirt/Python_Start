string1 = input('Введите строку 1: ')
string2 = input('Введите строку 2: ')
c = 0
for i in range(len(string1) - len(string2) + 1):
    if string1[i:i+len(string2)] == string2:
        c += 1
print(c)
