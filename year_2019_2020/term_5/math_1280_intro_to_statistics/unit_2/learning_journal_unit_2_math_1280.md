
# Learning Journal Unit 2 MATH 1280

## Part 1
### Daily Reflections
#### Date: 06/25/20
Worked on last weeks learning journal. Ran 21 miles. Finished learning journals for math 1280, 1201.
#### Date: 06/26/20
Completed reading, notes, self-quiz and assignment for MATH 1280.
#### Date: 06/27/20
Learned we scraping. Worked on web scraping project.
#### Date: 06/28/20
Started speech transcription project.
#### Date: 06/29/20
Worked on speech transcription project.
#### Date: 06/30/20
Learned how to use Docker. Worked on web scraping project.
#### Date: 07/01/20
Worked on web scraping project. Practiced using Docker with two previous projects, didn't really work.
#### Date: 07/02/20
Did a Pyspark tutorial. Worked on Pyspark with the IBM A.I. Enterprise Workflow certification course. Finished and submitted learning journal unit 2 MATH 1280.

## Part 2
1. "A frequency is the number of times a given datum occurs in a data set.", (Yakir, p. 17).
2. "A relative frequency is the fraction of times a value occurs.", (Yakir, p. 17).
3. The relative frequency is basically a percentage of every unique observation in your data out of the total observations. The frequency is how many times a unique observations appears. While a frequency can be any whole number representing the amount of times that particular value appears, a relative frequency will always be between the number 0 and 1.

#### References:
Yakir, B. (2011). Introduction to statistical thinking. The Hebrew University.

## Part 3
```r
> getwd()
[1] "/////uopeople_computer_science/year_2019_2020/term_5/math_1280_intro_to_statistics/math_1280_global_material/data_math_1280"
> ex.1 <- read.csv('ex1.csv')
> summary(ex.1)
       id              sex         height     
 Min.   :1538611   FEMALE:54   Min.   :117.0  
 1st Qu.:3339583   MALE  :46   1st Qu.:158.0  
 Median :5105620               Median :171.0  
 Mean   :5412367               Mean   :170.1  
 3rd Qu.:7622236               3rd Qu.:180.2  
 Max.   :9878130               Max.   :208.0  
```