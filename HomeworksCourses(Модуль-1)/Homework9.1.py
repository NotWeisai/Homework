a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = a * b
if a != 0 and b != 0:
    maxim = max(a, b)
    if maxim % a == 0 and maxim % b == 0:
        x = maxim
    else:
        maxim += 1

print('multiple = ', x)