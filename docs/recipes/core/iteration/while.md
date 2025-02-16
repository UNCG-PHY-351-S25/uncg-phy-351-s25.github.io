# Repeat While or Until Something Is True

___
## Problem to Solve

> **I want to repeatedly execute a chunk of code while or until some condition is true, however many times that may be.**

___
## Background Knowledge

As the recipe [_Repeat Code a Specific Number of Times_](./for.md) said, Python has two basic ways of iterating over (i.e., repeatedly executing) a chunk of code:

1. Applying the code to every element of an ordered collection ("iterable") of things, or

2. Executing the code over and over as long as some logical condition is true.

This recipe focuses on the second. It's useful for situations like:

- I want to repeat a calculation until the result reaches some threshold value.
- I want to read lines from a datafile until reaching the end of the file.
- I want to simulate a system until it stops changing.

___
## Base Recipe

```python
while <<boolean expression>>:
    # Code to repeat over and over until the expression is False.
```
Notes:

1. Replace `<<boolean expression>>` with an actual expression that evaluates to `True` or `False`. This expression can be:
    - the literal `True` (in which case the loop will run forever) or `False` (in which case it won't run at all), 
    - a variable with a boolean value,
    - a boolean expression like `x < 10` or `r != 0`,
    - a compound expression like `(x < 10) and (y < x)`, or
    - a function call that returns a boolean value.

1. Something that the code block does should affect the boolean expression in some way, such that it eventually evaluates to `False` rather than `True`, or the loop will run forever. (Unless, of course, your goal is to write a program that will run until something external terminates it.)

## Variant A: Pre-Initialization

The `while` loop checks `<<boolean expression>>` at the beginning of each iteration, which means it checks before the first iteration occurs. Sometimes, that's a problem, for example if you want to repeat a chunk of code until its result meets some criterion. Before the first iteration, there isn't any result to check!

Some languages have a `repeat… until` construct to handle this particular situation. Python doesn't, but that's not a bit deal. A good solution is to pre-initialize a variable that the loop will check.

Sometimes, you can just precede the `while` statement with a line that sets a variable calculated in the loop to some arbitrary value that will ensure that the first `<<boolean expression>>` evaluates to `True`. Other times, it's easier or less convoluted to define a _flag_ variable like this:

```python
keep_looping = True
while keep_looping:
    # Some calculation or another…
    keep_looping = <<boolean expression>>
```

If it's more semantically meaningful, you can use a flag variable that becomes `True` when the termination condition occurs:

```python
end_loop = False
while not end_loop:
    # Some calculation or another…
    end_loop = <<boolean expression>>
```

Either way, the `<<boolean expression>>` can now safely refer to variables and values that the code in the loop produces.

Tip: Instead of `condition_met` or `continue_loop`, use a variable name that captures the specific condition: `end_of_data_reached`, `calculation_converged`, `object_moved`, etc.

Another approach is to initialize a variable used in the calculation with a value that you know will make the loop execute for the first time, but will not mess up the calculation. For example, let's say you've got a calculation that produces various values of `x`, and you want to repeat it until `x` exceeds some threshold that you're sure will be positive. This would work:

```python
x = -1
while x <= <<threshold value>>:
    x = <<some calculation>>
```
This will **not** work if the calculation uses the previous value of `x`, or if you cannot specify an initial value that you're sure will always be less than the threshold.

## Variant B: Tracking Two Successive Updates

Commonly, the body of a `while` loop updates the value of some particular variable according to a calculation. Sometimes, that calculation needs to use the variable's previous value to find the new value, like this:

```python
x = <<some initial value>>
while <<boolean expression>>:
    x = <<some calculation involving x>>
```
In the calculation line, the `x` on the right of the assignment operator `=` will be the old value, and the result of the calculation will be assigned to `x` thereafter (i.e., into the next iteration).

If the calculation requires the values of the previous _two_ iterations, you'll have to do a bit more work. Here's one possibility:

```python
x_old = <<some initial value>>
x_new = <<some other initial value>>
while <<boolean expression>>:
    x_old, x_new = x_new, <<some calculation involving x_old and x_new>>
```
What's going on here?

The use of the comma is a clever way to make two assignments happen **simultaneously**:

- The previous value of `x_new` is given to `x_old`, while, simultaneously,
- The previous values of `x_old` and `x_new` are used to calculate the new value of `x_new`.

You could solve this without use of the comma trick, but you'd need to introduce yet another variable, and you'd have to do a fair amount of careful value-passing between them.

___
## Examples

### Example 1: Squares

Consider the series defined by $s_n \equiv 2\,s_{n-1} + 1$ with $s_0 = 1$: ${1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, \ldots}$. Let's write a function that will find the smallest value in the series that exceeds some given integer $N$.

```python
def smallest_s_exceeding(N):
    s = 1
    while s <= N:
        s = 2*s + 1
    return s
```

Simple, no?

Let's hair that up a bit…

### Example 2: Fibonacci Sequence

The Fibonacci sequence is defined as the series of numbers that begins with $\{0, 1\}$, and continuing according to the rule that each number is the sum of the two preceding numbers: $F_n = F_{n-1} + F_{n-2}$. The first few numbers in the sequence are $\{0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, \ldots\}$.

For some obscure reason, let's say we want a function that will find the smallest Fibonacci number that exceeds some given integer $N$.

```python
def smallest_fibonacci_exceeding(N):
    F_old, F_new = 0, 1
    while F_new <= N:
        F_old, F_new = F_new, F_old + F_new
    return F_new
```

Since each Fibonacci number depends on the two previous numbers in the sequence, we used Variant B of the recipe.
___
