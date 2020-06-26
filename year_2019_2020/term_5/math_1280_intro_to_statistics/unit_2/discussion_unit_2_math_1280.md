
# Discussion Unit MATH 1280

## Part 1
Fruits are categorical values or qualitative data. If I was going to code fruit into a data frame, they would be `factor` types. Furthermore, it does not make sense to "average" categorical variables, it does however make sense to get the mode or most common element.

## Part 2
Quiz scores are `numeric` values, in this situation at least, since you could also use other representations for scores such as letters, and in that case, they would be of type `factor`. 
```r
> qs <- c(94,93,85,0)
> mean(qs)
[1] 68
```
**68** is the mean score.

## Part 3
You can't really get the mean of categorical values, at least the information gathered wouldn't be very useful. In machine learning converting categorical variables to numeric is very common. For example, if I had a dependent variable saying that a service is active or inactive I could change those values like so: {active: 1, inactive: 0}, and if I get the mean of this data I might end up with any number between 0 and 1 such as 0.44. This doesn't exactly tell me a whole lot of useful information.

If I wanted to obtain something similar to the mean of a numerical value for a categorical value I would chose to use the mode instead. In this situation, the mode would be `A`, and these values would most definitely be coded as `factor`

## Part 4
The difference here is that the mean is of use with numerical values, and not of use with categorical values. Getting the mean of categorical values is usually not very helpful.