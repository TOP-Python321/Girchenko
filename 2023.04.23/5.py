text = input('Заполните текст телеграммы: ')

price = 30
payment = 0

for i in text.replace(' ',''):
    payment += price
    
print(f'{payment // 100} руб. {payment % 100} коп.')


# Заполните текст телеграммы ниже: 
# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп