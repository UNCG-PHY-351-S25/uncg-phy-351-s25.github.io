# Use Python Functions

___
## Problem to Solve

> **I want to use predefined mathematical (or other) functions, like sine or absolute-value, in my calculation.**

___
## Introduction

Python has a truly incredible arsenal of ready-to-use functions available to you. A few are built into core python, many many more are available through python's "standard library modules", and a truly humongous number are available through a vast ecosystem of third-party add-on modules that you can download and install as needed.

I think it's fair to say that before you spend time and effort figuring out how to do a coding task, it's worth stopping and asking yourself: "Does this seem like the kind of thing that people might commonly want to do, or is it really idiosyncratic to my situation?" If the former, there's probably a function already in existence for it. Depending on how hard the task is, and how critical your code's need for efficiency is, finding that function may or may not be the worth the time. The question is worth entertaining, though, and getting familiar with the range of functionality available to you is **definitely** worthwhile.

In this recipe, we'll focus predominantly on mathematically-oriented functions, but the same process applies to string (text) manipulation, rearranging collections of things, serving up web pages, and so on.

___
## Recipe for Built-In Functions

(This barely deserves the name "recipe".) If you need functionality provided by core python functions, just use them, like this: `function_name()` for a function that takes no arguments, or `function_name(argument_value_1, argument_value_2, ...)` for a function that takes one or more arguments.

- To get the absolute value of the number stored in variable `x`, use `abs(x)`.
- To calculate the seventh power of `x`, `pow(x, 7)` and `x**7` are equivalent.
- To round a floating-point number `a` to its nearest integer, use `round(a)`.
- To round a floating-point number `a` to `n` decimal places, use `round(a, n)`.

That's about it for mathematically-oriented functions, unless you want to check whether a particular variable is storing an integer, floating-point, or complex number:

```python
>>> a, b, c = 3, 3.0, 3+0j
>>> type(a), type(b), type(c)
(<class 'int'>, <class 'float'>, <class 'complex'>)
```

Or, you can (sometimes) forcibly change a variable to a different numeric type:

```python
>>> int(b)
3
>>> type(int(b))
<class 'int'>
>>> s = "3.14"
>>> round(s)
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    round(s)
    ~~~~~^^^
TypeError: type str doesn't define __round__ method
>>> round(float(s))
3
>>> float(c)
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    float(c)
    ~~~~~^^^
TypeError: float() argument must be a string or a real number, not 'complex'
```

