# Physics 351 Spring 2025 Course Syllabus

Welcome to PHY 351, **_Introduction to Computational Physics_**!

Computers have become essential in all aspects of physics. That shouldn't surprise you, because they've become essential in almost all aspects of almost anything; even my toothbrush has a tiny computer in it. Let's zoom in on one key function of computers in physics: **_they can do math for us._**

- In **experimental physics**, computers can analyze huge quantities of data in extraordinarily sophisticated ways (in addition to controlling the apparatus and collecting the data).
- In **theoretical physics**, they can perform calculations and solve equations that would be difficult, or perhaps even impossible, with analytic ("paper-and-pencil") methods alone.
- And they've created a third branch of physics, **computational physics**, in which we use direct computer simulation of physical systems (rather than physical experiments or analytic modeling) to explore their behavior and develop understanding.

Much of the software to do such things is custom-written by physicists, using specialized coding tools and approaches. Skill with these tools and approaches is a scientific superpower that will pay off over and over, whether you stay in physics or take your skills to something else.

The purpose of this course is to show you the foundational tools and methods of computational physics, and to start your journey along the path from beginner to fluent to expert.

___
## Administrivia

### Catalog information

* **Credits:** 3 (3:3:0 = 150 min/wk in class + 6-ish hrs/wk outside class for a “typical” course).
* **Course format:** Face-to-face synchronous on-campus (but see below).
* **Prerequisites:** Grade of C or better in both PHY 292 and CSC 120, or permission of instructor.
* **Corequisites:** PHY 321, or permission of instructor. Corequisite need not be taken concurrently; prior completion is adequate.
* **For whom planned:** This course is designed for Physics majors, and is required for the Physics BS and BA degrees.
* **Bulletin description:** Introduction to computational methods used in physics and engineering, including computational simulation of physical systems, numerical solution of mathematical problems, and familiarity with scientific programming tools.

### Instructor information

**Instructor:** Associate Prof. Ian D. Beatty (he, him, his)
* **Email:** idbeatty@uncg.edu
* **Office:** Petty 328
* **Phone:** 336.256.1279 (goes to MS Teams so 🤷‍♂️)
* **Physics & Astro Slack:** @Beatty
* **Twitter**: *Nope. So done with that.*

**Office Hours:** To be announced — once I find out what days & times work best for y’all. In the meantime, ask me when you can drop by, or make an appointment. Office hours are in person (Petty 328) or via MS Teams (with prior notice so I can start it up), as you prefer. Connection details are on the course *Canvas* site.

### Communication

*Slack* is generally the fastest way to reach me. (Details are on *Canvas*.) Email is safer for something that must not fall through the cracks, but you may have to wait a few hours or even until the next day. Please do not assume you can reliably get my attention during evenings or weekends, as family responsibilities dominate those.

I will occasionally need to reach you, personally or collectively, about important course changes, reminders, or issues. It is essential that you receive and actually read messages I send to your UNCG email address, either directly or via *Canvas* course announcements. Please configure your *Canvas* notification settings, email filters, and personal habits accordingly.

___
## Course Objectives

### Overall Goal

Consider learning a foreign language: Knowing the meaning of a collection of words is marginally useful if you're trying to communicate with someone. Being _fluent_ is orders of magnitude more useful, and lets you communicate things that are orders of magnitude more complex.

One part of "fluency" is having practiced the translation of words often enough that it becomes automatic in your head, so you don't have to think about it. Another part is knowing a toolkit of _idioms_ and other common language patterns for accomplishing specific communication goals. Knowing an idiom or pattern for a particular idea means I don't have to figure out how to piece words together to communicate it; that problem is already solved. I just reiterate the pattern, tweaking it as appropriate for the situation at hand.

This course is organized around the idea that much of the challenge of becoming "fluent" with scientific coding is assembling a mental library of common idioms and patterns — known ways to arrange chunks of code to accomplish specific kinds of tasks. We'll call them **_recipes_**. Some are one-liners, some are patterns spread over many lines of code or even an entire program, and some are just sequences of steps to follow. All have the same purpose: Faced with a computational task, knowing a recipe for it means you don't have to stare at the screen and wonder how to start.

