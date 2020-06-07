
# Discussion Assignment Unit 7 CS 1101

## Part 1, using tuples over lists:
Tuples are pretty much just lists that are immutable when you get right down to it. If you ever need to pass data around that can't be changed then a tuple is the way to go. When using a dictionary you cannot initialize a key as a list, since they are mutable and thus not hashable. You also lose out on a lot of very useful functions like enumerate which lets you retrieve data from your iterable and its location within that iterable.

```python
locations = dict()
locations[['USA', 'Texas']] = 'Austin'

print(locations.items())
```
### Output:
```sh
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    locations[['USA', 'Texas']] = 'Austin'
TypeError: unhashable type: 'list'
```
### The fix:
```python
locations = dict()
locations[('USA', 'Texas')] = 'Austin'

print(locations.items())
```
### Output:
```sh
dict_items([(('USA', 'Texas'), 'Austin')])
```

## Part 2, using tuples over dictionaries:
Dictionaries are very useful, they neatly organize your data and you can access values a lot faster because of their hash table system. Quite frequently in programming you will need to iterate through something, and often in a particular order. Dictionaries don't offer a great way to predictably iterate through something in order. Tuples are a great alternative, they are predictable and immutable.

```python
locations = {
    'first': ('France', 'Bordeaux'),
    'second': ('Italy', 'Liguria'),
    'third': ('Spain', 'Sanlucar De Barrameda'),
    'fourth': ('Israel', 'Tel Aviv')
}

for i, key in enumerate(locations):
    print(key, locations[key], i)
```
### Output:
See below that the order in which the keys of `locations` are initialized are not the same when iterated through.
```sh
first ('France', 'Paris') 0
third ('Spain', 'Sanlucar De Barrameda') 1
second ('Italy', 'Liguria') 2
fourth ('Israel', 'Tel Aviv') 3
```

```python

locations = {
    'first': ('France', 'Bordeaux'),
    'second': ('Italy', 'Genoa'),
    'third': ('Spain', 'Sanlucar De Barrameda'),
    'fourth': ('Israel', 'Tel Aviv')
}

wineries = {
    'Bordeaux': 'Malartic Lagraviere',
    'Genoa': 'Punta Crena',
    'Sanlucar De Barrameda': 'Valdespino'
}

for loc, wine in zip(locations, wineries):
    print(locations[loc], wineries[wine])
```
### Output:
As you can see here the wineries do not match up with their corresponding locations. Spain and Italy's wine gets mixed up.
```sh
('France', 'Bordeaux') Malartic Lagraviere
('Italy', 'Genoa') Valdespino
('Spain', 'Sanlucar De Barrameda') Punta Crena
```

### The fix:
```python
locations = (
    ('first', ('France', 'Bordeaux')),
    ('second', ('Italy', 'Genoa')),
    ('third', ('Spain', 'Sanlucar De Barrameda')),
    ('fourth', ('Israel', 'Tel Aviv'))
)

wineries = (
    ('Bordeaux', 'Malartic Lagraviere'),
    ('Genoa', 'Punta Crena'),
    ('Sanlucar De Barrameda', 'Valdespino')
)

for i, (loc, wine) in enumerate(zip(locations, wineries)):
    print(i, loc, wine)
```
### Output:
```sh
0 ('first', ('France', 'Bordeaux')) ('Bordeaux', 'Malartic Lagraviere')
1 ('second', ('Italy', 'Genoa')) ('Genoa', 'Punta Crena')
2 ('third', ('Spain', 'Sanlucar De Barrameda')) ('Sanlucar De Barrameda', 'Valdespino')
```
