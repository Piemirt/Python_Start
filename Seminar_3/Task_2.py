# Напишите функцию, которая принимает номер месяца и язык (русский или английский), а возвращает его название.
#   Пример:         Ввод:
#                       print(month_name(3, 'en'))
#                       march
#                   Ввод:
#                       print(month_name(3, 'ru'))
#                       март

def Month(x, y):
    listEn = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    listRu = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

    if 0 < x < 13:
        if y == 'en':
            return listEn[x - 1]
        if y == 'ru':
            return listRu[x - 1]
    else:
        print('Такого месяца нет')


print(Month(14, 'en'))
