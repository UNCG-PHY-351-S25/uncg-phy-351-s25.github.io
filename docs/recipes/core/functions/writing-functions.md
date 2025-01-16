# Write Your Own Functions

___
## Problem to Solve

> **I want to easily reuse a particular calculation multiple times, with different givens.**

___
## Introduction

IMHO, the biggest challenge facing coders of any level, writing code for any kind of application, is managing the _complexity_ of the task. In any program beyond the truly trivial (or larger software ecosystem!), there is simply more going on — more bits of functionality, more state information to track, more causal interconnections — than any human being can hold in their head. Without some powerful methodologies for managing the complexity, the task can be nearly impossible; and even if one completes a program that _seems_ to work, it's really hard to be confident it's bug-free and reliable.

Defining your own _functions_ that wrap up well-defined chunks of functionality into reusable units is one of the most powerful tools programmers have devised to deal with this. The basic idea is that one takes a sub-task of manageable complexity and writes code to accomplish it, in a way that is as decoupled from the rest of the larger problem as possible. That chunk of code is packaged in such a way that other code can refer to it and use it as a single python expression — a "function". In that way, once the function has been written and tested, the programmer can forget about the complexity it encapsulates, and for cognitive load purposes it becomes a single "thing".

Here's an example: How do you think the computer calculates, say, `math.sin(0.143)` when you put that into your program? Deep in the code for the `math` module is a _function definition_ that instructs the computer to calculate a fairly complicated series approximation to the sine, with lots of logic to accurately and efficiently handle edge cases like very tiny angles. Do you really want to have to think about all of that every time you need to take the sine of something? Nope…

Okay, enough philosophy. Let's get to the nuts-and-bolts. 

___
## Recipe

### Step 1: _Define_ The Function

Before your code can _use_ a function, it has to _define_ a function. If you want `do_thing(3)` to mean something to the python interpreter when it encounters that expression, you first have to send code to the interpreter that tells it what that expression means. This is the template for a _function definition_:

```python
def function_name(arg_1, arg_2, …):
    """ Here goes a descriptive comment telling a human reader what the function
        does, including what the various arguments will affect and what kind
        of value it will return.
    """
    pass # REPLACE this with the code that will implement your function's
    pass # behavior, in as many or few lines as is required.
    
    return result_to_return

# Other code that follows here is NOT part of the function.
```

Notes:

1. The first line, beginning with `def`, is called the _function signature_. It specifies everything that client code — code that uses this function — needs to know about how to call it.

