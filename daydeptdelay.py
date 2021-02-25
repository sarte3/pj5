import pandas as pd

deptdelay = pd.read_csv('data/2007.csv', header=None)

dd = deptdelay.set_index(1)

dd = dd.loc[3:6, 2]

print(dd)