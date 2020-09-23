import pandas as pd

df = pd.read_csv("units-conversion-table.csv", sep=",")
df = df.rename(columns={'conversion_type': 'Conversion_type',
                        'from': 'From',
                        'to': 'To',
                        'multiply_by': 'Multiply_by'}, inplace=False)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1675, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1683, in print("Категории конвертации. ВведитPyObjectHashTable.get_item
KeyError: False
=======
import pandas as pd

df = pd.read_csv("units-conversion-table.csv", sep=",")
df = df.rename(columns={'conversion_type': 'Conversion_type',
                        'from': 'From',
                        'to': 'To',
                        'multiply_by': 'Multiply_by'}, inplace=False)
>>>>>>> second-homework

The above exception was the direct cause of the following exception:

solitude_from_num = [i for i in ranTraceback (most recent call last):
  File "/home/crabron/PycharmProjects/pythonProject/main.py", line 38, in <module>
    (df['From' == "Kilometer"]) &
  File "/home/crabron/PycharmProjects/pythonProject/venv/lib/python3.7/site-packages/pandas/core/frame.py", line 2902, in __getitem__
    indexer = self.columns.get_loc(key)
[print(i[0], i[1]) for i in solitude_from]
sel_2 = int(input())
print("В какую штуковину из списка выше вы хотите конвертировать?")
sel_3 = int(input())
print("Сколько у вас штуковин для конвертации?")
sel_2_value = float(input())
print("Предупреждение:")
df1 = df[df["To"] == d_solitude_from.get(sel_2)]
df2 = df1[df["From"] == d_solitude_from.get(sel_3)]
print("Результат:")
print(sel_2_value * float(df2.iloc[0]["Multiply_by"]))
