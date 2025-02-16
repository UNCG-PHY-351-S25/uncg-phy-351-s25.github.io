# Factor Out Subfunctions

___
## Problem to Solve

> **I want to break a complicated calculation into pieces to keep it manageable.**

You will find, as you write more complicated code — multi-step calculations, multi-body physics simulations, etc. — that most of the work is done inside functions you define. For example, in a Visual Python simulation of interacting objects, you may have a function `update_scene()` whose job is to move all the 3D objects to new locations. That function will have to calculate all the interaction and constraint forces, determine the resulting accelerations of all the objects, determine how their velocities and positions change, and then give the commands to actually modify the scene.

If you try to put all the code for this into the one function, it will become painfully long and hard to work with. The smart approach is to **_factor_** it into multiple small, mostly-independent calculations, and to put each one in its own function. Functionality that is factored out of one function and put into another is called a **_subfunction_**.

___
## Recipe

Here's the general pattern:
```python
def subfunction_1(arg1, ...):
    """ Encapsulates one bit of functionality. """
    result = ... # Calculate something using one or more lines of code
    return result

def subfunction_2(arg1, arg2, ...):
    """ Encapsulates a different bit of functionality. """
    other_result = ... # Calculate something using one or more lines of code
    return other_result

def main_function(arg_A, arg_B, ...):
    """ Does something complicated. """
    x = ... # Calculation
    z = subfunction_1(x, arg_B, ...)
    q = subfunction_2(z, ...)
    end_result = ... # Calculation
    return end_result
```
Hopefully it's obvious that you can give the functions, arguments, and variables any names that reflect their actual purposes and meanings.

It's entirely possible to call the same subfunction multiple times from the same main function, or even from different other functions. (A function can even call itself… That's called _recursion_, and can be a powerful technique, but be careful that it doesn't go on forever.)

### When should you factor code into a subfunction?

That's a judgment call. When considering whether to factor a particular chunk of code into a subfunction, ask yourself:

- Is this chunk of code doing something with one purpose, which could be described as the purpose of the possible subfunction?
- Is this chunk of code connected to the surrounding code fairly loosely, so that all it would need are a few input arguments and a return value or two? Or does it use and/or change multiple variables from the code around it in ways that are hard to cleanly factor?
- Is it long enough to be worth factoring?
- Overall, would moving this bit out make the code easier or harder to understand and debug?

Sometimes it's worth putting a single line of code into a subfunction, if the line is nontrivial and doing so improves code readability. The ability to give that chunk a descriptive name (it's function name) can, all by itself, significantly aid readability.

BTW, one very significant advantage of factoring code into subfunctions is that you can test the subfunctions individually to make sure they work correctly. Finding a head-scratcher of a bug is much easier if you've narrowed it down to somewhere in a five-line function than if it's somewhere in a 40-line function.

___
## Example

Let's say we need to calculate the total electrostatic potential energy stored in an arrangement of three charged point particles. Doing that requires summing the three pairwise potential energies, so calculating the potential energy of a pair is a sensible subfunction. Also, doing each pair calculation requires finding a distance, which _could_ be done inline, but could also be factored out for clarity.

```python
from math import sqrt

def distance(x1, y1, z1, x2, y2, z2):
    """ Returns the distance between two points in 3D.
    """
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def two_body_potential(q1, x1, y1, z1, q2, x2, y2, z2):
    """ Returns the potential energy of two point charges, in SI 
        units.
    """
    k = 8.9875517873681764e9 # N m² C⁻²
    r = distance(x1, y1, z1, x2, y2, z2)
    return k * q1 * q2 / r

def three_body potential(q1, x1, y1, z1, q2, x2, y2, z2, q3, x3, y3, z3):
    """ Returns the total potential energy of three point charges, in SI 
        units.
    """
    return (two_body_potential(q1, x1, y1, z1, q2, x2, y2, z2) +
            two_body_potential(q1, x1, y1, z1, q3, x3, y3, z3) +
            two_body_potential(q2, x2, y2, z2, q3, x3, y3, z3))
```
Side note: The most awkward part of all this is passing around four arguments for every particle. I wouldn't actually do this; instead, I'd pack them together into _tuples_ or _lists_ or — getting fancy — something called a _named tuple_. We'll be covering _tuples_ and _lists_ in Level A-05. After doing that, if you want to teach yourself about named tuples, <a href="https://realpython.com/python-namedtuple/" target="_blank">be my guest!</a>

___
