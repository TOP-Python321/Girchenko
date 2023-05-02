list_num = [ ]

while True:
    num = int(input('Введите целое число: '))
    if num % 7 != 0:
        list_num.reverse()
        print(f'{list_num}')
        break
    list_num.append(num)
    

# Введите целое число: 7
# Введите целое число: 7
# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 13
# [21, 14, 7, 7]