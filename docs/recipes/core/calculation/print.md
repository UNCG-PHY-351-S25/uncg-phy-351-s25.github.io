# Print Formatted Output

___
## Problem to Solve

> **I want to control the output of my code so that I can include text, specify precision, and so on.**

___

## Introduction

A bare python expression produces a result when evaluated. That result is of some particular type: an integer, a floating-point or complex number, a text string, or perhaps something else. The IPython console or other interactive python session will display that result according to some default rule it has for that type. The result will probably provide sufficient information, but may be ugly or otherwise not quite as human-friendly as you'd like. (This is especially important when writing _scripts_, which we'll get to in the next recipe, [Write a Calculation Script](scripts.md).)

To control the details of python code output, use the built-in `print()` function. Using it can be drop-dead simple, or mysteriously arcane and complex, depending on what your goals are. We'll build the complexity up gradually in this recipe.

### A bit of terminology and conceptual background…

* _Statements_ are chunks of python code that make changes to the python environment when they are executed, like importing a module or functions from it, or defining a variable and setting its value. Programmers call these "side effects". You can think of them as imperative sentences: "Do this." Statements generally stand alone on a line (or a multi-line block), and don't "return" a value.
* _Expressions_ are chunks of python code that are evaluated and converted into some kind of value or object when they are executed. They don't do anything other than produce this value. Often, they are part of a statement, such as the right-hand side of `x = 5.0 * sin(radians(15))`. Expressions can be made up of other expressions: `15` is an expression, as are `radians(15)` and `sin(radians(15))`. In IPython, when a "bare expression" — a line of python code that is an expression and not a statement — is sent to the python interpreter, the interpreter returns its value, and IPython displays that value as an "output" line.

When working in IPython, the difference between values displayed as the result of expression evaluation and values displayed by `print()` is easy to overlook. The difference is important, however, and will be much more obvious when we move beyond IPython and start writing script files. For now, the key fact to stick into your memory is that `print(...)` is a _statement_ that returns no result, but has the "side effect" of displaying text to the user. An expression simply returns a value, which might get used as part of a larger expression or statement, might be displayed to the user, or might be totally ignored depending on the context.

One benefit of using `print()` statements to see your calculation results is that you get a whole lot of control over _how_ values are displayed. You can embed numbers in text, control decimal digits or significant figures, force or prevent the use of scientific notation, control widths, etc.

## Recipe A: Just Print one Value

If all you want to do is get a value to display, and you're fine with python's default choices, just pass it to `print()` as an argument:

```python
from math import sin
theta = 0.01
sin_theta = sin(theta)
print(sin_theta)
```
produces
```text
0.009999833334166664
```

## Recipe B: Print Multiple Values

If you pass multiple comma-separated arguments to `print()`, it will print them all, separated by spaces. (Note that any python expression can be an argument to `print()`, not just a variable name.)

```python
print(theta, sin_theta, theta - sin_theta)
```
produces
```text
0.01 0.009999833334166664 1.6666583333574403e-07
```

(Note how python automatically switches to scientific notation when the number is very small.)

You can change the separation character from a space to something else (say, a comma) by specifying the `sep` keyword argument:

```python
print(theta, sin_theta, theta - sin_theta, sep=', ')
```
produces
```text
0.01, 0.009999833334166664, 1.6666583333574403e-07
```

You can even squish the values together with no separation at all by specifying an empty string as the separator:

```python
print("Twelve", 12.0, 12, sep='')
```
produces
```text
Twelve12.012
```

