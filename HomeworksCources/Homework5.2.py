s = input('Введите строку: ')
s = list(s)
def correction():
    s[0] = s[0].upper()
    for i in range(len(s)-2):
        if s[i] in '.!?':
            s[i+2] = s[i+2].upper()
    return ''.join(s)

print(correction())
correction()