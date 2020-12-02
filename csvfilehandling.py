import pandas as pd
df = pd.read_csv('csvfilehandling.csv',na_values={
    'EmployeeName':['NaN','a']
})
try:
    df.fillna('Keshav')
    df.to_csv('csvfilehandling.csv',index=False)
except Exception as e:
    print(e)
# print(df)