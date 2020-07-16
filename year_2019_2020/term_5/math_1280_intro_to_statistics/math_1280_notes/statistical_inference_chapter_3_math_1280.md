
# Statistical Inference Chapter 3 MATH 1280

## Descriptive Statistics
### 3.1: Student learning objective
* Use histograms and box plots in order to display data graphically.
* Calculate measures of central location: mean and median.
* Calculate measures of the spread: variance, standard deviation, and inter-quartile range.
* Identify outliers, which are values that do not fit the rest of the distribution.

### 3.2: Displaying data
A statistical graph is a tool that helps you learn about the shape of the distribution of a sample. This can help with identifying outliers and clusters in the dataset.

#### 3.2.1: Histograms
A histogram consists of contiguous boxes. It has an x and y axis, the x axis is labeled with what the data represents, and the y axis presents the frequencies. The histogram is constructed by dividing the range of the data (x-axis) into equal intervals. 

#### 3.2.2: Box plots
The box plot is constructed from five values:
* Smallest.
* 1st Quartile.
* The median.
  * The center of the data.
  * It separates the data into halves, where half the values are smaller and the other half are larger, or equal.
  * The median does not have to be the a value in the dataset, it just has to be in the center.
  * Also the 2nd quartile.
* 3rd Quartile.
* Largest.

Quartiles are numbers that separate the data into quarters
* The first quartile is the middle value of the lower half of the data.
* The second quartile is the middle value of the data.
* The third quartile is where $\frac{3}{4}$ of the values are less than and one fourth is greater than.

Data points that are much to large or much too small in comparison to the vast majority of the of the observations will be identified as outliers.

The inter-quartile range is: $IQR=Q_3-Q_1$. A data point that is larger than the third quartile plus 1.5 times the inter-quartile range will be marked as a potential outlier. Likewise the data point smaller than the first quartile minus 1.5 times the inter-quartile range will also be marked as an outlier.

### 3.3: Measures of the center of data
The most popular measures of the central location of the data is mean and median. The median is a better measure when dealing with outliers but the mean is more commonly used. 

A sample can be denoted as such: $\bar{x}$.

The mean can be calculated by averaging all the data point or it can also be calculated with the relative frequencies of the values that are present in the data. In the latter one multiplies each distinct value by its relative frequency and then sums the products across all values. 

#### 3.3.1: Skewness, the mean and the median
A distribution is symmetrical if a vertical line can be drawn at some point in the histogram such that the shape to the left and to the right of the vertical line are mirror images of each other.

Skewing is the direction of the data goes. The relation between the mean and the median reflects skewing. 

If the distribution of the data is skewed to the left then the mean is less than the median. If the distribution is skewed to the right then the median is less than the mean.

### 3.4: Measures of the spread of data
One measure of the spread of the data is the inter-quartile range, however the most important measure is the standard deviation. In a dataset there are as many deviations as there are data values. The variance is in principle the average of the squares of the deviations. 

When you take away the average of the observations of the result of: $x-\bar{x}$, upon making that calculation we obtain the deviations. 

To get the variance we sum the square of the deviations and divide by the total number of data values minus one. The standard deviation is obtained by taking the square root of the variance.

#### Getting the variance in R:
`sum((x - x.bar)^2) / (length(x) - 1)`

$\textrm{variance}=\sum_{i=0}^n\frac{(x - \bar{x})^2}{n - 1}$

#### Getting the standard deviation in R:
`sqrt(sum((x - x.bar)^2) / (length(x) - 1)`

$\textrm{standard deviation}=\sqrt{\sum_{i=0}^n\frac{(x - \bar{x})^2}{n - 1}}$

If the variance is provided as a result of dividing the sum of squares by the number of observations minus one then we call that the *sample variance*. If we were to not calculate that subtraction operation, it would be called the population variance. The reason for this comes from the theory of statistical inference. Unless the data is small dividing by $n$ or $n-1$ does not introduce much of a difference.

The variance is a squared measure and does not have the same units as the data. Taking the square root solves this problem. The standard deviation measures the spread of the data in the same units as the data.

The sample standard deviation is either 0 or larger than 0. When it is 0, there is no spread and the data values are very spread out over the mean. Outliers can make the standard deviation very large.

The standard deviation is a measure of how far out values are from the mean. For example: If the data contains the value 7 and if the mean is 5 and the standard deviation is 2, then the value 7 is one standard deviation away from the mean, because $5+1\times2=7$. 

In symmetrical distributions the standard deviation is very helpful but in skewed distributions it is less so. The reason being, the two sides of a skewed distribution have different spreads. In a skewed distribution, it is better to look at the first quartile, the median, the third quartile, the smallest value, and the largest value.

## Exercises

#### Question 3.1
1. 
   * x1 -> Histogram 1 -> Box plot 2
   * x3 -> Histogram 2 -> Box plot 3
   * x2 -> Histogram 3 -> Box plot 1
2. Yes
3. No

#### Question 3.2
1. 4.666667
2. 2.425914
3. 4
4. 4
5. 2.198347

## Glossary
* Median: A number that separates ordered data into halves: half the values are the same number or smaller than the median and half the values are the same number or larger than the median. The median may or may not be part of the data.
* Quartiles: The number that separates the data into quarters. Quartiles may or may not be part fo the data. The second quartile is the median of the data.
* Outlier: An observation that does not fit the rest of the data.
* Inter-quartile range (IQR): The distance between the third quartile (Q3) and the first quartiles (Q1). IQR = Q3 - Q1.
* Mean: A number that measures the central tendency. A common name for mean is average. The term mean is a shortened form of arithmetic mean. By definition, the mean for a sample (denoted by $\bar{x}$) is $\bar{x}\frac{\textrm{sum of all values}}{\textrm{number of values}}.
* Sample variance: Mean of the squared deviations from the mean. Square of the standard deviation. For a set of data, a deviation can be represented as $x-\bar{x}$ where $x$ is a value of the data and $\bar{x}$ is the sample mean. The sample variance is equal to the sum of the squares of the deviations divided by the difference of the sample size and 1.
* Sample standard deviation: A number that is equal to the square root of the variance and measures how far data values are from their mean. $s=\sqrt{s^2}$.

### Discussion 
It would definitely depend. In machine learning and data science outliers are generally something that we try to get rid of outliers are they can cause issues with the interpretability of the data. For example if we were to try and create a report for a company trying to tell them what kind of customers we have (age, background, interest in the company), outliers are not a typical representation of what our customer base looks like. Therefore we might want to rid ourselves of the outliers in favor of more consistent and reportable results. 

Commonly Used Symbols

The symbol∑means to add or to find the sum.
n= the number of data values in a sample.
x= the sample mean.
s= the sample standard deviation.
f= frequency.
f/n= relative frequency.
x= numerical value.Commonly Used Expressions
x×(fx/n) = A value multiplied by its respective relative frequency.
∑ni=1xi= The sum of the data values.
∑x(x×fx/n)= The sum of values multiplied by their respective relativefrequencies.
x− ̄x= Deviations from the mean (how far a value is from the mean).
(x− ̄x)2= Deviations squared.Formulas:
Mean:   ̄x=1n∑ni=1xi=∑x(x×(fx/n))•Variance:s2=1n−1∑ni=1(xi− ̄x)2=nn−1∑x((x− ̄x)2×(fx/n))
Standard Deviation:s=√s2
