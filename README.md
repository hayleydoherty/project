# project
programming and scripting project

## Fisher's Iris Data Set

British biologist and statistician Ronald Fisher first published his *Iris data set* in 1936 in his paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis[1].  This data set is commonly used in statistics, pattern recognition and visualisation to this day.  The data set consists of 50 samples from three species of iris, Iris setosa, Iris virginica and Iris versicolor. From each of the 150 samples, four measurements were taken which were the length and width of both petal and sepal. A small problem with the dataset is that there is disagreement amongst botanists as to whether the Iris plant has sepals! However this problem has not had an effect on the use of the dataset for statistical purposes as *Web of Science* lists roughly 4000 citations to Fisher's 1939 paper [2]. 


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

A test for normality was performed on each group of data to determine if they were normally distributed.  The test used for this was Shapiro's test and an example of the code and the output is below.  The result is output as (test statistic, p-value).  The p-value below is not significant (> 0.05) meaning that the data is normally distributed. 
	
	stats.shapiro(setosa['sepal_width'])
	(0.968691885471344, 0.20465604960918427)

Following these tests I determined that the Fisher dataset could be analysed parametrically and so went on to perform a one-way ANOVA.  I used a function in the SciPy module to perform this analyses.  Below is an example of the code used to perform the ANOVA test.  In this example, sepal width of the three species of Iris are being comapred against each other.  The result, also below, shows that there is a significant difference between the three groups as the p-value is below 0.05.  In order to determine exactly which groups are different from each other I next performed post-hoc analysis.

	stats.f_oneway(setosa['sepal_width'], versicolor['sepal_width'], virginica['sepal_width'])
	F_onewayResult(statistic=47.36446140299382, pvalue=1.3279165184572242e-16)
	
To perform the post-hoc analysis I imported another Python module called statsmodels after seeing an example of it being used for post-hoc testing on pythonfordatascience.org[3].  I chose Tukey's test as it compares the means of all pairs of groups so we can determine which groups are different to the others.  
	
	mc1 = MultiComparison(df['sepal_width'], df['variety'])
	print(mc1.tukeyhsd())

Below is an example of the results output by the Tukey post-hoc test.  This example is a comparison of the mean sepal width between the different species of iris.  The null hypothesis which states that there arer no differences between the groups is rejected in all cases meaning that all groups are significantly different from each other.

					 Multiple Comparison of Means - Tukey HSD, FWER=0.05          
		======================================================================
			 group1          group2     meandiff p-adj   lower   upper  reject
		----------------------------------------------------------------------
			Iris-setosa Iris-versicolor   -0.648  0.001 -0.8092 -0.4868   True
			Iris-setosa  Iris-virginica   -0.444  0.001 -0.6052 -0.2828   True
		Iris-versicolor  Iris-virginica    0.204 0.0089  0.0428  0.3652   True
		----------------------------------------------------------------------


Next we were asked to create histograms of each variable and save them as png files.  I used Matplotlib to do this.  For each variable, I wanted to split the data into the three species groups as I believe viewing the groups separately will provide more information.  The first line of code below generates a histogram of the data frame of the sepal length variable. I limited the data frame to the first 50 rows as these values are in the Iris setosa species.  By doing this, it outputs a histogram of only the sepal lenghts of the flowers in the setosa group.  Similarly, for the Iris- versicolor group the data frame was limited to the rows [50:100] as they contained the data relevant to this species and the final 50 rows were included in the data frame used to create the histogram for the Iris- virginica species.

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
	
Each of the three groups (species) are in all the graphs with one of the four variables on the x-axis and another (or the same) on the y-axis.  Producing this type of graph makes comparing the three groups aross the different variables easier as all possible combinations are side by side.


## My Findings
Based on the results from the descriptive statistics and the tests for normality and homogeneity of variance, I concluded that the data wassuitable to be tested parametrically.  As there are more than two groups using t-tests would be inappropriate so I chose to use one-way ANOVA tests to analyse the data.  The first variable I will discuss is sepal width.  The results of the ANOVA indicated that there was a significant difference between the species in regards to their sepal width as the p-value was less than 0.05.  The Tukey post-hoc test revealed that the sepal width of all three species of iris were different to each other.  

		![Boxplots of Sepal Width](C:\Users\Hayle\Documents\H DIP\Programming\project\SepalWidth.png?raw=true "Sepal Width")
		
The next variable to look at is sepal length.  The results of the ANOVA indicated that there was a significant difference between the species in regards to their sepal length as the p-value was less than 0.05.  The Tukey post-hoc test revealed that the sepal length of all three species of iris were different to each other.  		

	![Boxplots of Sepal Length](C:\Users\Hayle\Documents\H DIP\Programming\project\SepalLength.png?raw=true "Sepal Length")

As with the results for sepal width and length, the results for petal width and length showed that each group was statistically different from the others.  Tukey's post-hoc tests revealed that the null hypothesis could be rejected for all of the comparisons made, meaning all groups were different to each other.

	![Boxplots of Petal Width](C:\Users\Hayle\Documents\H DIP\Programming\project\PetalWidth.png?raw=true "Petal Width")

	![Boxplots of Petal Length](C:\Users\Hayle\Documents\H DIP\Programming\project\PetalLength.png?raw=true "Petal Length")


My findings suggest that it is possible to classify an Iris flower as a member of one of these three species based on the measurements analysed above; sepal width and length and petal width and length.  It also appears that the setosa species is less closely related to the other two species as versicolor and virginica are to each other as the differences in variables measured appears to be bigger between the setosa group and versicolor group and the setosa group and virginica group compared to the differences between the versicolor and virginica groups.







[1]FISHER, R. A. (1936) ‘THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS’, Annals of Eugenics. doi: 10.1111/j.1469-1809.1936.tb02137.x.
[2] Kozak, Marcin & Łotocka, Barbara. (2013). What should we know about the famous Iris data?. Current science. 104. 579-580. 
[3]https://pythonfordatascience.org/anova-python/