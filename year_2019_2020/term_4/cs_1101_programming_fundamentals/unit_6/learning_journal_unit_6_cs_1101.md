
# Learning Journal Unit 6 CS 1101

## Part 1:
```python
food = 'what are the names of the foods in the cupboard'
food = food.split(' ')
del food[:3]
food.sort()
food.extend(['brand', 'new', 'items'])
food = ' '.join(food)
print(food)
```
Output:
```
cupboard foods in names of the the brand new items
```

## Part 2:
```python
oh_my_god_so_many_lists = [[[[[[4], 8], 15], 16], 23], 42]
the_star_operator = 9 * 9
slices_of_not_pizza = oh_my_god_so_many_lists[:4]
i_want_to_be_greater = 10
i_want_to_be_greater += the_star_operator
lamb = lambda x: x != 42
no_winning_powerball_number_for_me = filter(lamb, oh_my_god_so_many_lists)
#slices_of_not_pizza.join() # I thought that this was the proper notation, but I was confusing it with .sort()
```

## Part 3:
Peer assessment with programming assignments has been fine so far. The only issue I have is with leaving comments on peoples work when it doesn't have any flaws. When someone writes a program and they're pretty much spot on about everything, I find it hard to come up with anything to say other than good job, but when I notice bugs I don't have any issue with pointing them out. As far as other people's feelings about my assessments go, I don't think I know or could since it is an anonymous activity.