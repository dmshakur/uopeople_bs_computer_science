
# Precalculus chapter 1
# Relations and functions

## Sets of real numbers and the Cartesian coordinate plane
> Set: A well defined collection of objects which are called the 'elements' of the set. Here, 'well-defined' means that it is possible to determine if something belongs to the collection or not, without prejudice.

#### Ways to describe sets
1. Verbal method: Use a sentence to define a set.
2. Roster method: Begin with a left brace '{', list each element fo the set only once and then end with a right brace '}'.
3. Set-builder method: A combination of the verbal and roster methods using a 'dummy variable', such as $x$.

Sets of numbers:
1. The empty set, which has no numbers: $\emptyset = \{\} = \{ x|x\neq x\}$.
2. Natural numbers: $\mathbb{N}=\{1,2,3,...\}$.
3. Whole numbers: $\mathbb{W}=\{1,2,3,...\}$.
4. Integers: $\mathbb{Z}=\{...,-1,-2,-1,0,1,2,3,...\}$.
5. Rational numbers: $\mathbb{Q}=\{\frac{a}{b}|a\in\mathbb{Z}\texttt{ and } b\in\mathbb{Z}\}$.
    * Another way to describe rational numbers is: $\mathbb{Q}=\{x|x \texttt{ possesses a repeating or terminating decimal representation. }\}$.
6. Real numbers: $\mathbb{R}=\{x|x \texttt{ possesses a decimal representation. }\}$.
7. Irrational numbers: $\mathbb{P}=\{x|x \texttt{ is a non-rational real number. }\}$.
   * An irrational number is a decimal which neither repeats nor terminates.
      * Examples:
      * $\pi$
      * $\sqrt{2}$
      * $0.101001000100001...$
8. Complex numbers: $\mathbb{C}=\{a+bi|a,b\in\mathbb{R}\texttt{ and } i=\sqrt{-1}\}$.

Every natural number is a whole number, every whole number is an integer, and each integer is a rational number.

For interval notation we list the left endpoint then the right endpoint, with spare brackets '[' and ']'. If an endpoint is included in that interval use a 'closed' dot to indicate membership in the interval. Otherwise we use parentheses, '(' or ')', and an 'open' circle to indicate that the endpoint is not part of the set. If it doesn't have finite endpoints then either positive or negative $\infty$ is used.

Interval notation:
|Set of real numbers|Interval notation|
|-|-|
|$\{x\|a<x<b\}$|$(a,b)$|
|$\{x\|a\leq x<b\}$|$(a,b]$|
|$\{x\|a<x\leq b\}$|$[a,b)$|
|$\{x\|a\leq x\leq b\}$|$[a,b]$|
|$\{x\|x<b\}$|$(-\infty,b)$|
|$\{x\|x\leq b\}$|$(-\infty,b]$|
|$\{x\|x>a\}$|$(a,\infty)$|
|$\{x\|x\geq a\}$|$[a,\infty)$|
|$\mathbb{R}$|$(-\infty,\infty)$|

#### Intersection
The intersection of $A$ and $B$: $A\cap B=\{x|x\in A \textsf{ and } x \in B\}$.
The union of $A$ and $B$: $A\cup B = \{x|x\in A \textsf{ or } x \in B \textsf{ (or both)}\}$.
The intersect of two sets is the overlap of the two sets - the elements which the sets have in common.

> Problem 1.1.1. Express the following sets of numbers using interval notation.
1. $(-\infty,-2]\cup[2,\infty)$.
2. $(-\infty,3)\cup(3,\infty)$.
3. $(-\infty,-3)\cup(-3,3)\cup(3,\infty)$.
4. $(-1,3]\cup{5}$.

A $x$-coordinate is also called an abscissa, and a $y$ coordinate is sometimes called an ordinate. Taken together the two compromise the Cartesian coordinates of a point.

#### Important facts about the Cartesian coordinate plane
* $(a,b)$ and $(c,d)$ represent the same point in the plane if and only if $a=c$ and $b=d$.
* $(x,y)$ lies on the x-axis if and only if $y=0$.
* $(x,y)$ lies on the y-axis if and only if $x=0$.
* The origin is the point $(0,0)$. It is the only point common to both axes.

> Problem 1.1.2. Plot the following points:
```python
import matplotlib.pyplot as plt
import sns as sns
sns.set()
# labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'O']
x = [5, -(5/2), -5.8, 4.5, 5, 0, -7, 0, 0]
y = [8, 3, -3, -1, 0, 5, 0, -9, 0]
plt.scatter(x, y) #, labels = labels)
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.show()
```

The axes divide the plane into four regions called quadrants, they are labeled with Roman numerals and proceed counter clockwise from the top right.
$$
\begin{matrix} II & I \\ III & IV \end{matrix}
$$

#### Symmetry:
Two points $(a,b)$ and $(c,d)$ in the plane are said to be symmetric about the...
* x-axis: if $a=c$ and $b=-d$.
  * In $(x,y)$, replace $y$ with $-y$.
* y-axis: if $a=-c$ and $b=d$.
  * In $(x,y)$, replace $x$ with $-x$.
* origin: if $a=-c$ and $b=-d$.
  * In $(x,y)$, replace $y$ with $-y$ and $x$ with $-x$.

> Problem 1.1.3. let $P$ be the point $(-2,3)$. Find the points which are symmetric to $P$ about the:
1. x-axis: $(-2,-3)$.
2. y-axis: $(2,3)$.
3. origin: $(2,-3)$.

#### The distance formula: 
The distance between the points $P(x_0,y_0)$ and $Q(x_1,y_1)$ is:
$$ d=\sqrt{(x_1-x_0)^2+(y_1-y_0)^2} $$

> Problem 1.1.4. Find and simplify the distance between $P(-2,3)$ and $Q(1,-3)$.

$$d=\sqrt{(1--2)^2+(-3-3)^2}$$
$$d=\sqrt{9+36}$$
$$d=\sqrt{45}$$
$$d=6.708203932$$

> Problem 1.1.5. Find all the points with x-coordinate 1 which are 4 units from the point $(3,2)$.

1. $(1,\sqrt{14}+2)$
$$4=\sqrt{(1-3)^2+(y_1-2)^2}$$
$$4=\sqrt{2+(y_1-2)^2}$$
$$4=\sqrt{2+\sqrt{14}^2}$$
2. $(1,-(\sqrt{14}+2))$

#### The midpoint formula
The midpoint of the line segment connecting $P(x_0,y_0)$ and $Q(x_1,y_1)$ is:
$$
M=(\frac{x_o+x_1}{2},\frac{y_0+y_1}{2})
$$

> Problem 1.1.6. Find the midpoint of the line segment connecting $P(-2,3)$ and $Q(1,-3)$.
$$M=(\frac{-2+1}{2},\frac{3+-3}{2})$$
$$M=(-0.5,0)$$

> Problem 1.1.7. If $a\neq b$, prove that the line $y=x$ equally divides the line segment with endpoints $(a,b)$ and $(b,a)$.

