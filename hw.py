import pandas as pd

df = pd.read_csv('dz.csv')
df.dropna(inplace=True)  # удаляем строки с NaN
print(df)

group = df.groupby('City')['Salary'].mean()
print(group)

print("==========")

###############################

df_2 = pd.read_csv('IMDb 2024 Movies TV Shows.csv')

print(df_2.head())
print(df_2.info())
print(df_2.describe())

