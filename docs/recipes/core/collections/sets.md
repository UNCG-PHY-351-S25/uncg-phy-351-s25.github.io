# Identify Unique & Shared Elements with Sets

___
## Problem to Solve

> **I want to keep track of a collection of unique values and perhaps compare the values present in different such collections.**

A python _set_ is a collection of elements whose properties are analogous to the mathematical concept of a set. 

The key differences between a _set_ and a _list_ are:

- A set is a collection of unique elements, so it cannot contain duplicates.

- A set is unordered, so the order of elements is not guaranteed, and you cannot access its elements by index.

- A set is mutable, but it cannot contain mutable elements (e.g., lists or dictionaries).

- Set objects support several operations that are specific to set logic (union, intersection, etc.)

Some online introductions:

- <a href="https://www.w3schools.com/python/python_sets.asp" target="_blank">W3 Schools: _Python Sets_</a>

- <a href="https://www.geeksforgeeks.org/python-sets/" target="_blank">Geeks for Geeks: _Python Sets_</a>

___
## A Few Recipes

### determining the number of elements in a set

```python
set1 = {1, 2, 3, 4, 5}  # a set of integers
len(set1)  # yields 5
```

### finding the intersection of two sets

```python
set1 = {1, 2, 3, 4, 5}  # a set of integers
set2 = {3, 4, 5, 6, 7}  # another set of integers
set3 = set1.intersection(set2)  # the intersection of set1 and set2
print(set3)  # yields {3, 4, 5}
```

### finding the union of two sets

```python
set1 = {1, 2, 3, 4, 5}  # a set of integers
set2 = {3, 4, 5, 6, 7}  # another set of integers
set3 = set1.union(set2)  # the union of set1 and set2
print(set3)  # yields {1, 2, 3, 4, 5, 6, 7}
```

### finding the elements in one set that aren't also in a second set

```python
set1 = {1, 2, 3, 4, 5}  # a set of integers
set2 = {3, 4, 5, 6, 7}  # another set of integers
set3 = set1.difference(set2)  # the difference of set1 and set2
print(set3)  # yields {1, 2}
```

### finding the elements in either set that aren't in both sets

```python
set1 = {1, 2, 3, 4, 5}  # a set of integers
set2 = {3, 4, 5, 6, 7}  # another set of integers
set3 = set1.symmetric_difference(set2)  # the symmetric difference of set1 and set2
print(set3)  # yields {1, 2, 6, 7}
```

### removing duplicate elements from a list

This is a useful trick!

```python
list1 = [1, 4, 3, 4, 2, 1, 5, 1, 6, 4]  # a list of integers
list2 = list(set(list1))  # convert the list to a set and back to a list
print(list2)  # yields [1, 2, 3, 4, 5, 6] -- order is not guaranteed!
```

