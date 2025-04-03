# Shuffle and/or Sample From a Set

___
## Problem to Solve

> **I want to randomly mix a sequence of things and/or randomly choose a subset of them.**

Here are two closely-related tasks:

1. **Shuffling:** Given a sequence of things, randomize their order.

1. **Sampling:** Given a sequence of things, randomly choose a subset of them.

The second may sound a lot like what `choices()` does, as presented in [the previous recipe](choices.md), but there's a key difference: `choices()` with `k > 1` chooses multiple items **with replacement**, so that one item can possibly be picked multiple times. "Choose a random subset", on the other hand, does not allow replacement: An item can only appear once in the subset; once it's chosen, it can't be chosen again.

Again, the recipes below will assume that `import random` has already been executed.

___
## Recipes for Shuffling

To randomize the order of the items in a list:

```python
# Assuming `some_list` is a list of things:
random.shuffle(some_list)
# `some_list` is now shuffled.
```

Note that unlike most of the other functions in `random`, `shuffle()` does not return a new list. Instead, it modifies the list you give it.

As a consequence, you cannot call `shuffle()` on an immutable sequence like a tuple. If you want to shuffle a tuple, you can convert it to a list, shuffle the list, and then convert it back to a tuple:

```python
# Assuming `some_tuple` is a tuple of things:
shuffled_tuple = tuple(shuffle(list(some_tuple)))
# `shuffled_tuple` is now a shuffled version of `some_tuple`.
```

Since sets are in principle unordered, shuffling them makes no sense. If you want to access a set's elements in a randomized order:

```python
# Assuming `some_set` is a set of things:
list_from_shuffled_set = shuffle(list(some_set))
```

Dictionaries are also unordered. Let's say you want to do something with the items in a dictionary, and it's important to randomize the order. You can do this:

```python
# Assuming `some_dict` is a dictionary of things:
randomized_keys = shuffle(list(some_dict.keys()))
for key in randomized_keys:
    # Do something with `some_dict[key]`, for example:
    print(f"The key {key} is associated with the value {some_dict[key]}")
```

(I have no idea why you'd want to print out the key-value pairs in a random order, but you get the idea…)

___
## Recipes for Sampling

To randomly choose a subset of items from a list or tuple, use `random.sample()`:

```python
# Assuming `some_sequence` is a list or tuple of things:
random_subset = random.sample(some_sequence, num_to_choose)
```

This produces a list containing `num_to_choose` items randomly chosen from `some_sequence`.

If you want to sample from a set, you can convert it to a list and then back again:

```python
# Assuming `some_set` is a set of things:
random_subset = set(random.sample(list(some_set), num_to_choose))
```

You can use the same trick to randomly sample from a dictionary. (I'll [use a "dictionary comprehension"](../../core/collections/iterate-pythonically.md) to compactly make a new dictionary with just the chosen key/value pairs. You could accomplish the same thing by creating an empty dictionary and then iterating over the keys in `random_key_sample`, adding those keys and their associated values to the new dictionary.)

```python
# Assuming `some_dict` is a dictionary of things:
random_key_sample = random.sample(list(some_dict.keys()), num_to_choose)
subset_dict = {
    key: some_dict[key]
    for key in random_key_sample
}
```

