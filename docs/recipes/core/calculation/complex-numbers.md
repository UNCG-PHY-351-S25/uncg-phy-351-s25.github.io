# Use Complex Numbers

___
## Problem to Solve

> **I want to do a calculation that involves complex numbers.**

___
## Introduction

Rejoice — python has built-in support for complex numbers, right alongside integers and real (floating-point) numbers!

The only real catch is that the functions in the `math` module don't work with complex numbers. That's not an issue, since the `cmath` module has all the same functions, but written to handle both real and complex numbers equally well.

___
## Recipe A: Assembling and Disassembling Complex Numbers

If you have actual numbers (not variables) for the real and imaginary parts, you can specify a complex number with what's called a _literal_:

```python
>>> c1 = 3 + 2j  # positive real and imaginary parts
>>> c2 = -3 - 2j  # negative real and imaginary parts
>>> c3 = 2j  # imaginary part only, real part is zero
>>> c4 = 3 + 0j  # a complex number with zero imaginary part
```

Note that a "complex number with zero imaginary part" is still recognized as a complex number by python, even though it's mathematically equivalent to a real number. Also note that you can get $\sqrt{-1}$ (which we commonly call "i" in physics) by using `1j`.

Python follows the engineering convention of using `j` to represent the imaginary unit, rather than the mathematician's `i`. This is because `i` is often used as a loop index in python code, and `j` is less likely to be confused with a variable name.

If you have real and imaginary parts stored in separate variables, you can construct a complex number from them with the `complex()` _constructor function_. Let's assume that the variables `a` and `b` already hold numeric values from prior calculations. We can make them the parts of a complex number via:

```python
>>> c = complex(a, b)
>>> c
(3-4j)
```

If you're doing a calculation and you need something like $i\phi$ where $\phi$ is a variable represented by `phi` in your code, you can put that into a python formula as either `complex(0, phi)` or `1j * phi`. I personally prefer the latter, as it's closest to the original math notation.

You can extract the real and imaginary part of a complex number thusly:

```python
>>> z = 3.5 - 4.2j
>>> z.real
3.5
>>> z.imag
-4.2
```

This works for complex expressions, not just variables:

```python
>>> (3.5 - 4.2j).real
3.5
>>> (z**2 - 2*z + 1).imag
-21.0
```

It should be obvious to you that:

```python
>>> complex(z.real, z.imag) == z
True
```

___
## Recipe B: Doing Math with Complex Numbers

Python's standard arithmetic operators (`+`, `-`, `*`, `/`, `**`) work properly with complex numbers. Nothing special is needed. (Note that the `//` and `%` operators for integer division and remainder don't, because those operations are not mathematically defined for complex numbers. Don't blame python.)

Python's **built-in** numeric functions `abs()`, `pow()`, and `sum()` work properly with complex numbers. Others don't, because they're not mathematically well-defined.

> **The functions in the `math` module do NOT work with complex numbers!**

However, if you simply use `cmath` instead of `math`, you'll get all the same functions, but written to handle both real and complex numbers equally well.

___
## Recipe C: Working with Complex Numbers in Polar Form

In addition to the _rectangular_ or _Cartesian_ representation of a complex number $z = a + b\,i$, in physics we often use the _polar_ representation $z = r\,e^{i\theta}$, where $r$ is called the _magnitude_ of $z$ and $\theta$ the _phase_. If we know $a$ and $b$, we can calculate $r$ and $\theta$, or vice-versa.

Of course, python can do that for us. In addition to complex-aware copies of the functions in the `math` module, `cmath` has a few special-purpose functions for working with complex numbers:

