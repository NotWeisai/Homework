print('Введите первое число:')
a = float(input())
print('Введите второе число:')
b = float(input())
if a > b:
    print('Наибольшее число: ', a)
elif a == b:
    print('Числа равны, наибольшее: ', a)
else:
    print('Наибольшее число: ', b)