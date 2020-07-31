
# Assignment Unit 6 MATH 1280

1. The first task is to review some information that might be useful later:
   
* Write a brief definition of the word "quartile" as we have used it in previous weeks. Be sure to provide a citation: The word quartile refers to a data set that we split up into fours, where the first split represents the first quartile, the second split represents the seconds quartile and so on (p. 32, Statistical Inference).
* Write a brief definition of the word "quantile" as it might be used in statistics. Be sure to provide a citation (do not cut and paste... use your own words to summarize what you discovered): A quantile is very similar to a quartile, except in this case we have a greater degree of flexibility. In this case we can choose how many quantiles we want, whereas quartiles always result in a four way split (Quantile, Wikipedia). 
* From within interactive R, enter the command shown below (the command shows a help page for the pbinom command).  Provide a very brief description of the arguments that are passed to the pbinom() command ("arguments" in computer programming are the options that you give to a function so that the function can calculate what you want it to).  Note that one of the arguments is lower.tail = TRUE, and because there is a value assigned to it with the equals sign, it means that if you do not enter a new value for lower.tail, it will be set to TRUE by default.  Do not type the ">" into R, it is the command prompt: > ?pbinom

`pbinom(q, size, prob, lower.tail = TRUE, log.p = FALSE)`\
`q`: This is representative of the input for quantile, which can be a vector or a scalar value.\
`size`: This is representative of the number of trials or you could call them attempts.\
`prob`: This denotes the probability that `q` will occur in `size`.\
`lower.tail = TRUE`: When set to TRUE you get the probability to the right of `q`.\
`log.p = FALSE`: Converts all probabilities to logarithmic probabilities.

2. You can use the dbinom() command (function) in R to determine the probability of getting 0 heads when you flip a fair coin four times (the probability of getting heads is 0.5): dbinom(0, size=4, prob=0.5)

Find the equivalent values for getting 1, 2, 3, or 4 heads when you flip the coin four times.  TIP: after you run the first dbinom() command, press the up arrow and make a small change and run it again.

probability of getting  exactly 1 head: 0.2500

probability of getting exactly 2 heads: 0.3750

probability of getting exactly 3 heads: 0.2500

probability of getting exactly 4 heads: 0.0625

1. Use the pbinom() function in R to show the cumulative probability of getting 0, 1, 2, 3, or 4 heads when you flip the coin 4 times (this is the same as finding the probability than the value is less than or equal to 0, 1, 2, 3, or 4.)

probability of getting no more than 0 heads: 0.0625

probability of getting no more than 1 head: 0.3125

probability of getting no more than 2 heads: 0.6875

probability of getting no more than 3 heads: 0.9375

probability of getting no more than 4 heads: 1.0000

4. The following R command will show the probability of exactly 6 successes in an experiment that has 10 trials in which the probability of success for each trial is 0.5:

dbinom(6, size=10, prob=0.5)
(True/False) True

5. Read Yakir (2011, pp. 68-69) carefully review the meaning of the pbinom function (related to tests that a value will be “equal to” versus “less than or equal to” a criterion value).  What is the probability of getting fewer than 2 heads when you flip a fair coin 3 times (round to 2 decimal places)? 0.5

6. What is the probability of getting no more than 3 heads when you flip a fair coin 5 times (be sure to understand the wording differences between this question and the previous one—round to 2 decimal places)? 0.81

---------------------------------------------------

Information

The exponential distribution is a continuous distribution.  The main R functions that we will use for the exponential distribution are pexp() and qexp().   Here is an example of the pexp() function:

Leaves are falling from a tree at a rate of 10 leaves per minute. The rate is 10, or we can say that lambda = 10 (meaning 10 leaves fall per minute). The leaves do not fall like clockwork, so the time between leaves falling varies. If the time between leaves falling can be modeled with an exponential distribution, then the probability that the time between leaves falling will be less than 5 seconds (which is 5/60 of a minute) would be:

(note: this is an explanation of how pexp() works, you will answer a different question below)

   pexp(5/60, rate=10)

which is about 0.565 (meaning that the probability is a bit higher than 50% that the next time-span between leaves falling will be less than 5 seconds).

For tasks 7-12, assume that the time interval between customers entering your store can be modeled using an exponential distribution. You know that you have an average of 4 customers per minute, so the rate is 4, or you can say that lambda = 4  according to Yakir (2011, p. 79-80). 

It is easiest to keep everything in the original units of measurement (minutes), but you can also translate that to seconds because a rate of “4 customers per minute” is the same as “4 customer per 60 seconds,” and you can divide each number by 4 to get a rate of “1 customer per 15 seconds” or a rate of “1/15 customers per second.” 

7. What is the expectation for the time interval between customers entering the store?  Be sure to specify the units of measurement in your answer (see Yakir, 2011, pp. 79-80).  Round to 3 decimal places: 0.234 hours.

8. What is the variance of the the time interval?  Be sure to specify the units of measurement in your answer. Round to 3 decimal places: 22.667 minutes

9. The pexp() function is introduced at the bottom of Yakir, 2011, p. 79, and there are some tips above.  What is the probability that the time interval between customers entering the store will be less than 15.5 seconds. Be sure to enter values so that everything is in the same unit of measurement.  Be sure to specify the units of measurement in your answer.  Round your answer to 3 decimal places: 0.644 hours.

10) What is the probability that the time interval between customers entering the store will be between 10.7 seconds and 40.2 seconds (see Yakir (2011, p. 79-80)? 0.421

11) The qexp() function in R allows you to enter a probability, and it will tell you the criterion value (“cutoff point”) that corresponds to that probability value (e.g., if you enter .05 it tells you the cutoff point below which 5% of the values in the distribution fall). 

What value of x would be the criterion value (cut-off point) for the top 5% of time intervals (Round to 3 decimal places, and include the units of measurement)? 0.749

---------------------------------

12) Describe in your own words the meaning of the number that the following R command produces (you are asked to interpret the resulting number so that we understand what that number means).

pexp(1.2, rate=3)

The result of the function is the cumulative probability that 1.2 will occur in 3.

---------------------------------

Information

You have now had practice with the binomial distribution and the exponential distribution.  The approach to solving problems for the normal distribution is similar to that for the exponential function, but obviously you use different R functions (usually pnorm() or qnorm()).

For the following three exercises, assume that you have a normally distributed random variable, called A, with a mean of  7, and a population standard  deviation of 3.

13. What is the probability that a randomly selected value from variable A will be greater than 9 (see Yakir, 2011 p. 88-89, 100)? 0.748

14. What value of variable A would be the cutoff point (criterion value) for identifying the lowest 4% of values in variable A (use the qnorm function)? 6.240

15. What is the probability that a randomly selected value from variable A will be more than one standard deviation above its mean (there are couple ways to solve this, one way is to use the standard normal distribution, Yakir, 2011, p. 90-91) ? 0.159

References:
n.a. (n.d.). Quantile. Retrieved from https://en.wikipedia.org/wiki/Quantile
Yakir, B. (2011). Introduction to Statistical Thinking. The Hebrew University.