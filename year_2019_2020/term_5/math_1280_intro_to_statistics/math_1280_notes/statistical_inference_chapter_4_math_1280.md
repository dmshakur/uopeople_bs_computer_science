
# Statistical Inference Chapter 4 MATH 1280 Notes

## Probability

### 4.2: Different forms of variability
Data is obtained by selecting from the target population and measuring the quantities of interest for the subjects that belong to the sample.

There are various ways to summarize the variability of data typically with the many visualization tools available like box plots and histograms.

Different measurements like the inter-quartile range and mean can tell us about the spread or range of our data.

We can use these diagrams and ranges for investigating our data.

The variability of a random variable is not unlike the probability of our selecting a sample from a population. 

Variability is a certain level of uncertainty, and chance, in this context.

The variability of the data is related to observable values and data points we can examine. As far as the rest of the measures of variability go, they are less concrete and not explicitly derived from observable quantities.

### 4.3: A population
In most cases where large populations are considered we cannot take the entire populations data, so we sample. A problem in statistics is when we try to guess the unknown quantity on the basis of the data we don't have.

A attribute of a population is a parameter, while an attribute of a sample is a statistic. Quartiles and medians are examples of both.

The sample variance is created with the sum of squared differences between the observations and the mean. Sample variance is denoted as $s^2$.

The standard deviation of the population is denoted with $\sigma$, and is the square root of the variance. When we want to know the general variation of a data set we can use the 

Sample variance:
$$ 
s^2=\frac{\sum_{i=1}^N(x_i-\bar{x})^2}{N-1}
$$

Population variance:
$$ 
\sigma^2=\frac{\sum_{i=1}^N(x_i-\mu)^2}{N}
$$

### 4.4: Random variables
Now we will consider the variability of a random variable.

A random variable is th future outcome of a measurement, before the measurement is taken. Therefore a random variable is like the potential of what can be obtained from your data. But once you take a value, or random variable (which I think is just an observation, or maybe its an observations attribute), it ceases to be a random variable. Because we know what it is it is no longer random.

You can't know for certain what a random variable is or will be, but you may find patterns that could give you a probability of what could be obtained.

In reference to random variables we call the approximated chance we will draw on a specific random variable a probability.


### 4.4.1: Sample space and distribution
The formal definition of a random variable.\
A random variable refers to numerical values, typically the outcome of an observation, a measurement, or a function thereof.

You may grab a random variable from the possible values in what is called the sample space. The probability that you will grab any one random variable is the height of the distribution divided by the total frequency of variables.

Random variables are denoted with upper case letters. Values that we may get from them are denoted as lower case letters.

The following equation is tell us the the probability of $X$ being obtained is the right side value.
$$
P(X=168)=0.03476
$$

If we wanted to find the probability of finding a value that was a certain distance, $Y$, from a point in our data we could take $X$ and subtract $Y$. Then take the absolute value and check its relation to the condition. Such as: $P(|X-170|\leq10)$.

If we take the mean of the result of the previous

If we apply the subtraction of a value to a list and apply get the absolute value of that, then we have the distance of each value from the subtracted value. If we don't take the absolute value we can get the distance and direction, if needed.

When you take the mean of a sequence of logical expressions with boolean results, the true values become ones and the false values become zeros. Thus the percentage of true values is the result.

The probability function of a random variable is defined for any value that the random variable may obtain and produces the distribution of the random variable.

Subsets of values are denoted as events.

### 4.4.2: Expectation and standard deviation
It is possible to calculate the mean with a method other than adding all the values up and dividing by $n$. Equation: $\sum_xx\frac{f_x}{n}$.

The expectation is the sum of the products of $x$ and the probability of $x$. The expectation equation:
$$
E(X)=\sum_xxP(x)
$$

Two variants of the sample variance equation:
$$
s^2=\frac{\sum_{i=1}^n(x_i-\bar{x})^2}{n-1}
\\ \texttt{} \\
s^2=\frac{n}{n-1}\sum_x(x-\bar{x})^2\frac{f_x}{n}
$$

The variance equation:
$$
Var(x)=\sum_x(x-E(X))^2P(x)
$$
The variance equation is very similar to the second variant of the sample variance equation, except $\bar{x}$ is replaced the expectation, $E(X)$, and the relative frequency is replaced with the probability.

The standard deviation of a random variable is the square root of the variance.

### 4.5: Probability and statistics
Probability serves as the mathematical foundation for the development of statistical theory.

### 4.6: Exercises
Question 4.1.
1. $\frac{1}{21}$
2. $\frac{6}{21}$
3. $\frac{12}{21}$
4. $\frac{9}{21}$
5. $\frac{12}{21}$
6. $\frac{68}{21}$
7. $-\frac{153}{21}$
8. $0.585015089$

Question 4.2.
1. 0.125
2. 0.875

### 4.7 Summary
Glossary
* Random variable: The probabilistic model for the value of a measurement, before the measurement was taken.
* Sample space: The set of all values a random variable may obtain.
* Probability: A number between 0 and 1 which is assigned to a subset of the sample space. This number indicates the likelihood of the random variable obtaining a value in that subset.
* Expectations: The central value for a random variable. The expectation of the random variable $X$ is marked by $E(X)$.
* Variance: The (squared) spread of a random variable. The variance of the random variable $X$ is marked by $Var(X)$. The standard deviation is the square root of the variance.

### Discussion in the Forum
Random variables are used to model situations in which the outcome, before the fact, is uncertain. One component in the model is the sample space. The sample space is the list of all possible outcomes. It includes the outcome that took place, but also all other outcomes that could have taken place but never did materialize. The rationale behind the consideration of the sample space is the intention to put the outcome that took place in context. What do you think of this rationale?When forming your answer to this question you may give an example of a situation from you own field of interest for which a random variable can serve as a model. Identify the sample space for that random variable and discuss the importance (or lack thereof) of the correct identification of the sample space.For example, consider a factory that produces car parts that are sold to carmakers. The role of the QA personnel in the factory is to validate the quality of each batch of parts before the shipment to the client. To achieve that, a sample of parts may be subject to a battery of quality test.Say that 20 parts are selected to the sample. The number of those among them that will not pass the quality testing may be modeled as a random variable.The sample space for this random variable may be any of the numbers 0, 1, 2,. . . , 20. The number 0 corresponds to the situation where  all parts in the sample passed the quality testing. The number 1 corresponds to the case where 1 part did not pass and the other 19 did. The number 2 describes the case where 2 of the 20 did not pass and 18 did pass, etc.



### Summary of formulas
Population size:
$$
N=\textrm{the number of observations in the population}
$$
Population average:
$$
\mu=\frac{1}{N}\sum_{i=1}^{N}x_i
$$
Expectation of a random variable:
$$
E(X)=\sum_xxP(x)
$$
Population variance:
$$
\sigma^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\mu)^2
$$
Sample variance:
$$
s^2=\frac{1}{N}\sum_{i=1}^{N}(x_i-\bar{x})^2
$$
Variance of a random variable:
$$
Var(X)=\sum_x(x-E(X))^2P(x)
$$