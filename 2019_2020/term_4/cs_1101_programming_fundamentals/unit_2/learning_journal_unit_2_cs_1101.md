
# Learning Journal Unit 2 CS 1101

## D'angelo Shakur

## Part 1

The volume of a sphere is 4/3πr3, where π has the value of "pi" given in Section 2.1 of your textbook. 
Write a function called print_volume(r) that takes an argument for the radius of the sphere, and prints the volume of the sphere.
Call your print_volume function three times with different values for radius.

```python
import math

def print_volume(r):
    return (4 / 3) * (math.pi * r * 3)

print_volume(4.1)
Output: 51.52211951887259

print_volume(2.2)
Output: 27.646015351590183

print_volume(9)
Output: 113.09733552923254
```


## Part 2

Write your own function that illustrates a feature that you learned in this unit. 
The function must take at least one argument. The function should be your own creation, not copied from any other source. 
Do not copy a function from your textbook or the Internet.

```python
from random import random

def dot_product(list_1, list_2):
    if (len(list_1) is not len(list_2)):
        return "Invalid arguments, pass in 2 lists, tuples or other iterable type"
    dot = 0
    for i in range(len(list_1)):
        dot += list_1[i] * list_2[i]
    return dot

def create_list(num):
    return [random() for i in range(num)]

print('dot_product one:', dot_product(create_list(4), create_list(4)))

print('dot_product two:', dot_product(create_list(7), create_list(9)))

print('dot_product three:', dot_product("string theory", "cats talking about eating food"))
```
#### Output
```
>>> dot_product one: 1.146331724958921
>>> dot_product two: Invalid arguments, pass in 2 lists, tuples or other iterable type
>>> dot_product three: Invalid arguments, pass in 2 lists, tuples or other iterable type
```

Include all of the following in your Learning Journal:

The code for the function that you invented.
The inputs and outputs to three calls of your invented function.
A description of what feature(s) your function illustrates.

### Description of invented function

I decided to create a function that calculates the dot product of two lists. It was the first thing I thought of since I've spent so much time learning about neural networks, and I had to learn what a dot product for a neural network I wrote in C++.

So the first thing I do is set my program up to be able to create random numbers with `from random import random`, I will need the function `random()` in order to create random numbers so I won't have to type them in manually. After my `import` I define my invented function, `dot_product(list_1, list_2)`. Basically what it does it takes two lists or tuples then it initializes a number in a variable to zero which will be for storing the return value, the dot product of both arguments. Getting the dot product is simple all you need to do is take two lists, then iterate through their length, and multiply every element of a common position, `i`. You cannot do this with two lists that are not of the same length so inside my function I have a if statement set up to ensure it's proper use. If I wanted to take this further I would make a class similar to numpy arrays so I could use matrices as an argument for `dot_product()`, as well as lists. Before iterating over the two inputs, in the function, I initialize and set a variable to a value of `0`, this variable will serve as base number that is the sum of products for every multiplication operation conducted on the two arguments. After that variables initialization I set up a `for i in range()` loop that takes the length of the first argument as a limiter. Then using `i` as the index for bracket notation in lists, I take the product of each element in each list of position `i` and add it to the previously created variable. When the loop is done return the variable and exit the function returning to the previous stack call. 



