
# Learning Journal, Unit 1, CS_1101

### Student: D'angelo M. Shakur
### Date: 4/11/20

#### Part 1
---
> QUERY: If you are trying to print a string, what happens if you leave out one of the quotation marks or both and why

If you leave out either quotation mark you get the following error `SyntaxError: EOL while scanning string literal`. If you leave out both you get a different error `NameError: name 'string' is not defined`.

The first error is referring to the EOL or end of line being reached without ever seeing the end of the string or the closing quotation mark, `'`.
The second error is the interpreter thinking that there is a variable named in this case `string`, so it sees the print function executes, looks for what seems to be a variable, looks for the variable, doesn't find it, then produces an error.
---
> QUERY: You can use a minus sign to make a negative number like -2. What happens for each of the following and why?

Operations coincide in the same order displayed as the numbered text directly below.
```
2++2 # RESULT: 4
2--2 # RESULT: 4
2+-2 # RESULT: 0
2-+2 # RESULT: 0
```
0. This operation poses no issue and computes 4, showing that it is adding the two numbers together, this operation seems to ignore the second plus sign or uses it as a signifier that it is a positive number.
0. Running this code subtracts negative 2 from positive 2 correctly computing 4.
0. Adding negative 2 to positive 2 results in 0, here a minus in front of the second number signifies that its a negative number.
0. Subtracting positive 2 from positive 2 results in 0, this operation seems to ignore the second plus sign or uses it as a signifier that it is a positive number.

It is possible that adding a + sign in front of a numerical value in python makes the value positive, although I am unable to find any resources online saying so. It seems like the most plausible hypothesis as none of the operations create behavior that says the assumption is untrue.
---
> QUERY: In mathematical notation, leading zeros are OK, as in 02. What happens if you try this in Python and why.

When leading zeros are used in Python the following error occurs, `SyntaxError: invalid token`, so as a result leading zeros should not be used.
---
> QUERY: What happens if you have two values with no operator and a space in between them and why?

The same error as the above issue, `SyntaxError: invalid token`. If all you wanted to do was display them a comma would suffice, in between the two values, or if you wanted to use mathematical operations there would be no error. But if you have just a space the interpreter won't know what to do and thus throws an error.
---
#### Part 2
---
> QUERY: Describe at least **three** additional Python experiments that you tried while learning Chapter 1. Show the Python inputs and their outputs, and *explain what you learned* from the results of each example.

0. `string + string` in the Python terminal resulted in the error, `NameError: name 'string' is not defined`. Indicating that it is trying to find the variable `string` where there is none, thus `string` as a variable should be defined before use.
0. `'string' + 'string'` in the Python terminal concatenated both strings and output `'stringstring'`. Therefore adding 2 strings together results in concatenation.
0. `7**'string'` another command I used in the terminal, the error resulting is as follows `TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'`. I knew that this would result in an error but I though it might be fun to try.
0. `'string'**7` essentially the reverse of the previous command which resulted in the same error with only the value types being switched in display to, `TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'`, to represent the order in which they were used.
0. `type(print)` & `type(print())`, two different commands but I decided to include them both in the same entry. The output for the first command and second command is as follows, as well as in the same order as the commands. `<class 'bulitin_function_or_method'>`, `<class 'NoneType'>`. The first commands output is obvious and easy to interpret, the function/method is built into Python, and it is of the class type. The second command however outputs class as the type, however it says that it is `'NoneType'` which I thought was interested since it most certainly is not nothing and is something. I suspect that the method for the class returns nothing or some kind of empty value, so it is just saying so.
