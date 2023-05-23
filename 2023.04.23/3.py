num = int(input('Введите число: '))
divider, sum_num = 1, 0

# СДЕЛАТЬ: этот цикл выполняет лишние итерации — подумайте, при каких значениях divider остаток от деления никогда не сможет быть равным нулю
while divider <= num:
    result = num % divider
    if result == 0:
        sum_num += divider
    divider += 1

print(sum_num)


# Введите число: 10
# 18

# Введите число: 50
# 93


# ИТОГ: доработать — 2/3
