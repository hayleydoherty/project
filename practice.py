import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

setosa = df[(df['variety'] == 'Iris-setosa')]
#setosa.reset_index(inplace= True)
versicolor = df[(df['variety'] == 'Iris-versicolor')]
#versicolor.reset_index(inplace= True)
virginica = df[(df['variety'] == 'Iris-virginica')]
#virginica.reset_index(inplace= True)

plt.hist(setosa["sepal_length"])
plt.title("Sepal Length - Iris Setosa")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("setosa.png")
plt.clf()



'''sns.boxplot(x="variety", y="sepal_width", data = df)
plt.savefig("Spairs.png")
plt.clf()
sns.boxplot(x="variety", y="sepal_length", data = df)
plt.savefig("Sairs.png")
plt.clf()
sns.boxplot(x="variety", y="petal_width", data = df)
plt.savefig("Sirs.png")
plt.clf()
sns.boxplot(x="variety", y="petal_length", data = df)
plt.savefig("Spas.png")

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
plt.clf()'''