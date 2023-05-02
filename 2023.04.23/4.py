digit = int(input('Введите разряд числа: '))
max_num = int(digit * '9')
count = 0

for num in range((max_num + 1) // 10, max_num + 1):
    i = 2
    while i * i <= num:
        if not num % i:
            break
        i += 1
    else: 
        count += 1

print(count)      

  
# Введите разряд числа: 3
# 143

# Введите разряд числа: 6
# 68906