(This use case makes no sense, but situations do arise where it's helpful.)

## Recipe C: Inserting Values Into Text

Python has a special kind of string called an "f-string" (for "formatted string") that allows you to insert values into specific locations in a string. To use this, prepend a `f` before the opening quote, and put curly braces `{…}` around the value(s) to be inserted:

```python
print(f"Theta is {theta}, its sine is {sin_theta}, and their difference is {theta - sin_theta}.")
```
produces
```text
Theta is 0.01, its sine is 0.009999833334166664, and their difference is 1.6666583333574403e-07.
```

## Recipe D: Controlling Number Format

Look at that last output line. Notice that python displayed the first two numbers in traditional decimal notation, but chose to display the third number in scientific notation. By default, it displays very large and very small floating-point numbers in scientific notation, and uses decimal notation in between.

You can force python to use a particular format by including a _format specifier_ like this:

```python
print(f"Theta is {theta:e}, its sine is {sin_theta:e}, and their difference is {theta - sin_theta:f}.")
```
This produces
```text
Theta is 1.000000e-02, its sine is 9.999833e-03, and their difference is 0.000000.
```
If you include `:f` (for "floating-point") inside the curly-braces and after the variable or expression, python will display the number in decimal notation regardless of its size. If you include `:e` (for "exponential") instead, python will display the number in scientific notation. (`e` means "exponential".) Or, if you use `:g` (for "general"), python will choose between the two formats based on the number's size.

Although `:g` is very similar to using no specifier at all, the results can be slightly different:

```python
diff = theta - sin_theta
print(f"The difference can be shown as {diff}, {diff:f}, {diff:e},or {diff:g}.")
```
produces
```text
The difference can be shown as 1.6666583333574403e-07, 0.000000, 1.666658e-07,or 1.66666e-07.
```
Examine carefully, especially the number of digits shownf

## Recipe E: Controlling Precision

Format specifiers also let you control the number of digits displayed in the number. When using the `f` or `e` specifiers, you can specify the number of digits past the decimal point to show. (With the `f` specifier, the number of digits before the decimal point is whatever it is. With the `e` specifier, the exponent is chosen so that there's always one digit before the decimal point.)

When using `g`, on the other hand, you can specify the number of **significant figures** (not decimal digits) to show for whichever format python chooses (floating-point or exponential). **Warning**: the way that python counts significant figures for floating-point numbers is not always the way physicists count them, so beware! (I've)

```python
x = 0.123456789
y = x * 1e-6
z = 0.01
print(f"x is {x:.4f}, {x:.4e}, and {x:.4g}.")
print(f"y is {y:.4f}, {y:.4e}, and {y:.4g}.")
print(f"z is {z:.4f}, {z:.4e}, and {z:.4g}.")  # See what `.4g` does here!
```
produces
```text
x is 0.1235, 1.2346e-01, and 0.1235.
y is 0.0000, 1.2346e-07, and 1.235e-07.
z is 0.0100, 1.0000e-02, and 0.01.
```

## Recipe F: Controlling Precision Programmatically

This is a cute trick that you probably won't need often, but when you do, is super-handy to know: You can use a variable to specify the number of digits displayed by the `f`, `e`, and `g` formats. Just wrap the variable in its own set of curly braces `{...}`, inside the normal curly-braces around the value to be displayed.

```python
some_value, sigfigs = 22.0 / 7.15e5, 3
print(f"The value obtained is {some_value:.{sigfigs}g}.")
```
produces
```text
The value obtained is 3.08e-05.
```

## Recipe G: Percentages

A common way to display numbers between 0 and 1, when they represent the relative amount of something, is as a percentage. If you were doing this by hand, you'd multiply the number by 100 and then stick a "%" sign at the end. Python can do that for you! All you have to do is to use `%` as the format specifier instead of `f`. A number before the `%` indicates how many decimal digits to display, just as with `f`. For example:

```python
print(f"One-sixth is about {1/6:.3%}.")
```
will produce
```text
One-sixth is about 16.667%.
```

## Recipe H: Commas for Big Numbers

For human readability, grouping the digits of big numbers with commas is common. Here's how to make python do this:

```python
big_number = 1234567.89
print(f"A big number: {big_number:,}!")
```
produces
```text
A big number: 1,234,567.89!
```

(By the way, you can separate long numeric literals in python code for readability too, but you have to use underscores instead of commas. The numbers `1234567` and `1_234_567` mean exactly the same thing, but it's easier to see from the second thats the value is a bit over one million.)


## Recipe I: Other Formatting Capabilities

f-strings have WAY more functionality available, including things like left-padding the output with spaces to fill up a particular total width (in characters), which can be useful for making vertical columns of values line up. For a deeper dive, see:

- For a wordy introduction, the _Real Python_ tutorial [How to Format Floats Within F-Strings in Python](https://realpython.com/how-to-python-f-string-format-float/).
- For a "cheat sheet" summary of how to do different things, _Python Morsels'_ [Python f-string tips & cheat sheets](https://www.pythonmorsels.com/string-formatting/).
    - Here's a neat little trick I personally use a lot when debugging more complicated code: [Self-documenting expressions](https://www.pythonmorsels.com/string-formatting/#self-documenting-expressions-debugging).

___
(This recipe has no "An Example" section because the recipe bits are basically all examples.)
