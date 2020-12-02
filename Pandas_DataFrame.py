import numpy as np, pandas as pd
# arr = np.arange(1,51).reshape(5,10)
# l1 = ['A','B','C','D','E']
# l2 = ['a','b','c','d','e','f','g','h','i','j']
# df = pd.DataFrame(arr,l1,l2)
# print(df)
# print()
# df = df[df>25].dropna()5
# print(df)
# print()
# print(df.iloc[0])
# print(df.loc['B'])
# df['a'] = [1,2,3,4,5]
# print('\n\n',df)
# C='B'
# print('\n\n',df.loc[C,'c'])
# print('\n\n',df[df['j']>=10])
# print(df[df['a']>0]['D'])
# df = df.reset_index()
# print(df)
# print(df.loc[0])

# l = ['G1','G2']
# arr1 = np.arange(1,13).reshape(2,6)
# print(pd.DataFrame(arr1,l,[1,2,3,1.2,5,6]))

t = [('G1',1),('G1',2),('G1',3),('G2',1),('G2',2),('G2',3)]
t = pd.MultiIndex.from_tuples(t)
df = pd.DataFrame(np.arange(1,13).reshape(6,2),t,['A','B'])
print(df)
print(df.apply(lambda x: x*2))
df['C'] = df['A'] * df['B']
print(df)
# print(arr)
# sal = pd.read_csv('Salaries.csv')
# print(sal.head().transpose())