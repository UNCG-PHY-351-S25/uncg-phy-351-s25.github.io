# Safety-Check Arguments

___
## Problem to Solve

> **I want to make my function robust against incorrect or unexpected arguments.**

When you write quick, short-term-use functions for yourself, you probably don't need to worry about this. However, if you're writing functions as part of a larger project, and/or for others to use, and/or for you to use in the future, sparing a line or few of code to idiot-proof them against inappropriate arguments is wise.

I showed you a foretaste of this back in [_Ask for User Input_](../calculation/user-input.md), but now (a) it's more important, and (b) we've got better tools to deal with it.

___
## Recipe

A function must guard against two basic kinds of argument error:
- being passed a value of an incorrect type (like a float when an integer is expected, or a list \[coming soon\] instead of a single value), and
- being passed a value of the right type but an inappropriate value (like a negative value for a mass).

### Flavor A: Type Checking

To check the type of an argument, you can explicitly test whether it's got the right type, like this:

```python
def demo_function(x):
    """ A function that requires `x` to be a float. """
    if not isinstance(x, float):
        raise TypeError("x must be a float")
    # Proceed with the function using `x`...
```

Wait, what's with this `raise TypeError(...)` stuff?!? 🧐

That's the python way of triggering an error message to the user.

- `raise` says `An error has occurred, and unless the code that's called me can do something smart to handle it, the user had better be informed!'

- `TypeError` indicates the kind of error that's occurred. Python has many built-in error types for you to choose from and you can even define your own. The two you're most likely to need for now, however, are:
    - `TypeError`: for when an object of inappropriate type is encountered.
    - `ValueError`: for when an object of the right type but inappropriate value is encountered.

- "x must be a a float" is the message that will be displayed to the user. You can write whatever you like here, but it's good to be specific about what's wrong so the poor user (likely you) has some idea what to do about it.

If you're okay with either an integer or floating-point value (since you can use an integer pretty much anywhere a float is expected), you can write:

```python
def demo_function(x):
    """ A function that requires `x` to be a float or int. """
    if not isinstance(x, (float, int)):
        raise TypeError("x must be a float or int")
    # Proceed with the function using `x`...
```

Sometimes, checking an argument value's type this way is the right approach. However, very often we don't actually care what the type of the argument is, so long as we can use it for our purposes. For example, if we want a float, so what if we're given an integer? We can use that just fine anywhere a decimal number is needed! So, instead of checking the type, we just _coerce_ it to an adequate type:

```python
def demo_function(x):
    """ A function that requires `x` to be interpretable as a float. """
    x = float(x)
    # Proceed with the function using `x`...
```

If the user (or other code) calls `demo_function` with any kind of value that can be turned into a float — such as a float, an integer, or a string representing a legitimate floating-point literal like "3.2e4" — it'll get turned into a float, and the function can happily proceed.

OTOH, if the function receives something that can't be coerced into a float, python will raise a `ValueError` with a message like `could not convert string to float: '2.5 m/s'`. You don't need to bother with your own `raise` statement.

By the way, there's a third approach: Don't bother to check or coerce the argument at all. Just use it, and let python raise an error when it reaches a point where the argument's type is problematic. Depending on the situation, this might be fine, or it might open the door to hard-to-interpret errors or hard-to-fix bugs. Use your judgment. In particular, if it's obvious that an incorrect argument type will quickly cause an error to occur, you're probably okay omitting the explicit check. However, if an incorrect type might cause unintended behavior rather than an error, explicitly checking becomes essential.

- Forward reference: A common situation when a wrong type won't raise an error is when code expects a _list_ (which we'll get to soon), but is given a _string_ instead. If `x` represents a list, `x[3]` produces the fourth element in the list. However, if `x` represents a string, `x[3]` produces the fourth character in the string — a totally different thing, and potentially very confusing, especially if the list is supposed to be a list of strings!

### Flavor B: Value Checking

This is straightforward: Use an `if` statement to test the argument's value with the appropriate boolean expressions, and raise a `ValueError` if the test fails.

```python
def demo_function(x):
    """ A function that requires `x` to be a positive number. """
    if x <= 0:
        raise ValueError("x must be positive!")
    # Proceed with the function using `x`...
