# Find and Fork a Repo on GitHub
___

## Problem to Solve

> **I want to make my own copy of a course level repo (the "package" that assignments come bundled in) so that I can start working on it.**
___

## Background Knowledge

### Git and GitHub

[_Git_](https://git-scm.com/) is a software tool and system that helps programmers manage and collaborate on complex coding projects. One can install and run _Git_ on just about any computer.

[_GitHub_](https://github.com/) is an online service that provides web-based Git support. It helps developer teams collaborate, keep track of (and occasionally roll back) changes to a software project, and track issues to address. We'll use it as a way for me to distribute assignment files to you, for you to submit your work back to me, and for me to provide you with specific feedback about your code.

_GitHub_ runs on some huge server farm somewhere, and talks to _Git_ runningh on your computer.

On _GitHub_, an _organization_ ("org") is a space for a group of people to share and collaborate on coding projects. Prof. Beatty has created an organization for PHY 351.


### Repos and Course Assignments

On GitHub, the fundamental container or package for a coding project is called a _repository_, or "_repo_" for short. A repo is a collection of files and directories that can be shared with others and perhaps jointly edited. GitHub is built upon the [_git_](https://git-scm.com/) version control system, which takes care of (a) keeping a historical record of all changes to a repo's files over time, with snapshots of how it looked at various points in time; and (b) checking for and helping to reconcile conflicts that might arise between different contributor's edits and contributions.

I've divided the PHY 351 course content into six "worlds" (if we get that far). Each world is divided into multiple "levels". For example, _World A_ is about _Core Python_ skills. Within it, _Level 01_ is called _Workflow_ and focuses on how to use the course's "tech stack" — the combination of technology platforms and tools you'll use to do the course. A level consists of several individual "Exercises", each of which focuses on one of the course's computational physics "Recipes". Most levels end with a "Miniboss", a slightly more complex challenge that asks you to apply a combination of the recipes from the level.

I've chosen to package each "level" as one GitHub repo (repository). To "do" a level, the essence of what you need to accomplish is:

1. **Find the level repo** in our course "org" (organization) on GitHub.
2. **_Fork_** that repo to make your own copy to do your work in.
2. **_Clone_** your copy of the level repo to your account on Beskar, the server where you'll do your coding work.
3. **Read the instructions** in the repo and complete the specified tasks for each of the exercises and the miniboss.
4. Periodically **_commit_** your work to version control (to create snapshots that you could roll back to if necessary), and **_push_** all changes your copy of the repo on GitHub.
4. When all work for the exercises and miniboss is done, do a final commit-push, and then submit your work to me for credit by **_opening a pull request_** ("pullreq") from your copy of the repo to the course org's original version of repo. (This sounds weird. I'll explain more when we get there.)

For this recipe, we're just focusing on Steps 1 and 2 of this process, which includes getting familiar with GitHub and how I've set up our course "org" within it.
___

## Recipe

### Part A: Create a GitHub Account (once only)

For this course, you'll need to have your own account with the _GitHub_ service. Even if you already have one, you'll probably need to create a new one, because you'll need a GitHub account whose username is your UNCG username. Here's how to do that:

1. In a web browser, open [https://github.com/](https://github.com/) in a new browser tab or window.

1. The page you land on should have a prominent "Sign up for GitHub" button next to a blank for your email address. Enter your **UNCG** email address and click.

1. Follow the account creation steps (email authentication, etc.).

    * IMPORTANT: When prompted for "Username", choose your UNCG user ID: The portion of your UNCG email address before the "@" symbol.
    
    * Pick your password carefully, as you'll need to use it frequently. (May I suggest getting and learning to use a good password management program? I use _1Password_.)

    * At the appropriate step, identify yourself as a "student". Choose the free student plan.

1. When you get to the page with "The home for all developers — including you" at the top, you've succeeded!


### Part B: Get Added to the Course "Org" (once only)

1. Now that you've created your GitHub account, tell Prof. Beatty. He'll add you to the coure GitHub org.

1. Wait… ⏳⌛️… until…

1. Prof. Beatty lets you know that you've been added. Then, you can progress to the next step.


### Part C: Find the Course Org

When I tell you I've done that (or you're impatient and want to check by yourself):

1. Point your web browser to [https://github.com/UNCG-PHY-351-F22](https://github.com/UNCG-PHY-351-F22). (You might want to bookmark this.)

    * If you see "This organization has no public repositories", I haven't added you yet (or I did it wrong).

    * If you see "You made it! Welcome to the private GitHub space for UNCG's PHY 351 in Spring 2025", all is good and you're ready to proceed to the next task.

2. Feel free to explore a little, if you wish. Don't go _too_ far down any rabbit-holes, however: We've got work to do!

### Part D: Find the Level Repo

Remember that course assignments are packaged up into _repositories_ ("repos"), one level per repo. All the org repos available to you are listed on the org's repo page.

1. Along the top of the GitHub page for our org are several tab-style links: "Overview", "Repositories", "Projects", etc. **Click on "Repositories"**.
    - This should take you to a page listing repositories, with names like `uncg-phy-351-s25.github.io` and `A-01`.

1. If the list of repos gets inconveniently long as the semester progresses and Beatty releases more levels, note that the page has tools to let you search by repo name (or just a part of a name), sort the list in various ways, etc.

1. Click on the name of the repo you want to start work on.
    - This should take you to the repo's home page. Under a bit of fairly cryptic header info you'll see a list of files and folders in the repo. In the right sidebar is a brief "About" section.


### Part E: Fork the repo (once per repo/level)

In GitHub parlance, _forking_ a repo means making your own copy of it, so that you can make modifications without affecting anyone else.

A forked repo keeps track of the original "upstream" repo that it was forked from. One benefit is if the upstream repo changes, you can choose to _sync_ your forked repo with the changes in the upstream repo. (For a course level repo, that will probably occur when I inevitably discover bugs or confusing bits in an assignment that students have already started working on.)

As the owner of a forked repo, you can also request that the upstream repo incorporate changes you've made in your fork. This is called _issuing a pull request_ ("pullreq" — my own nickname for it).

Before you can start working on the assignments in a course level, you have to fork the level repo. (Otherwise, every student would be making changes to the same set of files, and pandemonium would erupt.)

1. If you're not already looking at the home page of the level repo (on the GitHub website), get there as described above in Part D.

1. Way up at the top right of that page, find the button that says "Fork". **Click it.** (Don't click on the little down-arrow to its right; click the main part that has the word "Fork".)
    - This should take you to a "Create a new fork" page.

1. In the form, change "Owner" to "UNCG-PHY-351-S25".
    - That will cause a scary red warning that "The repository \[XXX\] already exists on this account." Don't worry about it! Instead:

1. To the end of the repo name (such as "A-01"), append a hyphen and your GitHub ID (to make the name something like "A-01-idbeatty").

1. Leave "Description" as it is (though changing it won't break anything).

1. Leave "Copy the `main` branch only" checked.

1. Click the big green "Create fork" button.

When you do, you should be taken to the home page of your new repo. The repo name, which includes both the level name and your GitHub ID, will help you distinguish your copy of the repo from the original distributed by Prof. Beatty.

