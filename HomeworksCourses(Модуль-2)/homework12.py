# -*- coding: utf-8 -*-
"""Homework12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zN4cmkuvE-j9eaRG4A2JdUXDLR9Nr5bF
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import math

c = np.linspace(1, 15, 1000)
cos = np.cos(c)
sin = np.sin(c)
x = (cos*math.sqrt(2)*cos) / (1 + sin**2)
def y(x):
  cosx = np.cos(x)
  sinx = np.sin(x)
  return ((x*math.sqrt(2)*sinx*cosx) / (1 + sinx**2))
plt.figure(figsize=(10, 5))
plt.plot(y(x), linewidth=2, color='g', dashes=[4, 2], alpha=0.5)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Вот такая моя функция')
plt.show()

X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
plt.figure(figsize = (10, 10))
plt.scatter(X, Y, c = 'purple', marker='<', alpha = 0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Задание 2')
plt.legend()
plt.grid()
plt.show();

data = np.random.normal(16, 2, 1000)
plt.hist(data, bins = 30, color = 'r', alpha = 0.5)