email = input("Введите адрес электронной почты: ")


if email[0] != '@' \
    and email.count('@') > 0 \
    and email.count('.') > 0 \
    and email.rfind('.') > email.find('@'):
    print("Да")
else:
    print("нет")
    
# Введите адрес электронной почты: roman.girchenko99@mail
# Нет
# Введите адрес электронной почты: romangirchenko99@mail.ru
# Да