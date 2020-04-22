import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

'''plt.hist(df["sepal_width"]) wouldnt read sepal width from csv because space between the , and "sepal_width" in file
plt.show()'''

#Pandas describe function for descriptive statistics
print("Sepal Length")
print(df["sepal_length"].groupby(df["variety"]).describe())
print("Sepal Width")
print(df["sepal_width"].groupby(df["variety"]).describe())
print("Petal Length")
print(df["petal_length"].groupby(df["variety"]).describe())
print("Petal Width")
print(df["petal_width"].groupby(df["variety"]).describe())

#Levene's test for homogeneity of variance
print(stats.levene(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width']))

print(stats.levene(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length']))

print(stats.levene(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width']))


print(stats.levene(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length']))


#calculating differences for use in normality test
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


plt.hist(df["sepal_length"][0:50])
plt.title("Sepal Length - Iris Setosa")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Length- Iris setosa.png")
plt.clf()

plt.hist(df["sepal_length"][50:100])
plt.title("Sepal Length - Iris Versicolor")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Length- Iris versicolor.png")
plt.clf()

plt.hist(df["sepal_length"][100:150])
plt.title("Sepal Length - Iris Virginica")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Length- Iris virginica.png")
plt.clf()

plt.hist(df["sepal_width"][0:50])
plt.title("Sepal Width - Iris Setosa")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Width- Iris setosa.png")
plt.clf()

plt.hist(df["sepal_width"][50:100])
plt.title("Sepal Width - Iris Versicolor")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Width- Iris versicolor.png")
plt.clf()

plt.hist(df["sepal_width"][100:150])
plt.title("Sepal Widgth - Iris Virginica")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Sepal Width- Iris virginica.png")
plt.clf()

plt.hist(df["petal_length"][0:50])
plt.title("Petal Length - Iris Setosa")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Length- Iris setosa.png")
plt.clf()

plt.hist(df["petal_length"][50:100])
plt.title("Petal Length - Iris Versicolor")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Length- Iris versicolor.png")
plt.clf()

plt.hist(df["petal_length"][100:150])
plt.title("Petal Length - Iris Virginica")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Length- Iris virginica.png")
plt.clf()

plt.hist(df["petal_width"][0:50])
plt.title("Petal Width - Iris Setosa")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Width- Iris setosa.png")
plt.clf()

plt.hist(df["petal_width"][50:100])
plt.title("Petal Width - Iris Versicolor")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Width- Iris versicolor.png")
plt.clf()

plt.hist(df["petal_width"][100:150])
plt.title("Petal Widgth - Iris Virginica")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Petal Widgth- Iris virginica.png")
plt.clf()


sns.pairplot(df, hue="variety")
plt.savefig("Scatter plot of variable pairs.png") 













