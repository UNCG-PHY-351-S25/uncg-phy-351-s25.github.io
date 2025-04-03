# Generate Random Integers

___
## Problem to Solve

> **I want an integer randomly chosen from some range.**

If you need your code to randomly pick an integer within some range, with all outcomes equally likely (like rolling a die), this is your recipe.

All of these recipes use the `random` module, which is part of the Python standard library. You can read about it in the [Python documentation](https://docs.python.org/3/library/random.html). For the sake of brevity, the recipes will assume that `import random` has already been executed.

___
## Recipes

### generating a random integer between 0 and $N - 1$, inclusive

The `random` module's basic function for generating random integers is `randrange(…)`. Like the `range(...)` function for iteration, `randrange(N)` produces a randomly-chosen integer between 0 and $N - 1$, inclusive.

To select a random element from a list or other indexable sequence:

```python
one_value = random.randrange(len(my_list))
```

If you want to specify a lower bound other than zero, call the function with two arguments. For example, to select any value from a list **other than the first**:

```python
one_value = random.randrange(1, len(my_list))
```

The `randrange()` function can take an optional third argument that specifies an increment or step, so you could conceivably get it to produce a randomly-chosen integer from the set $\{2, 5, 8, 11, \dots, 32\}$ by calling `random.randrange(2, 33, 3)`. It doesn't take keyword arguments, though, so <a href="https://docs.python.org/3/library/random.html#functions-for-integers" target="_blank">read the documentation</a> if you want to do that.


### generating an integer between $a$ and $b$, inclusive

A common annoyance and source of bugs is the fact that we often think "I want a random number from 1 to 20", and accidentally write `random.randint(1, 20)`, which can never produce `20` as a result. Unless you need the weird `step` functionality of `randrange`, it's generally easier and safer to use `randint(a, b)`, which produces a random integer between `a` and `b`, inclusive.

To simulate a six-sided die:

```python
roll_value = random.randint(1, 6)
```

To generate random integer coordinates between -10 and +10 inclusive:

```python
x = random.randint(-10, 10)
y = random.randint(-10, 10)
```

To simulate rolling two six-sided dice and adding their values:

```python
craps_roll = random.randint(1, 6) + random.randint(1, 6)
```

Make sure not to use `2 * random.randint(1, 6)` instead. That simulates rolling one die and doubling it.

