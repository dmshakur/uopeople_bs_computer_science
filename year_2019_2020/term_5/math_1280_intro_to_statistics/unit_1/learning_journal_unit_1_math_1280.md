
# Learning Journal Unit 1 MATH 1280

## Part 1:
### Date: 06/18/20
I completed all the learning materials for this week before 13:00, except for the comments needed for the discussion forum, that is something that I will have to do throughout the week as more people write posts.

I have only had one issue with the material this week and that was in regard to a question on the self-quiz, question 6 specifically.

> The average number of calls that arrived between 8:00 AM and 8:10 AM during the working days of any month is:

I am not 100% sure I understand why this particular questions answer is parameter, instead of statistic. I think I can understand its a parameter because we are saying any month, and I'm not sure if saying any constitutes literally any month instead of just any of the provided data from the months of Sep. and Feb.

Other than that there haven't been any issues or problems with the material.

## Part 2:
The first row in the table represents the numbers present in the list, and the second row is the frequency of the above value, or how many times it appears in the list. I don't need to alter the table to test my theory, all I have to do is look at the available data and see in the table that `9` is in the first row but not the second, then I can look at the list of values and determine there is a nine in it. Therefore the top row would have to be the actual values, not the frequency.
```R
x <- c(5, 8, 4, 1, 5, 6, 5, 9, 4, 2, 5, 7, 5, 3, 6, 4, 5, 3, 7, 6)

table(x)
```
#### Output:
```R
1 2 3 4 5 6 7 8 9 
1 1 2 3 6 3 2 1 1 
```

## Part 3:
 <!-- Task (References: Question 1.1 page 10-12 and self-Quiz Unit 1 Question 6 and 7)

a) Read section 1.5 in the Yakir textbook.  If you were a teacher and had 30 students in your class and wanted to know the class average on the first quiz, would you use a parameter or a statistic?  Why?

b) If you wanted to know how many people in your country recognize the name of your new company, would you use a parameter or a statistic?  Why? -->
### Part A:
This would be an example of a parameter since you were only interested in a single class. If you were however interested in an entire school but only used one classes data as a measurement for how well the school is doing, then you would be using a statistic.

### Part B:
If I wanted to know how many people knew the name of my new company I would use a statistic. Using a parameter in this case would result in a massive workload, that is unrealistic to achieve. Since there are over 300 million people in the country, finding every single one of them would be the only way to determine the opinion of the population, of my country. I would instead come up with someone to reach as many people as I can, or leverage data science strategies such as web crawling and machine learning to find references to my company on places like twitter. Since places like twitter or instagram are places where many people socialize, it is reasonable to say that the percentage of people that are aware of my company's name is representative of the rest of the population. At least that would be far more reasonable than drawing a parameter from the population.