# Use Global Variables (Sparingly!)

___
## Problem to Solve

> **I need to get values deep into a function or subfunction, and passing them via arguments is tedious.**

___
## Background Knowledge

In general arguments and return values are the preferred methods of getting variable values into and out of functions. However, sometimes you'll define some variables at a very high level in your code that will need to be referenced in multiple places, including deep inside functions and subfunctions. Passing those variables from function to function to function through a succession of arguments can be tedious, and can clutter up code and make it harder for a human to quickly identify the arguments that are of particular significance for a specific function.

In such situations, you can use **_global variables_**. Here are some definitions:

- **_Local variable_**: A variable that is defined inside a function, and is therefore accessible only to that function.

- **_Global variable_**: A variable that is defined outside of any function, and is therefore accessible to all functions.

Python actually has one other category, which only occurs when a subfunction is defined (not just called) inside another function. I'll call this an _internal subfunction_. The type you saw in the previous recipe, where the subfunction definition occurs outside the function that calls it, is an _external subfunction_.

- **_Nonlocal variable_**: For an internal subfunction, a variable that is defined in the scope of an enclosing function.

Remember this:

1. Variables defined inside a function ("local variables") are only accessible within the function itself and any subfunctions also defined <u>within</u> that function.

1. Variables defined outside of any function ("global variables") are accessible to all functions.

1. Global variables, and variables local to an enclosing function, cannot be altered without using the `global` keyword to make it clear you're not trying to create a new local variable that happens to have the same name.

To keep life simple, I recommend avoiding nested function definitions ("internal subfunctions") unless you've got a very specific reason to use one.

If you want a more thorough tutorial on global variables, <a href="https://realpython.com/python-use-global-variable-in-function/" target="_blank">here's one.</a>

### Why NOT to use global variables

Use global variables sparingly. When you're trying to find a bug in your code or just convince yourself that your logic is right, tracing the flow of values into and back out of functions via arguments and return values is fairly straightforward. However, when global variables can be accessed from anywhere, the flow of information gets much more complicated and harder to follow. Bugs become more likely.

_Change_ global variables from within functions even more sparingly… preferably _never_. Why? Because it's extremely easy for one bit of your code to change a global function in a way that breaks some other bit of your code, and whether/how the breakage occurs can depend on the details of execution order, number of repetitions, etc.

Beatty's rule of thumb:

> **Use global variables to define constants that don't change and need to be accessed in multiple places. Avoid changing the values of global variables if you possibly can.**

___
## Recipes

### Flavor A: Using a Global Variable

```python
# Define a global variable
MY_GLOBAL = 42

def my_function():
    """ Uses a global variable. """
    return 2 * MY_GLOBAL - 1
```
BTW, a common coding convention is to put the names of variables that are intended to be constants — defined once and never changed — in all-caps, especially if they are globals.

### Flavor B: Changing a Global Variable

If you want a function to change, not just read, the value of a global variable, you have to include an extra step. Without the `global` keyword, the function will define its own variable `MY_GLOBAL` in its own scope rather than use the global one.

```python
# Define a global variable
MY_GLOBAL = 42

def my_function(a, b):
    """ Alters a global variable. """
    global MY_GLOBAL
    MY_GLOBAL += 1
```

### Flavor C: Inheriting Local Variables

Here's the recipe for having an internal subfunction inherit variables from an enclosing function:

```python
def outer_function(arg1, arg2, arg3):
    """ Defines a local variable and an internal subfunction. """
    inner_var_1 = ...  # Define a local variable somehow

    def inner_function(argA):
        """ Uses one or more local variables from the enclosing function. """
        a_result =  ... # Calculate using arg1, arg2, arg3, and/or inner_var_1 as well as argA
        return a_result

    return inner_function(...) # Call the internal subfunction with any legitimate expression
```

Again, I think the complexity of this approach is rarely worthwhile.

___
## Examples

### Generic Mix-n-Match

Here's a generic example that showcases both internal and external subfunctions, with access to local, nonlocal, and global variables. (I can think of no good reason to structure code like this, but it's an illustration.)

```python
# Define a global variable:
a_global_var = 1.0

def external_sub():
    print(f"external_sub: {a_global_var = }")
    # Won't work:
    # print(f"external_sub: {a_local_var = }")

def main():

    def internal_sub():
        print(f"internal_sub: {a_global_var = }")
        print(f"internal_sub: {a_local_var = }")

    # Define a local variable:
    a_local_var = 2.0
    
    print(f"main: {a_global_var = }")
    print(f"main: {a_local_var = }")
    internal_sub()
    external_sub()

main()
```

### Actual Physics Example

For some obscure purpose related to electromagnetism, let's say you need to write a function that takes the charges and positions of three particles arranged along the x-axis, and calculates and returns two values: (a) the net force acting on particle #3, and the electrostatic potential energy it has because of the other two (i.e., the energy required to bring particle #3 in "from infinity"). Here's one good way to implement that:

```python
# Constants
k = 8.9875517873681764e9 # N m² C⁻²

def F(qA, xA, qB, xB):
    """ Calculate the electrostatic force of repulsion on particle
        B due to particle A.
    """
    return k * qA * qB * (xB - xA) / abs(xB - xA)**3

def U(qA, xA, qB, xB):
    """ Calculate the electrostatic potential energy between
        two particles.
    """
    return k * qA * qB / abs(xB - xA)

def force_and_energy_on_3(q1, x1, q2, x2, q3, x3):
    """ Calculate the net electrostatic force AND potential energy
        on/of particle 3 from 1 and 2.
    """
    F_net = F(q1, x1, q3, x3) + F(q2, x2, q3, x3)
    U_net = U(q1, x1, q3, x3) + U(q2, x2, q3, x3)
    return F_net, U_net
```

An alternative way to do this, reducing the passing of arguments somewhat, would be to use internal subfunctions:

```python
# Constants
k = 8.9875517873681764e9 # N m² C⁻²

def force_and_energy_on_3(q1, x1, q2, x2, q3, x3):
    """ Calculate the net electrostatic force AND potential energy
        on/of particle 3 from 1 and 2.
    """
    def F_from(q, x):
        """ Calculate the electrostatic force of repulsion on particle
            3 (in inherited scope) due to a particle with charge `q`
            at location `x`.
        """
        return k * q * q3 * (x - x3) / abs(x - x3)**3
    
    def U_from(q, x):
        """ Calculate the electrostatic potential energy of particle
            3 (in inherited scope) with a particle with charge `q`
            at location `x`.
        """
        return k * q * q3 / abs(x - x3)
    
    F_net = F_from(q1, x1) + F_from(q2, x2)
    U_net = U_from(q1, x1) + U_from(q2, x2)
    return F_net, U_net
```
Personally, I don't think the modest shortening of the argument lists is worth the additional cognitive load of having to figure out where the various variable values come from.

___
