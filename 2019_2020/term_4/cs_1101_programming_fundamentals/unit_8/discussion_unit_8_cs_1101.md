
# Discussion Unit 8 CS 1101

Exceptions are very important when it comes to files, because without them we will increase our likelihood of causing an unwanted problem. For example if we write the wrong kind of information to a file, don't load a file correctly, or if there isn't a file where we requested one. Using exceptions gives us the ability for our program to run and have the ability to either find a way to fix an issue or let us pin point the problem.

## Part 1:
```python
try:
    file = open('file_name')
except:
    print('error opening file')
```
### Production solution:
To fix this issue I would implement conditional statements to determine if there is a file already there. If there isn't a file there, giving the user the option to create a new one is one possible solution.

## Part 2:
```python
try:
    file = open('new_file', 'w')
    file.read()
except:
    print('error in creating or reading file')
```

### Production solution:
In this situation checking whether or not the file is open for reading would be the first step, and not allowing the method `.read()` to be called if that requirement is not met.

## Part 3:
```python
try:
    file = open('temp', 'a')
    file.write('poof')
except:
    print('error in opening or appending to file')
```

### Production solution:
This is another example of opening a file that is not there. Before opening a file it is necessary to check if it is actually there (in production).
