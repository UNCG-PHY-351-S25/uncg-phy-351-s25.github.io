# Recipes for Randomness

Present-day computers are deterministic machines, so nothing they do can be truly random. However, neither is rolling a pair of dice or flipping a coin. The outcome of those is determined by the initial conditions — how the dice are rolled or the coin is flipped — and the environment, but in ways that make the outcome totally unpredictable and **effectively** random. Similarly, computers have algorithm for random number generation that can produce numbers that, for almost any purpose, are effectively random. We call these **pseudorandom numbers**.

In fact, designing algorithms that are as fast as possible, and yet still effectively random even to applications that are extraordinarily sensitive to subtle correlations between successive outcomes, is an important niche in computer science. For additional (purely optional) reading, see <a href="https://en.wikipedia.org/wiki/Pseudorandom_number_generator" target="_blank">Wikipedia's article _Pseudorandom number generator_</a>.

This collection of recipes illustrates ways to achieve common randomness-related goals in physics applications. The recipes are pretty basic, since python's `random` module provides built-in support for nearly all common use cases.

1. [**Generate Random Integers**](integers.md): I want an integer randomly chosen from some range.

1. [**Pick Randomly From a Set of Options**](choices.md): I want to randomly choose one item from a collection of possible choices.

1. [**Shuffle and/or Sample From a Set**](sampling.md): I want to randomly mix a sequence of things and/or randomly choose a subset of them.

1. [**Generate Random Real Numbers**](reals.md): I want a real number (a float) randomly chosen from some range.

1. [**Draw From a Weighted Distribution**](distributions.md): I want a number randomly chosen such that the probability of various outcomes follows a specified probability distribution.

1. [**Reproduce "Random" Results**](seeding.md): I want to be able to reproduce the same sequence of "random" numbers for testing or sharing with others.
