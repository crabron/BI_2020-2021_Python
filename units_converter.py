import pandas as pd

#make conflict
df = pd.read_csv("units-conversion-table.csv", sep=",")
df = df.rename(columns={'conversion_type': 'Conversion_type',
                        'from': 'From',
                        'to': 'To',
                        'multiply_by': 'Multiply_by'}, inplace=False)

solitude_type = [i for i in df.Conversion_type.unique()]
solitude_type_num = [i for i in range(1, len(solitude_type) + 1)]
solitude_type = zip(solitude_type_num, solitude_type)
d_solitude_type = dict(solitude_type)
for i in d_solitude_type.keys():
    print(i, d_solitude_type.get(i))
print("Категории конвертации. Введите цифру соответствующее нужной категории.")
sel_1 = int(input())
type_get = d_solitude_type.get(sel_1)
solitude_from = [i for i in df[df["Conversion_type"] == type_get].From.unique()]
solitude_from_num = [i for i in range(1, len(solitude_from) + 1)]
solitude_from = zip(solitude_from_num, solitude_from)
d_solitude_from = dict(solitude_from)
for i in d_solitude_from.keys():
    print(i, d_solitude_from.get(i))
print("В данной категории возможна конвертация следующих штуковин. "
      "Введите число соответствующее нужной штуковине, из которой Вы хотите конвертировать.")
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
