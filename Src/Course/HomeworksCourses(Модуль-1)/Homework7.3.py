from functools import reduce
print('Введите числа:')
List = input()
list1 = List.split()
L = list(map(int, list1))
print(reduce(lambda x, y: x if x>y else y, L))