import pandas as pd

# data = [1, 2, 3, 4, 5]
# s = pd.Series(data)
# print(s)
#
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'Gender': ['Female', 'Male', 'Male', 'Male'],
#     'City': ['New York', 'London', 'Paris', 'Berlin'],
#     'Country': ['USA', 'UK', 'France', 'Germany']
# }
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df.info(7))
print(df.head(7))
print(df.describe())
print(df[['Country name', 'Regional indicator']])
print(df.loc[56, 'Healthy life expectancy'])
print(df[df['Healthy life expectancy'] > 0.7])