The "course content" is a collection of recipes for you to learn. They are organized on a website, for convenient access. We have no textbook or other reading material, except for miscellaneous online reference materials to supplement the recipes.

### Learning Objectives

By learning what the recipes accomplish and how to apply them, you will achieve the course learning outcomes:

- Be able to use the "scientific python stack" to perform interactive calculations, write programs, run programs, and work with data. This "stack" includes the core python language; scientific python libraries (specifically _numpy_, _matplotlib_, and _scipy_); git and _GitHub_; and the _JupyterLab_ environment and its tools.

- Be able to construct and customize publication-quality data plots, including features like error bars and best-fit lines.

- Understand and computer representations of numbers and their implications for accuracy and efficiency.

- Know and be able to apply some foundational "numerical methods" for doing math computationally, including solving nonlinear equations, finding the maxima and minima of functions, calculating derivatives and integrals, and solving ordinary differential equations.

- Be able to create animated three-dimensional visual simulations of physical systems.

___
## Course Content and Organization

The course will present you with a large number of computational physics _recipes_, asking you to practice applying them to ever-more-complex problems. Using the metaphor of videogame progression, the recipes are grouped into "levels", which are grouped into five "worlds". A tentative outline of the worlds and their levels (subject to change as we go) is:

- **World A: Core Python**
    - Level 01: Workflow
    - Level 02: Calculation
    - Level 03: Custom Functions
    - Level 04: Iteration
    - Level 05: Tuples & Lists
    - Level 06: Sets & Dictionaries

- **World B: Numerical Methods for Solving**
    - Level 01: Solving Nonlinear Equations
    - Level 02: Finding Maxima & Minima

- **World C: Scientific Python**
    - Level 01: Machine Arithmetic
    - Level 02: Arrays
    - Level 03: 2D (y vs. x) Plotting
    - Level 04: Histograms
    - Level 05: Reading & Writing Files

- **World D: Numerical Methods for Calculus**
    - Level 01: Pseudorandomness
    - Level 02: Numerical Differentiation
    - Level 03: Numerical Integration

- **World E: Visual Python for Simulation**
    - (Levels TBD)

- **World F: Numerical Methods for ODE Integration**
    - (Levels TBD)

___
## Learning Activity and Course Assignments

### Philosophy and Approach

I started programming in seventh grade, when I went to junior high school, met friends who had Apple II computers, and encountered BASIC. It rocked my world, magnitude 9.5. Since then I've written functional, useful code in at least a dozen different programming languages, and dabbled with a dozen more. During that entire time I've taken precisely one programming course, in high school. Almost everything I've learned about coding and computer use has been self-taught.

I firmly believe that one learns coding by doing it, not by reading about it or listening to someone explain it. Learning to program, and writing programs, and getting better at it is endless problem-solving, problem after problem after problem. You can embrace the struggle and enjoy the puzzles, or… 

Consequently, this course consists almost entirely of you working your way through a carefully-orchestrated sequence of computational physics challenges. I won't be lecturing or assigning readings. I've tried to give you enough initial orientation to each challenge and enough supporting reference material that you'll have a pretty good idea how to proceed. You will get stuck on things and encounter moments of confusion. That's not just normal, it's desirable: because the flash of insight or key bit of information that gets you unstuck and unconfused is where the most important learning happens?

However, you are NOT meant to struggle through this alone and potentially frustrated. One part of my role in the course is to create the structure and scaffolding for you to work through. Another is to be available to help you when, where, and how you need: to answer a question, to suggest a better approach, to inform you of a key language feature you are unaware of, to help you find a bug, to interpret a mysterious error message, and so on. This is way more efficient for both of us and effective for you than if I tried to pre-warn you of everything you might struggle with and everything you might need to know.

