first_cell = input('Введите значение первой клетки: ')
second_cell = input('Введите значение второй клетки: ')

color_first_cell = (ord(first_cell[0]) + int(first_cell[1])) % 2 
color_second_cell = (ord(second_cell[0]) + int(second_cell[1])) % 2

if color_first_cell == color_second_cell:
    print('Да')
else:
    print('Нет')


# Введите значение первой клетки: a2
# Введите значение второй клетки: h7
# Да
