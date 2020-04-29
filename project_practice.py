import scipy.stats as stats
import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

setosa = df[(df['variety'] == 'Iris-setosa')]

versicolor = df[(df['variety'] == 'Iris-versicolor')]

virginica = df[(df['variety'] == 'Iris-virginica')]



#Levene's test for homogeneity of variance
lev = stats.levene(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width'])
print(lev)

lev2 = stats.levene(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length'])
print(lev2)

lev3 = stats.levene(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width'])
print(lev3)

lev4 = stats.levene(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length'])
print(lev4)

plt.hist(df["sepal_length"][0:50])
plt.title("Sepal Length - Iris Setosa")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("a.png")
plt.clf()

plt.hist(df["sepal_length"][50:100])
plt.title("Sepal Length - Iris Versicolor")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("b.png")
plt.clf()

'''#calculating differences for use in normality test
sw_diff1 = setosa['sepal_width'] - versicolor['sepal_width']
sw_diff2 = setosa['sepal_width'] - virginica['sepal_width']
sl_diff1 = setosa['sepal_length'] - versicolor['sepal_length']
sl_diff2 = setosa['sepal_length'] - virginica['sepal_length']
pw_diff1 = setosa['petal_width'] - versicolor['petal_width']
pw_diff2 = setosa['petal_width'] - virginica['petal_width']
pl_diff1 = setosa['petal_length'] - versicolor['petal_length']
pl_diff2 = setosa['petal_length'] - virginica['petal_length']

#Shapiro test for normality
print(stats.shapiro(sw_diff1))
print(stats.shapiro(sw_diff2))
print(stats.shapiro(sl_diff1))
print(stats.shapiro(sl_diff2))
print(stats.shapiro(pw_diff1))
print(stats.shapiro(pw_diff2))
print(stats.shapiro(pl_diff1))
print(stats.shapiro(pl_diff2))


print(stats.f_oneway(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width']))

print(stats.f_oneway(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length']))

print(stats.f_oneway(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width']))

print(stats.f_oneway(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length']))


#with open("descriptive_stats.txt", "w") as f:
    #f.write("Sepal Length\n")
    #sepl= (df["sepal_length"].groupby(df["variety"]).describe())
    #sepl.to_csv("descriptive_stats.txt")
    
#with open("descriptive_stats.txt", "a") as f:
    #f.write("\nSepal Width\n") 
    #sepw= (df["sepal_width"].groupby(df["variety"]).describe())
    #sepw.to_csv("descriptive_stats.txt")
    #f.write("\nPetal Length\n") 
#pet.l= (df["petal_length"].groupby(df["variety"]).describe())
#print()
#print ("Petal Width") 
#print(df["petal_width"].groupby(df["variety"]).describe())


print(stats.ttest_ind(setosa['sepal_width'], versicolor['sepal_width']))
print(stats.ttest_ind(setosa['sepal_width'], virginica['sepal_width']))

print(stats.ttest_ind(setosa['sepal_length'], versicolor['sepal_length']))
print(stats.ttest_ind(setosa['sepal_length'], virginica['sepal_length']))

print(stats.ttest_ind(setosa['petal_width'], versicolor['petal_width']))
print(stats.ttest_ind(setosa['petal_width'], virginica['petal_width']))

print(stats.ttest_ind(setosa['petal_length'], versicolor['petal_length']))
print(stats.ttest_ind(setosa['petal_length'], virginica['petal_length']))'''
