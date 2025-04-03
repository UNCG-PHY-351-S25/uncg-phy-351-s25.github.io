# Manage Sequences of Values with Lists

___
## Problem to Solve

> **I want to build, modify, retrieve elements from, and iterate over a sequence of values.**

A list is basically just like a tuple, except that it can be modified in all kinds of ways after it has been created: Lists are _mutable_. You can add elements, remove elements, change the value of existing elements, and so on.

You can do almost anything with a list that you can do with a tuple, so I won't repeat those recipes here.

- (Exception: The fact that tuples are _immutable_ makes them _hashable_, which means that they can be used as keys in dictionaries and as elements of sets. That is occasionally useful.)

Again, I'll point you to some online introductions:

- <a href="https://www.w3schools.com/python/python_lists.asp" target="_blank">W3 Schools: _Python Lists_</a>

- <a href="https://www.geeksforgeeks.org/python-lists/" target="_blank">Geeks for Geeks: _Python Lists_</a>

___
## A Few Recipes

### change the value of an existing list element

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1[2] = 99  # change the value at index 2
print(list1)  # yields [1, 2, 99, 4, 5]
```

### append an element to a list

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.append(6)  # add 6 to the end of the list
print(list1)  # yields [1, 2, 3, 4, 5, 6]
```

### append multiple elements to a list

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.extend([6, 7, 8])  # add 6, 7, and 8 to the end of the list
print(list1)  # yields [1, 2, 3, 4, 5, 6, 7, 8]
```

Note that `append()` can only add one element at a time; to add multiple elements at once, use `extend()`.

### insert an element at a specific index

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.insert(2, 99)  # insert 99 at index 2
print(list1)  # yields [1, 2, 99, 3, 4, 5]
```

### remove a specific value from a list

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.remove(3)  # remove the first occurrence of 3
print(list1)  # yields [1, 2, 4, 5]
```

### remove an element at a specific index

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.pop(2)  # remove the element at index 2
print(list1)  # yields [1, 2, 4, 5]
```

The `pop()` method returns the value of the element its removing, so you can do something like this:

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
i = 2
print(f"Removed {list1.pop(i)} from position {i} position in the list")
print(list1)  # yields [1, 2, 4, 5]
```

### remove the last element from a list

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.pop()  # pop() with no argument means "the last element"
print(list1)  # yields [1, 2, 3, 4]
```

### remove all elements from a list

```python
list1 = [1, 2, 3, 4, 5]  # a list of integers
list1.clear()  # remove all elements
print(list1)  # yields []
```
### sort a list

```python
list1 = [5, 2, 4, 3, 1]  # a list of integers
list1.sort()  # sort the list in place
print(list1)  # yields [1, 2, 3, 4, 5]
```
### sort a list in reverse order

```python
list1 = [5, 2, 4, 3, 1]  # a list of integers
list1.sort(reverse=True)  # sort the list in place, in reverse order
print(list1)  # yields [5, 4, 3, 2, 1]
```

### build a list iteratively

This is a very common idiom in computational physics:

```python
list1 = []  # an empty list
for i in range(5):
    list1.append(i**2)  # add the square of i to the list
print(list1)  # yields [0, 1, 4, 9, 16]
```

### create a list from a string

```python
list1 = list("abc")  # a list of characters
print(list1)  # yields ['a', 'b', 'c']
```

### create a list from a range object

```python
list1 = list(range(5))  # a list of integers
print(list1)  # yields [0, 1, 2, 3, 4]
```

