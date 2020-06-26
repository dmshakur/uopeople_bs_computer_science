
# Assignment Unit 2 MATH 1280

## Tasks
1. Define 'sepal', 'petal':
   * Sepal: The calyx of a flower, enclosing the petals and typically green and leaf-like.
   * Petal: Segments of the corolla of a flower.
2. D
3. [1: 0.16, 2: 0.17, 3: 0.02, **4: 0.23**, **5: 0.23**, 6: 0.16, 7: 0.03], 3 and 4 are tied here.
4. I simply took every cumulative relative frequency value, from 1.00 to 0.16, subtracted the cumsum to the left and typed it into my computer. Upon looking at the resulting values I determined that there were two values which were the same, that were also the greatest.
5. R code:
```r
> flower.data <- read.csv("flowers.csv")
> names(flower.data)
```
#### Output:
```r
[1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species" 
```
6. 150
7. ["Sepal.Length": numeric,"Sepal.Width": numeric,"Petal.Length": ,Petal.Width": numeric,"Species": factor]
8. 24
9. 8
10. That 8 out of the 150 total observations have a sepal width of 2-2.3, and that this range represents about 5% of the total observations.
11. 3
12. 147 or 98%
13. Mode
14. Frequency table for species:
```r
> table(flower.data$Species)
```
#### Output
```r
    setosa versicolor  virginica 
        50         50         50 
```
15. The table included words instead of numbers because when the CSV file was read that is what was in the CSV file. If we wanted to we could convert them numerical values, but R doesn't do that for us, nor should it. The second row corresponds to the number of times each species appears in the dataset, 50 for each is a perfectly distributed dataset.