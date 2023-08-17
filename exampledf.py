import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("D:/Dataset/Athlete_events_outliers.csv")
print(data)
a=plt.hist(data['Age'])
print(a)
b=plt.scatter(data['Height'],data['Weight'])
print(b)
c=(data[data['Sex']=='M'],data['Medal'].value_counts().plot(kind='bar'))
print(c)
d=(data[data['Year']==2000],data['Name'].value_counts().plot(kind='bar'))
print(d)

