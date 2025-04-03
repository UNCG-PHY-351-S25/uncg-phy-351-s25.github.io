# Group Related Values Into Tuples

___
## Problem to Solve

> **I want to collect a few values together into a group that I can treat as one "thing", and that won’t need to change.**

In python, a _tuple_ is an ordered collection of items. Unlike a _list_ a tuple cannot be modified after it has been created: we say that tuples are _immutable_.

Rather than reinvent the wheel, I'll direct you to some on line introductions to tuples:

- <a href="https://www.w3schools.com/python/python_tuples.asp" target="_blank">W3 Schools: _Python Tuples_</a>

- <a href="https://www.geeksforgeeks.org/tuples-in-python/" target="_blank">Geeks for Geeks: _Tuples in Python_</a>

___
## A Few Recipes

_In all of these, we'll use the variable names `t`, `t1`, `t2`, etc. to refer to tuples._

### create a tuple explicitly

```python
t1 = (1, 2, 3, 4, 5)  # a tuple of 5 integers (a "five-tuple")
t2 = 1, 2, 3, 4, 5  # parentheses can be omitted IF the result is unambiguous
t3 = ('electron', 'muon', 'tau')  # a three-tuple of strings
t4 = ((1, 2), (11, 12), (21, 22))  # a 3-tuple of 2-tuples
t5 = (22/7, math.pi, math.sqrt(2))  # elements can be the result of expressions
```

### create a tuple from a different collection type

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
t1 = tuple(list1)  # from a list
t2 = tuple('abc')  # from a string: yields ('a', 'b', 'c')
t3 = tuple(range(5))  # from a range object: yields (0, 1, 2, 3, 4)
```

### create an empty or one-element tuple

```python
t1 = ()  # an empty tuple
t2 = tuple()  # another empty tuple
t3 = (3-2j,)  # a one-element tuple (note the comma)
t4 = tuple([22/7])  # another one-element tuple
```

### determine the length of a tuple

```python
t1 = (3, -2, 14, 7, 0)  # a 5-tuple
len(t1)  # yields 5
```

### access individual elements of a tuple

```python
t1 = (3, -2, 14, 7, 0)  # a 5-tuple
t1[0]  # yields 3
t1[1]  # yields -2
t1[-1]  # yields 0 (the last element)
t1[-2]  # yields 7 (the second-to-last element)
```

### change the value of a tuple — NOPE!

```python
t1 = (5, 12, 13)  # a 3-tuple
t1[1] = -12  # TypeError: tuples are immutable!
t1 = (t1[0], -12, t1[2])  # must create a new tuple with the new value(s)
```

### concatenate two tuples

```python
t1 = (1, 2, 3)  # a 3-tuple
t2 = (4, 5, 6)  # another 3-tuple
t3 = t1 + t2  # yields (1, 2, 3, 4, 5, 6)
```

### create a repeating tuple

If you, for some reason, want to create a tuple with the same value repeated multiple times, you can do it like this:

```python
t1 = (1, 2, 3)  # a 3-tuple
t2 = t1 * 3  # yields (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

The original tuple that gets repeated could have only one element, or two, or 17 as you wish.

### nest tuples

```python
t1 = (1, 2, 3)  # a 3-tuple
t2 = (4, 5, 6)  # another 3-tuple
t3 = (t1, t2)  # a 2-tuple of 3-tuples
t4 = ((1, 2), (11, 12), (21, 22))  # a 3-tuple of 2-tuples
```

### access elements of a tuple one at a time

```python
for one_value in t1:
    print(one_value)  # or do anything else with the value
```

