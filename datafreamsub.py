# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:22:03 2023

@author: SPTINT-20
"""
import pandas as pd
data=pd.DataFrame([[22,23,24],
                   [18,25,24],
                   [15,12,22]],
columns=['maths','english','kannada',])
print(data)
d=data.sum()
print(d)
d=data['maths'].sum()
print (d)
d=data['english'].max()
print (d)
d=data['kannada'].min()
print (d)
d=data.agg(['sum','min','max'])
print (d)



