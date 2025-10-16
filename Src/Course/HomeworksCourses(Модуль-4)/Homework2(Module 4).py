"""
# Задание

В рамках этого задания вам предстоить поработать с уже известным вам датасетом mnist из рукописных цифр. Вам необходимо выполнить многоклассовую классификацию и затем пройти валидацию с вашей моделью, достигнув определённого уровня accuracy. Здесь бОльшая часть кода уже готова, вам останется лишь реализовать ту его часть, где вы инициализируете и обучаете модель из библиотеки scikit-learn. При успешном прохождении валидации, в ячейке вы должны увидеть сообщение "Хорошая работа!". После этого запустите другие ячейки с вычислением различных метрик, чтоб лучше оценить качество своей модели. Успехов!

### Подсказка!!! (открывать, если совсем ступор)

__Подсказка: при инициализации модели есть параметры solver, penalty - посмотрите в документации, какие значения они могут принимать и добейтесь максимальной accuracy в зависимости от этих параметров__

# Импорт необходимых библиотек
"""

!pip install scikit-plot

# Commented out IPython magic to ensure Python compatibility.
from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import scikitplot as skplt
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

"""# Загрузка датасета и его визуализация"""

mnist = fetch_openml(data_id=554) # https://www.openml.org/d/554

type(mnist.data), type(mnist.categories), type(mnist.feature_names), type(mnist.target)

data = np.array(mnist.data)
targets = np.array(mnist.target)

plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(data[0:5],
                                           targets[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)
    plt.title('Training: ' + label, fontsize = 20);

X_train, X_test, y_train, y_test = train_test_split(data[:10000,:],
                                                   targets[:10000].astype('int'), #targets str to int convert
                                                   test_size=1/7.0,
                                                   random_state=0)

X_train.shape, X_test.shape

"""# Обучение модели

***Важно! Инициализируйте модель с параметрами n_jobs=5, tol=0.01 (чтоб процесс обучения был быстрее), а также max_iter= 1000.***
"""

### Здесь должен быть ваш код инициализации модели
LogReg = LogisticRegression(solver = 'saga', penalty = 'l1', n_jobs=5, tol=0.01, max_iter=1000)

### Здесь должен быть ваш код обучения модели
LogReg.fit(X_train, y_train)

"""# Валидация модели"""

y_pred = LogReg.predict(X_test)

accuracy = np.mean(y_pred == y_test)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.9, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision
precision = precision_score(y_test, y_pred, average='weighted')
print("Precision:", precision)

# Calculate recall (sensitivity)
recall = recall_score(y_test, y_pred, average='weighted')
print("Recall (Sensitivity):", recall)

# Calculate F1-score
f1 = f1_score(y_test, y_pred, average='weighted')
print("F1-Score:", f1)

skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)

print(classification_report(y_test, y_pred))
