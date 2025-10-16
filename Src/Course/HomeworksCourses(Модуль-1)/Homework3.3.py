print('Введите число, до которого нужно вывести числа, кратные 7:')
n = int(input())
i = 0
print('Числа, кратные 7:')
while True:
    i += 1
    con = i * 7
    if con > n:
        break
    print(con)