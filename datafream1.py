import pandas as pd
import numpy as np

data={'First score':[np.nan,47,78,64],
      'Second score':[85,47,np.nan,97],
      'third score':[np.nan,78,96,20],
      'fourth score':[52,48,96,np.nan]}
df=pd.DataFrame(data)
print(df)
print(df.notnull())
print(df.isnull())
print(df.fillna(785))
print(df.fillna(method='pad'))
print(df.fillna(method='bfill'))
print(df.dropna())
