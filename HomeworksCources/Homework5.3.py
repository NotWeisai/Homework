s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
list_s1 = list(s1)
list_s2 = list(s2)
if list_s1.sort() == list_s2.sort():
    print('Строки являются анаграммой')
else:
    print('Строки не являются анаграммой')