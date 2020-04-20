
# Programming Assignment Unit 2 CS 1101

## D'angelo Shakur

### Note: ``` denotes the beginning and end of a code block or terminal output.

### Program:

```python
def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines(toggle_print_statement = True):
    if toggle_print_statement:
        print('Printing nine lines')
    for i in range(3):
        three_lines()

def clear_screen():
    print('Clearing screen')
    for i in range(2):
        nine_lines(toggle_print_statement = False)
        three_lines()
    new_line()

nine_lines()

clear_screen()
```

### Output of the program on my machine:

```sh
[Running] python -u "c:\\\\\\\\programming_assignment_unit_2_cs_1101.py"
Printing nine lines
.
.
.
.
.
.
.
.
.
Clearing screen
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

[Done] exited with code=0 in 0.112 seconds
```