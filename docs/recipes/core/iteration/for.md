# Repeat Code a Specific Number of Times

___
## Problem to Solve

> **I want to repeatedly execute a chunk of code, counting the repetitions.**

___
## Background Knowledge

### two ways of iterating

Python has two basic ways of iterating over (i.e., repeatedly executing) a chunk of code:

1. Applying the code to every element of an ordered collection ("iterable") of things, or

2. Executing the code over and over as long as some logical condition is true.

This recipe focuses on the first. (We'll get to the other soon.) It's useful for situations like:

- I want to repeat something a specific number of times.
- I want to do something with every number from $A$ to $B$.
- I want to do something with every element of a sequence of things.

### adjusting to python from from other languages

If you come to python from another programming language, this will likely trip you up:

> Python's `for` loop does not work like the `for` loop in many other, older programming languages like _C_ and _Java_. You can make it work like theirs' but you often shouldn't. Python's way is _better_.

Here's the essential difference:

- In many languages, a `for` loop is a mechanism for iterating while **incrementing a counter variable.**

- In python, a `for` loop is a mechanism for **iterating through the elements of an ordered collection of things.**

    - All languages have ways of achieving the same thing, and some (like JavaScript) have an equivalent `.forEach` method on arrays. It's usually clumsier than python's though.
    - Some newer languages, like _Julia_, _Swift_, and _Rust_, have adopted python's approach to `for`.

If you are not aware of this difference, you will try to make python behave like Java or C, and will end up with unnecessarily ugly, clumsy, un-pythonic code.

___
## Recipes

### Base Recipe

### Variant A: Counting (from zero)

If you want to count the iterations, perhaps so that you can use the iteration number in a calculation, here's the recipe:

```python
for i in range(N + 1):
    # Anything in here will be executed N times, with values of i successively
    # equal to 0, 1, 2, ..., N
```

The name `i` is fairly traditional in programming to represent an iteration number. However, if the counter has meaning in your code, I suggest picking something more descriptive, such as `row_num` (for successive rows in a table), `particle` (for successive particles in a physics calculation), or `power` (for successive powers of a number). Pick something that will make the code easier to interpret.

How does this recipe work? We haven't talked in detail about _collections_ yet, but here's the basic idea: the built-in python function `range(limit)` produces a sequence of integers, beginning with 0 and ending with **the last integer before `limit`**. For example, `range(5)` produces the sequence `0, 1, 2, 3, 4`. Note that the value of the "upper limit" argument is not itself included in the sequence produced!

> Forgetting that `range` begins withy 0 (not 1) and ends with `limit - 1` (not `limit`) is a common source of bugs in python code.
>
> Remember it this way:
> 1. In python, we always count from 0 unless explicitly told otherwise.
> 2. `range(N)` produces a N-element count.
> 3. So, in python, `N` elements are counted `0`, `1`, `2`, ..., `N-1`.

### Variant B: Just Repeating Some Number of Times

If you want to repeat a chunk of code $N$ times but don't need the code to know which iteration it's on, you can do exactly the same thing, and just ignore the counter variable `i` or whatever you've called it.

However, python programmers have a convention for naming variables that are not intended to be used: the underscore character, `_`. So, to repeat something $N$ times without numbering the iterations, use this:

```python
for _ in range(N):
    # Code in here will be repeated N times.
```

The use of `_` immediately tells a reader not to worry about whether or how the counter index is being used, and that this is a simple $N$-times-through repetition.

### Variant C: Counting from One (or something else)

The `range` function has an optional argument that lets you specify the starting value of the sequence. Note that it comes _before_ the required endpoint argument:

```python
for n in range(first_val, stop_before):
    # Anything in here will be executed N times, with values of in successively
    # equal to first_val, first_val + 1, first_val + 2, ..., stop_before - 1
```

Again, take note: the sequence of values will **include the first value** but **exclude the second value**. As a result, the number of iterations will always be `last_val - stop_before`.

### Variant D: Counting by Steps

The `range` function has a third optional argument that lets you specify the step size of the sequence. This can be used to count by twos, threes, or any other integer increment:

```python
for val in range(first_val, stop_before, step_size):
    # Anything in here will be executed repeatedly times with values of val
    # successively equal to first_val, first_val + step_size, 
    # first_val + 2 * step_size, ..., 
```
What will the last value be? That depends on how many multiples of the step size fit in before reaching the `stop_before` value. Python will continue iterating until adding another value of `step_size` would reach or exceed `stop_before`, and will then cease.

### Variant E: Counting Down

Counting downwards is as easy as specifying a negative step size, and choosing a larger starting value than the stopping value:

```python
for count in range(start_val, stop_before, -step_size):
    # Code here will execute repeatedly, with values of count starting at
    # start_val and decreasing by step_size each time, stopping just before
    # reaching or going past stop_before.
```

### Variant F: Counting by Non-Integer Steps

Alas, the `range()` function only works with integers. If you need to count by non-integer steps, you have
three options:

1. Count by integers, but multiply the counter variable by some fractional step size when you use it. This works if you want to count by regular steps that can be easily obtained from an integer sequence.

2. Use a `while` loop (coming in a recipe soon) and do all the initializing, incrementing, and endpoint-testing yourself. This is very flexible, but puts the work on you instead of on python, and can be more error-prone.

3. Use features similar to `range` from the `numpy` library, which we'll cover in a future unit. This will generally be your best bet, once you've learned that skillset.

___
## Examples

### Example 1: Uncounted Repetitions

Here's a function that creates a one-dimensional _fractal_ by repetition. It begins with the simple pattern `█ █`. Every iteration, it replaces all `█` characters with the initial pattern of `█ █`, and replaces all space characters with a block of three spaces. Thus, in each iteration, the length of the string triples.

Imagine that instead of growing the length of the string, you're "zooming in" and seeing that each apparently-full cell actually has a hole in it. This is the essence of a _fractal_: Self-similarity at different scales.

```python
def fractal_string(depth):
    """ Generates a string of `X` and ` ` characters with a fractal density
        structure.
    """
    full_cell = '█ █'
    empty_cell = '   '
    s = full_cell
    for _ in range(depth):
        s = s.replace(' ', '~')
        s = s.replace('█', full_cell)
        s = s.replace('~', empty_cell)
    return s
```

Copy-paste it into an IPython console (or script) and play with it! (It looks better if you go to a really small font size or zoom level, so that you can get more characters on one output line.)

### Example 2: Counting

If a biased coin lands on "heads" with probability $p$, the probability of obtaining $N$ heads in a row is $p^N$. Here's a function that displays the probability of increasingly long strings of heads:

```python
def heads_runs(p, n_max):
    """ Displays the probability of obtaining successively longer runs of
        "heads" with a biased coin whose probability of landing on "heads"
        in any given flip is `p`. `n_max` sets the longest run considered.
    """
    for n in range(1, n_max + 1):
        print(f"Probability of {n:2} heads in a row: {p**n:.2%}.")
```
(Note: I'm omitting the usual safety-checks on arguments so you can focus on the point of the recipe. In real code, I'd convert n_max to an integer and make sure both arguments had meaningful values.)

### Example 3: Countdown with changing interval

Want to write code for NASA Mission Control?

```python
import time
from IPython import get_ipython

def countdown(starting_time):
    """ Counts down in real-time, announcing every ten seconds until ten
        seconds are left, and then every second. If the starting time is
        greater than 10 s, it is rounded up to the nearest multiple of 10
        seconds.
    """
    get_ipython().run_line_magic("clear", "")
    if (starting_time > 10) and (starting_time % 10 != 0):
        starting_time += 10 - starting_time % 10
    if starting_time >= 20:
        for t in range(starting_time, 10, -10):
            print(f"  Launch in T minus {t} seconds")
            time.sleep(10)
    print("  Launch in ", end="")
    for t in range(min(10, starting_time), 0, -1):
        print(f"{t}… ", end="")
        time.sleep(1)
    print("\n🚀🚀🚀 BLASTOFF!!! 🚀🚀🚀")
```

### Example 4: Non-integer steps

For those of you taking special relativity in PHY 321: What are the values of gamma for speeds of 0, 0.05c, 0.1c, ..., c?

```python
from math import sqrt
def gamma():
    """ Display the values of the Lorentz factor "gamma" for velocities
        from zero up to 1 (in SR units), showing every increment of 0.1.
    """
    for d in range(0, 100, 5):
        v = d / 100
        gamma = 1 / sqrt(1 - v**2)
        print(f" v = {v:.2f} => gamma = {gamma:.5f}")
    print(f" v = {1:.2f} => gamma = infinite!")
```

___
