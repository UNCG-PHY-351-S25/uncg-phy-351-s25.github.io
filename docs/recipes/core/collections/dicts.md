# Organize Labeled Collections with Dictionaries

___
## Problem to Solve

> **I want to collect related values together, with the ability to access the elements by some meaningful label rather than by a numeric index.**

_Dictionaries_ ("dicts") are a core workhorse of the python language. Much of python itself is built using dictionaries, which means they are very full-featured and optimized.

Like tuples, lists, and sets, dictionaries are a collection of other values. The key difference is that they are key-value pairs: Each _value_ you stick into a dictionary is associated with a _key_ that you can use to retrieve it later.

- List or tuple: Access an element by its index, for example `mylist[3]`.

- Dictionary: Access an element by its key, for example `mydict['mass']`.

Some online introductions:

- <a href="https://www.w3schools.com/python/python_dictionaries.asp" target="_blank">W3 Schools: _Python Dictionaries_</a>

- <a href="https://www.geeksforgeeks.org/python-dictionary/" target="_blank">Geeks for Geeks: _Dictionaries in Python_</a>

___
## A Few Recipes

The thing that makes dictionaries more complicated to work with than other kinds of collection is the fact that they contain both keys and values.

### building a dictionary one key-value pair at a time

```python
dict1 = {}  # an empty dictionary
dict1['mass'] = 9.11e-31  # add a key-value pair
dict1['charge'] = -1.6e-19  # add another key-value pair
dict1['spin'] = 1/2  # add another key-value pair
print(dict1)  # yields {'mass': 9.11e-31, 'charge': -1.6e-19, 'spin': 0.5}
```

(This is often something you'll do with a loop, adding one item to the dictionary per iteration.)

### building a dictionary from multiple key-value pairs at once

```python
dict1 = {
    'mass': 9.11e-31,
    'charge': -1.6e-19,
    'spin': 1/2
}  # a dictionary with 3 key-value pairs
print(dict1)  # yields {'mass': 9.11e-31, 'charge': -1.6e-19, 'spin': 0.5}
```

### extracting the set of keys

```python
key_set = set(dict1.keys())  # the set of keys in dict1
print(key_set)  # yields {'mass', 'charge', 'spin'}
```

### extracting the keys to a list

```python
key_list = list(dict1.keys())  # the keys in a list
print(key_list)  # yields ['mass', 'charge', 'spin']
```

### extracting the values (without keys) to a list

```python
value_list = list(dict1.values())  # the values in a list
print(value_list)  # yields [9.11e-31, -1.6e-19, 0.5]
average_value = mean(value_list)  # the average of the values
max_value = max(value_list)  # the maximum value
```

### iterating over the keys

```python
for key in dict1:
    print(key)  # yields 'mass', 'charge', 'spin'
```

### iterating over the values

```python
for value in dict1.values():
    print(value)  # yields 9.11e-31, -1.6e-19, 0.5
```

### iterating over the key-value pairs

```python
for key, value in dict1.items():
    print(f"{key} = {value}")  # yields "mass = 9.11e-31", "charge = -1.6e-19", "spin = 0.5"
```

### checking if a key is in the dictionary

```python
if 'mass' in dict1:
    print("`mass` is in the dictionary")
else:
    print("`mass` is NOT in the dictionary")
```

### finding the key corresponding to the maximum or minimum value

```python
max_key = max(dict1, key=dict1.get)  # the key corresponding to the maximum value
max_val = dict1[max_key]  # the maximum value
min_key = min(dict1, key=dict1.get)  # the key corresponding to the minimum value
min_val = dict1[min_key]  # the minimum value
```

### getting a list of the keys sorted according to their values (in ascending order)

```python
sorted_keys = sorted(dict1, key=dict1.get)  # the keys sorted by their values
```

You can then extract the associated values via `dict1[key]` for whatever key(s) you want.

To get the keys in **descending** order of their values, include the optional `reverse=True` argument to the `sorted()` function.

___

Dictionaries have many more features and utility methods, so make sure to read through the references linked above.

