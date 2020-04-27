# project
programming and scripting project

## Fisher's Iris Data Set

British biologist and statistician Ronald Fisher first published his *Iris data set* in 1936 in his paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis[1].  This data set is commonly used in statistics, pattern recognition and visualisation to this day.  The data set consists of 50 samples from 3 species of iris, Iris setosa, Iris virginica and Iris versicolor. From each of the 150 samples, 4 measurements were taken which were the length and width of both petal and sepal. A small problem with the dataset is that there is disagreement amongst botanists as to whether the Iris plant has sepals! However this problem has not had an effect on the use of the dataset for statistical purposes as *Web of Science* lists roughly 4000 citations to Fisher's 1939 paper [2]. 


## My Investigation

Fisher's data set is publicly available online and can be freely downloaded in .csv format.  This file format can be loaded into Pandas data frame and analysis performed on it.  
For my investigations I first inported the various libraries needed to analyse and graph the data set.  This included:
	-Seaborn
	-Matplotlib
	-Pandas
	-NumPy
	-Scipy.stats
	-statsmodels.stats.multicomp
	
I used Pandas to output descriptive statistics of each variable in the data set, grouped by their species.  This allows us to see measures including mean, median, min, max and standard deviation of the data.  
By using Pandas to read each variable separately and group the variable by 'variety' (species), I was able to get meaningful descriptive stats of each variable and easily compare the stats of the different groups.  Below is an example of the code I used to do this, with a new line for each variable.
	
	df["variable"].groupby(df["variety"]).describe()

We were asked to have the descriptive statistics ouput to a text file when the program is run however I have been unable to figure out how to do this without having the whole program output to a text file (using > in the command prompt when running the analysis.py file).

As part of my investigation I performed some basic analysis of the data using statistical modules available in python.  One such module is the SciPy.stats module.  First, I used statistical functions available in this module to determine if the data should be analysed parametrically or non-parametrically.  This required that the data be tested for homogeneity of variance and normality using the Levene Test and Shapiro Test.  For data to be tested parametrically, it must satisfy two of the following three assumptions, the data is distributed normally, it displays homogeneity of variance and there are equal number of data points in each of the groups to be tested.

Below is an example of the code used to perform the Levene test of homogeneity of variance.  The example below is looking at the sepal width data for all three species of Iris and determining if the spread(variance) od data is simialr between the groups.  As the p-value is not significant (p-value is > 0.05) we can conclude that the groups disply equal variances.

	stats.levene(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width'])
	LeveneResult(statistic=0.6475222363405327, pvalue=0.5248269975064537)


	stats.shapiro(setosa['sepal_width'])
	(0.968691885471344, 0.20465604960918427)


Following my analysis I determined that the Fisher dataset could be analysed parametrically and so went on to perform a one-way ANOVA.  

	stats.f_oneway(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width'])
	F_onewayResult(statistic=47.36446140299382, pvalue=1.3279165184572242e-16)
	

Next we were asked to create histograms of each variable and save them as png files.  I used Matplotlib to do this.  For each variable, I wanted to split the data into the 3 species groups as I believe viewing the groups separately will provide more information.  The first line of code below generates a histogram of the data frame of the sepal length variable. I limited the data frame to the first 50 rows as these values are in the Iris setosa species.  By doing this, it outputs a histogram of only the sepal lenghts of the flowers in the setosa group.  Similarly, for the Iris- versicolor group the data frame was limited to the rows [50:100] as they contained the data relevant to this species and the final 50 rows were included in the data frame used to create the histogram for the Iris- virginica species.

	plt.hist(df["sepal_length"][0:50])

I used Matplotlib to add a title and axis titles to the histograms.

	plt.title("Sepal Length - Iris Setosa")
	plt.xlabel("Sepal length(cm)")
	plt.ylabel("No. of flowers")

I used the following code to save the histograms as a png file.  This were saved in the same folder as the python script.

	plt.savefig("Sepal Length- Iris setosa.png")

The code below is used to 'clear' the graph after it is saved or else the following histogram will be imposed on top of the preceding graph.

	plt.clf()


Lastly we were asked to output a scatter plot of each pair of variables. To do this I used Seaborn which is a data visualization library used with python.  The code below was used to create a 4 x 4 grid of all possible variable pairs.  
	sns.pairplot(df, hue="variety")
	plt.savefig("Scatter plot of variable pairs.png")
	
Each of the 3 groups (species) are in all the graphs with one of the four variables on the x-axis and another (or the same) on the y-axis.  Producing this type of graph makes comparing the 3 groups aross the different variables easier as all possible combinations are side by side.



[1]FISHER, R. A. (1936) ‘THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS’, Annals of Eugenics. doi: 10.1111/j.1469-1809.1936.tb02137.x.
[2] Kozak, Marcin & Łotocka, Barbara. (2013). What should we know about the famous Iris data?. Current science. 104. 579-580. 