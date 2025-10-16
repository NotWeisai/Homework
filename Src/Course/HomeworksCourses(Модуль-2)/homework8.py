import numpy as np

arr = np.random.randint(1, 10, size=100)    #Задание 1
(arr > 7).mean() * 100

b = 0                    #Задание 2
for i in range(1000):
  arr = np.random.randint(1, 10, size=100)
  a = (arr > 7).mean() * 100
  if a == 20:
    b += 1
print(b/1000)

arr = np.array([np.arange(1, 11)] * 10)    #Задание 3
arr

arr.sum(axis=0)    #Задание 4
