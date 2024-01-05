import numpy as np
import pandas as pd
import matplotlib.pyplot as plt               # Импортирую нужные библиотеки
import seaborn as sns

df = pd.read_csv('/content/archive.zip')    # Считываю csv файл и вывожу на экран
df

df[df['price'] == df['price'].min()]['bedrooms'].min()      # Часть 1. Задание 1. Нахождение минимального количества спален в домах с минимальной ценой

df[df['bedrooms'] <= df['bathrooms']]['bathrooms'].count()    # Часть 1. Задание 2. Подсчёт кол-ва домов, в которых кол-во спален меньше или равно кол-ву ванных комнат

df[df['guestroom'] == 'yes']['price'].min()     # Часть 1. Задание 3. Минимальная цена дома с гостевой комнатой

df_price = df[(df['price'] <= 2000000) | (df['price'] >= 5000000)]['price'].count()   # Часть 1. Задание 4. Для начала подсчитываем кол-во домов с нужной нам стоимостью. Результаты вывожу для наглядности.
df_price

df_airconditioning = df[((df['price'] <= 2000000) | (df['price'] >= 5000000)) & (df['airconditioning'] == 'yes')]['airconditioning'].count()    # Часть 1. Задание 4. Далее подсчитываем кол-во домов нужной стоимости,
df_airconditioning                                                                                                                              # которые имеют кондиционеры. Результаты вывожу для наглядности.

df_mean = (df_airconditioning / df_price) * 100           # Часть 1. Задание 4. Теперь находим часть домов нужной стоимости, которые имеют кондиционеры.
df_mean

sns.stripplot(data=df, x='price', hue='parking', y='area', alpha = 0.9, palette='deep')     # Часть 2. Всё видно на графике.
plt.show();

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))    # Часть 3.

axes[0, 0].scatter(df[df['guestroom'] == 'yes']['price'], y=df[df['guestroom'] == 'yes']['area'], c = 'green', alpha = 0.5, label = 'Есть')    # Отмечаю разным цветом наличие и отсутствие гостевой комнаты и подписываю.
axes[0, 0].scatter(df[df['guestroom'] == 'no']['price'], y=df[df['guestroom'] == 'no']['area'], c = 'red', alpha = 0.5, label = 'Нет')
axes[0, 0].set_title('Наличие/отсутствие гостевой комнаты')
axes[0, 0].set_xlabel('Цена')
axes[0, 0].set_ylabel('Площадь')
axes[0, 0].grid()
axes[0, 0].legend()

axes[0, 1].scatter(df[df['basement'] == 'yes']['price'], y=df[df['basement'] == 'yes']['area'], c = 'green', alpha = 0.5, label = 'Есть')     # Отмечаю разным цветом наличие и отсутствие подвала и подписываю.
axes[0, 1].scatter(df[df['basement'] == 'no']['price'], y=df[df['basement'] == 'no']['area'], c = 'red', alpha = 0.5, label = 'Нет')
axes[0, 1].set_title('Наличие/отсутствие подвала')
axes[0, 1].set_xlabel('Цена')
axes[0, 1].set_ylabel('Площадь')
axes[0, 1].grid()
axes[0, 1].legend()

axes[1, 0].scatter(df[df['hotwaterheating'] == 'yes']['price'], y=df[df['hotwaterheating'] == 'yes']['area'], c = 'green', alpha = 0.5, label = 'Есть')   # Отмечаю разным цветом наличие и отсутствие отопления
axes[1, 0].scatter(df[df['hotwaterheating'] == 'no']['price'], y=df[df['hotwaterheating'] == 'no']['area'], c = 'red', alpha = 0.5, label = 'Нет')        # с помощью горячей воды и подписываю.
axes[1, 0].set_title('Наличие/отсутствие обогрева с помощью горячей воды')
axes[1, 0].set_xlabel('Цена')
axes[1, 0].set_ylabel('Площадь')
axes[1, 0].grid()
axes[1, 0].legend()

axes[1, 1].scatter(df[df['prefarea'] == 'yes']['price'], y=df[df['prefarea'] == 'yes']['area'], c = 'green', alpha = 0.5, label = 'Есть')     # Отмечаю разным цветом наличие и отсутствие предбанника и подписываю.
axes[1, 1].scatter(df[df['prefarea'] == 'no']['price'], y=df[df['prefarea'] == 'no']['area'], c = 'red', alpha = 0.5, label = 'Нет')
axes[1, 1].set_title('Наличие/отсутствие предбанника')
axes[1, 1].set_xlabel('Цена')
axes[1, 1].set_ylabel('Площадь')
axes[1, 1].grid()
axes[1, 1].legend()

plt.show();

data1 = df[df['airconditioning'] == 'yes']['price']         # Часть 4.
data2 = df[df['airconditioning'] == 'no']['price']
plt.hist(data1, bins = 30, color='green', alpha=0.5, label = 'Наличие кондиционеров')
plt.hist(data2, bins = 30, color='red', alpha=0.5, label = 'Отсутствие кондиционеров')
plt.title('Гистограммы наличия/отсутствия кондиционеров')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.legend()
plt.grid()
plt.show()
