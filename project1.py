
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

'''plt.hist(df["sepal_width"]) wouldnt read sepal width from csv because space between the , and "sepal_width" in file
plt.show()'''



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
plt.clf()'''


sns.pairplot(df, hue="variety")
plt.savefig("Scatter plot of variable pairs.png") 













