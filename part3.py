import pandas as pd

df = pd.read_csv('animal.csv')

print(df)

df.fillna(0, inplace=True)  # заменяем NaN на 0
print(df)

# df.dropna(inplace=True)  # удаляем строки с NaN
# print(df)

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()   # группируем по столбцу
print(group)

df.to_csv(path_or_buf='animal2.csv', index=False)