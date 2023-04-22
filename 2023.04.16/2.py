divisible = int(input('Укажите делимое: '))
divisor = int(input('Укажите делитель: '))
answer = divisible // divisor
remains = divisible % divisor

if remains == 0:
    print(f'{divisible} делится на {divisor} нацело \n'
          f'частное: {answer}')

if remains != 0:
    print(f'{divisible} не делится на {divisor} нацело \n'
          f'неполное частное: {answer}\n'
          f'остаток: {remains}')


# 20 делится на 10 нацело
# частное: 2

# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1
