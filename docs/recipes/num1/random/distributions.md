# Draw From a Weighted Distribution

___
## Problem to Solve

> **I want a number randomly chosen such that the probability of various outcomes follows a specified probability distribution.**

In scientific computing and data science/statistics, a common task is to randomly generate numbers such that some values are more likely than others. The weightings of the various values are specified by a _distribution_, which is basically what a histogram of sampled values would look like in the limit of infinitely many values and infinitely narrow histogram bins. The most famous distribution is the normal (a.k.a. Gaussian) distribution, colloquially known as the "bell curve".

The built-in `random` module provides a few functions for generating pseudorandom numbers from some a few common distributions. The add-on packages _numpy_ and _scipy_, which we'll get to a bit later in the course, provide many, many more.

___
## Recipes

### discrete distribution: the _binomial_ distribution

A _discrete_ distribution is one that can only produce specific values (typically integers), but not any values in between them.

Imagine flipping a biased coin, which comes up "heads" with probability $p$ and "tails" with probability $1 - p$. Now imagine flipping that coin $N$ times, keeping track of the total number of "heads" and "tails" that comes up. What is the probability of getting no "heads" at all and $N$ "tails"? Of getting one "heads" and $N - 1$ "tails"? Of getting 2 and $N - 2$? Etc… This is called the <a href="https://en.wikipedia.org/wiki/Binomial_distribution" target="_blank">_binomial distribution_</a>.

If you want to generate random numbers between 0 and $N$ whose relative likelihood follows this distribution, you can use the `random.binomialvariate()` function. The first argument is the number of trials (coin flips), and the second argument is the probability of "heads".

```python
def simulate_N_coin_flips(N, p=0.5):
    n_heads = binomialvariate(N, p)
    print(f"Out of {N} flips, {n_heads} were heads and {N - n_heads} were tails.")
    return n_heads
```

## continuous distribution: the _normal_ (Gaussian) distribution

A _continuous_ distribution is one that can produce any value in a range, not just specific values.

The most famous continuous distribution is the _normal_ (or Gaussian) distribution, which is the classic "bell curve". It is defined by two parameters: the mean (average), about which the bell-shaped peak is centered; and the standard deviation, a measure of the width of the peak about that mean.

To generate random numbers between $-\infty$ and $+\infty$ whose relative likelihood follows this distribution, you can use the `random.gauss()` function. The first argument is the mean, and the second argument is the standard deviation.

For example, to generate a list of 160 simulated student's test scores, assuming a mean of 75 and a standard deviation of 10, you could do this:

```python
scores = []
for i in range(160):
    scores.append(gauss(75, 10))
```

That has two problems: It can produce scores greater than 100 or less than zero, and almost all the scores will be non-integer values. If you wanted to fix that, you could do this:

```python
scores = []
for i in range(160):
    score = min(100, int(random.gauss(75, 10)))
    score = max(0, score)
    scores.append(round(score))
```

By the way, if compactness were more important than readability, you could do this in a single line:

```python
# Do you really want to match up this many parentheses to make sure the expression is correct?
scores = [max(0, min(100, round(random.gauss(75, 10)))) for i in range(160)]
```

### other continuous distributions

The `random` module provides a few other continuous distributions, including one for exponentially-decreasing probabilities (`expovariate()`) and several obscure, specialized ones. They all work in essentially the same way as `random.gauss()`.

___
