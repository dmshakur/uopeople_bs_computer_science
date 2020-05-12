
Learning Journal Unit 5 CS 1101

> Apologies for the lack of proper formatting my laptop is broken so I have to use my phone.

## Part 1:

```python
prefixes = 'JKLMNOPQ'
suffix = 'uack'

for letter in prefixes:
     print(letter + (suffix if letter == 'O' or letter == 'Q' else suffix[1:]))
```

## Part 2:

```python
str = 'string'

beginning = str[:2]
middle = str[2:-2]
end = str[-2:]
s = str[0]

print(beginning, middle, end, s)
```
## Output:
```sh
st ri ng s
```

### beginning:
Showcases slicing a string from beginning up to but not including the 2nd index.

### middle:
Here the string str is sliced from the inside and ending inside. 

### end:
Here the string is slicing from the 2nd from the last to the last, including.

### s:
This operation just assigns the 0th character to s.

The first two examples make use of non negative positional arguments for the slicing operator.

The 2nd and 3rd examples make use of negative indexing. Where the element is the nth from the last element versus being strictly the nth element.

The last example makes use of the nth element, with no other characters being assigned to s except for element n.
