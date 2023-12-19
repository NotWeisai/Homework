import pandas as pd
import numpy as np

df = pd.read_csv('/content/Customers (1).csv', delimiter = ';')
df

df.isnull().any()

df.dropna()

df.groupby('Profession')['Income'].mean()
