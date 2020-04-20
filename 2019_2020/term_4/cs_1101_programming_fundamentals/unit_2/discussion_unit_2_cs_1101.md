
# Discussion Assignment Unit 2 CS 1101

## D'angelo Shakur

## Part 1

### Define a function that takes an argument. Call the function, identify what code is the argument and what code is the parameter.

```python
from math import sqrt

def standard_deviation(values, is_sample = False):
    values.sort()
    std_dev = 0
    mean = 0
    n = len(values)
    if is_sample:
        n -= 1
    for val in values:
        mean += val
    mean /= len(values)
    for val in values:
        std_dev += (val - mean)**2
    std_dev = sqrt(std_dev / n)
    return std_dev

population = [10, 20, 22, 44, 55, 15, 22]

print(standard_deviation(population))
```
### Output
```sh
15.15150937398412
```

On the line of code above where `standard_deviation()` is defined there are two *parameters* called values and is_sample which is set to `False` by default. These parameters are like variables that exist only with in the functions code block, the only place they can be used. You can think of them as place holders for arguments, which I will get to next.

On the last line of the program's code it says, `standard_deviation(population)`, the part inside the parentheses `population`, is an argument. Arguments are what are passed into functions and then used of the parameters. Arguments can be passed into a function by setting the name of the parameter equal to the argument you want to pass through. The alternative is you pass the arguments in just as variable names, or expressions. In the previous case it wouldn't matter what order they are passed in since the parameters are being referred to explicitly, but without that level of definition you need to pass them in the function call in the order defined in the function definition.

## Part 2

### Call your function from Part 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which.

```python
print(standard_deviation(population))
print(standard_deviation([i for i in range(30)]))
print(standard_deviation([1, 4, 1, 56, 3, 52, 12]))

```
#### Output:
```sh
15.14150937398412
8.65544144839919
22.78381093707386
```

The first argument is the previously defined variable `population`, a variable is a container for value(s).
The second argument is an expression in the form of a list being initialized with a for in range loop. An expression is something that needs to be evaluated before it can be used, after evaluation it becomes a value, which can then be stored in a variable.
The third is a value. A value is any type of data that is or isn't contained within a variable, this one isn't.

## Part 3

### Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.

```python
def funky_function():
    valuable_variable = -100

print(valuable_variable)
```
#### Output
```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'valuable_variable' is not defined
```

The variable `valuable_variable` is initialized in the function `funky_function()`. When the function is called, the variable is initialized, this is the only time this will ever happen. When the function finishes and is pushed off the call stack all variables saved while that function is on top of the call stack are done with and deleted. "Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes.
An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically."
`tutorialspoint.com. (2018). How does garbage collection work in Python. Retrieved from
https://www.tutorialspoint.com/How-does-garbage-collection-work-in-Python`.
So as you can read once the function call is finished the variable `valuable_variable` gos out of scope if is collected immediately by Python's garbage collection system. It then ceases to exist in memory and if it is not in memory it cannot be used.

## Part 4

### Create a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain your results.

```python
def sample_func(testing):
    print(testing)

print(testing)
```
#### Output
```sh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'testing' is not defined
```

Here we are confronted with almost exactly the same problem as in the previous exercise. In `sample_func()`, we have a parameter called testing and parameters work very similarly to variables. The only difference being, parameters are only used in functions, and must be used when uninitialized. So in this example we are confronted with the same error, for the same reason. Another difference from the last exercise is when we are trying to call `testing` with `print()`, it isn't even initialized so if we were printing its value we would get a different error message saying we have an uninitialized variable being called.

## Part 5

### Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.

```python
def cow():
    cow_sound = "Moo"
    print(cow_sound)

cow_sound = "Meow"

print(cow_sound)
cow()
```
#### Output
```sh
Meow
Moo
```

When you define a variable inside a function that has the same name as a variable inside a function, that variable inside of the function is not being defined, it is reassigning value to the previously defined variable. So when you use the variable again after the function call is over it retains the value it was assigned and every time you use it you will get `Moo` in this example.

