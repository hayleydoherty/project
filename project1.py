


import pandas as pd
import numpy as np
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

#print (df.head(50))




print ("Iris-setosa") 
print(df.iloc[0:50].describe())

print ("Iris-versicolor") 
print(df.iloc[50:100].describe())

print ("Iris-virginica") 
print(df.iloc[100:150].describe())