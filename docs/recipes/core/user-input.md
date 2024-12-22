# Ask for User Input

___
## Problem to Solve

> **I want to be able to run my script (or let someone else run it) with various given values, without having to edit the script each time.**

Editing and re-running a script isn't hard if you already have the script open in your editor. However, it's possible to run a script without opening it in an editor; one way is to simply execute `python my_script.py` in a terminal, assuming the script file is in the current working directory. (On some systems, you may have to execute `python3 my_script.py` instead.) In such a case, it's convenient to let the script ask the user for values when it runs.

___
## Recipe

Python has a built-in `input()` function that asks the user for input. You can use this to get given values at run-time, but you'll need to do a bit of extra work to get numerical values and protect against incorrect entries. Here's the generic recipe:

```python
# Ask user for a value:
variable_name = input("Prompt string: ")

# Convert from a string to a float:
# (Use `int` for an integer or `complex` for a complex number.)
variable_name = float(variable_name)

# Do any necessary safety-checking, such as:
assert variable_name >= 0, "Value must be non-negative."

```

You can compactify this, if you want:
```python
variable_name = float(input("Prompt string: "))
assert variable_name >= 0, "Value must be non-negative."
```

Notes:

1. Change `variable_name` to the name you want to use for the value you're getting from the user: `m`, `v0`, or whatever.

2. Change `Prompt string` to an appropriate cue to the user. Be explicit about units, if appropriate, so you don't get a mass in grams when the code is expecting kilograms, or an angle in radians when it expects degrees.
    - Example: `m1 = float(input("Mass 1 (in kg): ))`

3. The `float(…)` or `int(…)` or `complex(…)` is necessary because the `input(…)` function returns the user's input as a string. Your code must _coerce_ it into the desired type.

4. If the user enters something that's not directly interpretable as the desired type, python will raise a scary error. We'll learn how to handle this gracefully later.
    - If the input is `2.5 kg`, `float(…)` will fail.
    - If the input is `3.2` or even `3.0`, `int(…)` will fail.
    - `complex(…)` is picky: `3-2j` is fine, but `3 - 2j` will fail because of the spaces around the minus sign. 🤷‍♂️

5. `assert` is a useful python keyword. Here's what it does:
    - If the logical statement following it is true, the line does nothing and the script continues to the next line.
    - If the logical statement is false, python raises an error and aborts the script, displaying a scary and cryptic error message to the user.
    - The comma and string after it are optional. If you provide them, the string will be displayed to the user as part of the error message. You can (and should) use this to tell the user specifically what they did wrong.

It's not hard to write a better version of this recipe that handles invalid input more gracefully — for example, letting the user try repeatedly until they get it right, and showing a friendly message instead of a scary python error dump when they get it wrong. However, that requires python features we haven't reached yet. So for now, this recipe will suffice.

If you want to ask for more than one value, just repeat this recipe more than once in your script.

___
## An Example

Let's write a simple little utility script that calculates a vector's $x$ and $y$ components from its magnitude and direction.

```python
# Imports:
from math import sin, cos, radians

# Ask for the magnitude:
mag = input("Vector's magnitude (without units): ")
mag = float(mag)
assert mag >= 0, "The magnitude must be non-negative!"

# Ask for the direction:
angle = input("Vector's direction (in degrees CCW from +x axis): ")
angle = float(angle)

# Calculate components:
x = mag * cos(radians(angle))
y = mag * sin(radians(angle))

# Report out:
print(f"=> The vector's components are ({x:.3g}, {y:.3g}).")
```
