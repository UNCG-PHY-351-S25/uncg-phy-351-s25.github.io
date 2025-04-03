# Determine Statistics of a Sequence

___
## Problem to Solve

> **I want to determine some simple statistical measures (like frequency, mean, and standard deviation) of a set of measurements, events, or data, and I don't want to store all of the individual values in memory.**

___
## Background Knowledge

### statistical measures

A common kind of task in physics (and much of science and engineering, even social science) is to characterize the properties of a set of values that have (or at least appear to have) random variability in them. Sometimes, this comes from the inherent uncertainty in measurement. Sometimes, we use deliberate randomness in a simulation to represent variables in a complex system that we can't model deterministically.

_Statistics_ is a vast and complicated subject all in itself, and we'll barely scratch the surface of it. A few ideas and techniques, however, will get you a long way.

Let's say we've got a collection of values — measurements, say — that seem to have random variability. Three questions we might reasonably want to ask are:

1. What is the _frequency_ (i.e, probability) that a particular outcome occurs? (That might mean the frequency of a specific value occurring, or the frequency that the value is above some threshold, or etc.)

    - This is commonly calculated as the number of cases that meet the criterion $n$ divided by the total number of cases $N$, and reported as either a decimal value between 0 and 1 or a percentage:

    $$ f = \frac{n}{N} $$

1. About what midpoint do the values tend to cluster? (Statisticians call this the _central tendency_.) We have more than one way to characterize this, but buy far the common is the _mean_ or _average_:

    $$ \bar{x} = \frac{1}{N} \sum_{i=1}^N x_i $$

1. How broadly or narrowly spread are the values about this midpoint? That is, how much _variability_ do they have? Again, multiple ways of characterizing this exist, but many are based on or related to the _standard deviation_ of the values:

    $$ \text{SD}(x) = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2} $$

Many other statistical measures exist, each with their own applications and virtues.

### calculating on the fly

Most statistical measures, such as the three given above, are defined in a way that assumes you have the entire collection of values available to work with. This often true. When it is, by far the easiest way to calculate them is with library functions such as those in the `statistics` module.

Sometimes, however, it's convenient or necessary to calculate these statistics in a "running" or "on-the-fly" way as you encounter the values one at a time, such that you don't need to store all of the individual values in memory. (If you're analyzing a billion particle collider events, not having to store and read a billion values can _really_ speed things up.)

Not all statistical measures can be calculated in this way, but the three given above can.

#### frequency

This one is easy:

1. As you iterate through your cases, keep a running count of the total number $N$ (unless that's already known), and another running count of the number of cases $n$ that fits the criterion you want a frequency for.

2. At the end, calculate the frequency as the ratio of the two counts: $f = n / N$.

#### mean (average)

This is slightly less obvious. The idea is that as we iterate through the values, we keep track of the average of all cases to date; and as we encounter a new value, we calculate the new average as an appropriately weighted combination of the old average and the new value.

1. Before beginning the iteration, initialize a variable for the "running mean" $\bar{x}$ to zero, and another variable for the case number $i$ to zero.
1. In each step in the iteration, with each new value $x_i$,
    1. Increment the case counter $i \leftarrow i + 1$.
    1. Calculate the difference between this value and the old running mean, $\delta = x_i - \bar{x}$.
    1. Update the running mean as $\bar{x} \leftarrow \bar{x} + \delta / i$.
1. After handling the last case (value), the overall average is the last value of the running mean $\bar{x}$, and the total number of values is the last value of the case counter $i$.

#### standard deviation

This one is even less obvious. The basic idea is to keep a running sum of the _squared differences_ between each value and the running mean at the time that value was encountered, in a way similar to the running sum of the mean, and then to calculate the standard deviation from that running sum after finishing the last iteration.

1. Before beginning the iteration, initialize a variable for the "running mean" $\bar{x}$ to zero, a variable for the "running sum of squared differences" $S$ to zero, and another variable for the case number $i$ to zero.
1. In each step in the iteration, with each new value $x_i$,
    1. Increment the case counter $i \leftarrow i + 1$.
    1. Calculate the difference between this value and the old running mean, $\delta = x_i - \bar{x}$.
    1. Update the running mean as $\bar{x} \leftarrow \bar{x} + \delta / i$.
    1. Update the running sum of squared differences as $S \leftarrow S + (x_i - \bar{x}) \delta$.
1. After handling the last case (value):
    - the overall average is the last value of the running mean $\bar{x}$,
    - the total number of values is the last value of the case counter $i$, and 
    - the standard deviation is $\text{SD}(x) = \sqrt{S / (i - 1)}$.

Note that you can't calculate the standard deviation without calculating the mean.

**Critical detail:** You might wonder (like I initially did) why in step 2.4 we update $S$ with $(x_i - \bar{x}) \delta$ instead of just using $\delta^2$, since we calculated $\delta = x_i - \bar{x}$ in step 2.2. THe reason is that between these two steps, in 2.4, we updated the value of the running mean $\bar{x}$, so in step 2.3 $\delta$ uses the **old** $\bar{x}$ while $(x_i - \bar{x})$ uses the **new** $\bar{x}$.

___
## Recipe: Frequency

Here's the pattern for calculating the probability that a particular outcome occurs:

```python
n_positive = 0
for _ in range(N):
    value = # Get or generate the next value in the data set
    if <<condition>>:
        n_positive += 1
frequency = n_positive / N
```
Replace `<<condition>>` with a boolean expression that returns `True` if `value` meets the criterion you want a frequency for. That might be as simple as `value == target_value`, or `value > threshold`, or something more complex.

## Variant: Iterating Through a Collection

The syntax here might not match how your code actually gets its data values. As you'll see in _Collections_, it's possible to iterate directly over a collection of values. In such a case, the recipe looks like this:

```python
n_positive, N = 0, 0
for value in <<data_collection>>:
    N += 1
    if <<condition>>:
        n_positive += 1
frequency = n_positive / N
```

## Recipe: Mean and Standard Deviation

Here's the pattern for calculating the mean and standard deviation:

```python
from math import sqrt
mean, S = 0, 0
for i in range(1, N + 1):
    value = # Get or generate the next value in the data set
    delta = value - mean
    mean += delta / i
    S += (value - mean) * delta
standard_deviation = sqrt(S / (i - 1))
```

## Variant: Mean and Standard Deviation with Collection

> This is a forward reference, put here for completeness. It uses ideas we won't encounter until a later section, and you can safely ignore it for now.

If want the mean and standard deviation of the values in a _collection_, the recipe looks like this:

```python
from math import sqrt
i, mean, S = 0, 0, 0
for value in <<data_collection>>:
    i += 1
    delta = value - mean
    mean += delta / i
    S += (value - mean) * delta
standard_deviation = math.sqrt(S / (i - 1))
```

There's actually a slightly more "pythonic" way to handle this:

```python
from math import sqrt
mean, S = 0, 0
for i, value in enumerate(<<data_collection>>, 1):
    delta = value - mean
    mean += delta / i
    S += (value - mean) * delta
standard_deviation = sqrt(S / (i - 1))
```
Again, if this `enumerate(...)` stuff is gibberish to you, ignore it for now.

___
