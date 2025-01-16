# Execute Code Conditionally

___
## Problem to Solve

> **I want my code to decide what to do based on the circumstances.**

___
## Recipe

This recipe isn't specifically about writing functions — the topic of this level — but I'm including it here because it's very common for functions to include conditional logic.

### Execute or Not, Depending

Let's say you've got a chunk of code (maybe one line, maybe several) that your program should execute under certain circumstances, but skip over under others. The solution is to wrap that chunk in an `if` block:

```python
if boolean_expression:
    # Code to execute if condition is True.
    # Can be multiple lines

# Code to execute regardless...
```

Replace `boolean_expression` with any expression that evaluates to either `True` or `False`. That could be:
- a boolean variable whose value was set to `True` or `False` earlier in the program;
- a comparison using one of python's [comparison operators](https://realpython.com/python-boolean/#comparison-operators), like `x < y`, `r >= 1`, or `s == "hello"`;
- a call to a function that returns a boolean value, such as `isinstance(x, int)` or `email_address.endswith(".com")`; or
- a combination of the above, using the logical operators `and`, `or`, and `not`.

(By the way, a convenient shorthand for `if x > a and x < b:` is `if a < x < b:`.)

Indentation is what distinguishes the body of the `if` block — the lines that will execute or not depending on the value of `boolean_expression` — from subsequent code that will execute either way. (The blank line I inserted just to improve human readability; the python interpreter doesn't care.)

A warning about a common error: If you define a variable for the first time inside an `if` block, later code can't safely assume that variable will have been defined. You could get an error like `NameError: name 'xxx' is not defined` that doesn't show up until the first time your code is run with conditions that make `boolean_expression` evaluate to `False`.

One common solution is to define the variable **before** the `if` statement, giving it some appropriate default value (which depends on the circumstances): zero, or an empty string, or whatever. Then, the code inside the `if` block can change the value of the variable if necessary, and later code can safely assume the variable has been defined.

### Execute One Chunk Or Another

An alternate case is that you might want your code to execute one chunk of code if some condition holds, and a different chunk if it doesn't. That's what the optional `else` clause of the `if` statement is for:

```python
if boolean_expression:
    # Code to execute if condition is True.
    # Can be multiple lines
else:
    # Code to execute if condition is False.
    # Can be multiple lines, too.

# Code to execute regardless...
```

Because one block or the other will necessarily execute, you can safely define a variable inside this `if` construct as long as you define it in both branches.

### Execute One Of Several Chunks

You can also choose between more than two possible chunks of code to execute, but you'll need more than one boolean expression to do so. Here's a three-chunk version:

```python
if boolean_expression_1:
    # Code to execute if condition 1 is True.
elif boolean_expression_2:
    # Code to execute if condition 1 is False and condition 2 is True.
else:
    # Code to execute if both condition 1 and condition 2 are False.
```

Note that if `boolean_expression_1` evaluates to `True`, the value of `boolean_expression_2` is totally irrelevant.

You can have arbitrarily many `elif` clauses, but only one `else` clause, and the `else` clause must come last. If you have more than one `elif` clause, the interpreter will evaluate them in order, from top to bottom, and execute the first block of code whose condition is `True`.

```python
if boolean_expression_1:
    # Code to execute if condition 1 is True.
elif boolean_expression_2:
    # Code to execute if condition 1 is False and condition 2 is True.
elif boolean_expression_3:
    # Code to execute if conditions 1 and 2 are False and condition 3 is True.
else:
    # Code to execute if all conditions are False.
```

### Consider Two Criteria Simultaneously

If your code needs to take different actions depending upon **both** of two conditions, you've got a couple of possible approaches. The most complex case is one where you have four different possible outcomes, depending on whether each of the two conditions is `True` or `False`. Here's one approach:

```python
if boolean_expression_1 and boolean_expression_2:
    # Code to execute if both conditions are True.
elif boolean_expression_1:
    # Code to execute if condition 1 is True and condition 2 is False.
elif boolean_expression_2:
    # Code to execute if condition 1 is False and condition 2 is True.
else:
    # Code to execute if both conditions are False.
```

Here's a different approach, using nested `if` statements:

```python
if boolean_expression_1:
    if boolean_expression_2:
        # Code to execute if both conditions are True.
    else:
        # Code to execute if condition 1 is True and condition 2 is False.
else:
    if boolean_expression_2:
        # Code to execute if condition 1 is False and condition 2 is True.
    else:
        # Code to execute if both conditions are False.
```

I think the first is easier to read, but YMMV. On the other hand, the second approach lets you use a different second criterion depending on the value of the first:

```python
if boolean_expression_1:
    if boolean_expression_2a:
        # Code to execute if conditions 1 and 2a are True.
    else:
        # Code to execute if condition 1 is True and condition 2a is False.
else:
    if boolean_expression_2b:
        # Code to execute if condition 1 is False and condition 2b is True.
    else:
        # Code to execute if both conditions are False.
```

**Be very careful about any kind of complex, nested conditional logic.** It's very easy to write code that you *think* will act the way you want, but that behaves differently under some rare circumstances that fall through a hole in your logic. Even screwing up the indentation of an `else` can change your code's behavior. Try hard to find the simplest, "flattest", most linear solution you can.

___
## Examples

Here's a simple example of an `if` block in action. (I've hard-coded the parameters `V_0` and `L` to keep the example uncluttered.)