### Exercises: Relations and functions
2. $[0,5]$: Correct
3. $(-1,6]$: Correct
4. $(0,4]$: Correct
5. $\emptyset$: Correct
6. $(-\infty,5]$: ***Incorrect***, real answer: $(-\infty,0)\cup[1,5]$
7. ${5}$: Correct
8. $(-\infty,5)\cup(5,\infty)$: Correct
9. $(-\infty,-1)\cup(-1,\infty)$: Correct
10. $(-\infty,-3)\cup(-3,4)\cup(4,\infty)$: Correct
11. $(-\infty,0)\cup(0,2)\cup(2,\infty)$: Correct
12. $(-\infty,-2)\cup(-2,2)\cup(2,\infty)$: Correct
13. $(-\infty,-4)\cup(-4,0)\cup(0,4)\cup(4,\infty)$: Correct
14. $(-\infty,-1]\cup[1,\infty)$: Correct
15. $(-\infty,\infty)$: ***Incorrect***, real answer: $(-\infty,3)\cup[2,\infty)$
16. $(-\infty,-3]\cup(0,\infty)$: Correct
17. $(-\infty,6]$: ***Incorrect***, real answer: $(-\infty,5]\cup{6}$
    *  I failed to realize that values in between 5 and 6 are invalid.
18. ${-1,1}\cup(2,\infty)$: Incorrect, real answer: ${-1}\cup{1}\cup(2,\infty)$
    1.  I failed to realize that values in between -1 and 1, as well as in between 1 and 2, are all invalid numbers.
19. $(-3,3)\cup{4}$: Correct
20. 
```python
import pandas as pd
import seaborn as sns
import math
sns.set()
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'O']
x = [-3, 1.3, math.pi, 0, -5.5, -8, 9.2, 7]
y = [-7, -2, math.sqrt(10), 8, 0, 4, -7.8, 5]
df = pd.DataFrame(list(zip(x, y, labels)), columns = ['x', 'y', 'label'])
sns.relplot(x = 'x', y = 'y', hue = 'label', data = df)
```
21. : ***75%*** Correct
    * $I$: ${C,D,H}$
    * $II$: ${E,F}$
    * $III$: ${A}$
    * $IV$: ${B,G}$
      * $D$ is on the positive y-axis
      * $E$ is on the negative x-axis
22. $M=(0.5,3.5)$, $D=5$: ***75%*** Correct, real answer $M_x=-1$
23. $M=(1,-4)$, $D=\sqrt{160}$: Correct
24. $M=(1,1.5)$, $D=\sqrt{26}$: Correct
25. $M=(\frac{2.5}{3},1.75)$, $D=\sqrt{9.5}$: ***50%*** Correct, real answer: $D=\frac{\sqrt{37}{2}}
26. $M=(1.3,-1.3)$, $D=\sqrt{74}$: Correct
27. $M=(-0.7071067811865476,-0.8660254037844386)$, $D=\sqrt{45}$: Correct
28. $M=(8.94427190999916,4.330127018922193)$, $D=\sqrt{83}$: Correct
29. $M=(x,y)$, $D=\sqrt{x^2+y^2}$: ***50%*** Correct, real answer: $M=(\frac{x}{2},\frac{y}{2})$
30. $(3+\sqrt{7},-1)$, $(-(3+\sqrt{7}),-1)$: ***50%*** Correct $y=(3-\sqrt{7},-1)$
31. $(-1,0)$, $(1,0)$: ***Incorrect***, real answer: $(0,3)$
32. $(0,\sqrt{3}+1)$, $(0,-(\sqrt{3}+1))$: Incorrect, real answer: $(-1+\sqrt{3},0),(-1-\sqrt{3},0)$
    *  Very close to the real answer, just got things mixed up in my head.
33. $(1,-1)$, $(-1,1)$: Incorrect, real answer: $(\frac{\sqrt{2}}{2},-\frac{\sqrt{2}}{2})$,$(-\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2})$
34. $D=5$, $C=(-4,4)$: ***50%*** Correct, real answer: $C=(4,-4)$
35. I don't even know what this means: Incorrect
36. Not really sure how to answer this one either.
37. A: False, B: False
38. I don't think you can create a square with the given coordinates
39. $\infty$
40. Add a new dimension $z$. The new formulas might be the same but with an added $z$, instead of having partial equations for $x$ and $y$, we would also have a partial equation for $z$.

## Relations
A relation is a set of points on a plane.

#### Equations of vertical and horizontal lines
* The graph of the equation $x=a$ is a vertical line through $(a,0)$.
* The graph of the equation $y=b$ is a horizontal line through $(0,b)$.

### Graphs of equations

#### The fundamental graphing principal
The graph of an equation is the set of points which satisfy the equation. That is, a point $(x,y)$ is on the graph of an equation if and only if $x$ and $y$ satisfy the equation. Here satisfaction means that the equation is true.

Of all the points on the graph of an equation, the places where the graph crosses or touches the axes hold special significance. These are called the intercepts of the graph. Intercepts come in two distinct varieties: $x$-intercepts and $y$-intercepts. Defined below.
#### Suppose the graph of an equation is given
* A point on a graph which is also on the $x$-axis is called an $x$-intercept of the graph.
* A point on a graph which is also on the $y$-axis is called an $y$-intercept of the graph.
  
#### Finding intercepts of the graph of an equation
* $x$-intercepts have the form $(x,0)$; set $y=0$ in the equation and solve for $x$.
* $y$-intercepts have the form $(0,y)$; set $x=0$ in the equation and solve for $y$.

#### Testing the graph of an equation for symmetry
* About the $y$-axis - substitute $(-x,y)$ into the equation and simplify. If the result equivalent to the original equation, the graph is symmetric about the $y$-axis.
* About the $x$-axis - substitute $(x,-y)$ into the equation and simplify. If the result is equivalent to the original equation, the graph is symmetric about the $x$-axis.
* About the origin - substitute $(-x,-y)$ into the equation and simplify. If the result is equivalent to the original equation, the graph is symmetric about the origin.

> Problem 1.2.4. Find the $x$- and $y$-intercepts of the graph of $(x-2)^2+y^2=1$. Test for symmetry. Plot additional points as needed to complete the graph.
* $x$: ${3,1}$.
* $y$: $\emptyset$.

