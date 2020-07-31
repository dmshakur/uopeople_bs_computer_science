
# Learning Journal Unit 6 MATH 1280

## Part 1
#### Date 07/23/20
Finished learning journal for unit 5, MATH 1280.
Participated in research study.
#### Date 07/24/20
Participated in research study.
#### Date 07/25/20
Read Statistical Inference chapter 6.
#### Date 07/26/20
Worked on logger and unit tests for A.I.E.W. certification, almost complete.
#### Date 07/27/20
Worked on MATH 1280 notes and discussion post.
#### Date 07/28/20
Worked on MATH 1280 notes and self-quiz.
#### Date 07/29/20
Worked on MATH 1280 assignment, and graded quiz.
Worked on data science automation project, fully implemented, just need to debug.
#### Date 07/30/20
Finished MATH 1280 learning journal. 

## Part 2
#### A:
The normal distribution is the most commonly used distribution. It is most effective when you have a large sample space and least effective when you have the inverse. When people take samples of a population they often find that data forms a normal distribution, since there are observations that represent the most common occurrence and as you get further away from this central commonality you end up with ever lower probabilities. This particular distribution can be described as bell-shaped (Yakir, B., 2011).

Yakir, B. (2011). Introduction to Statistical Thinking. The Hebrew University

#### B:
The `pnorm` function is very similar to the dnorm function in that it calculates the probability that something will occur. However, the main difference here is that the `pnorm` function calculates the cumulative probability versus the density. 

N.a. (n.d.). Normal, The normal distribution. Retrieved from https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/Normal

## Part 3
In the R repl, any value that is equal to or less than 28.47304 is in the first percentile, $x\le1\%$ and any value that is equal to or higher than 121.527 is in the last percentile, $x\ge99\%$. 
```R
> x <- 0:150
> mean <- 75
> s.d <- 20
>
> qnorm(0.99, mean, s.d)
[1] 121.527
> qnorm(0.01, mean, s.d)
[1] 28.47304
```
