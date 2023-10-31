print('Введите список чисел:')
numbers = (input())
A = numbers.split()
B = list(map(int, A))
y = B[-1]
print(f'Возведение в {y} степень')
B1 = list(map(lambda x: x**y, B))
print('Список, возведённый в указанную степень: ', B1[:-1])