### Exercises
```python
import seaborn as sns
import pandas as pd
import math
sns.set()

# 1. Correct
df = pd.DataFrame(zip(
  [-3, -2, -1, 0, 1, 2, 3],
  [9, 4, 1, 0, 1, 4, 9]
), columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)

# 2. Correct
df = pd.DataFrame(((−2,0),  (−1,1),  (−1,−1),  (0,2),  (0,−2),  (1,3),  (1,−3), columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)

# 3. Correct
xy = []
for i in range(-2,3):
  xy.append((i, 2*i))
df = pd.DataFrame(xy, columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)

# 4. Correct
xy = []
for i in range(-6,7):
  xy.append((6/i, i))
df = pd.DataFrame(xy, columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)

# 5. Correct
xy = []
for i in range(-2, 3):
  xy.append((i, 4 -pow(i, 2)))
df = pd.DataFrame(xy, columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)

# 6. Correct
xy = []
for i in [0, 1, 4, 9]:
  xy.append((math.sqrt(i), i))
df = pd.DataFrame(xy, columns = ['x', 'y'])
sns.relplot(x = 'x', y = 'y', kind = 'line', data = df)
```
7. Every point on the x-axis greater than -4, with a y-axis value of -2
8. Every point on the x-axis less than and equal to 4, with a y-axis value of 3
9. Every point on the y-axis greater than 1, with a x-axis value of -1
10. Every point on the y-axis less than and equal to 5, with a x-axis value of 2
11. Every point on the y-axis greater than -3 up to 4, with a x-axis value of -2
12. Every point on the y-axis from -4 to less than 3, with an x-axis value of 3
13. Every point on the x-axis less than 3 and greater than or equal to -2
14. Every point on the x-axis greater than -4 and up to 4
15. Every point on the x axis & y-axis greater than -2
16. Every point on the x-axis & y-axis less than and equal to 3
17. Every point on the x-axis greater than 0, and every point on the y-axis less than 4
18. Every point on the x-axis less than and equal to 3, every point on the y-axis less than 2
19. Every point on the x-axis greater than 0, and every point on the y-axis less than 4
20. Every point on the x-axis greater than or equal to $-\sqrt{2}$ and less than and equal to $\frac{2}{3}$, and every point on the y-axis greater then $\pi$ and less than and equal to $\frac{9}{2}$
21. $\{(1,4),(0,3),(-2,1),(-4,-1)\}$. ***Incorrect***, elements are in the wrong order.
22. $\{(x,3)|x \geq -3\}$. Correct
23. $\{(2,y)|y > -3\}$. Correct
24. $\{(-2,y)|-4\leq y\lneq 3\}$. Correct
25. $\{(x,2)|-4<x\leq 3\}$. Correct
26. $\{(x,y)|-\infty<x<\infty,0\leq y<\infty\}$. ***Incorrect***, was thinking in terms of interval notation.
27. $\{(x,y)|-2\lneq x<\infty,-\infty<y<\infty\}$. ***Incorrect***, was thinking in terms of interval notation.
28. $\{(x,y)|-3\lneq x\leq 2,-\infty<y<\infty\}$. ***Incorrect***, was thinking in terms of interval notation.
29. $\{(x,y)|0\leq x<\infty,0\leq y<\infty\}$. ***Incorrect***, was thinking in terms of interval notation.
30. $\{(x,y)|-4<x<5,-3<y<2\}$. Correct
31. Every point on the y-axis with an x-axis value of -2. Correct
32. Every point on the y-axis with an x-axis value of 3. Correct
33. Every point on the x-axis with a y-axis value of 3. Correct
34. Every point on the x-axis with a y-axis value of -2. Correct
35. Every point on the y-axis with an x-axis value of 0. Correct
36. Every point on the x-axis with a y-axis value of 0. Correct
37. This will basically form a grid with every integer by integer value being occupied.
38. Anytime a line is displayed on a graph where any endpoint is non-inclusive, is an example of an irrational number, since the number before any integer, for example, would consist of an infinite amount of numbers.
39. The x-axis value starts at 1, and doubles til $\infty$. The y-axis value starts at 0 and increases by 1 til $\infty$.
40. The x-axis values start from $-\infty$ and increase by 1. The y-axis values iterate through $\{9,4,1,0,1,4\}$, repeatedly, where 0 meets with 0 on the x-axis.
```python
import seaborn as sns
import pandas as pd

# 41. No y intercept. Yes x intercept.
xy = []
for i in range(-10, 11):
  xy.append((i,i**2 + 1))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 42. 
xy = []
for i in range(-10, 11):
  xy.append((i, i**2 - (2 * i) - 8))

sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 43.
xy = []
for i in range(-10, 11):
  xy.append((i, i**3 - i))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 44. 
xy = []
for i in range(-10, 11):
  xy.append((i, (i**3 / 4) - (i * 3)))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 45.
xy = []
for i in range(-10, 11):
  xy.append((i, math.sqrt(x - 2)))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 46.
xy = []
for i in range(-10, 11):
  xy.append((i, (2 * sqrt(i + 4) - 2)))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 47.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if 7 == (3 * x - y):
      xy.append((x, y))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 48.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if 10 == ((3 * x) - (2 * y)):
      xy.append((x, y))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 49.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if 16 == ((x + 2)**2 + y**2):
      xy.append((x, y))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))

# 50.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if 1 == (x**2 - y**2):
      xy.append((x, y))
# 51.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if 36 == ((4 * y**2) - (9 * x**2)):
      xy.append((x, y))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))
# 52.
xy = []
for x in range(-100, 101):
  for y in range(-100, 101):
    if -4 == (x**3 * y):
      xy.append((x, y))
sns.relplot(x = 'x', y = 'y', data = pd.DataFrame(xy, columns = ['x', 'y']))
```

## Introduction to functions

#### Functions
A relation in which each x-coordinate is matched with only one y-coordinate is said to describe $y$ as a function of $x$.

$y$ cannot be a function of $x$ if there is another point with the same $x$ value as $x$.

#### The vertical line test
A set of points in the plane represents $y$ as a function of $x$ if and only if no two points lie on the same vertical line.

> Problem 1.3.2. Use the vertical line test to determine which of the following relations describes $y$ as a function of $x$.

Only graph $S$ passes the vertical line test.

> Problem 1.3.3. Use the vertical line test to determine which of the following relations describe $y$ as a function of $x$.

Only graph $S_2$ passes the vertical line test, because the line includes every point except for the point below the individual black point.

#### Suppose $F$ is a relation which describes $y$ as a function of $x$.
* The set of the x-coordinates of the points in $F$ is called the domain of $F$. The values are not repetitive.
* The set of the y-coordinates of the points in $F$ is called the range of $F$. The values are not repetitive.

> Problem 1.3.4. Find the domain and range of the function $F=\{(-3,2),(0,1),(4,2),(5,2)\}$.

The domain of $F$: $\{-3,0,4,5\}$
The range of $F$: $\{1,2\}$

It is called *projecting* when we collapse the curve of a line to better visualize the terms in it. You can use interval notation to determine the range of a line. 

All functions are relations but not all relations are functions.

> Problem 1.3.5. Determine which equations represent $y$ as a function of $x$.

1. $y$ is a function of $x$. Incorrect
2. $y$ is a function of $x$.
3. 


### Exercises
1. Domain: $\{-3,-2,-1,0,1,2,3\}$, Range: $\{0,1,4,9\}$: Correct
2. No: Correct
3. Domain: $\{-7,-3,3,4,5,6\}$, Range: $\{0,4,5,6,9\}$: Correct
4. Domain: $\{1,4,9,16,25,36,...\}$, Range: $\{2,4,6,8,10,12,...\}$: Correct
5. No: Correct
6. No?: ***Incorrect***, real answer: Domain: $\{x - x \texttt{ is irrational }\}, Range: $\{1\}$
7. Domain: $\{1,2,4,8,16,32,...\}$, Range: $\{0,1,2,3,4,5,...\}$: Correct
8. Domain: $\{...,-3,-2,-1,0,1,2,3,...\}$, Range: $\{0,1,4,9\}$: Sort of correct
9. No: Correct
10. Domain: $[-2,4)$, Range: $\{3\}$: Correct
11. No: ***Incorrect***, Real answer: Domain: $(-\infty,\infty)$, Range: $[0,\infty)$
12. No: ***Incorrect***
13. Domain: $\{-4,-3,-2,-1,0,1\}$, Range: $\{-1,0,1,2,3,4\}$: Correct
14. No: Correct
15. Domain: $(-\infty,\infty)$, Range: $[1,\infty)$: Correct
16. No: Correct
17. Domain: $[2,\infty)$, Range: $[0,\infty)$: Correct
18. Domain: $(-\infty,\infty)$, Range: $(\infty,4]$: Correct
19. No: Correct
20. Domain: $[-5,-3)\cup(-3,3)$, Range: $(-2,-1)\cup[0,4)$: Correct
21. Domain: $[-2,\infty)$, Range: $[-3,\infty)$: Correct
22. No: Correct
23. Domain: $[-5,4)$, Range: $[-4,4)$: Correct
24. Domain: $[0,4)\cup(3,6]$, Range: $(-4,-1]\cup[0,4]$: Correct
25. Domain: $(-\infty,\infty)$, Range: $(-\infty,4]$: Correct
26. Domain: $(-\infty,\infty)$, Range: $(-\infty,4]$: Correct
27. Domain: $[-2,\infty)$, Range: $(-\infty,3]$: Correct
28. Domain: $(-\infty,\infty)$, Range: $(-\infty,\infty)$: Correct
29. Domain: $(-\infty,0]\cup(1,\infty)$, Range: $(-\infty,1]\cup\{2\}$: Correct
30. Domain: $[-3,3]$, Range: $[-2,2]$: Correct
31. No: Correct
32. Domain: $(-\infty,\infty)$, Range: $\{2\}$: Correct
33. Yes: Correct
34. Yes: Correct
35. No: Incorrect
36. No: Correct
37. No: Incorrect
38. No: Correct
39. No: Correct
40. Yes: Correct
41. No: Correct
42. Yes: Correct
43. No: Correct
44. Yes: Correct
45. Yes: Correct
46. No: Incorrect
47. No: Correct
48. $[min(P),max(P)]$
49. Only if two classmates shared an email address, which I do not see happening at all, why would anyone do that? No two social security numbers are the same, and two phone numbers being shared is unlikely, unless two students lived in the same home and shared a home number.
50. No
51. No
52. No
53. No

