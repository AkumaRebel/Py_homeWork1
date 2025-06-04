name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))

print(' ')
print('Обычный способ')
print('Ваше имя: [', name,'], Фамилия [', surname, '], Возраст: [', age, ']')
print(' ')
print('f-string')
print(f'Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет')
print(' ')
print('format()')
print('Ваше имя: {}, Фамилия: {}, Возраст: {} лет'.format(name,surname,age))

