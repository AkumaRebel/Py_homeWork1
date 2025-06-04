a = input('Введите число: ')

if not a.isdigit(): 
    print('Ошибка') #Проверка на то, что введено число
else:
    a = int(a)
    if a % 2 == 0: 
        print('Число четное')
    else:
        print('Число нечетное')

    