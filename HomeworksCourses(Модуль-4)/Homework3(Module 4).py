"""
# Задание

В рамках этого задания вам предстоить подобрать оптимальное число соседей для алгоритма kNN. Датасет здесь будет сгенерирован с помощью специальной функции datasets.make_classification из библиотеки scikit-learn. Часть кода уже написана, её рекомендуется не изменять, а только запустить код в ячейках. Собственно, вам требуется подобрать такое число соседей k, чтоб вы прошли валидацию в соответствующей ячейке "Валидация модели". Очень полезно будет, если вы посмотрите на питон-ноутбук, ссылка на который в конце конспекта к этому вебинару или же посмотрите на то, как подобное исследование проводит преподаватель на вебинаре. Успехов!

Код с вебинара: https://colab.research.google.com/drive/11oGsSE5vcSMdMkGmKRSqKhLEb4TEvwf3

# Импорт библиотек
"""

!pip install scikit-plot
import scikitplot as skplt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

"""# Работа с данными"""

hard_problem = datasets.make_classification(
    n_samples=100,
    n_features=100,
    n_informative=50,
    n_classes=3,
    n_redundant=50,
    n_clusters_per_class=1,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    *hard_problem,
    test_size=0.3,
    random_state=1,
)

"""# Обучение модели

Обучим модель с k=8:
"""

clf = KNeighborsClassifier(n_neighbors=8)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
accuracy_score(y_test, predictions)

# Ваш код для поиска оптимального значения k

accuracies = []
ks = range(1, 30)
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    acc = accuracy_score(y_test, pred)
    accuracies.append(acc)

# Ваш код для построения графика зависимости accuracy(k) - метрики accuracy в зависимости от числа k

fig, ax = plt.subplots()
ax.plot(ks, accuracies)
ax.set(xlabel="k",
       ylabel="Accuracy",
       title="Performance of knn")
plt.show()

"""# Обучение модели с лучшим числом соседей k:"""

k_optim = 16 # здесь введите ваше оптимальное значение k

clf = KNeighborsClassifier(n_neighbors=k_optim)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

"""# Валидация модели"""

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.8, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)

print(classification_report(y_test, y_pred))
