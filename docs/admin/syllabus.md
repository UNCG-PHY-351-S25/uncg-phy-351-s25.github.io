# Physics 351 Spring 2025 Course Syllabus

_Version 1.1, 2025-01-16_
___

Welcome to PHY 351, **_Introduction to Computational Physics_**!

Computers have become essential in all aspects of physics. That shouldn't surprise you, because they've become essential in almost all aspects of almost anything; even my toothbrush has a tiny computer in it, and I didn't even get the version that talks to an iPhone app 😦.

Let's zoom in on a key function of computers in physics: **_they can do math for us._**

- In **experimental physics**, computers can analyze huge quantities of data in extraordinarily sophisticated ways (in addition to controlling the apparatus and collecting the data).
- In **theoretical physics**, they can perform calculations and solve equations that would be difficult or even impossible with analytic ("paper-and-pencil") methods alone.
- They've also created a third branch of physics, **computational physics**, in which we use direct computer simulation of physical systems (rather than physical experiments or analytic modeling) to explore their behavior and develop understanding.

Much of the software to do such things is custom-written by physicists, using specialized coding tools and approaches. **Skill with these tools and approaches is a scientific superpower** that will pay off over and over, whether you stay in physics or take your skills to something else — like, for example, epidemiology, computational immunology, or financial modeling.

The purpose of this course is to show you the foundational tools and methods of computational physics, and to start your journey along the path from beginner → fluent → expert.

___
## Administrivia

### Catalog information

* **Credits:** 3 (3:3:0 ⇒ 150 min/wk in class + 6-ish hrs/wk outside class for a “typical” course).
* **Course format:** Face-to-face synchronous on-campus, technically (but not really, see below).
* **Prerequisites:** Grade of C or better in both PHY 292 and CSC 120, or permission of instructor.
* **Corequisites:** PHY 321, or permission of instructor. Corequisite need not be taken concurrently; prior completion is adequate.
* **For whom planned:** This course is designed for Physics majors, and is required for the Physics BS and BA degrees.
* **Bulletin description:** Introduction to computational methods used in physics and engineering, including computational simulation of physical systems, numerical solution of mathematical problems, and familiarity with scientific programming tools.

### Instructor information


**Instructor:** Associate Prof. Ian D. Beatty (he, him, his)

- **Email:** [idbeatty@uncg.edu](mailto:idbeatty@uncg.edu)
- **Office:** Petty 328
- **Phone:** 336.256.1279 (goes to MS Teams, not my actual phone, so 🤷‍♂️)
- **Physics & Astro Slack:** `@Beatty`
- **<s>Twitter</s>**: *Nope. So done with that. Instead,* **Bluesky**: `@ianbeatty.com`

**Office Hours:** To be announced — once I find out what days & times work best for y’all. In the meantime, ask me when you can drop by, or make an appointment. Office hours are in person (Petty 328) or via MS Teams (with prior notice so I can start it up), as you prefer. Connection details are on the course *Canvas* site.

### Communication

*Slack* is generally the fastest way to reach me. (Details are on *Canvas*.) Email is safer for something that must not fall through the cracks, but you may have to wait a few hours or even until the next day. I try to be responsive during off-hours, especially to things that might prevent you from working productively, but please do not assume you can reliably get my attention during evenings or weekends. I have three kids and an under-maintained house that need my attention too.

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

- Be able to construct and customize publication-quality data plots, with features like error bars and best-fit lines.

- Understand computer representations of numbers and their implications for accuracy and efficiency.

- Be able to create animated three-dimensional visual simulations of physical systems.

- Know and be able to apply some foundational "numerical methods" for doing math computationally, including solving nonlinear equations, finding the maxima and minima of functions, calculating derivatives and integrals, and solving ordinary differential equations.

### Philosophy and Instructional Approach

I started programming in seventh grade when I went to junior high school, met friends who had _Apple II_ computers, and encountered BASIC. It rocked my world, magnitude 9.5. Since then I've written functional, useful code in at least a dozen different programming languages, and dabbled with a dozen more. During that entire time I've taken precisely one programming course, in high school. Almost everything I've learned about coding and computer use has been self-taught.

I firmly believe that one learns coding by _doing_ it, not by reading about it or listening to someone explain it. Learning to program, and writing programs, and getting better at it is **endless problem-solving**, problem after problem after problem. You can embrace the struggle and enjoy the puzzles, or… 😵

Consequently, this course consists almost entirely of you working your way through a carefully-orchestrated sequence of computational physics challenges. I won't be lecturing or assigning readings. I've tried to give you enough initial orientation to each challenge and enough supporting reference material that you'll have a pretty good idea how to proceed. **You will get stuck on things** and encounter moments of confusion and, yes, frustration. That's not only normal, it's desirable: because **that flash of insight or key bit of information that gets you unstuck and unconfused is where the most important learning happens.**

