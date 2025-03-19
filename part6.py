import pandas as pd
import matplotlib.pyplot as plt

data = {"value": [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 39]}

df = pd.DataFrame(data)

df.boxplot(column='value')  # создаем диаграмму
plt.show()  # показываем диаграмму

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]    # выбираем нужные значения

df_new.boxplot(column='value')  # создаем диаграмму
plt.show()