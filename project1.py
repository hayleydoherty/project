import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

'''plt.hist(df["sepal_width"]) wouldnt read sepal width from csv because space between the , and "sepal_width" in file
plt.show()'''

#Pandas describe function for descriptive statistics
print("Sepal Length")
print(df["sepal_length"].groupby(df["variety"]).describe())
print("\nSepal Width")
print(df["sepal_width"].groupby(df["variety"]).describe())
print("\nPetal Length")
print(df["petal_length"].groupby(df["variety"]).describe())
print("\nPetal Width")
print(df["petal_width"].groupby(df["variety"]).describe())

setosa = df[(df['variety'] == 'Iris-setosa')]
setosa.reset_index(inplace= True)
versicolor = df[(df['variety'] == 'Iris-versicolor')]
versicolor.reset_index(inplace= True)
virginica = df[(df['variety'] == 'Iris-virginica')]
virginica.reset_index(inplace= True)

#Levene's test for homogeneity of variance
print("\nLevene's test for homogeneity of variance")
print("Sepal Width:")
print(stats.levene(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width']))
print('\nSepal Length')
print(stats.levene(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length']))
print('\nPetal Width')
print(stats.levene(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width']))
print('\nPetal Length')
print(stats.levene(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length']))


'''#calculating differences for use in normality test
sw_diff1 = setosa['sepal_width'] - versicolor['sepal_width']
sw_diff2 = setosa['sepal_width'] - virginica['sepal_width']
sl_diff1 = setosa['sepal_length'] - versicolor['sepal_length']
sl_diff2 = setosa['sepal_length'] - virginica['sepal_length']
pw_diff1 = setosa['petal_width'] - versicolor['petal_width']
pw_diff2 = setosa['petal_width'] - virginica['petal_width']
pl_diff1 = setosa['petal_length'] - versicolor['petal_length']
pl_diff2 = setosa['petal_length'] - virginica['petal_length']'''

#Shapiro test for normality
print("\nShapiro test of normality")
print("Output is test statistic and p-value")
print('Sepal Width')
print('Iris-setosa')
print(stats.shapiro(setosa['sepal_width']))
print('Iris-versicolor')
print(stats.shapiro(versicolor['sepal_width']))
print('Iris-virginica')
print(stats.shapiro(virginica['sepal_width']))
print('\nSepal Length')
print('Iris-setosa')
print(stats.shapiro(setosa['sepal_length']))
print('Iris-versicolor')
print(stats.shapiro(versicolor['sepal_length']))
print('Iris-virginica')
print(stats.shapiro(virginica['sepal_length']))
print('\nPetal Width')
print('Iris-setosa')
print(stats.shapiro(setosa['petal_width']))
print('Iris-versicolor')
print(stats.shapiro(versicolor['petal_width']))
print('Iris-virginica')
print(stats.shapiro(virginica['petal_width']))
print('\nPetal Length')
print('Iris-setosa')
print(stats.shapiro(setosa['petal_length']))
print('Iris-versicolor')
print(stats.shapiro(versicolor['petal_length']))
print('Iris-virginica')
print(stats.shapiro(virginica['petal_length']))


#One-Way ANOVA
print("\nOne-Way ANOVA results:")
print("Sepal Width:")
print(stats.f_oneway(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width']))
print("\nSepal Length:")
print(stats.f_oneway(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length']))
print("\nPetal Width:")
print(stats.f_oneway(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width']))
print("\nPetal Length:")
print(stats.f_oneway(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length']))

# Posthoc test- Tukey's HSD
print("\nPost-hoc test performed to determine which groups are statistically significantly different from each other")
print("Sepal Width:")
mc1 = MultiComparison(df['sepal_width'], df['variety'])
print(mc1.tukeyhsd())
print()
print("\nSepal Length:")
mc2 = MultiComparison(df['sepal_length'], df['variety'])
print(mc2.tukeyhsd())
print()
print("\nPetal Width:")
mc3 = MultiComparison(df['petal_width'], df['variety'])
print(mc3.tukeyhsd())
print()
print("\nPetal Length:")
mc4 = MultiComparison(df['petal_length'], df['variety'])
print(mc4.tukeyhsd())



'''plt.hist(df["sepal_length"][0:50])
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
plt.savefig("Scatter plot of variable pairs.png") '''













