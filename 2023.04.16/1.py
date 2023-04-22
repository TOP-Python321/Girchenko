num_one = input('Введите первое число: ')
num_two = input('Введите второе число: ')
num_three = input('Введите третье число: ')
sum_num = 0

# ИСПРАВИТЬ здесь и далее: проверка isdecimal() избыточна, потому что будет провалена каждый раз, когда в соответствующей переменной оказывается строковое представление вещественного числа
# КОММЕНТАРИЙ: первый коммит был лучше
# СДЕЛАТЬ: revert commit для коммита с первыми изменениями в 1.py и затем merge (необходимо будет вручную разрешить конфликт — заодно потренируетесь):
#  https://git-scm.com/docs/git-revert
if num_one.isdecimal():
    sum_num += int(num_one)
elif float(num_one) > 0:
    sum_num += float(num_one)

if num_two.isdecimal():
    sum_num += int(num_two)
elif float(num_two) > 0:
    sum_num += float(num_two)

if num_three.isdecimal():
    sum_num += int(num_three)
elif float(num_three) > 0:
    sum_num += float(num_three)

print(sum_num)


# Введите первое число: 10
# Введите второе число: -9
# Введите третье число: 8.765
# 18.765


# ИТОГ: хорошо — 2/3
