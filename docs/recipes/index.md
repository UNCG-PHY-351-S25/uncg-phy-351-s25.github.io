# Computational Physics Recipes

## What _is_ a computational physics "recipe"?

One of the most difficult aspects of learning to code — for physics, or any other end — is staring at a blank code editor with only a general, high-level of what you want to accomplish, and no clear idea of what code to write to accomplish it. This is the "blank page problem."

_Ever been there? Yeah, me too._

If you've solved similar problems before, then you can probably start by recreating what you did and modifying it. But what if you haven't?

If you can find an example of someone else's solution to a similar problem, you may be able to copy and modify it… Although depending on the complexity of the problem and the transparency or opaqueness of the example, understanding it well enough to know what to modify (and how), without breaking anything, may be be hair-pullingly infuriating.

My solution to this is to offer you a cookbook of "recipes" — starting points that show you how to accomplish various common kinds of coding and computational physics tasks. They are meant to be clear, especially about which bits are essential and which are meant for you to fit to your specific needs. They also include examples, and sometimes variations upon the basic recipe for situations that are similar but differ in some important way.

Some recipes are procedural, describing a sequence of steps for you to follow. Some are syntactic, showing specific python code to accomplish a task. Some are structural, recommending approaches to organizing code in pursuit of your goal.

Often, recipes include key conceptual and/or informational knowledge about python, numerical methods, and the practice of computational physics. Understanding the ideas and knowing the facts is an essential part of using the recipes correctly, flexibly, and successfully.

The recipes in this compendium are organized in the order of the course assignments that accompany them, grouped into "units" or "chapters" or whatever you want to call them:

## Recipes by PHY 351 course unit


- [**Skillset A: Core Python**](core/)

    I use the term _core python_ to mean the standard parts of the python ecosystem: the base python language and the "standard library" of modules that is typically installed along with it. For purposes of this course I'm also including the tool stack we'll use to work with python: _GitHub_ and _git_, _JupyterLab_ and its pieces, and a little of the _Unix_ command-line.

- [**Numerical Methods 1: Finding Roots & Extrema**](num1/)

    Now that we've covered the essentials of python, let's take a break from "learning to code" in order to "learn why to code" — that is, how to use those skillz to do some physics-y stuff.

- [**Skillset B: Scientific Python**](scipy/)

    Here we introduce recipes focused on aspects of python central to numerically-intensive work. These include a deep understanding of how computers handle numbers, working with arrays and matrices of values, creating plots and other data visualizations, and reading to or writing from data files. Along the way, we'll introduce _numpy_ and _matplotlib_, add-ons to the python language that support numerically-focused work.

- [**Numerical Methods 2: Numerical Calculus**](num2/)

    Doing math involves more than solving equations; it often requires taking derivatives and integrating. Computers can do that too! The key involves forgetting most of what you learned in calculus courses, and going back to the initial definitions of "derivative" and "integral"… and then applying a whole lot of numerical cleverness.

- [**Numerical Methods 3: ODE Integration**](num3/)

    Most of the central principles of physics are expressed as differential equations, and — consequently — a great deal of "doing physics" comes down to solving differential equations. In the space of all differential equations that we might reasonably encounter in physical problems, only a tiny sliver can be solved analytically. For the rest, we turn to computational methods. In this chunk, we introduce recipes for solving ordinary differential equations (ODEs) numerically. (Partial differential equations — PDEs — are such a vast topic that we won't be able to address them in this course. _Sorry!_)

- [**Skillset C: Visual Python**](visual/)

    Yeah, "solving" a physics problem and getting a bunch of numbers out – or even a pretty plot — is nice, but there's no substitute for _seeing_ the behavior of your modeled system evolve in realtime. _VPython_ ("visual python") is an add-on toolkit for doing exactly that, and it makes constructing and animating 3D simulations embarrassingly easy.