```python
def V(x):
    """ Represents the potential energy function V(x) of a quantum particle in a
        finite square well of depth `V_0` and width `L` centered on the origin.
    """
    V_0 = 13.2  # eV: the 
    L = 1.0e-9  # meters
    if abs(x) < L/2:
        V = -V_0
    else:
        V = 0
    return V
```

(Imagine what a plot of V(x) vs. x would look like.)

Of course, one can simplify this code by taking advantage of the fact that encountering a `return` statement immediately exits the function:

```python
def V(x):
    """ Represents the potential energy function V(x) of a quantum particle in a
        finite square well of depth `V0` and width `L` centered on the origin.=
    """
    V_0 = 13.2  # eV: the 
    L = 1.0e-9  # meters
    if abs(x) < L/2:
        return -V_0
    return 0
```

Here's a function that describes velocity vs. time for a vehicle that sits at rest until $t = 0$, then accelerates at $2.5\text{ m/s}^2$ for ten seconds, and then coasts at constant speed for 15 seconds, and then slows down at $-1.0\text{ m/s}^2$ until it comes to a stop:

```python
def vehicle_velocity(t):
    """ Describes velocity vs. time, v(t), for a vehicle that sits at rest 
        until $t = 0$, then accelerates at $2.5\text{ m/s}^2$ for ten seconds, 
        and then coasts at constant speed for 15 seconds, and then slows down
        at $-1.0\text{ m/s}^2$ until it comes to a stop.

        Parameters:
        - t (float): a time in seconds.

        Returns: the velocity in m/s.
    """
    if 0 <= t <= 10:
        # During acceleration phase: v = 0 + (2.5 m/s^2) * t
        return 2.5 * t
    elif 10 < t <= 25:
        # During coasting phase: constant velocity from the end of
        # the acceleration phase, vd = 2.5 m/s^2 * 10 s = 25 m/s
        return 25.0
    elif 25 < t <= 40:
        # During deceleration phase: v = 25 m/s - (1.0 m/s^2) * (t - 25)
        return 25.0 - 1.0 * (t - 25)
    else: # t < 0 or t > 40
        return 0.0
```

## Bonus Tidbit: The Ternary Operator

You can totally ignore this if you want, but for the curious: python has a "ternary operator" that can implement a simple if/else construct in one line. It only works when each clause is a single expression, and where the construct's objective is to return one of two values (rather than, say, doing something else like printing). Here's the template:

```python
variable_to_set = value_if_true if boolean_expression else value_if_false
```

Here's the first example above, the potential energy function, rewritten with a single line of body code using construct:

```python
def V(x, V_0=13.2, L=1.0e09):
    """ Represents the potential energy function V(x) of a quantum particle in a
        finite square well of depth `V0` and width `L` centered on the origin.
    """
    return -V_0 if abs(x) < L/2 else 0
```

Don't overuse it! Code readability can suffer. It's best when the first value is _usually_ the value chosen, but sometimes the second is needed under rare circumstances.
___
