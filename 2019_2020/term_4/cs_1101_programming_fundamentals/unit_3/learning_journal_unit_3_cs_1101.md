
# Learning Journal Unit 3 CS 1101

## Part 1:
Copy the countdown function from Section 5.8 of your textbook.
Write a new recursive function `countup` that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

```python
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
```
```sh
>>> countup(-3)
-3
-2
-1
Blastoff!
```
#### Solution:
```python
def countup(n):
    if n >= 0:
        print('Blaston!')
    else:
        print(n)
        countup(n + 1)
```

## Part 2:
Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.) If the number is positive, the program should call countdown. If the number is negative, the program should call `countup`. Choose for yourself which function to call (`countdown` or `countup`) for input of zero.

### Provide the following.
The code of your program.
Output for the following input: a positive number, a negative number, and zero.
An explanation of your choice for what to call for input of zero.

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
Write your own unique Python program that has a runtime error. Do not copy the program from your textbook or the Internet. Provide the following.

* The code of your program.
* Output demonstrating the runtime error, including the error message.
* An explanation of the error message.
* An explanation of how to fix the error.

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