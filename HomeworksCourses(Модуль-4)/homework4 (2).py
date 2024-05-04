import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('/content/titanic.csv')
df

df.isna().sum()

df = df.dropna(axis = 0)
df.isna().sum()

df.describe(include = ['object'])

df = df.drop(['Name', 'Gender', 'Ticket', 'Cabin', 'Embarked'], axis = 1)

df_normalized = df - (df.mean(axis = 0) / df.std(axis = 0))

X = df_normalized.drop('Survived', axis = 1)
Y = df['Survived']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 45)

Logreg = LogisticRegression()
Logreg.fit(X_train, Y_train)
Y_pred_logreg = Logreg.predict(X_test)

KNN = KNeighborsClassifier()
KNN.fit(X_train, Y_train)
Y_pred_knn = KNN.predict(X_test)

"""### F1 score"""

F1_logreg = f1_score(Y_test, Y_pred_logreg)
F1_knn = f1_score(Y_test, Y_pred_knn)

print('F1 score логистической регрессии', F1_logreg)
print('F1 score для KNN', F1_knn)

if F1_logreg > F1_knn:
  print('Логистическая регрессия справилась лучше')
else:
  print('KNN справился лучше')
