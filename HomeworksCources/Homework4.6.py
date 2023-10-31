print('Введите строку:')
s = input()
x = s.find('(')
x1 = s.rfind('(')
y = s.find(')')
y1 = s.rfind(')')
Res = s[x+1:y]
Res1 = s[x1+1:y1]
print(f'''Результат:
{Res}
{Res1}''')