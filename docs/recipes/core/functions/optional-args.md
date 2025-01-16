# Make Arguments Optional

___
## Problem to Solve

> **I want to write a function with an argument that the user can ignore unless they want to override the "normal" value with something else.**

___
## Recipe

### Step 1: _Define_ the Function With Default Values

You can make any one of a function's arguments _optional_ — meaning that calling code can either specify a value for it or omit it entirely — by supplying a _default value_ in the function signature:

```python
def function_name(arg_1, arg_2=default_value_2):
    """ Template for a function that has one required and one optional argument.
    """
    pass # Replace these two lines with actual code that does
    pass # something with arg_1 and arg_2.
    return result
```

Replace `default_value_2` with the specific value you want the function to use for the value of `arg_2` if the calling code doesn't provide one.
    - You can specify a numeric literal, a string literal, a variable, or a more complicated python expression.
    - However, mind that the variable or expression will be evaluated only once, at the time the function definition is sent to the interpreter, and NOT every time the function is called.
    - A literal number, string, or boolean value is by far the most common kind of default value.

### Step 2: _Call_ the Function With or Without the Optional Argument

When calling a function with an optional argument, you can either provide a value for the optional argument or omit it. If you omit it, the function will use the default value specified in the function definition.

Both of these function calls are valid:

```python
a = function_name(val_1, val_2)
b = function_name(other_val_1)
```

### Elaboration: Mixing and Matching Multiple Optional Arguments

If more than one argument is optional, and calling code provides fewer than the maximum number of values, which optional arguments get the passed values and which use default values?

Any values provided by the calling code will be assigned to arguments from left to right according to the function signature, **unless told otherwise by explicit argument names**. Consider this function definition:

```python
def function_name(x=0, y=0):
    """ Template for a function that has two optional arguments.
    """
    pass # Do something with x and y.
    return result
```

The function can be called in any of these ways:

```python
out_1 = function_name()      # Sets x to 0 and y to 0
out_2 = function_name(1)     # Sets x to 1 and y to 0
out_3 = function_name(1, 2)  # Sets x to 1 and y to 2
out_4 = function_name(y=2)   # Sets x to 0 and y to 2
```

The following are also legitimate, but unnecessary. The first two might be worth writing for the sake of clarity; the third is simply confusing.

```python
out_5 = function_name(x=1)       # Sets x to 1 and y to 0
out_6 = function_name(x=1, y=2)  # Sets x to 1 and y to 2
out_7 = function_name(y=2, x=1)  # Sets x to 1 and y to 2
```

Side note: It is possible to define a function that can accept any number of optional arguments, either with or without argument names in the calling code. However, that requires the use of _collections_ that we have not yet looked at.

___
## Example

```python
import math
def projectile_range(v0, theta, h=0, g=9.81):
    """ Calculate the range of a ballistic projectile without air resistance, launched
        from an arbitrary height above the ground.
    
        Parameters:
        - v0: The projectile's initial velocity (m/s)
        - theta: the projectile's launch angle above horizontal (degrees)
        - h: the launch height above the ground (m), defaults to zero
        - g: the local gravitational constant (m/s**2), defaults to Earth
        
        Returns: the horizontal distance the projectile travels, in meters, before
            hitting the ground.
    """
    # Convert angle from degrees to radians.
    theta_rad = math.radians(theta)
    
    # Calculate range using the standard formula derived in intro physics.
    range_ = (v0 * math.cos(theta_rad) / g) * (
        v0 * math.sin(theta_rad) + math.sqrt((v0 * math.sin(theta_rad))**2 + 2 * g * h)
    )
    
    return range_
```

Note: This uses `range_` instead of `range` for the name of the returned variable because `range` is the name of a built-in python function that we don't want to collide with. Appending an underscore is a common way of working around conflicts between desirable variable names and already-existing python names.

Usage:

```python
v, theta, h = 85, 25, 10
print("On level ground and in the absence of air drag, the horizontal distance traveled")
print(f"by a ballistic projectile fired with muzzle speed {v} m/s at an angle of {theta}")
print(f"degrees above the horizontal is {projectile_range(v, theta):.2f} meters.")
print()
print(f"If the projectile is launched from a height of {h} meters above the ground,")
print(f"the horizontal distance traveled is {projectile_range(v, theta, h):.2f} meters.")
print()
g_moon = 1.625  # Moon's gravity is about 1/6th of Earth's.
print("If launched on the moon from ground level, the distance traveled would be")
print(f"{projectile_range(v, theta, g=g_moon):.2f} meters.")
```
___
