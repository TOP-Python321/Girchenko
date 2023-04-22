first_cell = input('Введите значение первой клетки: ')
second_cell = input('Введите значение второй клетки: ')

a = ord(first_cell[0]) - ord(second_cell[0])
b = ord(first_cell[1]) - ord(second_cell[1])

if (a >= -1 and a <= 1) and (b >= -1 and b <= 1):
    print('Да')
else:
    print('Нет')


# Введите значение первой клетки: d2
# Введите значение второй клетки: e3
# Да

# Введите значение первой клетки: d2
# Введите значение второй клетки: d4
# Нет
