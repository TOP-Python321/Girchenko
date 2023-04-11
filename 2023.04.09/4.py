number = int(input('Введите трехзначное число: '))
one_num = number  // 100
two_num = number // 10 % 10
three_num = number % 10
print(f'''Сумма цифр = {one_num + two_num + three_num}
Произведение цифр = {one_num * two_num * three_num}''')

# Сумма цифр = 9
# Произведение цифр = 27