## Function notation
If we think fo the domain of a function as a set of inputs and the range as a set of outputs, we can think of a function $f$ as a process by which each input $x$ is matched with only one output $y$. Since the output is completely determined by the input $x$ and the process $f$, we symbolize the output with function notation: $f(x)$, read '$f$ of $x$'. In this case the parentheses do not imply multiplication as they do elsewhere, so context should be clear. 

The value of $y$ is completely dependent on $x$, therefore $x$ is often called the independent variable, and the argument of $f$, whereas $y$ is often called the independent variable.

> Problem 1.4.1. Suppose a function $g$ is described by applying the following steps, in sequence.
> 1. Add 4.
> 2. Multiply by 3
> Determine $g(5)$ and find an expression for $g(x)$.

$$g(5)=27$$

> Problem 1.4.2. Let $f(x)=-x^2+3x+4$.
> 1. Find and simplify the following.
>   * $f(-1)$, $f(0)$, $f(2)$
>   * $f(2x)$, $2f(x)$
>   * $f(x+2)$, $f(x)+2$, $f(x)+f(2)$
> 2. Solve $f(x)=4$.

1. Simplify 1
   * 1.1
      * $--1^2=1$
      * $3*-1=-3$
      * $-1+-3+4=0$
      * $f(-1)=0$
   * 1.2
      * $-0^2=0$
      * $3*0=0$
      * $0+0+4=4$
      * $f(0)=4$
   * 1.3
      * $-2^2=2$
      * $3*2=6$
      * $2+6+4=12$
      * $f(2)=12$
2. Simplify 2
   * 2.1
      * $-(2x)^2=(2x)^2$
      * $3*(2x)^2=3(2x)^2$
      * $(2x)^2+3(2x)^2=3+(4x)^4$
      * $$
   * 2.2
      * $$
      * $$
      * $$
      * $$
3. Simplify 3
   * 3.1
      * $$
      * $$
      * $$
      * $$
   * 3.2
      * $$
      * $$
      * $$
      * $$
   * 3.3
      * $$
      * $$
      * $$
      * $$
4. $x=3$

There is no general distributive property of function notation. If a function is called and gives an invalid output, then that value if not allowed, in other words that value is not in the domain of the function. 

> Problem 1.4.3. Find the domain fo the following functions.

1. $(-\infty,\frac\{4\}\{3\})$
2. $(-\infty,\infty)$
3. $x\neq \{3\}$
4. $(-\infty,0)\cup\{1\}$
5. $[-3,33)\cup(33,\infty)$
6. $x\neq 0$

An applied domain is a mathematical equation that has no restrictions, except those in the physical space. For example, can't have a negative number of grapes, and you wouldn't buy 100,000 pounds of grapes from the store. Typically, an applied domain is stated explicitly. In this case, it would be common to see something like $c(g)=1.5g$, $0\leq g\leq100$, meaning the number of pounds of grapes purchased is limited from $0$ up to $100$. 

> Problem 1.4.4. The height of $h$ in feet of a model rocket above ground $t$ seconds after lift-off is given by:
> 1. Find and interpret $h10$ and $h60$
> 2. Solve $h(t) = 375$ and interpret your answers
$$ h(t)=\begin{cases}
-4t^2+100t, & \texttt{if } 0\leq t\leq20\\
0, & \texttt{if } t>20
\end{cases}$$

1. $h(10)=500$, $h(60)=0$
2. $t=\{5,15\}$

The previous type of function is called a piecewise function. 

## Exercises
1. Multiply 2; add 3; divide by 4.
   * $f(x)=\frac{x2+3}{4}$: Correct
2. Add 3; multiply 2; divide 4.
   * $f(x)=\frac{(x+3)2}{4}$: Correct
3. Divide 4; add 3; multiply 2.
   * $f(x)=(\frac{x}{4}+3)2$: Correct
4. Multiply 2; add 3; take the square root.
   * $f(x)=\sqrt{x2+3}$: Correct
5. Add 3; multiply 2; take the square root.
   * $f(x)=\sqrt{(x+3)2}$: Correct
6. Add 3; take the square root; multiply 2.
   * $f(x)=2\sqrt{x+3}$: Correct
7. Take the square root; subtract 13; make the quantity the denominator of a fraction with a numerator of 4.
   * $f(x)=\frac{4}{\sqrt{x}-13}$: Correct
8. Subtract 13; take the square root; make the quantity the denominator of a fraction with a numerator of 4.
   * $f(x)=\frac{4}{\sqrt{x-13}}$: Correct
9.  Take the square root; make the quantity the denominator of a fraction with a numerator of 4; subtract 13.
    * $f(x)=\frac{4}{\sqrt{x}}-13$: ***Incorrect***, real answer: $\frac{4}{\sqrt{x}}-13$
10. Make the quantity the denominator of a fraction with numerator 4; take the square root; subtract 13.
    * $f(x)=\sqrt{\frac{4}{x}}-13$: Correct
11. $f(x)=2x+1$
    1. $f(3)=7$: Correct
    2. $f(-1)=-1$: Correct
    3. $f(\frac{3}{2})=4$: Correct
    4. $f(4x)=6x+1$: ***Incorrect***, real answer: $8x+1$
    5. $4f(x)=8x+4$: Correct
    6. $f(-x)=2x+1$: ***Incorrect***, real answer: $-2x+1$
    7. $f(x-4)=2x-3: ***Incorrect***, real answer: $2x-7$
    8. $f(x)-4=2x-3$: Correct
    9. $f(x^2)=2x^2-1$: ***Incorrect***, real answer: $2^2+1$
