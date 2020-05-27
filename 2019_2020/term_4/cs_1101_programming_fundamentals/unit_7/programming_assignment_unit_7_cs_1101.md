
# Programming Assignment Unit 7 CS 1101

## Part 1:

```python
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

def has_duplicates(str):
    for i, letter in enumerate(str):
        index = str.find(letter, i)
        if index >= 0 and str[index] == str[i]:
            return True
    return False

def has_duplicates(str):
    hist = histogram(str)
    for k, v in hist.items():
        if v > 1: return True
    return False
    
for str in test_dups:
    print('{} has {}duplicates'.format(str, '' if has_duplicates(str) else 'no '))
```
### Output:
```sh
zzz has duplicates
dog has no duplicates
bookkeeper has duplicates
subdermatoglyphic has no duplicates
subdermatoglyphics has duplicates
```

## Part 2:
```python
alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"] 

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def missing_letters(str):
    str = histogram(str)
    alpha = []
    for letter in alphabet:
        if letter not in str:
            alpha.append(letter)
    return ''.join(alpha)


for str in test_miss:
    letters = missing_letters(str)
    print('"{}" uses all the letters'.format(str) 
        if len(letters) == 0 
        else '"{}" is missing letters {}'.format(str, letters))
```
### Output:
```sh
"zzz" is missing letters abcdefghijklmnopqrstuvwxy
"subdermatoglyphic" is missing letters fjknqvwxz
"the quick brown fox jumps over the lazy dog" uses all the letters
```
