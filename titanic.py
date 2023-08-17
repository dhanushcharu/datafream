import numpy as np
import pandas as pd
data=pd.read_csv("D:/Dataset/Titanic_dataset.csv",index_col='Name',)
print(data) 
print(data[['Age','Survived']])
print(data.loc['Allen, Mr. William Henry'])
print(data.iloc[1:10 ,1:15])
               