12. $f(x)=3-4x$
    1. $f(3)=-28$: ***Incorrect***, real answer: $-9$
    2. $f(-1)=7$: Correct
    3. $f(\frac{3}{2})=-3$: Correct
    4. $f(4x)=3-8x$: ***Incorrect***, real answer: $3-16x$
    5. $4f(x)=12-16x$: Correct
    6. $f(-x)=3-4(-x)$: ***Incorrect***, real answer: $4x+3$
    7. $f(x-4)=3-3x$: ***Incorrect***, real answer: $19-4x$
    8. $f(x)-4=3-3x$: ***Incorrect***, real answer: $-4x-1$
    9. $f(x^2)=3-4x^2$: Correct
13. $f(x)=2-x^2$
    1. $f(3)=-7$: Correct
    2. $f(-1)=1$: Correct
    3. $f(\frac{3}{2})=-\frac{1}{4}$: Correct
    4. $f(4x)=2-(4x)^2$: ***Incorrect***, real answer: $2-16x^2$
    5. $4f(x)=8-4x^2$: Correct
    6. $f(-x)=2-x^2$: Correct
    7. $f(x-4)=2-(x-4)^2$: ***Incorrect***, real answer: $-x^2+8x-14$
    8. $f(x)-4=-2-x^2$: ***Incorrect***, real answer: $-x^2-2$
    9. $f(x^2)=2-(x^2)^2$: ***Incorrect***, real answer: $2-x^4$
14. $f(x)=x^2-3x+2$
    1. $f(3)=2$: Correct
    2. $f(-1)=0$: ***Incorrect***, real answer: $6$
    3. $f(\frac{3}{2})=-\frac{9}{4}$: ***Incorrect***, real answer: $\frac{1}{4}$
    4. $f(4x)=x^2-7x+2$: ***Incorrect***, real answer: $16^2-12x+2$
    5. $4f(x)=4x^2-12x+8$: Correct
    6. $f(-x)=(-x)^2-3(-x)+2$: ***Incorrect***, real answer: $x^2+3x+2$
    7. $f(x-4)=(x-4)^2-3(x-4)+4$: ***Incorrect***, real answer: $x^2-11x+30$
    8. $f(x)-4=x^2-3x-2$: Correct
    9. $f(x^2)=(x^2)^2-3x^2+2$: ***Incorrect***, real answer: $x^4-3x^2+2$
15. $f(x)=\frac{x}{x-1}$
    1. $f(3)=\frac{3}{2}$: Correct
    2. $f(-1)=\frac{1}{2}$: Correct
    3. $f(\frac{3}{2})=3$: Correct
    4. $f(4x)=\frac{4x}{4x-1}$: Correct
    5. $4f(x)=\frac{4x}{x-1}$: Correct
    6. $f(-x)=\frac{-x}{-x-1}$: ***Incorrect***, real answer: $\frac{x}{x-1}$
    7. $f(x-4)=\frac{x-4}{x-5}$: Correct
    8. $f(x)-4=\frac{x-4}{x-1}$, maybe $x-4$: ***Incorrect***, real answer $\frac{x}{x-1}-4$
    9. $f(x^2)=\frac{x^2}{x^2-1}$: Correct
16. $f(x)=\frac{2}{x^3}$
    1. $f(3)=\frac{2}{27}$: Correct
    2. $f(-1)=2$: ***Incorrect***, real answer: $-2$
    3. $f(\frac{3}{2})=\frac{3}{\frac{27}{8}}$: ***Incorrect***, real answer: $\frac{16}{27}$
    4. $f(4x)=\frac{2}{(4x)^3}$: ***Incorrect***, real answer: $\frac{1}{32x^3}$
    5. $4f(x)=\frac{8}{x^3}$: Correct
    6. $f(-x)=\frac{2}{x^3}$: ***Incorrect***, real answer: $-\frac{2}{x^3}$
    7. $f(x-4)=\frac{2}{(x-4)^2}$: ***Incorrect***, real answer: $\frac{2}{(x-4)^3}$
    8. $f(x)-4=\frac{-2}{x^3}$: ***Incorrect***, real answer: $\frac{2}{x^3}-4$
    9. $f(x^2)=\frac{2}{(x^2)^2}$: ***Incorrect***, real answer: $\frac{2}{x^6}$
17. $f(x)=6$
    1. All answers = 6: mostly Correct
    2. 5 and 8 are ***incorrect***, since operations apply after the fact.
18. $f(x)=0$
    1. All answer = 0.
    2. 8 is ***Incorrect***, real answer $-4$
19. $f(x)=2x-5$
    1. $f(2)=-1$: Correct
    2. $f(-2)=-9$: Correct
    3. $f(2a)=4a-5$: Correct
    4. $2f(a)=4a-5$: ***Incorrect***, real answer: $4a-10$
    5. $f(a+2)=2a-1$: Correct
    6. $f(a)+f(2)=2a-6$: Correct
    7. $f(\frac{2}{a})=\frac{-1}{a}$: ***Incorrect***, real answer: $\frac{4}{a}-5$
    8. $\frac{f(a)}{2}=\frac{2a-5}{2}$: Correct
    9. $f(a+h)=2a+2h-5$: Correct
20. $f(x)=5-2x$
    1. $f(2)=1$: Correct
    2. $f(-2)=9$: Correct
    3. $f(2a)=5-4a$: Correct
    4. $2f(a)=10-4a$: Correct
    5. $f(a+2)=-2a+4$: ***Incorrect***, real answer: $1-2a$
    6. $f(a)+f(2)=6-2a$: Correct
    7. $f(\frac{2}{a})=5-\frac{4}{a}$: Correct
    8. $\frac{f(a)}{2}=\frac{5-2a}{2}$: Correct
    9. $f(a+h)=5-2a+2h$: ***Incorrect***, real answer: $5-2a-2h$
21. $f(x)=2x^2-1$
    1. $f(2)=7$: Correct
    2. $f(-2)=7$: Correct
    3. $f(2a)=2(2a)^2-1$: ***Incorrect***, real answer: $8a^2-1$
    4. $2f(a)=4a^2-3$: ***Incorrect***, real answer: $4a^2-2$
    5. $f(a+2)=2a+4^2-1$: ***Incorrect***, real answer: $2a^2+8a+7$
    6. $f(a)+f(2)=2a^2+6$: Correct
    7. $f(\frac{2}{a})=\frac{2}{a}^2-1$: Correct
    8. $\frac{f(a)}{2}=\frac{2a^2-1}{2}$: Correct
    9. $f(a+h)=2a+2h^2-1$: ***Incorrect***, real answer: $2a^2+4ah+2h^2-1$
22. $f(x)=3x^2+3x-2$
    1. $f(2)=16$: Correct
    2. $f(-2)=4$: Correct
    3. $f(2a)=12a^3-2$: ***Incorrect***, real answer: $12a^2+6a-2$
    4. $2f(a)=12a^3-4$: ***Incorrect***, real answer: $6a^2+6a-4$
    5. $f(a+2)=3a+6^2+3a+4$: ***Incorrect***, real answer: $3a^2+15a+16$
    6. $f(a)+f(2)=6a^3+14$: ***Incorrect***, real answer: $3a^2+3a+14$
    7. $f(\frac{2}{a})=\frac{6}{a}+$: ***Incorrect***, real answer: $\frac{12}{a^2}+\frac{6}{a}-2$
    8. $\frac{f(a)}{2}=\frac{6a^3-2}{2}$: ***Incorrect***, real answer: $\frac{3a^2+3a-2}{2}$
    9. $f(a+h)=3a^2+3h^3-2$: ***Incorrect***, real answer: $3a^2+6ah+3h^2+3a+3h-2$
