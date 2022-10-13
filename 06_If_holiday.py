# Программа принимает на вход 2 числа: номер месяца и номер дня в месяце, проверяет является ли день выходным. 
# Принимаем начало года на понедельник и считая год не високосным. Учитываем только гос праздники (НГ, 9 мая и т.д.)

month = int(input('Введите месяц (цифрой): '))              # ввод и проверка месяца
while month not in range (1,13):
    print ('Такого месяца нет.')
    month = int(input('Введите месяц (цифрой): '))      

day = int(input('Введите день: '))                          # ввод и проверка дня
if month == 2:
    while day not in range (1,29):
        print ('Введён неверный день.')
        day = int(input('Введите день: '))
elif month in (4,6,9,11):
    while day not in range (1,31):
        print ('Введён неверный день.')
        day = int(input('Введите день: '))
else:
    while day not in range (1,32):
        print ('Введён неверный день.')
        day = int(input('Введите день: '))              

day_type = 'Рабочий день'

if ((month == 1 and day in range (1,9)) or                  # проверка праздничных дней         
    (month == 2 and day == 23) or 
    (month == 3 and day == 8) or
    (month == 5 and day in (1,9)) or
    (month == 6 and day == 12) or 
    (month == 11 and day == 4)):
    day_type = 'Выходной день'

for i in range (1,month):                                   # приведение дня к элементу в диапазоне 1-365
    if i == 2:
        day+=28
    elif i in (4,6,9,11):
        day+=30
    else:
        day+=31

for i in range(6,365,7):                                    # проверка субботы и воскресенья
    if i == day:
        day_type = 'Выходной день'
for i in range(7,365,7):
    if i == day:
        day_type = 'Выходной день'

print(day_type)