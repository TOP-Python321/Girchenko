whole_part = input('Введите целую часть: ')
fractional_part = input('Введите дробную часть: ')
mile_in_km = 1.61
mile = float(whole_part + '.' + fractional_part)
print(f'{mile} миль = {round(mile * mile_in_km, 1)} км' )

# 547.258 миль = 881.1 км