[See here](https://realpython.com/python-built-in-functions/) if you want a thorough explanation of the core python functions available. (That's far beyond what this course requires.)

___
## Recipe for Standard Library Functions, Version A: Selective Import

To get a sense of the "modules" available in the python "standard library" — which come as part of a standard python installation, and therefore are always available to you — take a quick browse through [the python module index](https://docs.python.org/3/py-modindex.html), and drill down into any specific modules that catch your interest. At the very least, browse through [the `math` module](https://docs.python.org/3/library/math.html#module-math); you'll be using that A LOT.

It's necessary to "import" a module, or specific pieces of a module, before using them. In general, if you'll only be using a few of the functions in a module, it's best to import just those functions. Here's the generic recipe:

```python
from [module_name] import [comma-separated list of function names]
```
You can then use the functions you've imported exactly as if they were built-in functions. Here's a (very contrived) example:

```python
>>> from math import radians, degrees, sin, acos, sqrt
>>> angle = radians(76.543)
>>> degrees( acos( sqrt( 1 - sin(angle)**2 ) ) )
76.54299999999999
```

___
## Recipe for Standard Library Functions, Version B: Import the Module

If you'll be using many functions from one module — or if you'll be doing a fair amount of exploratory calculation and you don't really know which you'll be using and don't want to bother importing each function separately as you realize you need it — you can just import the whole module. Here's an example:

```python
>>> import math
>>> math.sin(math.radians(30))
0.49999999999999994
```

The general recipe is just `import module_name`, after which you must refer to the bits of the module with a prefix of `module_name.function_name(...)`. Yes, that can get a bit tedious.

You can make it a bit more compact by giving the module a shorthand name as you import it, using the `import module_name as nickname` syntax:

```python
>>> import math as m
>>> m.sin(m.radians(30))
0.49999999999999994
```

Just be careful that you don't accidentally define a variable `m` as well, or one will "shadow" the other:

```python
>>> import math as m
>>> m = 33
>>> m.sin(0)
Traceback (most recent call last):
  File "<python-input-33>", line 1, in <module>
    m.sin(0)
    ^^^^^
AttributeError: 'int' object has no attribute 'sin'
```

___
## Recipe for Standard Library Functions, Version C: Import Everything From the Module

If you really don't want to be bothered typing a prefix on every imported function, and just want everything in a module available as if it were all built-in or as if you'd listed EVERYTHING on an `from module_name import ...` line, you can, via the wildcard symbol `*` that means "everything":

```python
>>> from math import *
>>> angle = radians(76.543)
>>> sqrt( sin(angle)**2 + cos(angle)**2 )
1.0
```

**WARNING:** Everything in the module — which could include functions, constants, sub-modules, objects, and who-knows-what else — will get dumped into your namespace. That creates A LOT of potential for name collisions with your own variables, especially since you may not know all the names that were imported.

For example, in physics, the Greek letters "alpha" and "tau" are frequently used to represent angular acceleration and torque, respectively. Imagine that you're doing a rotational motion calculation, and the expression you've derived for an angular acceleration is

> $\alpha = \tau / I$ where $I = m \left[d \ \sin(30^\circ)\right]^2$

with given values are $\tau = 3.2 \times 10^5$, $m = 1500$, and $d = 18$ (all in SI units).

If you do this:

```python
>>> m, d, tau = 1.5e3, 18, 3.2e5
>>> from math import *
>>> I = m * (d * sin(radians(30)))**2
>>> tau / I
5.171345931835052e-05
```

…you'll be dead wrong. Compare the final result with this:

```python
>>> m, d, tau = 1.5e3, 18, 3.2e5
>>> import math
>>> I = m * (d * math.sin(math.radians(30)))**2
>>> tau / I
2.633744855967079
```

**Challenge:** Can you figure out why?

___
## An Example

**Problem:** An unpowered projectile is launched from the ground with an initial speed of 20 m/s at an angle of 50° above the horizontal. What are its speed and direction when it's height above the ground is 10 m?

**Solution:** Elementary kinematics allows one to derive expressions for the horizontal and vertical component of the projectile's velocity at any height $h$ (not greater than its maximum height, of course):

$$v_x(h) = v_{0,x} \qquad v_y(h) = \sqrt{v_{0,y}^2 - 2gh}$$

where $v_{0,x}$ and $v_{0,y}$ are the components of the projectile's initial velocity, $g$ is the acceleration due to gravity, and $h$ is the height above the ground. If $\theta_0$ represents the velocity's initial angle above horizontal, we can decompose the initial velocity vector into:

$$v_{0,x} = v_0 \cos(\theta_0) \qquad v_{0,y} = v_0 \sin(\theta_0)$$

We can use the expressions above to determine the components of the initial velocity vector, and then the velocity components at the given height. Once we know those, we can calculate the requested values by applying trig to find the magnitude and direction of the velocity vector at that height:

$$v(h) = \sqrt{v_x(h)^2 + v_y(h)^2} \qquad \theta(h) = \arctan\left(\frac{v_y(h)}{v_x(h)}\right)$$


```python
In [1]: import math as m

In [2]: v0, q0 = 20, m.radians(50)

In [3]: v0x, v0y = v0 * m.cos(q0), v0 * m.sin(q0)

In [4]: v0x, v0y
Out[4]: (12.855752193730787, 15.32088886237956)

In [5]: g = 9.806

In [6]: h = 10

In [7]: vx, vy = v0x, m.sqrt(v0y**2 - 2 * g * h)

In [8]: vx, vy
Out[8]: (12.855752193730787, 6.213665225403286)

In [9]: v = m.sqrt(vx**2 + vy**2)

In [10]: q = m.atan2(vy, vx)

In [11]: v, m.degrees(q)
Out[11]: (14.278655398881227, 25.79621315114633)
```

### Notes:

- I make liberal use of the "comma trick" to define two related variables on one line. You don't have to.

- Since you can't really use Greek letters in code, I've developed a habit of using `q` or `Q` in place of $\theta$, `w` in place of $\omega$, and `ph` in place of $\phi$. Because I do this regularly, my code is still readable, at least to me. Writing out the names like `theta` isn't a bad idea either. Nor is using descriptive names like `initial_angle` or `angular_freq`.

- **Python's trig functions all work in radians**, but we often use degrees for human interpretability, so converting back and forth is a way of life. Get used to this! A good practice is to make sure all angle variables in your code ALWAYS contain values in radians.

    - If given degrees, don't even store that value; immediately use `math.radians()` to convert to radians and store that in a variable, as I did in line 2.

    - If asked to report a result in degrees, calculate it in radians and use `math.degrees()` as you display it.

    - If you _really_ want to store a value in degrees in a variable, give it a name like `theta_deg` to remind yourself that it's in degrees.

- In line 4, I peeked at the values of the initial velocity components to make sure they seemed plausible. If I'd screwed up something, perhaps by forgetting to convert degrees to radians, I might have noticed it here.

- In line 10, I used the `math` module's `atan2()` function instead of the `atan()` function. It shouldn't really matter in this situation, but you should know about how they differ. [Go read about them in the `math` module documentation.](https://docs.python.org/3/library/math.html#math.atan) TLDR: `atan2` is smarter about figuring out the right quadrant. `atan` can't tell between the first and third quadrants, or between the second and fourth.