23. $f(x)=\sqrt{2x+1}$
    1. $f(2)=\sqrt{5}$: Correct
    2. $f(-2)=\emptyset$: Correct
    3. $f(2a)=\sqrt{4a+1}$: Correct
    4. $2f(a)=\sqrt{2a+1}2$: Correct
    5. $f(a+2)=\sqrt{3a+5}$: ***Incorrect***, real answer: $\sqrt{2a+5}$
    6. $f(a)+f(2)=\sqrt{2a+1}+\sqrt{5}$: Correct
    7. $f(\frac{2}{a})=\sqrt{\frac{4}{a}+1}$: Correct
    8. $\frac{f(a)}{2}=\frac{\sqrt{2a+1}}{2}$: Correct
    9. $f(a+h)=\sqrt{2a+2h+1}$: Correct
24. $f(x)=117$
    1. All answers are 117
    2. 4, 6, and 8 are ***Incorrect***, real answer: $234$, $234$, $\frac{117}{2}$
25. $f(x)=\frac{x}{2}$
    1. $f(2)=1$: Correct
    2. $f(-2)=2?$: ***Incorrect***, real answer: $-1$
    3. $f(2a)=a$: Correct
    4. $2f(a)=\frac{a}{2}$: ***Incorrect***, real answer: $a$
    5. $f(a+2)=\frac{a+2}{2}$:: Correct
    6. $f(a)+f(2)=\frac{a}{2}+1$: Correct
    7. $f(\frac{2}{a})=\frac{1}{2}$: ***Incorrect***, real answer: $\frac{1}{a}$
    8. $\frac{f(a)}{2}=\frac{\frac{a}{2}}{2}$: ***Incorrect***, real answer: $\frac{a}{4}$
    9. $f(a+h)=\frac{a+h}{2}$: Correct
26. $f(x)=\frac{2}{x}$
    1. $f(2)=1$: Correct
    2. $f(-2)=\frac{2}{-2}$: ***Incorrect***, real answer: $-1$
    3. $f(2a)=a$: ***Incorrect***, real answer: $\frac{1}{a}$
    4. $2f(a)=\frac{4}{a}$: Correct
    5. $f(a+2)=\frac{2}{a+2}$: Correct
    6. $f(a)+f(2)=\frac{2}{a}+1$: Correct
    7. $f(\frac{2}{a})=\frac{2}{\frac{2}{a}}$: ***Incorrect***, real answer: $a$
    8. $\frac{f(a)}{2}=\frac{\frac{2}{a}}{2}$: ***Incorrect***, real answer: $\frac{1}{a}$
    9. $f(a+h)=\frac{2}{a+h}$: Correct
27. $x=\frac{1}{2}$: Correct
28. $x=\frac{15}{2}$: Correct
29. $x=$: ***Incorrect***, real answer: $\pm\sqrt{3}$
30. $x=4$: ***50%*** Correct, real answer: $\{-3,4\}$
31. $x=-4$: Correct
32. $x=\frac{1}{2}$: Correct
33. $4$ or no answer: Unclear
34. $0$: ***50%*** Correct, real answer: $\{0,4\}$
35. Compute the values:
    1.  $1$: Correct
    2.  $2$: Correct
    3.  $0$: Correct
    4.  $2.001$: ***Incorrect***, real answer: $1.999$
    5.  $2.001$: ***Incorrect***, real answer: $1.999$
    6.  $\sqrt{5}$: Correct
36. Compute the values:
    1.  $1$: ***Incorrect***, real answer: $4$
    2.  $9$: Correct
    3.  $0$: Correct
    4.  $1$: Correct
    5.  $1$: Correct
    6.  $\sqrt{1--0.999^2}$: Correct
37. $(-\infty,\infty)$: Correct
38. $[4,\infty)$: ***Incorrect***, real answer: $(-\infty,\infty)$
39. $x\neq-1$: Correct
40. $x\neq1$: ***Incorrect***, real answer: $(-\infty,-2)\cup(-2,1)\cup(1,\infty)$
41. $(-\infty,\infty)$: Correct
42. $x\neq\sqrt{3}$: ***Incorrect***, real answer: $(-\infty,-\sqrt{3})\cup(-\sqrt{3},\sqrt{3})\cup(\sqrt{3},\infty)$
43. $x\neq6$: ***Incorrect***, real answer: $(-\infty,-6)\cup(-6,6)\cup(6,\infty)$
44. $x\neq2$: Correct
45. $[3,\infty)$: ***Incorrect***, real answer: $(-\infty,3]$
46. $(-\infty,\infty)$: ***Incorrect***, real answer: $[-\frac{5}{2},\infty)$
47. $[-3,\infty)$: Correct
48. $[7,\infty)$: ***Incorrect***, real answer: $(-\infty,7]$
49. $[\frac{1}{3},\infty)$: Correct
50. $(\frac{1}{3},\infty)$: Correct
51. $(-\infty,\infty)$: Correct
52. $[\frac{1}{3},3)\cup(3,\infty)$: Correct
53. $[\frac{1}{3},6)\cup(6,\infty)$: Correct
54. $(-\infty,\infty)$: Correct
55. $x\neq8$: Correct
56. $[0,8)\cup(8,\infty)$: Correct
57. $[8,\infty)$: Correct
58. $[7,9)$: Correct
59. $(-\infty,8)\cup(8,\infty)$: Correct
60. $x\neq\{0,\sqrt{\frac{1}{4}}\}$: ***Incorrect***, real answer: $(-\infty,-\frac{1}{2})\cup(-\frac{1}{2},0)\cup(0,\frac{1}{2})\cup(\frac{1}{2},\infty)$
61. $[0,5)\cup(5,\infty)$: Correct
62. $[0,25)\cup(25,\infty)$: Correct
63. $A(3)=9$, $A(x=6)=36$. $x$ is restricted to a value greater than 0 because there will be no square with that value being passed through the function. ***50%*** Correct, real answer: $Ax=\pm6)=36$
64. $A(2)=\pi4$, $A(r=4)=\pi16$, same reason as the previous question. ***50%*** Correct, real answer: $A(r=\pm4)=\pi16$
65. $V(5)=125$, $V(x=3)=27$: Correct
66. $V(3)=\frac{108\pi}{3}$, $V(r=2)=\frac{32\pi}{3}$: Correct
67. $h(0)=64$, $h(t=\{-2,2\})=0$, because you can't drop something below the ground. Correct
68. $T(0)=3$, $T(6)=69.5$, $T(12)=171.5$: ***Incorrect***, real answer: $T(0)=3$, $T(6)=33$, $T(12)=27$
69. $C(0)=27$, $C(2)=3$, $C(5)=2$: ***$\frac{2}{3}$*** Correct, real answer: $C(2)=11$
70. $F(0)=16$, $F(14)=102.71$, $F(28)=362.84$: ***$\frac{1}{3}$*** Correct, real answer: $F(14)=20.81$, $F(28)=22.64$
71. $P(0)=0$, $P(205)=139.77$: Correct
72. Interpret $C(n)$
    1. $C(20)=300$: Correct
    2. $C(50)=675$, $C(51)=612$: Correct
    3. $45$ books: Incorrect, real answer: $56$
73. Interpret $S(n)$
    1. $17.5$: Correct
    2. They are likely incentivizing large purchases with no shipping: Correct
