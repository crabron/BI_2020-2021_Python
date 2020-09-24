import pandas as pd
from itertools import count

df = pd.read_csv("units-conversion-table.csv", sep=",")
df = df.rename(columns={'conversion_type': 'Conversion_type',
                        'from': 'From',
                        'to': 'To',
                        'multiply_by': 'Multiply_by'}, inplace=False)
solitude_type_d = dict(zip(count(1), df.Conversion_type.unique()))
[print(i, v) for i, v in solitude_type_d.items()]
print("Категории конвертации. Введите число соответствующее нужной категории.")
sel_1 = int(input())
d_solitude_from = dict(zip(count(1), df[df["Conversion_type"] == type_get].From.unique()))
[print(i, v) for i, v in d_solitude_from.items()]
print("В данной категории возможна конвертация следующих штуковин. "
      "Введите число соответствующее нужной штуковине,"
      " из которой Вы хотите конвертировать.")
[print(i[0], i[1]) for i in solitude_from]
sel_2 = int(input())
print("В какую штуковину из списка выше вы хотите конвертировать?")
sel_3 = int(input())
print("Сколько у вас штуковин для конвертации?")
sel_2_value = float(input())
print("Результат:")
print(sel_2_value * float(df[(df['From'] == d_solitude_from.get(sel_2)) & \
                             (df['To'] == d_solitude_from.get(sel_3))].iloc[0]["Multiply_by"]))
                           
