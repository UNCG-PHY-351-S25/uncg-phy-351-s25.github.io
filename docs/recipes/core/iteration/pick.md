# Flip a Coin or Roll a Die

___
## Problem to Solve

> **My code needs to randomly pick or decide something.**

___
## Background Knowledge: Pseudorandomness

Computers are deterministic rule-following machines, and can't do things truly randomly. However, we can make them follow a sufficiently complex set of rules that are sufficiently sensitive to initial conditions that the outcome, is, for all practcal purposes, random. This is called *pseudorandomness*.

A deep dive into that is coming later in this course. For now, we just need a way to "flip a coin" (perhaps a biased one) or "roll a die" in order to write code that can make effectively-random decisions.

___
## Recipe: Flipping a (Biased) Coin

Goal: Simulate the probabilistic outcome of flipping a coin that comes up "heads" with probability $p$ and "tails" with probability $1-p$. (If $p = 0.5$, we say that the coin is "fair". If $p \neq 0.5$, we say that the coin is "biased".)

For the convenience of computer code, we'll represent "heads" as `True` and "tails" as `False`.

Python's `random` module has several useful functions. One of them is `random.random()`, which returns a (pseudo)random floating-point number in the range $[0, 1)$. (That notation means "from 0 to 1, including zero but not including 1".) We can use this to simulate a coin flip by returning `True` if the random number is less than $p$ and `False` otherwise.

```python
import random
def flip_coin(p=0.5):
    return random.random() < p
```
Easy, no? It's barely even worth wrapping up in a function.

### example: sequential flips

How many times in a row must I flip a fair coin to get 3 heads in a row?

```python
heads_in_a_row = 0
flips = 0
while heads_in_a_row < 3:
    if flip_coin():
        heads_in_a_row += 1
    else:
        heads_in_a_row = 0
    flips += 1
print(flips)
```

## Recipe: Rolling a Die

Goal: Simulate the probabilistic outcome of rolling a fair $N$-sided die.

The `random` module also has a function `random.randint(a, b)` that returns a (pseudo)random integer in the range $[a, b]$. We can use this to simulate a die roll by returning a random integer in the range $[1, N]$.

```python
import random
def roll_die(N=6):
    return random.randint(1, N)
```

### example: rolling two dice

How many times in a row must I roll two fair dice to get a sum of 7?

```python
sum_is_seven = False
rolls = 0
while not sum_is_seven:
    if roll_die() + roll_die() == 7:
        sum_is_seven = True
    rolls += 1
print(rolls)
```

___