74. Interpret $C(m)$
    1. $25$: Correct
    2. $27$: Incorrect
    3. After 1000 minutes the cost of each extra minute is 0.1. Correct
75. Interpret $\mathbb{Z}$
    1. $1$, $117$, $-2$, $10$: Somewhat correct, I was unaware of the notations meaning, upon discovering what it possibly meant I decided to leave the answer unchanged, but if were true then all values would be decremented by 1.
    2. You are interpreting a value and deciding if there is an acceptable value either equal to it or greater than it, and depending on that the value chosen will be different.
    3. Yes.
76. Write function
    1. $f(x)=x$
    2. $f(x)=x$
    3. $f(x)=x$

## Function arithmetic
#### Function arithmetic operations and syntax
* Sum: $(f+g)(x)=f(x)+g(x)$
* Difference: $(f-g)(x)=f(x)-g(x)$
* Product: $(fg)(x)=f(x)g(x)$
* Quotient: $(\frac{f}{g})(x)=\frac{f(x)}{g(x)}$

When using function arithmetic you use their outputs for the operation.

> Problem 1.5.1. Let $f(x)=6x^2-2x$ and $g(x)=3-\frac{1}{x}$.

1. 12
2. 50
3. Domain: $x\neq0$, simplification: $\frac{3-\frac{1}{x}-6x^2-2x}{x}$
   * Note: For some reason you can take an simple equation like above and take the fraction which is $\frac{1}{x}$ and extend the fraction to every term there is.
4. Domain: $x\neq\{0,\}$, simplification: $\frac{3-\frac{1}{x}}{6x^2-2x}$
##### Solution for problem 4:
1. $\frac{g(x)}{f(x)}$
2. $\frac{3-\frac{1}{x}}{6x^2-2x}$
3. $\frac{3-\frac{1}{x}}{6x^2-2x}*\frac{x}{x}$
Simplifying compound fractions
4. $\frac{(3-\frac{1}{x})x}{(6x^2-2x)x}$
5. $\frac{3x-1}{(6x^2-2x)x}$
6. $\frac{3x-1}{2x^2(3x-1)}$
Factor? what is happening here?
7. $\frac{1}{2x^2}$


We must find the domain of a function before simplifying otherwise we run the risk of not finding the true domain by canceling out parts of our equation that notify us of certain inclusions/exclusions within the domain.

#### The difference quotient
Given a function $f$, the difference quotient of $f$ is the expression:
$$ \frac{f(x+h)-f(x)}{h} $$
For reasons which will become clear in calculus, 'simplifying' a difference quotient means rewriting it in a form where the 'h' in the definition of the difference quotient cancels from the denominator. Once that happens, we consider our work to be done.

> Problem 1.5.2. Find and simplify the difference quotients for the following functions

1. $h^2-2x-4$, real answer $2x+h-1$
2. $2h$
3. $\frac{\sqrt{h}}{h}$

---

