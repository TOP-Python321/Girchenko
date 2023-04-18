num_one = float(input('Введите первое число: '))
num_two = float(input('Введите второе число: '))
num_three = float(input('Введите третье число: '))
sum_num = 0

if num_one > 0:
    sum_num += num_one

if num_two > 0:
    sum_num += num_two
    
if num_three > 0:
    sum_num += num_three
    
print(sum_num)

# Введите первое число: 10
# Введите второе число: -9
# Введите третье число: 8.765
# 18.765