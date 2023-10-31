print('Введите набор чисел:')
List = input()
list1 = List.split()
L = list(map(int, list1))
def Max(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    else:
        if len(L) > 1:
            Max1 = Max(L[1:])
        if L[0] < Max1:
            return Max1
        else:
            return L[0]
print(Max(L))