However, you are NOT meant to struggle through this alone and intolerably frustrated. One part of my role in the course is to create the structure and scaffolding for you to work through. Another is to be available to help you when, where, and how you need: to answer a question, to suggest a better approach, to inform you of a key language feature you are unaware of, to help you find a bug, to interpret a mysterious error message, and so on. This is way more efficient for both of us, and way more effective for you than, if I tried to pre-warn you of everything you might struggle with and everything you might need to know.

You are also welcome to support each other, as-comrades-in-arms, as long as you mind the boundary between "getting help" and "plagiarizing". For specifics on that boundary, see the _Academic Integrity Policy_ section below. And, I'll be showing you some ways that you can leverage AI tools to help you faster and better; see the _Artificial Intelligence Policy_ section below.

___
## Textbook and Technology

### Course "Textbook"

This course has no textbook. _Why?_ I'm glad you asked…

One of the most difficult aspects of learning to code — for physics, or any other purpose — is staring at a blank code editor with only a general, fuzzy idea of what you want to accomplish, and no clear idea of what code to write to accomplish it. This is the coder's version of the writer's "blank page problem".

_Ever been there? Yeah, me too._

If you've solved similar coding problems before, then you can probably start by recreating what you did and modifying it. But what if you haven't?

If you can find an example of someone else's solution to a similar problem, you may be able to copy and modify it… though depending on the complexity of the problem and the transparency or opaqueness of the example, understanding it well enough to know what to modify (and how), without breaking anything, may be be hair-pullingly infuriating.

My solution to this is to offer you a cookbook of "recipes" — starting points that show you how to accomplish various common kinds of coding and computational physics tasks. They are meant to be clear, especially about which bits are essential and which are meant for you to fit to your specific needs. They also include examples, and sometimes variations upon the basic recipe for situations that are similar but differ in some important way.

Some recipes are procedural, describing a sequence of steps for you to follow. Some are syntactic, showing specific python code to accomplish a task. Some are structural, recommending approaches to organizing code in pursuit of your goal.

Often, recipes include key conceptual and/or informational knowledge about python, numerical methods, and the practice of computational physics. Understanding the ideas and knowing the facts is an essential part of using the recipes correctly, flexibly, and successfully.

The collection of recipes is available to you on a website linked to from Canvas.

### Technology

Our course _Canvas_ site will serve as (a) a place to put general information such as my contact info, (b) a place for announcements, and (c) a place to keep track of the assignments you've completed.

We'll use the _GitHub_ website to distribute assignments to you and for you to submit your completed work bac, to me. (Don't worry, walking you through the setup and process for this is all in World A, Level 1.)

You'll do your actual coding-and-running on _Beskar_, the name I've given to the 48-core, 384-GB beast of a computational physics server that sits on my desk. You'll connect to it from wherever you want via web browser, so you don't need to worry about installing anything on your own computer, or whether your decrepit old laptop can manage.

Outside of class, the best way for us to communicate outside of class time is via _Slack_. Details are on Canvas. You are, of course, welcome to drop in on me during my open-office hours (listed on Canvas), or to make an appointment if that works better. It's really helpful for me to be able to send the occasional short, all-class announcement via Slack, so I really hope we can get everyone on board.

___
## Assignments, Grading, and Grades

To understand the structure of this course, don't look to other courses you've taken… Look to video games! 🕹️

### Organization

Content material of the course, and the assignments accompanying it, is divided into five _Worlds_:

- World A: Core Python

- World B: Numerical Solving, Finding & Randomness

- World C: Scientific Python

- World D: Numerical Calculus

- World E: Visual Python for Simulation

Each world is divided into several (~3-9) _Levels_. That's too many to list here, so you can find them in the Modules section on Canvas. (Warning: That's a work in progress. Levels for the first worlds will appear soon/already; later ones will appear… later. We're building this airplane as we fly! 😬)

Just like a videogame level has a sequence of challenges followed by a level boss, a course "level" has a sequence of exercises followed by what I'm calling a _miniboss_. Each exercise targets one particular computational physics _recipe_. (See below; for now, think of that as one skill or idea.) The miniboss is a somewhat more complex challenge that requires you to combine several of the level's recipes.

In addition to its levels, each world ends with a _superboss_ challenge: A considerably more complex, authentic computational physics investigation. In addition to identifying and applying the various recipes, you'll need to manage greater complexity and make important judgment calls about how to approach it. You'll also need to write up a bit of an "investigation report" documenting what your investigation revealed.

The whole course is kicked off by a brief _Intro_ with a couple of super-easy warm-up levels, and ended by an _Outro_ that's really just a final reflection assignment.

This set of levels (exercises and miniboss), superbosses, and the intro/outro bits are the only required work in the course. It has no quizzes, exams, attendance requirements, papers, or other such things. 🥳 Learn by doing, and prove it by having done. 

