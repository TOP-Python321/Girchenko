list_num = []

while True:
    num = int(input('Введите целое число: '))
    # КОММЕНТАРИЙ: в более сложных циклах тело цикла будет более длинным и сложным для восприятия, поэтому лучшей практикой будет вывести действия, выполняемые по завершении цикла, за пределы тела цикла
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


# ИТОГ: отлично — 3/3
