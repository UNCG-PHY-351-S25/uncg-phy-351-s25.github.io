# Arithmetic Operators

## the binary operators

Knowing your python **arithmetic operators** is essential. Here are python's relevant _binary operators_. ("Binary" means that they act on two quantities by being placed between them.)

**Addition: `+`**
> Just like standard mathematical notation. Implement "$3+4$" as `3 + 4`.

**Subtraction: `-`**
> Also just like standard mathematical notation. Implement "$3-4$" as `3 - 4`.

**Multiplication: `*`**
> NOT like standard mathematical notation. Python uses the asterisk character instead of the "times" sign, and does not recognize implicit multiplication when two quantities are side-by-side. Implement "$3 \times 4$" as `3 * 4`, and "$2x$" as `2 * x`.

> In python, `2a` is an illegal variable name (because it begins with a digit), and `2 a` is just invalid syntax in most contexts.

**Division: `/`**
> Like _some_ standard mathematical notation. Implement "$3 \div 4$" as `3 / 4`. 

> The numerator and denominator go on the left and right. Python has no way to arrange them vertically, as in "$\frac{3}{4}$". That means you can't put a compound expression like "$1 + x$" in the numerator or denominator without using parentheses to group it. (We'll discuss this more thoroughly in [_Operator Precedence_](precedence.md).)

**Exponentiation: `**`**
> NOT like standard mathematical notation OR most other programming languages OR scientific calculators OR just about anything else!
> Implement "$3^4$" like this: `3**4`.

> By the way, do _NOT_ use the exponentiation operator for scientific notation. A numeric literal like $2.99 \times 10^8$ should be entered as `2.99e8`, not as `2.99 * 10**8`. Why? Because python can interpret the first form directly as a floating-point number, with no arithmetic calculations needed. If you use the second form, python has to do two two floating-point calculations — exponentiation and multiplication. Both take processor time, and both introduce a tiny bit of round-off error. While the impact is tiny, it can really add up within a big loop or matrix. (Also, the first form is way more compact and generally easier to read.)

> **_Beware the up-carat!_**
> A very very _VERY_ common error among physics students (and instructors too 😬) is to use an up-carat `^`, as in `3^4`, instead of the double-asterisk — simply because it's such a habit from non-python work.

> Unfortunately, if you make this mistake in python, you won't get an error message or any other clear sign that you did something wrong, because **the up-carat IS a legitimate arithmetic operator in python!** It just doesn't do what you think it should. It does "bitwise exclusive or", an obscure binary-logic operation you'll probably never need.

> So if you accidentally use `^` instead of `**`, your calculation or program will probably run without errors. You'll either pull your hair out trying to figure out why its results are wacky, or — worse — be blithely ignorant that they're totally wrong.

> _You have been warned._ 👀

**Modulo `%`**
> (Also called the _modulus_ operator.) `x % y` yields the **remainder** when $x$ is divided by $y$. For example, `7 % 3` yields `1`, and `7.5 % 3` yields `1.5`.

**Floor Division `//`**
> This is complementary to modulo. `x % y` yields the integer number of times that $y$ divides into $x$ — in other words, the integer part of $x \div y$, discarding the remainder.

> You can be confident that you understand these operators when it's obvious to you why `(x // y) * y + x % y` always evaluates to the same value as `x / y`.

> _Modulo_ and _floor division_ don't show up much in physics, but they can be surprisingly useful in simplifying the logic of a program. For example, if you're iterating over $N$ things in groups of $m$ at a time, `N // m` is the number of full-sized groups you'll process and `N % m` is the number "left over" for a final, undersized group.

___
## the unary operator

_Unary_ operators act on a single quantity. Python only has two you're likely to need (unless you get into bitwise binary logic), and only one is meant for numeric calculations. (We'll meet the other one in an upcoming encounter with _Boolean Logic_.)

**Negation: `-`**
> Sticking a minus sign in front of a numerical quantity flips its sign, from positive to negative or negative to positive, exactly as you would expect. `-3 + 4` will evaluate to `1`, and `-(2 - 5)` to `3`.

> How does python know whether to interpret `-` as a binary subtraction operator or a unary negation operator? I can't think of an expression in which both interpretations of a particular `-` are syntactically legal.

___
## the assignment operators

It's fairly common in coding to want to set a variable's value to "its current value plus $k$" or "its current value minus $k$ or "$n$ times its current value" or "one-$n^\text{th}$ of its current value", or something like that. The point is that you want to change the value of a variable to be the result of a simple algebraic expression involving its current value.

This is easy enough to do with the algebraic operators above: `x = x + k`, `x = x - k`, `x = x * n`, `x = x / n`, etc. However, because this is so common, python offers you some shortcuts that are slightly more compact, and definitely quicker for a human reader to digest: the **assignment operators**.

| shortcut | is equivalent to |   | shortcut | is equivalent to |
| -------- | ---------------- | - | -------- | ---------------- |
| a += b   | a = a + b        |   | a **= b  | a = a**b         |
| a -= b   | a = a - b        |   | a %= b   | a = a % b        |
| a *= b   | a = a * b        |   | a //= b  | a = a // b       |
| a /= b   | a = a / b        |

___
## the importance of whitespace

The python interpreter doesn't care whether you put space characters around your operators or not. As far as it is concerned,

* `m=32/-2`, `m = 32 / - 2`, `m = 32/- 2`, `m = 32/ - 2`, `m=32 / -2`, and `m = 32 / -2`

are all entirely equivalent. However… **which is easiest for a human to interpret at a glance?**

That is NOT a small consideration! 

> **Important: Strive to make your code, and especially your numerical calculations, as clear and easy-to-read as possible.**

Adopting this habit will drastically reduce the likelihood that your calculations will contain unintended errors, and will make it easier for you to find errors when you're debugging. It will also reduce the cognitive burden on someone reading the code to figure out what it does. (That someone might very well be you, in the future, trying to remember WTH you were thinking when you wrote it.)

As a general rule: Unless you have a very specific reason to do otherwise, 

1. **Put one space character on either side of a binary operator.** That makes it easier to distinguish the operators from their operands.
2. **Exception: Don't put spaces around (`**`) for exponentiation.** That helps a reader quickly distinguish it from multiplication. And, as you'll see soon in _operator precedence_, it better communicates the order in which the operations will occur.
3. **Don't put a space between a unary minus and the value it's negating.** That makes clear it's a sign flip, not a subtraction.
4. **Put a space on either side of an assignment operator,** whether that be normal assignment with `=` or one of the shortcut operators like `+=`. That makes it easier to visually distinguish the expression to evaluate from the variable it's assigned to.
   - (The "walrus operator" is a bit of a special case, because it usually needs parentheses to have the intended effect. More on this later.)

Remember, space characters don't cost you anything and don't run out. You don't get bonus points for making your code as dense as possible. Quite the contrary — readability _does_ count!
___
