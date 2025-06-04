a = ''

while a != 'exit':
    a = input('Введите число или "exit" для выхода: ')
    
    if a == 'exit':
        break
    
    try:
        num = float(a)  
        
        
        b = [c for c in a if c.isdigit()]  # Оставляем только цифры
        c = len(b)
        
        print(f'В этом числе {c} цифр(ы)')
    except ValueError:
        print('Ошибка: введено не число')