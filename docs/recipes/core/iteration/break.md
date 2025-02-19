# Stop Iteration Early

___
## Problem to Solve

> **Sometimes my code needs to stop iterating before a loop has reached its normal end (of the range in `for`, boolean termination condition in `while`).**

___
## Recipe A: Early Termination of a 'for' Loop

If you want a normal `for` loop (of [any variant](./for.md)), but need to stop the loop early if some logical condition `<<logical_condition>>` is met, you can use a `break` statement:

```python
for <<counter variable>> in range(<<usual range arguments>>):
    # Can do stuff here…
    if <<logical_condition>>:
        break
    # Can do more stuff here…
```

### example: repeating until some condition, with a repetition limit

Here's a common use of this recipe: Let's say you're doing a calculation or simulation that involves repeating something until a logical condition is met. Examples:

- an approximation of a transcendental function that terminates when the change from one term to the next is below some threshold; or
- a simulation of a falling object that ends when it reaches the ground.

Normally, you'd use a `while` loop to express this. However, what if you also wanted to impose a maximum number of repetitions so that the calculation couldn't take longer than you're willing to wait, or possibly even forever?

The "obvious" approach might be to define a step-counter variable, increment it every time through the loop, and check it in the `while` loop's condition along with the normal condition, like this:

```python
t, t_max = 0, 1e6
x_max = 100
while (x < x_max and y > 0 and t < t_max):
    x, y = ... # Calculation that updates coordinates.
    t += 1
```

This involves some extra cruft, and gives the repetition limit — a "by the way, just in case" aspect of the code — on the same visual level of importance as the "real" physics or math. And it also gives no indication of why the loop ended.

Here's a better way:

```python
t, t_max = 0, 1e6
x_max = 100
for t in range(int(t_max)):
    x, y = ... # Calculation that updates coordinates.
    if x >= x_max:
        print("Reached the far wall.")
        break
    if y <= 0:
        print("Hit the ground.")
        break
```

___
## Recipe B: Early Termination of a 'while' Loop

The `while` loop can also be terminated early with a `break` statement, rather than "normally" when the condition on the `while` line ceases to be true. This might seem unnecessary, since any "extra" logical condition that can trigger a `break` can also be included in the `while` loop's condition with an `and not ...`. However, including a separate `break` statement might be preferable under a few circumstances:

1. The "extra" logical condition is complex, and you want to keep the `while` loop's condition simple and readable.

1. The "extra" logical condition is for an occasional case, and you don't want it to have the same visual importance as the "normal" condition.

1. The natural place to check the "extra" condition and possibly terminate the loop is in the middle of the loop's body, rather than at the beginning or end.

Here's the recipe:

```python
while <<normal condition>>:
    # Can do stuff here…
    if <<other condition>>:
        break
    # Can do more stuff here…
```

The example following the next recipe illustrates this.

___
## Recipe C: Doing Something Only After Normal Loop Completion

In some situations, you'll want your code to execute something after a loop has completed, but **only** if it ran to its normal completion rather than being terminated early by a `break` statement. Python has an easy (and rather unusual and syntactically confusing) way to do this.

Just like an `if` block, a `for` or `while` block can be followed by an `else` block. However, the meaning is totally different:

- After an `if` block, an `else` block says "do this bit if the `if` condition was false and the `if` block didn't execute.
- After a `for` or `while` block, an `else` block says "do this bit if the loop ran to its normal completion and wasn't terminated by a `break` statement."

Yeah, using the word "else" seems like a weird and non-intuitive choice. My guess is that someone decided to piggyback on the existing keyword, rather than having to introduce a new one like `conclusion`. (But, python has a keyword `finally` that could have been borrowed, so 🤷‍♂️.)

Here's the recipe for a `for` loop:

```python
for <<counter variable>> in range(<<usual range arguments>>):
    # Can do stuff here…
    if <<logical_condition>>:
        break
    # Can do more stuff here…
else:
    # Do this if the loop reached the end of the specified range, but not
    # if it was terminated by `<<logical_condition>>`.
```

And for a `while` loop:

```python
while <<normal condition>>:
    # Can do stuff here…
    if <<other condition>>:
        break
    # Can do more stuff here…
else:
    # Do this only if the loop stopped when `<<normal condition>>` became False,
    # not because `<<other condition>>` became True.
```

Yes, you _could_ accomplish this without the `else`, by using an `if` block after the loop that checks variable values to figure out which condition caused the loop to end. But why would you want to? That just forces you to include redundant logic, and introduces one more place for a bug to occur.

### example: guessing game

Yeah, this one is a bit silly, but it shows the idea.

```python
import random
def guess_the_number(max_value = 10):
    secret_number = random.randint(1, max_value)
    print(f"I'm thinking of a number between 1 and {max_value} inclusive. Can you guess it?")
    print("Enter `0` if you want to give up.")
    guess = int(input("  Your guess: "))
    while guess != secret_number:
        guess = int(input("  Nope! Try again: "))
        if guess == 0:
            print("Too bad. 😢")
            break
    else:
        print("You got it! 🎉")
```

___
## Recipe B: Early Termination of a 'while' Loop

The `while` loop can also be terminated early with a `break` statement, rather than "normally" when the condition on the `while` line ceases to be true. This might seem unnecessary, since any "extra" logical condition that can trigger a `break` can also be included in the `while` loop's condition with an `and not ...`. However, including a separate `break` statement might be preferable under a few circumstances:

1. The "extra" logical condition is complex, and you want to keep the `while` loop's condition simple and readable.

1. The "extra" logical condition is for an occasional case, and you don't want it to have the same visual importance as the "normal" condition.

1. The natural place to check the "extra" condition and possibly terminate the loop is in the middle of the loop's body, rather than at the beginning or end.

Here's the recipe:

```python
while <<normal condition>>:
    # Can do stuff here…
    if <<other condition>>:
        break
    # Can do more stuff here…
```

The example following the next recipe illustrates this.

___
## Recipe D: Skipping to the Next Iteration

Occasionally, you'll come across a situation where a loop should skip over the remainder of one iteration and start the next one. You can accomplish this by putting the part that you might need to skip over into the body of an `if` block, but there's a cleaner way: the `continue` statement. It can be used in either a `for` or a `while` loop.

```python
for <<counter variable>> in range(<<usual range arguments>>):
    # Can do stuff here…
    if <<skip condition>>:
        continue
    # Put code here that should only run if the skip condition is False.
```

```python
while <condition to continue>>:
    # Can do stuff here…
    if <<skip condition>>:
        continue
    # Put code here that should only run if the skip condition is False.
```

Without `continue`, this would look like:

```python
for <<counter variable>> in range(<<usual range arguments>>):
    # Can do stuff here…
    if not <<skip condition>>:
        # Put code here that should only run if the skip condition is False.
```

What are the advantages of using `continue`?

1. Readability: The code very clearly says "My intention is to skip ove the rest of the loop body if this condition is met."

1. Flatness: It avoids nesting the rest of the code one level deeper. If that code is fairly complex, with its own conditional logic and loops and other nested bits, every level of nesting you can avoid is a win.

___
