# Iterate Pythonically

___
## Problem to Solve

> **I want to accomplish various iteration-related tasks while keeping my code simple and easy.**

When iterating over the elements in a collection, it's easy to fall back on counter-based iteration like one would use in an old-fashioned language such as fortran, C, or java. Don't do that! Python has a different conceptualization of "iteration", and it's more powerful, convenient, and compact. Some situations do require the use of a counter variable and index-based collection access, but they're fairly rare.

It's also worth remembering that many tasks that require iteration in lower-level languages can be done with a single function or method call in python. For example, to find the sum of the elements in a list, you can do `sum(some_list)` instead of adding them up one at a time via iteration.

What follows is a few example recipes to illustrate the "pythonic way" to iterate over collections.

___
## A Few Recipes

### do something with every element of a tuple, list, or set

```python
for element in some_list_set_or_collection:
    # do something with element
```

### iterate over a sequence's elements in reverse order

```python
for element in reversed(some_sequence):
    # do something with element
```

### keep a counter variable while iterating

Sometimes you do need to count the iterations as you iterate through a sequences. That does not mean you should reach for `for i in range(...)` and access the elements by index! Python provides the `enumerate()` function specifically for this:

```python
for i, element in enumerate(some_sequence):
    print(f"Element number {i} is {element}.")
```

### iterating over corresponding items of two (or more) sequences

```python
list_of_sums =[]
for element1, element2 in zip(sequence1, sequence2):
    list_of_sums.append(element1 + element2)
```

### iterating over corresponding items of two (or more) sequences while keeping a counter

```python
for i, (x, y) in enumerate(zip(x_values, x_values)):
    print(f"The coordinates of point {i} are ({x}, {y}).")
```

### iterating over all combinations of elements from two sequences

The old-school way:

```python
# Not very pythonic:
for x in x_values:
    for y in y_values:
        print(f"The coordinates of point ({x}, {y}).")
```

The pythonic way:

```python
from itertools import product
for x, y in product(x_values, y_values):
    print(f"The coordinates of point ({x}, {y}).")
```

It's only the same number of lines the first time you use it; after that, the import statement doesn't need to be repeated. And in general, the less nested your code is, the easier it is to comprehend.

### iterating over a sequence in multi-element chunks

```python
from itertools import batched
for tuple_of_n_successive_elements in batched(some_sequence, n):
    # do something with each successive set of `n` elements
```

___
## Bonus Skill: Comprehensions

For tasks that require a short, simple iterative loop to produce a new list, set, or dict, python provides a special syntax called a _comprehension_. Comprehensions are a compact way to express the same thing you would do with a loop, but in a single line of code. They are often more readable than the equivalent loop, and they can be faster too.

- <a href="https://www.geeksforgeeks.org/python-list-comprehension/" target="_blank">Geeks for Geeks: _List Comprehension in Python_</a>

- <a href="https://openstax.org/books/introduction-python-programming/pages/9-5-list-comprehensions" target="_blank">OpenStax Intro to Python Programming: List Comprehensions</a>

### calculate values of a new list from corresponding elements of an old list

```python
old_list = [1.2, 3.4, 7.9, 12.4]  # just an arbitrary example
squares_of_old = [x**2 for x in old_list]
roots_of_old = [math.sqrt(x) for x in old_list]
roots_of_all = [math.sqrt(n) for n in range(1, 100)]
```

### filter a list to keep only some elements

```python
data = [random.uniform(-1, 1) for _ in range(10)]  # just fake data
positive_data = [x for x in data if x > 0]
divisible_by_7 = [x for x in range(1, 100) if x % 7 == 0]
```

### calculate values of a new list from only some values in an old list

```python
data_sqrts_1 = [math.sqrt(x) for x in data if x > 0]  # omit negative values
data_sqrts_2 = [math.sqrt(x) if x > 0 else 0 for x in data]  # replace negative values with 0
```

Comprehensions can also make sets, dictionaries, and a special kind of object called a _generator_, just by changing the syntax slightly.

### combine a keywords list and a values list into a dictionary

```python
keys = ['mass', 'charge', 'spin']
values = [9.11e-31, -1.6e-19, 1/2]
dict1 = {key: val for key, val in zip(keys, values)}
```

Note the curly-braces. List comprehensions use square brackets; set comprehensions use curly braces; and dict comprehensions use curly braces with a colon between the key and value.

