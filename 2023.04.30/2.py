fruits = "".split()

while True:
    fruit = input("Введите название фрукта: ")
    if len(fruit) > 0:
        fruits.append(fruit)
    else:
        break
        
if len(fruits) >= 2:
    fruits.insert(-1, "и")
    for elem in range(0, len(fruits) - 3):
        fruits[elem] = fruits[elem] + ","
    
print(" ".join(fruits))


# Введите название фрукта: банан
# Введите название фрукта: апельсин
# Введите название фрукта: мандарин
# Введите название фрукта: яблоко
# Введите название фрукта:
# банан, апельсин, мандарин и яблоко
