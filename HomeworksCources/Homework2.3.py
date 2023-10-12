print('Введите координату клетки по оси x:')
x = int(input())
print('Введите координату клетки по оси y:')
y = int(input())
if ((x % 2 == 0) or (y % 2 == 0)) and (x != y):
    print('YES')
else:
    print('NO')