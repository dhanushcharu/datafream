import pandas as pd
import numpy as np
import matplotlib.pyplot as p
df=pd.read_csv("D:/Dataset/Titanic_dataset.csv")
print(df)
print(df.head(10))
a=p.hist(df['Age'])
print(a)
p.scatter(df['Age'],df['Fare'])
print(df[df['Sex']=='female'])
print(df[['Sex','Pclass','Survived']])

b=df[df['Pclass']==3]
b=df[df['Sex']=='female']
df['Survived'].value_counts().plot(kind='bar')
print(df['Survived'].value_counts())
import seaborn as sns
a=sns.boxplot(df['Survived'])   
print(a)



