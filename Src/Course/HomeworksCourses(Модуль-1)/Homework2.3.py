print('Введите координату клетки по оси x:')
x = int(input())
print('Введите координату клетки по оси y:')
y = int(input())
if (x+y) % 2 == 0:
    print('NO')
else:
    print('YES')