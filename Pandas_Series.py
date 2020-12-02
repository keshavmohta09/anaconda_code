import numpy as np
import pandas as pd
# l = [1,2,3,'Keshav']
# d = {'a':1,'b':'c'}
# arr = np.array(l)
# print(pd.Series(l,('a','b','c',1)))
# print(pd.Series(arr))
# print(pd.Series(d))
a = pd.Series(['a','b','c'],[1,2,3])
b = pd.Series(['d','e','f'],[1,2,4])
print(a+b)