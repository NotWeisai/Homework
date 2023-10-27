print('Введите факториал:')
n = int(input())
mult = 1
i = 0
while True:
    i += 1
    mult = mult * i
    if n / i == 1:
        break
print(f'Факториал {n} равен: {mult}')
