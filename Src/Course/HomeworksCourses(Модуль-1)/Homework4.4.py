print('Введите текст:')
text = input()
result = text.replace(text[-1], 2*text[-1])
print('Результат: ', result[:-2])