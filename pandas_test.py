
import numpy as np
import pandas as pd

d = pd.read_csv('./1808/8yue_all.csv',header=0)
d2 = d.groupby('field')
for name,group in d2:
    print (name)
    print (type(group))
a = d.describe()[0,0]
print(a)
#print(d2.groups)
