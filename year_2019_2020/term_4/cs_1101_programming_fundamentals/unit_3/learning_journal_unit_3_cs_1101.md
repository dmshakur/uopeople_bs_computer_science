
# Learning Journal Unit 3 CS 1101

## Part 1:

```python
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
```
### Output:
```sh
>>> countup(-3)
-3
-2
-1
Blastoff!
```
### Solution:
```python
def countup(n):
    if n >= 0:
        print('Blaston!')
    else:
        print(n)
        countup(n + 1)
```

## Part 2:

#### Solution:
from random import random
```python
def count():
    user_input = int(input('Please enter a number\n'))
    print('\n')
    if user_input > 0:
        countdown(user_input)
    elif user_input < 0:
        countup(user_input)
    elif user_input == 0:
        print('Do it again')
        count()
count()
```
**Output for input `(0)`**
```sh
Please enter a number

```
**Output for input `(1)`**
```sh
1

Blastoff!
```
**Output for input `(-1)`**
```sh
-1

Blaston!
```

For an input of 0, I just called `count()` for that particular `elif` statement, so that the program never ends unless a number other than 0 is entered.


## Part 3:

#### Solution:
```python
def runtime_error(num):
  print(num)
  runtime_error(num / 0)

runtime_error(2)
```
**Output for input: `(2)`**
```sh
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    runtime_error(2)
  File "main.py", line 4, in runtime_error
    runtime_error(num / 0)
ZeroDivisionError: division by zero
```
This error message is a result of division by zero. In math dividing any number by zero is an illegal operation as it is in python and (most likely) all other programming languages. If you wanted to fix the error you would need to change the `0` in `runtime_error` to any other number. You would then be confronted with an error stating that you have reached the maximum recursion depth. In order to fix that error you will need to include an escape clause inside the function `runtime_error` or remove the recursive function call within `runtime_error`.