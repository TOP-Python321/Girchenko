first_cell = input('Введите значение первой клетки: ')
second_cell = input('Введите значение второй клетки: ')

if first_cell[0] == second_cell[0] or first_cell[1] == second_cell[1]:
    print("Да")
else:
    print("Нет")
    
# Введите значение первой клетки: d2
# Введите значение второй клетки: d8
# Да

# Введите значение первой клетки: d2
# Введите значение второй клетки: e5
# Нет