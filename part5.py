import pandas as pd
import numpy as np

dates = pd.date_range(start='2023-01-25', periods=10, freq='D')
values = np.random.rand(10)
df = pd.DataFrame({'Date': dates, 'Value': values})   # создаем датафрейм
df.set_index('Date', inplace=True)  # устанавливаем дату в качестве индекса
print(df)

month = df.resample('ME').mean()     # группируем по месяцам
print(month)