```

If your restrictions on the argument's value are more complicated, you can combine boolean expressions with `and`, `or`, and `not`, and/or you can use a multi-clause `if/elif/…` construct.

If you need to check multiple arguments, just put the checks one after another in the function body. If more than one is invalid, only the first will be caught, but that's usually enough for the user to make progress.

By the way, a slightly shorter and quicker way to accomplish this is to use the `assert` statement introduced earlier. For example:

```python
def demo_function(x):
    """ A function that requires `x` to be a positive number. """
    assert x > 0, "x must be positive!"
    # Proceed with the function using `x`...
```

The only significant **practical** difference here is that the user sees `AssertionError` instead of `ValueError`. That probably doesn't matter if a human gets the message, but sometimes the calling code will be written to "catch" certain errors and respond automatically.

Philosophically, however, programmers generally see _assertions_ (using `assert`) as safety-checks inside their code that should never raise an error unless something has gone wrong inside the program, whereas _exceptions_ (using `raise`) are for when the user or external code has done something wrong.

For the purposes of this course, I'll try to be explicit when an assigment cares what type of exception gets raised; otherwise, do as you see fit.

## Examples

Here's an example illustrating a common situation: a function requires an integer for something, such as the number of times to repeat something — a random choice, a time-step in a dynamical simulation, etc. The user might plausibly want to pass very large numbers: ten thousand, a million, five million, whatever.

The problem is that python interprets scientific notation such as `1e4`, `1e6`, and `5e6` as floating-point values, not integers. If you don't check for this and do the following, your user will get annoyed:

```python
def average_of_N(N):
    """ Generates a random number by a call to `roll_die` (whose definition 
        is not shown here), `N` times, and returns the average of all the
        values.
    """
    sum = 0
    for i in range(N):
        sum += roll_die()
    return sum / N
```
(We haven't formally introduced `for`-loop iteration or the `range` function yet. I'm assuming you've seen enough python to be able to interpret it.)

Here's an example of the problem:

```python
>>> average_of_N(10_000)
3.5042
>>> average_of_N(1e4)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[6], line 1
----> 1 average_of_N(1e5)

Cell In[1], line 7, in average_of_N(N)
      2 """ Generates a random number by a call to `roll_die` (whose definition 
      3     is not shown here), `N` times, and returns the average of all the
      4     values.
      5 """
      6 sum = 0
----> 7 for i in range(N):
      8     sum += roll_die()
      9 return sum / N

TypeError: 'float' object cannot be interpreted as an integer
```

The solution is simple, once you understand the problem:

```python
def average_of_N(N):
    """ Generates a random number by a call to `roll_die` (whose definition 
        is not shown here), `N` times, and returns the average of all the
        values.
    """
    N = int(N)
    sum = 0
    for i in range(N):
        sum += roll_die()
    return sum / N
```
Now, the function works as expected:

```python
>>> average_of_N(1e4)
3.4865
```

We still have a problem, however:

```python
>>> average_of_N(-1e4)
-0.0
```
We didn't get an error, but we did get a nonsensical result. If that function call were being made by other code, and its value used in some larger calculation, we might never realize that the nonsensical value was causing the calculation to be incorrect.

The problem, of course, it makes no sense to average something a negative number of times. We can fix this with a simple check:

```python
    def average_of_N(N):
        """ Generates a random number by a call to `roll_die` (whose definition 
            is not shown here), `N` times, and returns the average of all the
            values.
        """
        N = int(N)
        assert N > 0, "N must be positive!"
        sum = 0
        for i in range(N):
            sum += roll_die()
        return sum / N
```
Now:
```python
>>> average_of_N(-1e4)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[14], line 1
----> 1 average_of_N(-1e4)

Cell In[13], line 7, in average_of_N(N)
      2 """ Generates a random number by a call to `roll_die` (whose definition 
      3     is not shown here), `N` times, and returns the average of all the
      4     values.
      5 """
      6 N = int(N)
----> 7 assert N > 0, "N must be positive!"
      8 sum = 0
      9 for i in range(N):

AssertionError: N must be positive!
```

Get the idea? It's not hard; it just takes a bit of discipline to stop and ask, while writing a function, "What argument types or values are legitimate here? Will it break things or cause erroneous results if an invalid argument is provided? Maybe I better toss in a couple of lines of code just to be safe."
___