You are also welcome to support each other, as comrades in arms, as long as you mind the bright line between "getting help" and "plagiarizing". Here's the boundary: **any work you submit must be your own and represent your own understanding.** You can discuss solutions with other students and even scribble things on a communal whiteboard, but you should then **write up your solutions by yourself, starting from an empty page.** If you can’t do that, you don’t really understand it, and it’s dishonest to pretend that you do.

### Assignments

As described above, the course content for you to learn is represented as as compendium of "recipes", which are grouped into "levels" that are bundled into "worlds". These recipes are all described in detail on the course reference website. The description of (almost) each includes at least one example of how it can be applied in a physics context.

Accompanying this compendium is a parallel collection of assignments for you to work through. You'll access them via GitHub, work on them on a course server (Prof. Beatty's beast of a computational workstation), and submit them through GitHub. Each recipe has a corresponding _exercise_, which is a (hopefully) straightforward application of the recipe to a physics problem or situation. Completing this exercise should help transform the recipe from something you "know about" to something you "do".

The exercises are grouped into levels exactly as their corresponding recipes are. Most of the levels conclude with a _miniboss_, a somewhat more complex physics-type challenge that requires you to combine several of the level's recipes. My intention here is to help you develop the skill of seeing when and how to apply the recipes.

The levels are also grouped into worlds, and each world concludes with a _big boss_ challenge: A considerably more complex, authentic computational physics problem. In addition to identifying and applying the various recipes, you'll need to manage greater complexity and make important judgment calls about how to approach it.

These exercises, minibosses, and big bosses are the only required work in the course. It has no quizzes, exams, attendance requirements, papers, or other such things. Learn by doing, and prove you've learned by having done.

___
## Grading and Grades

### Assignment Grading

Exercises and minibosses are graded on an entirely all-or-nothing basis: Either they meet all the assignment specifications and are accepted, or they do not and are rejected. Fortunately, rejected just means "not accepted yet". You can fix and resubmit them as often as necessary until they meet all the specs and are accepted.

