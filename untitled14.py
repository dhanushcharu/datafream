import pandas as pd
import numpy as np

list1=[]
for i in range(50):
    if i%2==0 :
        list1.append(i)
        
ser=pd.Series(list1)
print(ser)