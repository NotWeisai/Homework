from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 45)

Options = {'criterion': ['gini', 'entropy'],
           'max_depth': [1, 2],
           'min_samples_split': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

Tree = DecisionTreeClassifier()
gridsearch = GridSearchCV(Tree, Options, cv = 5)
gridsearch.fit(X_train, Y_train)

Best_Options = gridsearch.best_params_
print('Лучшие параметры:', Best_Options)

Tree = DecisionTreeClassifier(criterion = 'gini', max_depth = 2, min_samples_split = 2)
Tree.fit(X_train, Y_train)
Y_pred = Tree.predict(X_test)
acc = accuracy_score(Y_test, Y_pred)
print('Оценка accuracy на тестовом наборе: ', acc)