You will progress much faster, and experience much less frustration, if you can figure out whether your solution meets ALL the specs BEFORE submitting it. (You'll also make my life a whole lot saner.) To help with that, each assignment comes packaged with some automated tests that you can run to check your solution. The test code won't catch absolutely everything, but should catch most errors and oversights. (It is still your responsibility to **carefully and thoroughly** read the assignment specs and verify that you've met them all.)

The grading of the big bosses is a bit more nuanced, in part because they're more complex, and allow more room for your judgment and discretion, and require some written explanation. Each assignment will lay out its grading criteria in as much specificity as I can manage.

### Course Grades

For this course, grades work videogame-style. Each exercise, miniboss, and big boss is worth a specified number of points. When you submit your work for one and that work is accepted, you earn all the corresponding points, and your course point total increases. (It's possible to earn somewhat more or less for a big boss, as just stated.)

- Exercise:  10 points — TENTATIVE
- Miniboss:  50 points — TENTATIVE
- Big boss: 200 points — TENTATIVE

You begin the course as a _rank 0_ computational physicist, and "level up" every time your course point total reaches the threshold for the next rank.

> INSERT POINTS-PER-RANK TABLE HERE

Ranks are associated with course grades, so increasing in rank increases your final course grade (although not for every rank).

> INSERT RANK-TO-GRADE TABLE HERE

Note that the course has no mechanism by which you can lose points, and therefore no way for your rank to decrease.The implication is that once you've earned enough points for a course grade of "C", say, that's the lowest grade you can possibly earn _no matter what happens for the remainder of the course_ (short of some kind of academic integrity violation, of course). So, instead of looking at big assignments and exams as hazards you can screw up to trash your grade, view them as opportunities to climb ever higher!

### Due Dates

The course is entirely self-paced. The only deadlines are those I'm imposing so that I have time to process submissions on my end (while remaining sane) and tabulate course grades before the University-imposed deadline for grade submission:

> STATE FINAL SUBMISSION DEADLINES HERE

Take note: **I am giving you a whole lot of rope to hang yourself with.** If you fail to pace yourself and make sufficient progress right from the start of the course, you will be in a whole world of hurt when the end of the semester hurtles towards you.

- Later assignments are harder. Big bosses take longer than minibosses, which take longer than exercises.
- Your other courses will likely get busier towards the end of the semester, leaving you less time for this one.
- When you start feeling the panic of the end-of-term approaching, you'll shift from a mindset of "take the time to figure this stuff out and show it" to "frantically try different things hoping to make the damn tests pass". The latter is generally LESS efficient, and definitely produces less actual learning.
- I will undoubtedly get quite busy with late-semester submissions, leaving me less time to help you when you're stuck.
- One danger of last-minute submissions is that I may very well find something amiss with your work and kick it back to you for corrections. You may not have time to make them. If I'm buried in last-minute submissions, I may not even have time to check yours before the deadline.

_You have been warned._

___
## Policies

### Attendance Policy

Given what you've read so far, you might be wondering what the purpose of class meetings is, and whether you need bother attending. Good question!

The first class or two will be important to get you up and running with our workflow: the various accounts, login identities, and tools you'll need to "do work" in this course. After that, class time is really nothing other than a place and time for you to work with me (and other students) close at hand to answer questions and help you get unstuck. Don't underestimate the value of instantaneous on-call support.

We may, collectively, agree to move class to a more convenient venue in Petty.

If nobody shows up for the start of class on any particular day, I may, after a few minutes, go back to my office. You can still find me there. Either way, I will be "on call" for you between 2:00 and 3:15 every Monday and Wednesday afternoon.[^1]

[^1]: _As of the time I'm writing this, I have a serious health issue that is likely to affect some of the details of my availability during the Spring 2025 semester, but in ways I don't yet know. I'll keep you posted as I learn more._


### Late Work Policy

You saw the part above about "no deadlines except for the final end-of-term submission deadlines", right? Late work is a non-issue in this course.

That being said: **Do not ask me for an "incomplete" simply because you haven't quite finished everything you wanted to by the deadlines.** According to the UNCG Catalog, a grade of _incomplete_ "indicates that the completion of some part of the work for the course has been deferred because of prolonged illness of the student or because of some serious circumstances beyond the student’s control."


### Accommodations

UNCG seeks to comply fully with the *Americans with Disabilities Act* (ADA). Students requesting accommodations based on a disability must be registered with the Office of Accessibility Resources and Services (OARS, 215 Elliott University Center, 336.334.5440, [http://oars.uncg.edu](http://oars.uncg.edu)).

### Academic Integrity Policy

You are, of course, expected to know and heed the University’s _Academic Integrity Policy_. Violations will be reported to the Dean of Students. A second violation at any time during your years as a student here leads to automatic suspension or expulsion, so this is serious stuff.

* [https://osrr.uncg.edu/academic-integrity-policy-pledge/](https://osrr.uncg.edu/academic-integrity-policy-pledge/)

As stated above, I encourage you to help each other and to work together to figure things out, but **any work you submit must be your own and represent your own understanding.** If at any time you are in doubt about where to draw the line between collaboration and plagiarism, ask me to clarify.

My experience is that the Physics majors who take this course are ethical and conscientious students who genuinely want to learn the topic and not just cheat their way to an undeserved grade. However, even usually-trustworthy students can make bad choices when they get overwhelmed and desperate. Recognize the temptation and ask me for help! Even better, don’t let yourself fall behind to the point that you might be so tempted. And don’t lend your solutions to another student, even to “just learn from, not copy.” That rarely ends well for anyone.

Code is inevitably idiosyncratic. Everyone's looks a little different in myriad ways that are really hard to fake, and I notice uncanny similarities even without looking for them. Don't take the chance.

Seriously, don’t jeopardize your reputation. Trust is easy to lose and very, very hard to regain.
___

_Version 1.0, 2024-12-29_