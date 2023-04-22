num_one = input('Введите первое число: ')
num_two = input('Введите второе число: ')
num_three = input('Введите третье число: ')
sum_num = 0

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
