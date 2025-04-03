# Pick Randomly From a Set of Options

___
## Problem to Solve

> **I want to randomly choose one item from a collection of possible choices.**

Sometimes, instead of generating a random integer from some range, you want to randomly pick one item from a collection of possible choices. Picking from a list or tuple can be done by generating a random integer and using it as an index, but that's unnecessary. It also doesn't work for a non-indexable collection like a set or dictionary.

The `random` module's `choice` function does this for you.

If you want to choose more than one item, and/or specify different weights (probabilities) for different items, use the `choices` function instead.


___
## Recipes: Single Choice

To pick one item from a list, tuple, or `range(...)`, or to pick one character from a string:

```python
# Assuming the variable `S` already refers to an appropriate list/tuple/etc.:
random_element = random.choice(S)
```

To pick one item from a set, convert it to a list or tuple:

```python
# Assuming the variable `some_set` already refers to an appropriate set:
random_element = random.choice(tuple(some_set))
```

To pick one item from a dictionary, use the `keys()` method to get a list of the keys and choose one of those randomly:

```python
# Assuming the variable `some_dict` already refers to an appropriate dictionary:
random_key = random.choice(list(some_dict.keys()))
random_value = some_dict[random_key]
```

___
## Recipes: Multiple Choices

The `choices` function can get a list of multiple items all randomly and independently chosen from a given sequence. The items are chosen "with replacement", which means an element is not "used up" when picked and can be picked again. As a result, it's entirely possible to choose more items than the length of the source sequence.

The first argument to `choices` is the sequence to choose from. If you want multiple items, pass a named argument `k` with the number of items you want to choose.

To get a sequence simulating ten consecutive rolls of a six-sided die:

```python
roll_sequence = random.choices(range(1, 7), k=10)
roll_sum = sum(roll_sequence)
```

To get a string of twelve random vowels:

```python
vowel_string = ''.join(random.choices('aeiou', k=12))
```

Side note: `''.join(list_of_strings_or_characters)` is a weird-looking python idiom for concatenating multiple strings or characters into one string. The idea is that the string before the period is inserted between each of the elements of `list_of_strings_or_characters`. So, `', '.join(["one", "two", "three"])` would produce the string `"one, two, three"`, and `''.join(["one", "two", "three"])` would produce the string `"onetwothree"` because the empty string `''` is used to as the separator.

___
## Recipes: Weighted Choices

Sometimes, you'll want to pick one item at random from a list of possibilities, but with some items being more likely than others. In that case, you can supply an optional second argument named `weights` to `choices`. It must have the same length as the sequence of options to choose from, and each element of `weights` should be a number that specifies the relative probability of the corresponding item in the sequence being chosen.

The weights don't have to be normalized, meaning that they don't have to sum to 1. The `choices` function will do that for you.

Let's say that (for some unfathomable reason) you want to choose three integers between 1 and 10 inclusive, but with a probability inversely proportional to the square of the integer. In other words, the number 1 should be one hundred times more likely than the number 10.

```python
option_values = list(range(1, 11))
weight_values = [1 / (x ** 2) for x in option_values]
three_random_choices = random.choices(option_values, weights=weight_values, k=3)
```

If you only want one value chosen with a weighted probability, leave `k` unspecified so that it defaults to 1. However, you'll still get a list with one element in it, so you'll need to slap a bit of indexing on the end to extract that value from the list:

```python
one_random_choice = random.choices(option_values, weights=weight_values)[0]
```

Unless you need unequal weighting, this makes `random.choice` more convenient than `random.choices` for picking a single item. For multiple items **or** unequal weighting, however, `random.choices` is the way to go.

