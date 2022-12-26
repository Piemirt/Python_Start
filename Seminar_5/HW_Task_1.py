#   Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")
find_txt = "абв"
list = [i for i in text.split() if find_txt not in i]
print(f'Результат: {" ".join(list)}')
