n = int(input('Введите число: '))
def find_dividers(n):
    dividers = [1]
    for i in range(2, n+1):
        if n % i == 0:
            dividers.append(i)
        else:
            i += 1
    if n == 0:
        return None
    return dividers
 
print(f'Все делители числа {n}: {find_dividers(n)}')