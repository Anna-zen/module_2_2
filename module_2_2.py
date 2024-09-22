#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third:
    print ('Одинаковых чисел: 3')
elif first == second or first == third or second == third:
    print('Одинаковых чисел: 2')
else :
    print('Одинаковых чисел: 0')
