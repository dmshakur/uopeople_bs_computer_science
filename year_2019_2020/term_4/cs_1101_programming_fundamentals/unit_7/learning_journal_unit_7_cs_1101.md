
# Learning Journal Unit 7 CS 1101

### Description:
It is merely a way to keep track of the amount of time spent running on any day of the week.
Every day corresponds to a day of the week, and every appended value is the next week of the day.
So index 0 is the first Saturday for example, and index 1 would be the following Saturday.
The inverted dictionary would only be useful if you wanted to find in what day did you run X amount of miles.

```python
running_log = {
    'day_1': [0.5, 1],        
    'day_2': [2],
    'day_3': [0.25],
    'day_4': [],
    'day_5': [0.3, 0.8],
    'day_6': [],
    'day_7': []
}
```
### Modified function:
```python
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = tuple(d[key])
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
```
### Original output:
```sh
{'day_3': [0.25], 'day_7': [], 'day_2': [2], 'day_4': [], 'day_5': [0.3, 0.8], 'day_1': [0.5, 1], 'day_6': []}
```

### Inverted Output:
```sh
{(0.5, 1): ['day_1'], (2,): ['day_2'], (0.3, 0.8): ['day_5'], (): ['day_4', 'day_7', 'day_6'], (0.25,): ['day_3']}
```
