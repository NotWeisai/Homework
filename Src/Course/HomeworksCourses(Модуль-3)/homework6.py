import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # один признак
y = 4 + 3 * X + np.random.randn(100, 1)  # целевая переменная с небольшим шумом
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("mse =", mse)

plt.figure(figsize = (10, 5))
plt.scatter(X_train, y_train, color = 'blue', label = 'Обучение', alpha = 0.5)
plt.scatter(X_test, y_test, color = 'green', label = 'Тест', alpha = 0.5)
plt.plot(X_test, y_pred, color = 'red', label = 'Линейная регрессия')
plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.title('Линейная регрессия, обучение, тест')
plt.legend()
plt.grid()
plt.show()
