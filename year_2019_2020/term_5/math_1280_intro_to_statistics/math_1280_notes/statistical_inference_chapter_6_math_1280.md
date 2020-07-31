
# Statistical Inference Chapter 6 MATH 1280

## The normal random variable

### 6.1: Student learning objective
The normal distribution is of a bell shape. It may serve as an approximation of other distributions. 

### 6.2: The normal random variable
The normal distribution is the most important of all that are used in statistics. Often times when using other distributions (e.g. Poisson), we find a normal distribution within.

### 6.2.1: The normal distribution
A normal random variable has a continuous distribution over the sample space of all numbers. It is denoted as $X\sim\textrm{Normal}(\mu,\sigma^2)$ and $\mu=E(X))$ and $\sigma^2=\textrm{Var}(X)$.

A normal random variable is more likely to obtain its value around the expectation. Values much larger or smaller than the expectation are substantially less likely, I think this is meant to say it is decreasing in density.

The R function `dnorm(x, mean, sd)` computes the density of the normal distribution.

The R function `pnorm(x, mean, sd)` computes the cumulative probability of the normal distribution.

The mean is set to `0` by default and the sd is set to `1` by default.

The smaller the variance the more concentrated the distribution of the random variable is about the expectation.


#### Example 6.1: `plot(dnorm(0:300, 100, 15), type = 'l')`.

### 6.2.2: The standard normal distribution
The standard normal distribution of standardized values, which are called z-scores. A z-score is the measurement measured in units of the standard deviation from the expectation.

If the expectation of a normal distribution is $2$ and the standard deviation is $3$, then the value of $0$ would be $2/3$ standard deviations smaller than the expectation.

$$
z=\frac{x-E}{\sigma}
$$

The standard normal distribution is the distribution of a standardized normal measurement. The expectation of the standard normal distribution is $0$ and the variance is $1$.

The R function `qnorm(probability, mean, sd)` computes the percentiles of the normal distribution. I believe that this function computes the amount of standard deviations away from the mean the probability is.

### 6.2.4: Outliers and the normal distribution
Using `qnorm` you can compute quartiles by simply specifying the percentage associated with that quartile, 0.25 for the first, 0.5 for the second, etc.

### 6.3: Approximation of the binomial distribution
The central limit theorem is how the normal distribution can emerge frequently in data.

### 6.3.1: Approximate binomial probabilities and percentiles

### 6.3.2: Continuity corrections

### 6.4: Exercises
Question 6.1
1. 