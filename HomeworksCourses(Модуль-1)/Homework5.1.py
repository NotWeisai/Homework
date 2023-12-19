from collections import Counter
s = (input('Введите строку: '))
Cities = s.split()
n = int(Cities[0])
cnt = Counter(Cities[1::])
val = list(map(int, cnt.values()))
k = 0
for i in val:
    if i > 1:
        k += i
        res = n - k
print(res)