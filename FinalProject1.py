import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

# Reading the data with pandas and creating a data frame, df
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

#Pandas describe function for descriptive statistics
#Outputs descriptive statistics of each variable grouped by species
print("Sepal Length")
print(df["sepal_length"].groupby(df["variety"]).describe())
print("\nSepal Width")
print(df["sepal_width"].groupby(df["variety"]).describe())
print("\nPetal Length")
print(df["petal_length"].groupby(df["variety"]).describe())
print("\nPetal Width")
print(df["petal_width"].groupby(df["variety"]).describe())

#Creating individual data frames for each species of iris
setosa = df[(df['variety'] == 'Iris-setosa')]
versicolor = df[(df['variety'] == 'Iris-versicolor')]
virginica = df[(df['variety'] == 'Iris-virginica')]

#Levene's test for homogeneity of variance using SciPy
print("\nLevene's test for homogeneity of variance")
print("Sepal Width:")
print(stats.levene(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width']))
print('\nSepal Length')
print(stats.levene(setosa['sepal_length'], versicolor['sepal_length'], virginica['sepal_length']))
print('\nPetal Width')
print(stats.levene(setosa['petal_width'], versicolor['petal_width'], virginica['petal_width']))
print('\nPetal Length')
print(stats.levene(setosa['petal_length'], versicolor['petal_length'], virginica['petal_length']))


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

#Using Matplotlib to generate histograms of each variable
#Sepal length
plt.hist(setosa["sepal_length"])
plt.title("Sepal Length - Iris Setosa")     #graph title
plt.xlabel("Sepal length(cm)")              #x-axis label
plt.ylabel("No. of flowers")                #y-axis label
plt.savefig("Setosa-Sepal Length Histogram.png")#saved as
plt.clf()       #clears graph so the next histogram is not imposed on top of previous one
#Code is the same for the rest of the histograms with the appropriate data, axis labels and titles added
plt.hist(versicolor["sepal_length"])
plt.title("Sepal Length - Iris Versicolor")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Versicolor-Sepal Length Histogram.png")
plt.clf()

plt.hist(virginica["sepal_length"])
plt.title("Sepal Length - Iris Virginica")
plt.xlabel("Sepal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Virginica-Sepal Length Histogram.png")
plt.clf()

#sepal width
plt.hist(setosa["sepal_width"])
plt.title("Sepal Width - Iris Setosa")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Setosa-Sepal Width Histogram.png")
plt.clf()

plt.hist(versicolor["sepal_width"])
plt.title("Sepal Width - Iris Versicolor")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Versicolor-Sepal Width Histogram.png")
plt.clf()

plt.hist(virginica["sepal_width"])
plt.title("Sepal Widgth - Iris Virginica")
plt.xlabel("Sepal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Virginica-Sepal Width Histogram.png")
plt.clf()

#Petal length
plt.hist(setosa["petal_length"])
plt.title("Petal Length - Iris Setosa")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Setosa-Petal Length Histogram.png")
plt.clf()

plt.hist(versicolor["petal_length"])
plt.title("Petal Length - Iris Versicolor")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Versicolor-Petal Length Histogram.png")
plt.clf()

plt.hist(virginica["petal_length"])
plt.title("Petal Length - Iris Virginica")
plt.xlabel("Petal length(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Virginica-Petal Length Histogram.png")
plt.clf()

#Petal Width
plt.hist(setosa["petal_width"])
plt.title("Petal Width - Iris Setosa")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Setosa-Petal Width Histogram.png")
plt.clf()

plt.hist(versicolor["petal_width"])
plt.title("Petal Width - Iris Versicolor")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Versicolor-Petal Width Histogram.png")
plt.clf()

plt.hist(virginica["petal_width"])
plt.title("Petal Widgth - Iris Virginica")
plt.xlabel("Petal width(cm)")
plt.ylabel("No. of flowers")
plt.savefig("Virginica-Petal Width Histogram.png")
plt.clf()

#Generated boxplots with seaborn so that I could get a visual representation of the spread of the data
#the three groups are on the same graph for each variable aming comparisons easier to make
sns.boxplot(x="variety", y="sepal_width", data = df)
plt.savefig("SepalWidth Boxplot.png")
plt.clf()
sns.boxplot(x="variety", y="sepal_length", data = df)
plt.savefig("SepalLength Boxplot.png")
plt.clf()
sns.boxplot(x="variety", y="petal_width", data = df)
plt.savefig("PetalWidth Boxplot.png")
plt.clf()
sns.boxplot(x="variety", y="petal_length", data = df)
plt.savefig("PetalLength Boxplot.png")

#made a pairplot with seaborn that outputs a scatter plot of every pair of groups for each variable
sns.pairplot(df, hue="variety")
plt.savefig("Scatter plot of variable pairs.png")













