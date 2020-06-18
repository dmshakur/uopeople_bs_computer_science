
# Statistical Inference Chapter 1 MATH 1280

## Probability
Probability is the mathematical theory used to study uncertainty. It deals with the chance of an event occurring, and different potential outcomes.

## Key terms
* Sampling: Taking information about a portion of a population and using it for statistical study. Such is data.
* Statistic: A number that is a property of a sample.
* Parameter: A number that is a property of a population.

# R programming environment
Numbers in R can be added together like so:
```R
1+2
```
#### Output:
```R
[1] 3
```
A function in R can be created like so:
```R
 c(5,5.5,6,6,6,6.5,6.5,6.5,6.5,7,7,8,8,9)
```
#### Output:
```R
[1] 5.0 5.5 6.0 6.0 6.0 6.5 6.5 6.5 6.5 7.0 7.0 8.0 8.0 9.0
```
You can save a vector of data under a name such as "x", like so:
```R
x <- c(5,5.5,6,6,6,6.5,6.5,6.5,6.5,7,7,8,8,9)
```
The `<-` operator is the assignment operator in R. Where it can assign something such as a function a number or an expression to text.

One can create a table that contains a count of the frequency of the different values in the data with the `table` function.
```R
table(X)
```
#### Output:
```R
5 5.5 6 6.5 7 8 9
1 1   3 4   2 2 1
```
A bar plot can be created with this table by wrapping it is a `plot()` function.
```R
plot(table(X))
```

## Exercises
#### Question 1.1
1. 500 registered voters are part of a population, and are a **sample**.
2. The percentage of registered voters for a whole party is a **parameter**.
3. The 42% of voters that prefer a female candidate are a **statistic**.
4. The voters that are registered to a certain party are a **population**.

#### Question 1.2
1. Number of days in which 5 customers where waiting: **3**.
2. Number of waiting customers that occurred the largest number of times: **1**.
3. THe number of waiting customers that occurred the least amount of times: **0**.

## Glossary
* Data: A set of observations on a sample from a population.
* Statistic: A numerical characteristic of the data. A stat estimates the corresponding population parameter.
* Statistics: The science of dealing with processing, presentation, and inference of data.
* Probability: A mathematical field that models and investigates the notion of randomness.

### Discuss in the forum
Yes it is appropriate to represent a population only by a sample. With the statistical tools available to us today that give us insight into and the ability to understand our data, we have the power to understand if even our data isn't sufficient, and that we need more. There are also times when we will not be able to obtain data from a population without extremely excessive work that far exceeds our abilities over a length of time that is reasonable, for example: the population of the United States. 