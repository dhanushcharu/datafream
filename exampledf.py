import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("D:/Dataset/Athlete_events_outliers.csv")
print(data)
a=plt.hist(data['Age'])
print(a)
b=plt.scatter(data['Height'],data['Weight'])
print(b)
c=plt.bar(data['Year']==2000)
print(c)
d=plt.bar(data['Sex']=='M')
print(d)

