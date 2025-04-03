# Reproduce "Random" Results

___
## Problem to Solve

> **I want to be able to reproduce the same sequence of "random" numbers for testing or sharing with others.**

___
## Background Knowledge

A pseudorandom number generator (PRNG) uses a mathematical algorithm to produce a sequence of numbers deterministically, but that jump around so wildly and _apparently_ unpredictably that they are effectively random.

They are not, however, truly unpredictable, for the simple reason that if you know the algorithm, you can regenerate the sequence perfectly.

To start the sequence, the algorithm must be started with an initial value called the _seed_. If a PRNG began with the same seed value every time your code invoked it, you'd always get the same sequence of "random" results, which wouldn't be very random-seeming at all. So, normally, the first time you invoke a PRNG it grabs an effectively-random seed value from the computer — for example, the number of milliseconds since the computer was last booted up.

- Effective random number generation has become so critical to applications such as cryptography and computer security that modern operating systems maintain an <a href="https://www.netdata.cloud/blog/understanding-entropy-the-key-to-secure-cryptography-and-randomness/" target="_blank">_entropy pool_</a> that software such as PRNGs can call on to ask for a random seed. The entropy pool is a collection of random bits that are collected from various sources, such as mouse movements, keyboard presses, and other unpredictable events.

Sometimes, however, being able to exactly reproduce a "random" sequence of numbers is useful: for example, so that you can re-run a simulation to reproduce an unusual, rare result that you discovered, or so that you can debug a simulation while knowing that the changes you're making are the only difference between runs.

For this purpose, PRNGs allow you to specify a "seed" value that they will use to initiate the pseudorandom sequence algorithm. If you provide the same seed in different runs, they'll produce the same "random" sequence in those runs.

___
## Recipe for Optional Seeding

Being able to specify a random seed so that you can get the same "random" sequence in different runs is useful. _Always_ producing the same "random" outcome is not generally helpful. Therefore, a useful approach is to allow the user to specify an optional seed value, and let the PRNG use its default seeding mechanism if they don't.

Let's say you're writing a function named `run_simulation()` that, as part of its work, generates a sequence of random outcomes. (Remember the _Drunkard's Walk_ miniboss?) You could apply this recipe:

```python
import random
def run_simulation(param_1, param_2, seed=None):

    # Set the random seed if one was provided:
    if seed is not None:
        random.seed(seed)

    # Do the rest of the simulation including random number generation with
    # calls like random.randint(), random.choice(), random.uniform(), etc.
```
___
## Recipe for Seed Reporting

The above recipe lets you specify a seed or use the default one, but it does not let you replay a simulation that used the default seed — if, for example, you serendipitously discovered some interesting outcome or rare bug in your code, and need to reproduce it. You have no way of knowing what the default seed was.

Python can't tell you, either. It does have a mechanism for saving and restoring the complete internal state of the PRNG, via `random.getstate()` and `random.setstate()`, but that state is a complex object that is not easily human-readable.

Here's a hack that gives you the effect of reporting the initial seed even when you let the system pick it. It works by letting the system pick a seed (if you didn't specify one), immediately generating a random number, and then using that number to re-seed the generator. You can always reproduce the subsequent output of the PRNG by re-seeding with that number.

```python
import random
def run_simulation(param_1, param_2, seed=None):

    # If no seed was provided, generate one in a reportable way:
    if seed is None:
        # Use the default seed to generate a new seed:
        seed = random.getrandbits(128)
    random.seed(seed)
    print(f"*** Random number generator seeded with `{seed}`.")

    # Do the rest of the simulation including random number generation with
    # calls like random.randint(), random.choice(), random.uniform(), etc.
```

___
## A Trivial Example

Just to demonstrate, let's write a program that flips 100 fair coins and reports the number of heads. The result should be different almost every time we run it… unless we run it from the same seed.

```python
import random
def flip_coins(num_flips, seed=None):
    # If no seed was provided, generate one in a reportable way:
    if seed is None:
        # Use the default seed to generate a new seed:
        seed = random.getrandbits(128)
    random.seed(seed)
    print(f"*** Random number generator seeded with `{seed}`.")

    # Flip the coins:
    heads = 0
    for _ in range(num_flips):
        if random.choice([True, False]):
            heads += 1
    return heads
```

If I save that in a file named `flip_coins.py` and then start an IPython console, I can do this:

```python
In [1]: %run flip_coins.py

In [2]: flip_coins(10000)
*** Random number generator seeded with `307492323691025515227351811167579029126`.
Out[2]: 5054

In [3]: flip_coins(10000)
*** Random number generator seeded with `308609459721083318912056881702551219257`.
Out[3]: 5026

In [4]: flip_coins(10000)
*** Random number generator seeded with `259201567887010425690323679171186305093`.
Out[4]: 4901

In [5]: flip_coins(10000, seed=307492323691025515227351811167579029126)
*** Random number generator seeded with `307492323691025515227351811167579029126`.
Out[5]: 5054
```

(If you find those seed numbers to be intimidatingly long, you can replace `getrandbits(128)` with `getrandbits(64)` or even `getrandbits(32)`. However, longer seeds have less chance of accidentally repeating the same seed in a "new", randomly-seeded run.)

___
