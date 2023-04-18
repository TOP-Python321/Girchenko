year = input('Введите год: ')

if year.isdecimal():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Да')
    else:
        print('Нет')

else:
    print('Вводите число!')

# 904
# Да