import pandas as pd

# data = {
#     "набор А": [85, 90, 95, 100, 105],
#     "набор B": [70, 80, 95, 110, 120]
# }
# stdA = df["набор А"].std()
# stdB = df["набор B"].std()
#
# print(f"Стандартное отклонение набора А: {stdA}")
# print(f"Стандартное отклонение набора B: {stdB}")

data = {
    "Возраст": [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    "Зарплата": [54000, 58000, 60000, 52000, 57000, 54000, 58000, 60000, 52000, 57000]
}

df = pd.DataFrame(data)
print(f"Средний возраст: {df['Возраст'].mean()}")
print(f"Медиана возраста: {df['Возраст'].median()}")
#print(f"Мода возраста: {df['Возраст'].mode()}")
print(f"Стандартное отклонение возраста: {df['Возраст'].std()}")

print(f"Средняя зарплата: {df['Зарплата'].mean()}")
print(f"Медиана зарплаты: {df['Зарплата'].median()}")
#print(f"Мода зарплаты: {df['Зарплата'].mode()}")
print(f"Стандартное отклонение зарплаты: {df['Зарплата'].std()}")


