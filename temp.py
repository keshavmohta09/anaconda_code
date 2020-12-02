import pandas as pd, numpy as np
# df = pd.DataFrame(np.arange(1,21).reshape(5,4),['R1','R2','R3','R4','R5'],['C1','C2','C3','C4'])
# print(df)
# a = ['R1']
# b = ['C1']
# df.loc[a,b] = 234567890
# print(df)
df = pd.read_csv('studentdata.csv')
qw = list(df[df['Name']=='Keshav Mohta'].index)
print(len(df))