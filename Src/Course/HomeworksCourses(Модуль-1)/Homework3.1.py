print('Введите число:')
Num = int(input())
Sum = 0
while Num != 0:
    s = Num % 10
    Sum += s
    Num = Num // 10
print('Сумма цифр числа: ', Sum)