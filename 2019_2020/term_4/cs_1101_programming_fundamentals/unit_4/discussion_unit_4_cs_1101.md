
# Discussion Assignment Unit 4 CS 1101

> Section 6.9 of your textbook ("Debugging") lists three possibilities to consider if a function is not working.
>
> * Describe each possibility in your own words.
> * Define "pre-condition" and "post-condition" as part of your description.
> * Create your own example of each possibility in Python code. List the code for each example, along with sample output from trying to run it.

## Pre-condition:
A pre-condition violation is when a function is called but the code within it is never executed. It means that before (pre) the condition (the code inside the function) is executed an error is thrown. This could happen when you don't pass in a correct amount of arguments.

```python
from math import exp

def tanh(num):
    numerator = exp(num) - exp(-num)
    denominator = exp(num) + exp(-num)
    return numerator / denominator

print(tanh()) # Problem
print(tanh(4.815)) # Solution
```
Output:
```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tanh() missing 1 required positional argument: 'num'

0.9998085623792909
```

## Post-condition:
A post-condition is when a function is called, but is not able to finish. In post-condition violations, after (post) the code block within the function (condition) incurs an error resulting in the program being unable to run properly.

```python
def mass_energy_equiv(m, c):
    return m * (c**2)

print(mass_energy_equiv("pecan banana pie", {"pecan": True, "banana": False})) # Problem
print(mass_energy_equiv(16.2, 3.42)) # Solution
```
```sh
  File "<stdin>", line 3
    print(mass_energy_equiv("pecan banana pie", {"pecan": True, "banana": False}))
        ^
SyntaxError: invalid syntax

189.48167999999998
```

## Return value:
When a function executes the code runs and an error happens after it finishes, this could be an error with your return value. If you were to create a function that generates some kind of data. But you use this function as an argument in another function for example, and that function needs to operate with a certain type of data and you generate the wrong type of data, you will get an error thrown.

```python
from math import exp

def sigmoid(x):
    return 1. / (1. + exp(-x))

fruit = ['empire', 'bosc', 'gala']
numbers = 48125162342

print(fruit /= sigmoid(2.2)) # Problem
print(numbers / sigmoid(2.2)) # Solution
```
```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /=: 'list' and 'float'

59380851286.350395
```
