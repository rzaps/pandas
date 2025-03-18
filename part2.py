import pandas as pd

df = pd.read_csv('hh.csv')

df['Test'] = [new for new in range(len(df))]  # создаем новый столбец
print(df)

df = df.drop(['Test'], axis=1)  # удаляем столбец
print(df)

df = df.drop(28, axis=0)  # удаляем строку
print(df)