- `abs(z)` returns the magnitude $r$. (Yes, this is the usual built-in `abs()` function. It's smart enough to know that the "absolute value" of a complex number is its magnitude.)
- `cmath.phase(z)` returns the phase $\theta$, in radians.
- `cmath.polar(z)` returns both the magnitude and phase as a two-element tuple `(r, theta)`.
- `cmath.rect(r, theta)` creates a complex number habving magnitude $r$ and phase $\theta$.

So, if you want to know the imaginary part of a complex number that has magnitude 1 and phase $\pi/4$, you can do this:

```python
>>> import cmath as cm
>>> z = cm.rect(1, cm.pi/4)
>>> z.imag
```

Or, more compactly, just `cmath.rect(1, cmath.pi/4).imag`. (The `cmath` module defines the same constants as `math`, such as `pi` and `e`, so you don't have to import two different packages. They're still real numbers.)

___
## Recipe D: Complex Conjugation

One additional operation you might need to do with a complex number (say, $z$) is to take its complex conjugate (denoted $z^*$). Mathematically, this is defined as flipping the sign ($+ \leftrightarrow -$) of the imaginary part, or replacing $i$ with $-i$ in the polar form, (or in any form composed of real numbers and explicit $i$s). Here's a possible, **but bad**, way to do that in python:

```python
>>> z_star = complex(z.real, -z.imag)  # Don't do this!
```

Instead, use the `conjugate()` function from the `cmath` module:

```python
>>> import cmath as cm  # If not done already imported, of course.
>>> z_star = cm.conjugate(z)
```

That's cleaner and easier for a human to interpret. It's also less error-prone, and slightly faster.

However, a warning: **Let python do the work for you!** You may be so used to doing complex arithmetic "by hand" that you try to do that in your code, too. For example, here are three different, mathematically equivalent ways to find the magnitude of a complex number `z`:

```python
>>> z_mag_1 = cm.sqrt(z.real**2 + z.imag**2)  # Don't do this.
>>> z_mag_2 = cm.sqrt(z.conjugate() * z)      # Don't do this either.
>>> z_mag_3 = abs(z)                          # Yes, do this!
```

If you think of the core python `abs()` function as meaning "give me the magnitude of this thing", it becomes a natural extension of absolute value, and results in cleaner, less error-prone, and (slightly) faster code.

___
## An Example

Let's say that we have a simple series circuit (one loop) with an AC voltage source, a resistor, an inductor, and a capacitor all in series, and we want to know the current flowing through the circuit as a function of time. In a course like PHY 412, you'd learn that it's trivial to analyze such a circuit using the method of _complex impedances_, and you could derive the following expression for the current in the circuit as a function of time:

$$ I(t) = \text{Re}\left(\frac{V_0\,e^{i\omega t}}{R + i \left( \omega L - \frac{1}{\omega C} \right)}\,\right) $$

where $\text{Re}(…)$ means "take the real part of".

For specific numerical values, let's say:

- The driving voltage is $V(t) = V_0\ \cos(\omega t)$ with $V_0 = 10\text{ V}$ and $f = 100\text{ Hz}$ (Remember that the angular frequency $\omega = 2\pi f$).
- The resistance, inductance, and capacitance of the resistor, inductor, and capacitor are $R = 100\ \Omega$, $L = 200\text{ mH}$, and $C = 10\ \mu\text{F}$ respectively.
- We want to know the current at times of $t = 0, 1, 2, 3, 4, 5, \text{and } 10\text{ ms}$.

Calculating these is easy with python!

```python
In [1]: Vo, f = 10, 100

In [2]: R, L, C = 100, 100e-3, 10e-6

In [3]: from cmath import pi, exp

In [4]: w = 2 * pi * f

In [5]: Z = R + 1j * (w * L - 1 / (w * C))

In [6]: Z
Out[6]: (100-96.32309002009944j)

In [7]: t = 0

In [8]: (Vo * exp(1j * w * t) / Z).real
Out[8]: 0.05187223045425429

In [9]: t = 1e-3

In [10]: (Vo * exp(1j * w * t) / Z).real
Out[10]: 0.012596863910223792

In [11]: t = 2e-3

In [12]: (Vo * exp(1j * w * t) / Z).real
Out[12]: -0.031490076495855286

In [13]: t = 3e-3

In [14]: (Vo * exp(1j * w * t) / Z).real
Out[14]: -0.06354887798885185

In [15]: t = 4e-3

In [16]: (Vo * exp(1j * w * t) / Z).real
Out[16]: -0.07133416803702705

In [17]: t = 5e-3

In [18]: (Vo * exp(1j * w * t) / Z).real
Out[18]: -0.051872230454254306

In [19]: t = 10e-3

In [20]: (Vo * exp(1j * w * t) / Z).real
Out[20]: 0.051872230454254306
```

A few comments:

- In entry 5, I'm calculating the denominator of the expression and stashing it in a temporary variable `Z`. This keeps the overall expression for the current from getting too ugly and error-prone. Since the denominator does not depend upon the time `t`, I don't have to recalculate it every time I change the value of `t`.
- Starting with entry 9, I'm just repeating a cycle of:
    1. up-arrowing twice to bring up the prior definition of `t`;
    2. left-arrowing to put the cursor left of the =`e`, hitting delete, and typing the new time value;
    3. hitting Enter (or shift-Enter) to set the new time value;
    4. up-arrowing twice to bring up the prior expression for the current; and
    5. hitting Enter or (shift-Enter) to reevaluate it.

    This is a very efficient way to repeat a calculation for different values of some variable.

- (Yes, its even easier to use a loop, which we'll get to in an upcoming recipe. And this is a natural situation in which to define a custom function for the current, which we'll also get to soon enough.)

- Instead of `Vo * exp(1j * w * t)` it would have been entirely equivalent to use `rect(Vo, w * t)` after importing `rect` from `cmath`. That's probably simpler and easier to read, **if** you're fluent with the polar form of complex numbers.
