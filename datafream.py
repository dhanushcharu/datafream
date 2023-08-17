# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:12:30 2023

@author: SPTINT-20
"""

import pandas as pd
data=pd.DataFrame([[1,2,3,4],
                   [1,2,3,4],
                   [1,2,3,4]],columns=['jan','feb','mar','apl',])
print(data)

d={'name':['x','y','z'],
   'age':[20,30,40]}
df=pd.DataFrame(d)
print(df) 

dt=pd.read_csv("D:/Dataset/Titanic_dataset.csv")
print(dt) 

data=pd.DataFrame([[22,23,24],
                   [18,25,24],
                   [15,12,22]],
columns=['maths','english','kannada',])
print(data)