### Assignment Grading

Let's call a level, superboss, or intro/outro level-type thing an "assignment". 

**Every assignment is graded on an entirely all-or-nothing basis: Either it meets all the assignment specifications and is accepted, or it does not and is rejected.** (Video game analogy: Either you make it through the level, or you die.)

Fortunately, rejected just means "not accepted yet". You can fix and resubmit an assignment as often as necessary to meet all the specs and be accepted. (Analogy: If you die, you start the level over.)

You will progress much faster, and experience much less frustration, if you can figure out whether your solution meets ALL the specs BEFORE submitting it. (You'll also keep me sane.) To help with that, most assignments come packaged with a battery of automated tests that will check your solution. You <s>can</s> MUST run and pass this before submitting it to me for verification. The test code won't catch absolutely everything, but should catch most errors and oversights. If we both do our jobs well, all I have to do is rubber-stamp your submission; you can already be confident that it will pass. (Analogy: When you screw up in a video game, you discover it immediately and usually dramatically.)

### Course Grades

You begin the course as a _Rank 0_ computational physicist. **Every time you successfully complete an assignment (level or superboss), you _level up_ one rank.** Simple, no? 

**Ranks correspond to course grades**. The higher your rank at the end of the course, the higher your final grade. The final rank-to-grade table is not yet finalized, since I haven't yet nailed down exactly what all the levels will be, and (more seriously) I am unsure how realistic my plan is. Here's a tentative version:

|   grade:   | A  | A– | B+ | B  | B– | C+ | C  | C– | D+ | D  | D– | F  |
|------------|----|----|----|----|----|----|----|----|----|----|----|----|
| **rank:**  | 27 | 25 | 24 | 22 | 21 | 20 | 18 | 17 | 15 | 14 | 13 | 0  |

Note that your rank can never decrease (barring some kind of academic integrity or course administration disaster). The implication is that **once you've levelled up to a certain grade, that's the lowest grade you can possibly earn _no matter what happens for the remainder of the semester_.** So relax! The only way to shoot yourself in the foot is to proceed too slowly. 

### Due Dates

Let me reiterate that: The only way to shoot yourself in the foot is to proceed too slowly.

The course is entirely self-paced. The only deadline is the end-of-term one I'm imposing so that I have time to process the last batch of submissions and enter course grades before the University-imposed deadline for grade submission.

> <big>**Only work that meets all assignment specifications and is submitted by <u>the end of the day (midnight) on Wednesday March 07</u> will count for course credit.**</big>

Take note: **I am giving you a whole lot of rope to hang yourself with.** If you fail to set a good pace right from the start of the course, you will be in a whole world of hurt when the end of the semester hurtles towards you.

$$ \frac{d}{dt}\left(\text{successful level completion}\right) \approx \frac{\text{desired grade}}{\text{remaining time}} $$

Note that as the remaining time decreases, the rate at which you must pass levels limits to infinity. And remember:

- Later assignments are harder. Superbosses take longer than minibosses, which take longer than exercises.
- Your other courses will likely get busier towards the end of the semester, leaving you less time for this one.
- When you start feeling the panic of the end-of-term approaching, you'll shift from a mindset of "take the time to figure this stuff out" to "frantically try different things hoping to make the damn tests pass". The latter is generally LESS efficient, and definitely produces less actual learning. It's also just a sucky place to be, psychologically.
- I will undoubtedly get quite busy with late-semester submissions, leaving me less time to kick back no-pass assignments quickly or help you when you're stuck. You may not have time for multiple submit-correct-resubmit cycles near the end, and if you're rushing, kickbacks become more likely.

_You have been warned._ 🧐

___
## Policies

### Attendance Policy

Given what you've read so far, you might be wondering what the purpose of class meetings is, and whether you need bother attending. Good question!

Attending the first class or two will be critical for getting you up and running with our workflow: the various accounts, login identities, and tools you'll need to "do work" in this course. After that, class time is really nothing other than a place and time for you to work while I and other students are close at hand to answer questions and help you get unstuck. Don't underestimate the value of instantaneous on-call support. Plus, having at least that 150 minutes per week of distraction-free time committed to the course can be a big help in keeping you on track.

I reserve the right to declare any particular class meeting "mandatory", with advance warning to you. I would do this if, for example, I've got something important to show or discuss with you that does not lend itself well to written channels, and that should be of value to all the students. _Spoiler alert: I intend to do this one day early on to demonstrate some ways of using AI tools to help you learn course skillz faster and better._  Missing such a "mandatory" class would incur no grade penalty aside from the natural consequences of missing out.

The room we've been assigned is inconvenient. We may collectively agree to move class to a more convenient venue in Petty.

For any particular class meeting, if nobody shows up for the start of class, I will probably go back to my office after a few minutes. You can still find me there. Either way, I will be "on call" for you between 2:00 and 3:15 every Monday and Wednesday afternoon.[^1]

[^1]: _As of the time I'm writing this, I am recovering from a serious health issue that may affect some of the details of my availability during the Spring 2025 semester in ways I don't yet know. I'll keep you posted._


### Late Work Policy

You saw the part above about "no deadlines except for the final end-of-term submission deadlines", right? Late work is a non-issue in this course.

That being said: **Do not ask me for an "incomplete" simply because you haven't quite finished everything you wanted to by the deadlines.** According to the UNCG Catalog, a grade of _incomplete_ "indicates that the completion of some part of the work for the course has been deferred because of prolonged illness of the student or because of some serious circumstances beyond the student’s control."


### Accommodations

UNCG seeks to comply fully with the *Americans with Disabilities Act* (ADA). Students requesting accommodations based on a disability must be registered with the Office of Accessibility Resources and Services (OARS, 215 Elliott University Center, 336.334.5440, [http://oars.uncg.edu](http://oars.uncg.edu)).

### Academic Integrity Policy

You are, of course, expected to know and heed the University’s _Academic Integrity Policy_. Violations will be reported to the Dean of Students. A second violation at any time during your years as a student here leads to automatic suspension or expulsion, so this is serious stuff.

* [https://osrr.uncg.edu/academic-integrity-policy-pledge/](https://osrr.uncg.edu/academic-integrity-policy-pledge/)

As stated above, I encourage you to help each other and to work together to figure things out, but **any work you submit must be your own and represent your own understanding.** Here's the bright red line:

> **Every line of code you submit must be crafted by you.\***
> 
> Not just typed, but _crafted_. Someone else can suggest a technique, or tell you that you need a third argument to something-or-other function, or point out the location of a syntax error in your code, but they can’t type it for you. They can’t dictate what you should type. They can’t give you a copy of their code to copy-paste or mimic.
> 
> You can discuss solutions with other students, but you should then **write up your code by yourself, starting from an empty screen.** If you can’t do that, you don’t really understand it, and it’s dishonest to pretend that you do.

If at any time you are in doubt about where to draw the line between collaboration and plagiarism, ask me to clarify.

My experience is that the Physics majors who take this course are ethical and conscientious students who genuinely want to learn the topic and not just cheat their way to an undeserved grade. However, even usually-trustworthy students can make bad choices when they get overwhelmed and desperate. Recognize the temptation and ask me for help! Even better, don’t let yourself fall behind to the point that you might be so tempted. And don’t lend your solutions to another student, even to “just learn from, not copy.” That rarely ends well for anyone.

Code is inevitably idiosyncratic. Everyone's looks a little different in myriad ways that are really hard to fake, and I notice uncanny similarities even without looking for them. Don't take the chance.

Seriously, don’t jeopardize your reputation. Trust is easy to lose and very, very hard to regain.

### Artificial Intelligence Policy

By the way, you may have noticed the asterisk `*` on the above "bright red line". That's because of AI. Tools like _ChatGPT_ are changing the way coding is done, very dramatically and rapidly, and I'd rather help you learn how to ride that wave than hold you back. So, I'll show you some ways to use AI tools to accelerate rather than bypass your computational physics learning. I'll share the "what to do" details as we go.

The explosive arrival and improvement of AI tools like _ChatGPT_ over the past couple of years have caused quite a furor within universities. Is it cheating for students to consult an AI tool for help on an assignment, or an improvement in learning efficiency? Does it bypass learning, or does it develop new skills that will be critical in the near-future economy?

Well, duh. All of the above, obviously. It depends very much on _how_ the AI is used. In that way it's no different from consulting a classmate or other human for help: They could help you learn, or save you the trouble of learning. One big difference here is that unlike a human, an AI can't make the judgment call about whether what you're asking is ethical, or about the best way to support your learning. So, that's all on you.

I'll say a bit more about specific do's and don'ts soon, when I show you some really cool ways to leverage AI. For now, here's the general rule:

> Ask an AI tool to answer general questions, suggest general approaches, explain specific functions or language features, give you an example of code that uses a particular function or language feature, identify a bug in your code that you can't find, or offer suggestions on a block of your code. **Do not have an AI tool produce code to solve your specific course assignment problems, and do not present code written by an AI as part of your own.**

Here's one other requirement:

> Any time you use an AI to help you with an assignment, you must say how in your submission. You can do that by including some comment lines in your code, or including a note in a separate markdown/text file you add to the submission file, or whatever makes sense in the context.

The most important reason for this is that I want to learn how y'all are using AI, so that I can get better at helping you learn to get better at using it!

This is new terrain for all of us. When in doubt, let's talk it out. I haven't figured it all out either. 😵‍💫
___

_Congratulations for making it all the way to the end!_ 🏆
