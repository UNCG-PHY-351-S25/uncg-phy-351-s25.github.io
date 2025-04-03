# Generate Random Real Numbers

___
## Problem to Solve

> **I want a real number (a float) randomly chosen from some range.**

In the earlier recipe [**Generate Random Integers**](integers.md), we saw how to randomly choose an integer from a range of integers. Physics applications tend to use real numbers (floats) more often than integers, so randomly generating those is important too.

These recipes assume you want to pick a number with in some range of values, with all possibilities in that range being equally likely. The technical term for that is "sampling from a _uniform_ distribution." If you need to weight some values more than others, see the next recipe, [**Draw From a Weighted Distribution**](distributions.md).

Again, we're assuming `import random` has been done.

___
## Recipe: Generate a Real Number Between 0 (inclusive) and 1 (exclusive)

Under the hood, this is the most fundamental of all pseudorandom number tasks; all the rest are built upon this. As a result, this is one is the fastest.

```python
zero_to_one = random.random()
```

That's it. The `random()` function returns a float in the range `[0.0, 1.0)` every time it's called. No arguments.

## Recipe: Flip a Biased Coin

One common application of this "flipping a biased coin", i.e., choosing between two alternatives where one outcome has probability $p$ and the other has probability $1 - p$. The recipe is:

```python
if random.random() < p:
    result = "heads"
else:
    result = "tails"
```

or, more compactly using python's "ternary operator" for one-line if/else,

```python
result = "heads" if random.random() < p else "tails"
```

You could accomplish the same thing with `result = random.choices(["heads", "tails"], [p, 1 - p])`, but that's considerably slower — by my tests, about 13 times slower.

## Recipe: Generate a Real Number Between Two Arbitrary Values

This is the most common need: Randomly pick a number between $a$ and $b$ (inclusive of endpoints), with all values in that range equally likely. The recipe is:

```python
# assuming `a` and `b` are already defined,
random_value = random.uniform(a, b)
```

___