#### Conjugates in fraction simplification
Outside resource:
[How to solve limits by conjugate multiplication](https://www.dummies.com/education/math/calculus/how-to-solve-limits-by-conjugate-multiplication/)

The conjugate of a two-term expression is just the same expression with subtraction switched to addition or vice-versa. However it seems that this doesn't apply to every operation, but only to operations of terms, exluding 'inner' terms, such as $\sqrt{x+y}$, in such a situation it would remain the same. But with $\sqrt{x}+\sqrt{y}$, the $+$ would be reversed to a $-$.

The product of conjugates is always the square of the first thing minus the square of the second thing. For example:
$$ \frac{(\sqrt{x}-2)}{(x-4)}*\frac{(\sqrt{x}+2}{(x+4)} $$
$$ \frac{\sqrt{x}^2-2^2}{(x-4)(\sqrt{x}+2)} $$

Since a square root squared is equal to the number in the square root  simplification takes place as follows:

$$ \frac{x-4}{(x-4)(\sqrt{x}+2)} $$
Cancel out the $(x-4)$ from the numerator and the denominator
$$ \frac{1}{\sqrt{x}+2} $$
Why $(x-4)$ is being replaced with a $1$, I do not know.

---

#### Classical applications of function arithmetic
* Let $x$ be the production level in this example, that is, the number of items produced in a given time period.
* Let $C(x)$ denote the function that calculates the total cost of producing $x$ items. Where $C(x)$ is the fixed cost and the cost when producing nothing.
* $\bar{C}(x)$ is the average/mean cost per item, the computation is as follows: $\bar{C}(x)=\frac{C(x)}{x}$.
* $p$ is the price charged per item.
* Here $x$ is the dependent variable and $p$ is the independent variable, or using function notation, we have the function $x(p)$.
* Our next function to consider is $R(x)$, for revenue. It computes the amount of money collected as a result of selling $x$ items.
* The last function $P(x)$, for profit, is the money earned after all costs are paid. $P(x)=(R-C)(x)=R(x)-C(x)$

> Problem 1.5.3. Let $x$ represent the number of dOpi media players produced and sold in a typical week. Suppose the cost in dollars to produce $x$ dOpis is given by $C(x)=100x+2000$, for $x\geq0$, and the price, in dollars per dOpi, is given by $p(x)=450-15x$ for $0\leq x\leq30$.

1. $2000$ is the cost for maintaining producability of dOpi media players, i.e. paying workers or running factory costs.
2. $300$ is the average cost per item.
3. $450$ is the cost for creating no items, and the cost for creating 20 items is $150$.
4. $x=30$, in this situation it seems that the price charged per item goes down to 0.
5. $R(x)=450x-15x^2$, $P(x)=115x^4-1550$.
6. $R(0)=0$, because the way that revenue is driven is with sales, and since none are made no $0$ dollars are made. $P(0)=-2000$ is the profit net for selling $0$ items, money is lost if no sales are made.

$$ 0 = P(x) $$
$$ 0 = -15x^2+350x-2000 $$
$$ -2000 = \frac{-15x^2+350}{x}$$

## Exercises
1. $f(x)=3x+1$, $g(x)=4-x$
   1. $(f+g)(2)=9$
   2. $(f-g)(-1)=-7$
   3. $(g-f)(1)=-1$
   4. $(fg)(\frac{1}{2})=17\frac{1}{2}$
   5. $(\frac{f}{g})(0)=0$
   6. $(\frac{g}{f})(-2)=\frac{6}{-5}$
2. $f(x)=x^2$, $g(x)=-2x+1$
   1. $(f+g)(2)=1$
   2. $(f-g)(-1)=-2$
   3. $(g-f)(1)=2$
   4. $(fg)(\frac{1}{2})=\frac{0}{8}$
   5. $(\frac{f}{g})(0)=\frac{0}{1}$
   6. $(\frac{g}{f})(-2)=\frac{5}{4}$
3. $f(x)=x^2-x$, $g(x)=12-x^2$
   1. $(f+g)(2)=10$
   2. $(f-g)(-1)=-8$
   3. $(g-f)(1)=11$
   4. $(fg)(\frac{1}{2})=\frac{-47}{16}$
   5. $(\frac{f}{g})(0)=\frac{0}{12}$
   6. $(\frac{g}{f})(-2)=\frac{4}{3}$
4. $f(x)=2x^3$, $g(x)=-x^2-2x-3$
   1. $(f+g)(2)=19$
   2. $(f-g)(-1)=2$
   3. $(g-f)(1)=-6$
   4. $(fg)(\frac{1}{2})=\frac{-1}{2}$
   5. $(\frac{f}{g})(0)=\frac{0}{-3}$
   6. $(\frac{g}{f})(-2)=\frac{3}{-16}$
5. $f(x)=\sqrt{x+3}$, $g(x)=2x-1$
   1. $(f+g)(2)=\sqrt{5}+3$
   2. $(f-g)(-1)=\sqrt{2}+2$
   3. $(g-f)(1)=-1$
   4. $(fg)(\frac{1}{2})=0$
   5. $(\frac{f}{g})(0)=\frac{\sqrt{3}}{-1}$
   6. $(\frac{g}{f})(-2)=\frac{-5}{1}$
6. $f(x)=\sqrt{4-x}$, $g(x)=\sqrt{x+2}$
   1. $(f+g)(2)=\sqrt{2}+2, 6?$
   2. $(f-g)(-1)=\sqrt{5}-1$
   3. $(g-f)(1)=0$
   4. $(fg)(\frac{1}{2})=\frac{7}{4}\sqrt{3}$
   5. $(\frac{f}{g})(0)=\frac{2}{\sqrt{2}}$
   6. $(\frac{g}{f})(-2)=\frac{0}{\sqrt{6}}$
7. $f(x)=2x$, $g(x)=\frac{1}{2x+1}$
   1. $(f+g)(2)=\frac{21}{20}$
   2. $(f-g)(-1)=-3$
   3. $(g-f)(1)=\frac{-5}{3}$
   4. $(fg)(\frac{1}{2})=\frac{1}{2}$
   5. $(\frac{f}{g})(0)=\frac{0}{1}$
   6. $(\frac{g}{f})(-2)=\frac{\frac{1}{-3}}{-4}$
8. $f(x)=x^2$, $g(x)=\frac{3}{2x-3}$
   1. $(f+g)(2)=7$
   2. $(f-g)(-1)=\frac{2}{5}$
   3. $(g-f)(1)=\frac{2}{-1}$
   4. $(fg)(\frac{1}{2})=\frac{1}{4}\frac{3}{\frac{-11}{4}}$
   5. $(\frac{f}{g})(0)\frac{0}{\frac{-3}{3}}$
   6. $(\frac{g}{f})(-2)=\frac{\frac{-3}{5}}{4}$
9. $f(x)=x^2$, $g(x)=\frac{1}{x^2}$
   1. $(f+g)(2)=\frac{17}{4}$
   2. $(f-g)(-1)=2$
   3. $(g-f)(1)=2$
   4. $(fg)(\frac{1}{2})=1$
   5. $(\frac{f}{g})(0)=\emptyset$
   6. $(\frac{g}{f})(-2)=\frac{\frac{1}{4}}{2}$
10. $f(x)=x^2+1$, $g(x)=\frac{1}{x^2+1}$
    1. $(f+g)(2)=\frac{26}{5}$
    2. $(f-g)(-1)=\frac{3}{2}$
    3. $(g-f)(1)=\frac{-3}{2}$
    4. $(fg)(\frac{1}{2})=1$
    5. $(\frac{f}{g})(0)=1$
    6. $(\frac{g}{f})(-2)=\frac{1}{4}$
11. $f(x)=2x+1$, $g(x)=x-2$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=2$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=4$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=3$
    4. $(\frac{f}{g})(x)=(-\infty,0)\cup(0,2)\cup(2,\infty)$
      * $(\frac{f}{g})(1)=\frac{3}{-1}$
12. $f(x)=1-4x$, $g(x)=2x-1$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=-2$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=-4$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=-3$
    4. $(\frac{f}{g})(x)=(-\infty,\frac{1}{2})\cup(\frac{1}{2},\infty)$
      * $(\frac{f}{g})(1)=\frac{-3}{1}$
13. $f(x)=x^2$, $g(x)=3x-1$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=3$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=-1$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=2$
    4. $(\frac{f}{g})(x)=(-\infty,\frac{1}{3})\cup(\frac{1}{3},\infty)$
      * $(\frac{f}{g})(1)=\frac{1}{2}$
14. $f(x)=x^2-x$, $g(x)=7x$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=7$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=-7$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=0$
    4. $(\frac{f}{g})(x)=(-\infty,0)\cup(0,\infty)$
      * $(\frac{f}{g})(1)=\frac{0}{7}$
15. $f(x)=x^2-4$, $g(x)=3x+6$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=6$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=-12$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=-27$
    4. $(\frac{f}{g})(x)=(-\infty,-2)\cup(-2,\infty)$
      * $(\frac{f}{g})(1)=\frac{-3}{9}$
16. $f(x)=-x^2+x+6$, $g(x)=x^2-9$
    1. $(f+g)(x)=(-\infty,\infty)$
      * $(f+g)(1)=0$
    2. $(f-g)(x)=(-\infty,\infty)$
      * $(f-g)(1)=16$
    3. $fg(x)=(-\infty,\infty)$
      * $(fg)(1)=-64$
    4. $(\frac{f}{g})(x)=(-\infty,3)\cup(3,\infty)$
      * $(\frac{f}{g})(1)=\frac{8}{-8}$
17. $f(x)=\frac{x}{2}$, $g(x)=\frac{2}{x}$
    1. $(f+g)(x)=(-\infty,0)\cup(0,\infty)$
      * $(f+g)(1)=\frac{5}{4}$
    2. $(f-g)(x)=(-\infty,0)\cup(0,\infty)$
      * $(f-g)(1)=\frac{-3}{2}$
    3. $fg(x)=(-\infty,0)\cup(0,\infty)$
      * $(fg)(1)=1$
    4. $(\frac{f}{g})(x)=(-\infty,0)\cup(0,\infty)$
      * $(\frac{f}{g})(1)=\frac{1}{4}$
18. $f(x)=x-1$, $g(x)=\frac{1}{x-1}$
    1. $(f+g)(x)=(-\infty,1)\cup(1,\infty)$
      * $(f+g)(2)=2$
    2. $(f-g)(x)=(-\infty,1)\cup(1,\infty)$
      * $(f-g)(2)=0$
    3. $fg(x)=(-\infty,1)\cup(1,\infty)$
      * $(fg)(2)=1$
    4. $(\frac{f}{g})(x)=(-\infty,1)\cup(1,\infty)$
      * $(\frac{f}{g})(2)=1$
19. $f(x)=x$, $g(x)=\sqrt{x+1}$
    1. $(f+g)(x)=[-1,\infty)$
      * $(f+g)(1)=1+\sqrt{2}$
    2. $(f-g)(x)=[-1,\infty)$
      * $(f-g)(1)=1-\sqrt{2}$
    3. $fg(x)=[-1,\infty)$
      * $(fg)(1)=\sqrt{2}$
    4. $(\frac{f}{g})(x)=(-1,\infty)$
      * $(\frac{f}{g})(1)=\frac{1}{\sqrt{2}}$
20. $f(x)=\sqrt{x-5}$, $g(x)=\sqrt{x-5}$
    1. $(f+g)(x)=(5,\infty)$
      * $(f+g)(1)=4$
    2. $(f-g)(x)=(5,\infty)$
      * $(f-g)(1)=0$
    3. $fg(x)=(5,\infty)$
      * $(fg)(1)=4$
    4. $(\frac{f}{g})(x)=(5,\infty)$
      * $(\frac{f}{g})(1)=1$
Find and simplify the quotient $\frac{f(x+h)-f(x)}{h}$.
21. 