ticket = input("Укажите номер билета: ")
number = [int(num) for num in ticket]

if sum(number[:3]) == sum(number[3:]):
    print("Да")
else: 
    print("Нет")
    
    
# Укажите номер билета: 456654
# Да
# Укажите номер билета: 258851
# Нет