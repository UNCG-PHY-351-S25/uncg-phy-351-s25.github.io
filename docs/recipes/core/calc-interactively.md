# Calculate Interactively

___
## Problem to Solve

> **I want to do a physics calculation that would be easy to do incorrectly in a calculator, and/or I might need to repeat it with different givens.**

___
## Recipe to Solve It

_This, too, is a "procedural" recipe. (I promise that actual code recipes are coming soon!)_

Let's assume that either you've solved the problem in question via paper-and-pencil, symbolically, and are now ready to plug in given constants, parameters, initial conditions, etc. to calculate one or more numerical results.

- Pro tip: Solve all but the most trivial physics problems **symbolically**, deriving a symbolic answer algebraically and simplifying as much as possible before inserting numerical values. If you're given numerical values and not variable names in the problem, define your own symbols! Even the local gravitational constant should be written as $g$ instead of $9.81 \, \text{m/s}^2$ or (gasp!) $9.8$ until the very end.

Overall, **follow the [launch, calculate, save](launch-calc-save.md) recipe**. This recipe provides advice on what to execute during the interactive IPython session.

1. **Define variables for the constants** you'll need, such as `g = 9.81` or `c = 3.00e8`.

    - Make sure your units are consistent! Putting everything into SI units (MKS) is often safest.

2. **Define variables for the other "given values"** in the problem.

    - Use legitimate python variable names that are as close as possible to the mathematical variable names you'd normally use: `m1` for $m_1$, `Vx0` for $V_{x}(t = 0)$, etc.
    - Again, make sure units are consistent. If you're given something in units that need to be converted, it's often easiest to write the conversion calculation directly into the variable definition. For example, if a problem says the mass of body 1 is 34.5 grams, enter `m1 = 34.5 / 1000` to get a numeric value in kilograms.
    - Multiple related values can be defined on one line with the "comma trick": `m1, m2 = 1.5, 4.0` or `Vx0, Vy0, Vz0 = 25, 0, 0`. 

3. **Construct arithmetic expressions** with [python's arithmetic operators](../../topics/core/operators.md) to calculate intermediate or final values.

    - Know and be careful of [operator precedence](../../topics/core/precedence.md), or you may get incorrect results.

1. **Import needed functions** from libraries like `math` and `complex` as you discover that you need them. (We'll have more about this in the next recipe, [use python functions](use-functions.md).)

1. **Build up complicated expressions from simpler chunks**, saving the values of the chunks in variables. Multiple simple expressions are way simpler to check and debug than one big, hairy one.

1. **Maximize readability** of arithmetic expressions by including appropriate whitespace around operators and (with a few exceptions) avoiding parentheses that are not required by operator precedence.

1. **Execute bare expressions** to display the final numerical values you seek. You can also do this for intermediate results, as a way of checking your work as you go.

___
## An Example

Let's say you've got a typical conservation of angular momentum problem from PHY 291:

> A thin rod of length $L = 50\text{ cm}$ and mass $M = 600\text{ g}$ sits on a horizontal surface, anchored to the surface by a pivot through its center. A puck of mass $m = 200\text{ g}$ slides across the tabletop with speed $v_\text{i} = 0.8\text{ m/s}$ strikes the rod at a distance $d = 20\text{ cm}$ from the pivot, perpendicular to the rod, and sticks to it. What is the rotational speed of the rod after the collision? Assume all forms of friction are negligible.

Applying the principle of conservation of angular momentum and some algebraic manipulations, you derive the following expression for the rod's post-collision rotational speed:

> $\omega = \frac{m\,d\,v_\text{i}}{m\,d + I} = v_\text{i}\left(1 + \frac{I}{m\,d}\right)^{-1}$
>
> where $I = \tfrac{1}{12}\,M\,L^2$ is the rotational inertia of the rod about its center.

Now it's time to calculate the numerical value, which means it's time to reach for python. After [firing up IPython](launch-calc-save.md), your interactive session might look something like the following. (IPython provides the bits that look like `In [1]: `; you provide what follows those.)

Defining constants and givens:

```python
In [1]: m, M = 0.200, 0.600

In [2]: L = 0.50

In [3]: d = 0.20

In [4]: v_i = 0.8
```

Calculate the rod's rotational inertia. (I could instead substitute the expression in for $I$ in the formula for the angular speed, but the result would be complicated enough to raise the risk of a mistake in the corresponding python expression. So, I'm obeying the recipe's advice to "Build up complicated expressions from simpler chunks".)

```python
In [5]: I = M * L**2 / 12
```

Calculate the final rotational speed:

```python
In [6]: v_i / (1 + I / (m * d))
Out[6]: 0.6095238095238096
```

(It's up to you to know that based on the units of your variables, the answer is in radians per second.)

Let's say that the problem included a part (b) that asks for the final rotational speed if the puck had instead hit and stuck to the very end of the rod. That's easy to calculate without very much repeated work. First, change the value of the relevant variable:

```python
In [7]: d = 0.25
```

Rather than retype the final formula, we can just press the keyboards up-arrow key three times to "walk back" through the session's command history, until the formula we want is displayed, and then press Enter to execute it again (with the current values of all variables):

```python
In [8]: v_i / (1 + I / (m * d))
Out[8]: 0.64
```

Out of curiosity, what was the numerical value of the rotational inertia?

```python
In [9]: I
Out[9]: 0.012499999999999999
```

(Again, it's up to you to know that based on the units of your variables, the answer is in kilogram-meters-squared. And you should definitely report your answer as $0.0125\text{ kg m}^2$, since those repeating-nines are certainly the result of machine round-off error, which we'll talk about in a later section of the course.)

Okay, we're done. Most of the time you'd just quit it with `exit`, but let's illustrate how to save the session history in case you want to refer back to it later. (For example, if you submit your answer and the numerical value gets marked wrong, you might want to compare what you did to the solutions to figure out whether you mis-entered something.)

```python
In [10]: %save p291-hw07-p3
The following commands were written to file `p291-hw07-p3.py`:
m, M = 0.200, 0.600
L = 0.50
d = 0.20
v_i = 0.8
I = M * L**2 / 12
v_i / (1 + I / (m * d))
d = 0.25
v_i / (1 + I / (m * d))
I

In [11]: exit
```

The lines of that output file could be copy-pasted into a new IPython session to recreate the calculations (possibly with some edits as you go, if you wish). Or, you could [run the entire file as a python script](scripts.md).
