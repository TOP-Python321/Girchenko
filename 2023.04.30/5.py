import ref_5

word = input('Введите слово: ').upper().replace('Ё', 'Е')

scores = 0

# ИСПОЛЬЗОВАТЬ: в циклах, генераторных выражениях итп давать переменным осмысленные имена ещё важнее!
print(sum(
    scores + score
    # ИСПОЛЬЗОВАТЬ: имена переменных i, j, k традиционно используются почти только для индексов
    for char in word for score, letters in ref_5.scores_letters.items()
    if char in letters
))


# Введите слово: радость
# 10
