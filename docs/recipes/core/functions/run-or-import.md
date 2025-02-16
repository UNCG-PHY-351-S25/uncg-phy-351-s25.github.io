# Run or Import From a Script

___
## Problem to Solve

> **I want to write a script that I can run, and I also want to use functions it defines in the console or other scripts.**

___
## Background Knowledge

This is not an unusual situation. One case is that you developed some reasonably general functions while solving one particular problem with a python script, and now would like to "borrow" those functions for a different calculation. You could copy-paste them, but perhaps you'd like to be able to improve or debug them in just one place while using them in multiple places.

Another, common case is that you write a python script specifically to define functions for other scripts to import, but you want to include some test or demonstration code in the script that will execute if you run the script directly rather than importing it.

Python has a mechanism for this, though it looks rather arcane. The key thing to understand is that when a python script is _run_, the python interpreter defines a special variable named `__name__` and sets it to the string `"__main__"`. However, when a script is _imported_, the interpreter sets `__name__` to the name of the script doing the importing. The recipe takes advantagre of this to decide whether to run some code or not.

___
## Recipe

```python
# Start with code that should be executed regardless of whether the script is 
# run or imported.

some_constant = ... # We can define constants available to scripts importing this one.

def function_one(arg1, arg2):
    """ A function available to scripts importing this one. """
    ...  # Calculate stuff
    return ...  # Return something

def function_two(arg1):
    """ Another function available to scripts importing this one. """
    return ...  # Return something

# Now, put the code to execute only if this script is run directly, but not when
# it is imported.
if __name__ == "__main__":
    # Code inside here will be executed only if the script is run, but not if it's
    #  imported. It can (but doesn't necessarily have to) use the constants and 
    # functions defined above.
    ...  # Do something
    ...  # Do something else
```

___
## Example

Let's say that you often need to calculate the range of a projectile, given its muzzle speed, launch angle, and (optionally) elevation of the launch point above the ground. You'd like to be able to call this function from other scripts that might, for example, iteratively search for the maximum range, or plot the range as a function of launch angle, or whatever. You'd also like to be able to run this script, have it prompt you for the input parameters, and then print out the result (to three significant figures, of course). Here's how you could accomplish that:

```python
# file: projectile.py

# Imports
from math import radians, sin, cos, sqrt

# Define constants:
g = 9.81  # N/kg == m/s**2

# Define the range function
def range(v0, theta, h=0.0):
    """ Returns the range of a projectile launched at speed v0 and angle theta.
        Optional argument h is the height of the launch point above the ground.
        SI units are presumed.
    """
    theta_rad = radians(theta)
    v0x, v0y = v0 * cos(theta_rad), v0 * sin(theta_rad)
    t_flight = (v0y + sqrt(v0y**2 + 2 * g * h)) / g
    return v0x * t_flight

# Provide the interactive interface if the script is run directly:
if __name__ == "__main__":
    v0 = float(input("Enter the initial speed (m/s): "))
    theta = float(input("Enter the launch angle (degrees above horizontal): "))
    h = float(input("Enter the height of the launch point above the ground (m): "))
    print(f"Range: {range(v0, theta, h):.3g} m")
```
In addition to running this script and providing the initial conditions interactively, you could have another script (or you, from the console) call it programmatically:

```python
from projectile import range
print(f"Test calculation: range = {range(50, 30):.3g} m")
```

And guess what? You know those useful modules like `math` and `cmath` that you import, or import functions from? _Now you can create your own libraries of useful functions!_ 🤯
___