2. Replace `function_name` with a name for your function that communicates, fairly clearly, what the function's purpose is.
    - In python, function names must follow the same rules as variable names: They must start with a letter, and consist only of letters, digits, and the underscore character. (Technically, the first character can be an underscore, but the python convention reserves this for special-purpose functions we don't need to get into here.) 
    - Python culture goes farther, recommending that function names begin with **lowercase** letters and use "snake_case", (an underscore between words) rather than "camelCase" (capital letter to start new words).

3. Replace `arg_1, arg_2, …` with a comma-separated list of _arguments_ that will be given specific values when the function is _called_ (used, executed).
    - The names you put here will become variables "holding" those values that the body of the function can refer to.
    - The names you use here can be different than whatever variables "outside the function" might be used to hand value to the function. **Code inside the function shouldn't care about the details of code outside the function, and vice-versa.**
    - A function can specify that it wants no arguments, or one, or two, or more… Or it can even be flexible in how many it requires (see below).

4. The descriptive comment just below the function signature line is called the _docstring_.
    - The docstring is optional, but it's worth writing. Someone else trying to figure out your code, or maybe even future you, will be very glad you took the time.
    - It's really good habit to write this comment FIRST, before you start writing the actual code. That can help you clarify in your own mind what, precisely, the function should do.
    - BTW, the triple-quotes bound a special kind of string literal that can span multiple lines. Other than the line breaks, it's just a normal string, like `"blah blah"`.

5. In python, **indentation matters!** The only thing telling the python interpreter which subsequent lines belong to the function definition and which are part of some other, subsequent code is the fact that the _body_ of the function is indented, and all by the same amount.
    - Warning: multiple space characters may _look_ like the same indentation as a tab character, but are not the same as far as the python interpreter is concerned. Fortunately, most modern code editors will proactively replace tabs with spaces for you, protecting you from this potentially infuriating source of mystery errors.

6. The code in the _function body_ is not evaluated when the function definition is sent to the interpreter! Rather, it is stashed, and is later executed when the function is called (used) by other code, using whatever argument values have been specified at that time.

7. Replace `result_to_return` with an expression that will evaluate to the result you want your function to return to whatever code called it.
    - You can replace `result_to_return` with the name of a variable that is defined and given a value in the function.
    - Alternatively, you can replace it with an expression that will be evaluated when the value is to be returned. It's even possible for a function to have no body at all other than the return line, and still be useful if that return line contains a calculation.
    - Some functions don't return anything, but have some desirable side effect such as writing data to a file or printing text to the screen. Those can either `return None` or have no return line at all.

### Step 2: _Call_ the Function

Once your code has defined a function, any code that is subsequently executed can _call_ (use) it simply by giving its name, followed by parentheses containing a list of values to be passed to the function's arguments:

```python
some_variable = function_name(value_1, value_2, …)
different_function( function_name(other_value_1, other_value_2, …) )
```

Note a critical difference: In python, `function_name` by itself is a reference to the function's code, whereas `function_name(…)` causes the function to execute (whether or not the parentheses are empty). The presence of the parentheses are the trigger that says "execute this".

- Black-belt tidbit: In python, you can pass a function around as an object, just like you can with a variable, by using its name without parentheses. The function's body is its "value" in the way that a number or string is a regular variable's value. That means you can actually pass a function as an argument to another function, and that other function can execute the one it's been given without knowing what it actually does! This is called a _callback_, and is a very useful technique for "decoupling" different portions of a code. In essence, it lets you pass "actions" around in the same way that you pass "values" around.

### Elaboration: Return Multiple Values

A recipe can easily return two or three (or, in principle, more) separate values via the "comma trick":

```python
def function_name(some_arg):
    """ Template for a function that returns two values
    """
    pass # Calculate result_1 and result_2 in some way.
    return result_1, result_2
```

To catch them, calling code also uses the comma trick:

```python
thing_1, thing_2 = function_name(val_for_some_arg)
```

Notes:

1. Technically, the function only returning one "value", but that value is something called a _tuple_ that packages multiple values together. The comma-separated list on the left-hand side of the calling code's assignment statement _unpacks_ the tuple into separate variables. We'll look at tuples more closely in an upcoming level.

2. There is, in principle, no limit to the number of values a function can return this way. However, if you're going to return more than two or three, you're probably better off wrapping them in one of python's _collections_, which are the focus of two upcoming levels.

3. Similarly, if the function needs to be flexible about how many values to return, the comma trick won't suffice and you'll need a _collection_ object.

___
## Some Examples

> These examples are pretty trivial, mostly because we haven't yet introduced the python structures (such as conditional logic and iteration) that get used in more complicated ones. Please take them in that spirit.

### No Arguments

Functions that take no arguments are uncommon, but are occasionally convenient. For example:

```python
from random import randint
def roll_3d6():
    """ Simulate rolling three six-sided dice and return the sum.
    """
    return randint(1, 6) + randint(1, 6) + randint(1, 6)
```

### One Argument

```python
from math import degrees
def degrees_bounded(angle_in_rad):
    """ Convert the given angle in radians to degrees, within the range [0, 360). Angles
        360˚ or greater get mapped to the equivalent angle within the first revolution,
        and negative angles get mapped to the equivalent positive angle.
    """
    return degres(angle) % 360
```


### Two Arguments

```python
def kinetic_energy(m, v):
    """ Calculate the kinetic energy of an object with the given mass and velocity.
    """
    return 0.5 * mass * velocity**2
```

### Multiple Return Values

```python
def cartesian_to_polar(x, y):
    """ Converts the given 2D Cartesian coordinates to polar coordinates. Returns the
        polar coordinates as (r, theta) with theta in radians.
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta
```

Note: This function body could be rewritten as a one-liner,

```python
def cartesian_to_polar(x, y):
    """ Converts the given 2D Cartesian coordinates to polar coordinates. Returns the
        polar coordinates as (r, theta) with theta in radians.
    """
    return math.sqrt(x**2 + y**2), math.atan2(y, x)
```

but sacrificing readability for brevity is rarely worthwhile.
___
