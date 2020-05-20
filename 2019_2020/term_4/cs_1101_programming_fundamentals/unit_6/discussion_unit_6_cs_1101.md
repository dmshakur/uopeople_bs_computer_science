
# Discussion Unit 6 CS 1101

## Part 1:
Objects can hold identical values, but they do not have to, an object can also point to two or more variables. Objects and values are not necessarily equivalent, an object is merely a container for values, while a value is actual data, like a number. For example when we do addition in Python we are not adding two objects together we are merely adding their values.

Since all lists create a new object in memory, the variables `var` and `new_var` are note equivalent even though they hold the same values. But the first element in each list are both identical.
```python
var = [1, 4, 2, 3]
new_var = [1, 4, 2, 3]
print(var is new_var)
print(var[0] is new_var[0])
```
#### Output:
```sh
False
True
```

## Part 2:
An object is a container for information like a number as an integer, or a sentence as a string. Aliasing is when an object is being referenced by two or more variables. Referencing is when a variable is pointing to an object in memory.

#### Objects:
```python
var = [1, 4, 2, 5]
```
When the variable `var` is initialized it creates an object in memory for use later. This object contains the list and its subsequent values.

#### Aliasing:
```python
var = 422
new_var = var
```
Since the variable `new_var` is assigned the value from `var`, a new object in memory is not created. Both of these variables hold the same value and point to the same place in memory. Here only one object exists in memory, but both values point to it, if either variable changes a new object is added to memory with the new value. Something is being aliased when an object in memory has more than one variable pointing to it.

#### Referencing:
```python
var = [1, 4, 2, 5]
```
When the variable `var` is created an object is saved in memory for later use, but the variable itself does not hold the actual object. The variable itself merely holds the reference for where the object resides in memory, much like a person's home address.

## Part 3
For part 3 of this week's discussion assignment I decided to write a simple map function for iterating over a list in Python. 

The parameters `map_to` are `fn`, and `iterable`. The first is intended to be a function and the second is intended to be a list. Once the function is called it creates a variable `temp` to hold the return value, `temp` is initialized with an empty list object. Then a for loop runs through the argument `iterable`. The argument function `fn` has the current element, `el`, passed through it where it returns a new value based on what the function does and is then appended to the end of the list `temp`. Upon exiting the function a reference to the object that `temp` points to is returned.

```python
def map_to(fn, iterable):
    temp = list()
    for el in iterable:
        temp.append(fn(el))
    return temp
```