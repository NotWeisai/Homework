import matplotlib.pyplot as plt

lr = 0.01
w = 0
b = 0
X = [1, 3, 7]
y = [2, 6, 14]

for i in range(len(X)):
  y_pred = w*X[i] + b
  w += 2*lr*X[i]*(y[i] - y_pred)
  b += 2*lr*(y[i] - y_pred)

print(f'w = {w}, b = {b}')

plt.scatter(X, y)
plt.plot(X, [w*x + b for x in X], color = 'green')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
