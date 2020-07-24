
# Statistical Inference Chapters 5 MATH 1280 Notes

## Random variables

### 5.1: Student learning objectives
In this section 4 different kinds of random variables will be observed:
* Continuous
  * Exponential
  * Uniform
* Discrete
  * Binomial
  * Poisson

### 5.2 Discrete random variables
Once again the textbook is repeating itself, I am really feel like this book is quite bloated. Why would you explain something over and over again, maybe it's just me.

A random variable is both the 'identification' of its sample space or data set and its probability.

A random variable where the values are separated by a space like integers, is called a discrete random variable. Binomial and poisson random variables are discrete.

Describing a random variable:
* The expectation is used to describe the central location, not the mean. The mean is used for the data as a whole.
* The variance and standard deviation are use to describe the spread.
* Parallel summaries are used for random variables (What is a parallel summary?).

### 5.2.1: The binomial random variable
The binomial random variable is used in settings where a trial has two possible outcomes that are repeated several times. To me this sounds like binary classification in ML. The outcome of the probability of successes for $n$ number of trials is what the binomial random variable will be. Sounds to me like it's the same thing as accuracy for a binary classification problem. 

A binomial distribution is viewed where $x$ is the amount of times that an event occurred and $y$ is the probability of occurrence.

The R function `dbinom(x, n (trials), prob)` is used for making this calculation. The output of this function is a sequence of the same size where each variable is the probability that the corresponding value will be the number of times out of $n$ that an event will happen. By getting the sum of the output of `dbinom` you can get the probability that all the events will occur.

The R function `pbinom(x, n (trials), prob)` produces the cumulative probability of the binomial.

In the case of the binomial random variable the expectation and the variance is reduced to: $E(X)=np$, $Var(X)=np(1-p)$. Where $n$ is the probability and $n$ is simply $n$ number of times.

### 5.2.2: The poisson random variable
This distribution is used as an approximation of the total number of occurrences of rare events. It's convenient when the maximum number of events is unknown or very large.

The poisson distribution is specified by the expectation, which we denote as $\lambda$. 

The R function `dpois(x, λ)` computes the probability.

The R function `ppois(x, λ)` computes the cumulative probability of the values of `x`.

To compute the expectation of a poisson distribution multiply `x` by the output of `dpois`.

In the poisson distribution the following is always true: $E(X)=Var(X)=\lambda$.

### 5.3: Continuous random variable
You have a continuous random variable when the outcome is an entire line of real numbers or interval.

With discrete variables you may use every possible value, but where continuous variables are concerned you will use an interval of values. Densities will often be used.

Where we will use the expectation formula: $E(X)=\sum_xxP(x)$, in continuous variables we turn it into the following:
$$
E(X)=\int(xf(x))dx
$$
where $f(x)$ is the density of $X$ at the value of $x$.

The variance formula is also replaced with:
$$
Var(X)=\int((x-E(X))^2f(x))dx
$$
Nonetheless, the intuitive interpretation of the expectation as the central value of the distribution that identifies the location and the interpretation of the standard deviation as the summary of the total spread of the distribution is still valid.

### 5.3.1: The uniform random variable
This distribution is used to model measurements that may have values in a given interval, with all values in this interval equally likely to occur.

The R function `dunif(x, interval_beg, interval_end)` can be used to compute the density of the Uniform distribution over the a set of integers. The density doesn't have to use integer values.

The R function `punif(x, interval_beg, interval_end)` computes the cumulative probability of the uniform distribution.

If any value in $x$ occurs outside of the interval then the probability of the outcome occurring is 0.

The expectation of a uniform random variable is in its center, where the equation is equal to: $E(X)=\frac{a+b}{2}$.

The variance of a uniform random variable is in its center, where the equation is equal to: $\textrm{Var}(X)=\frac{(b-a)^2}{12}$.

### 5.3.2: The exponential random variable
The exponential distribution is frequently used to model times between events. It is denoted as $X\sim\textrm{Exponential}(\lambda)$. There is a deliberate overlap between this distribution and the poisson distribution. If the distribution between events has an exponential distribution with a rate of $\lambda$ then the total number of occurrences within a unit interval of time has a poisson distribution.

The R function `dexp(x, prob)` computes the exponential distribution of an exponential random variable.
The R function `pexp(x, prob)` computes the cumulative probability of an exponential random variable.

The expectation of $X$ is given by the equation: $E(X)=1/\lambda$, and the variance is given by: $\textrm{Var}(X)=1/\lambda^2$.

There is generally a decrease in probability with an increase in $\lambda$

### 5.4: Exercises
Question 5.1
1. Using the equation for the expectation we get: $E(X)=np500\times0.09=45$.
2. To get the standard deviation we get the square root of the variance, $\textrm{Var}(X)=np(1-p)=500\times0.09\times0.91=40.95$.
3. 0.7556474


Question 5.2
1.
```R
> plot(dnbinom(0:15, 2, 0.5), type='h', col='blue', pch='o', lty=1)
> points(dnbinom(0:15, 4, 0.5), col='red', pch='*')
> lines(dnbinom(0:15, 4, 0.5), col='red', lty=2)
> points(dnbinom(0:15, 8, 0.8), col='dark red', pch='+')
> lines(dnbinom(0:15, 8, 0.8), col='dark red', lty3=3)
```