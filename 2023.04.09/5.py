# КОММЕНТАРИЙ: целый (мат.) — integer
whole_part = input('Введите целую часть: ')
fractional_part = input('Введите дробную часть: ')

mile_in_km = 1.61
# ИСПРАВИТЬ: f-строка отработает в такой ситуации быстрее
mile = float(f'{whole_part}.{fractional_part}')
km = round(mile * mile_in_km, 1)

# ИСПРАВИТЬ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
print(f'{mile} миль = {km} км')

# 547.258 миль = 881.1 км


# ИТОГ: отлично — 5/6
