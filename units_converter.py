Traceback (most recent call last):
  File "/home/crabron/PycharmProjects/pythonProject/venv/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2891, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 70, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 101, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1675, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1683, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/crabron/PycharmProjects/pythonProject/main.py", line 38, in <module>
    (df['From' == "Kilometer"]) &
  File "/home/crabron/PycharmProjects/pythonProject/venv/lib/python3.7/site-packages/pandas/core/frame.py", line 2902, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/home/crabron/PycharmProjects/pythonProject/venv/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2893, in get_loc
    raise KeyError(key) from err
KeyError: False
      Conversion_type       From          To     Multiply_by
0              Length  Kilometer       Meter     1000.000000
1              Length  Kilometer  Centimeter   100000.000000
2              Length  Kilometer  Millimeter  1000000.000000
3              Length  Kilometer        Mile        0.621371
4              Length  Kilometer        Yard     1093.610000
...               ...        ...         ...             ...
1132  Digital Storage   Pebibyte    Terabyte     1125.900000
1133  Digital Storage   Pebibyte     Tebibit     8192.000000
1134  Digital Storage   Pebibyte    Tebibyte     1024.000000
1135  Digital Storage   Pebibyte     Petabit        9.007200
1136  Digital Storage   Pebibyte    Petabyte        1.125900
