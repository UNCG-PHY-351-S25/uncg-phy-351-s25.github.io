# Commit and Push Changes to GitHub
___

## Problem to Solve

> **I want to make a snapshot of my work so far in case I need to roll back changes, and copy the current repo state back to GitHub for safekeeping.**

___
## Background Knowledge

### Committing

In _git_ and _GitHub_ parlance, _committing_ means "saving a snapshot of the current state of the repo". These snapshots are good for a few different things, including:

- At some future time, comparing the repo's state then to the snapshot in order to see precisely what has changed (even which specific lines within a file!); and
- Resetting the repo to how it was at the time of a particular snapshot, if you've gotten all tangled up in changes you were trying to make that aren't working and just want to undo everything since the snapshot.

Committing a repo is something that you do locally (i.e., on whatever machine you've been using to work on the repo — for us, that's usually Beskar). When you do, _git_ saves information about the current snapshot into a hidden folder that is stored in the repo, right alongside the repo's normal files.

> **I strongly recommend "doing a commit" every time you complete an exercise**, when you take a break after having done significant work on an assignment, or when you're about to make major changes to some code that you might possibly want to undo.

### Pushing

Before you started working on a repo in Beskar, you had to (a) _fork_ it on GitHub to make your own copy, and (b) _clone_ it to Beskar.

_Pushing_ means taking whatever changes you've made to the local (Beskar) clone of the repo and "pushing" them through the internet to GitHub so that it can update your on-GitHub copy accordingly.

> **Doing this frequently is very important!** As of the start of the Spring 2025 semester, Beskar is _not_ being backed up at all. (That's on my to-do list. It's not so easy.)

### Pulling

_Pulling_ means the converse: from Beskar, "pulling" down from GitHub any changes that may have occurred to your copy of the repo there and updating your local, on-Beskar clone accordingly.

This isn't something you're likely to need very often, unless (a) you've used GitHub's web-based editor to change something, or (b) I've made changes to the master repo that you originally forked and that I've told you to pull down. (In that case, you'll first have to pull the changes from the master to your fork. When the need arises, I'll explain how to do that.)

### Syncing

_Syncing_ just means doing both a push and a pull simultaneously, and reconciling any conflicts (e.g., if a file was edited both on Beskar and on GitHub). If only one version has changed, this is the same as doing the appropriate push or pull.

I recommend avoiding making edits on both GitHub and Beskar between pushes/pulls, because the conflict reconciliation process can be confusing and frustrating. If you never make changes directly on GitHub, you won't have to worry about this unless I have to distribute updates or bugfixes.

___
## Recipe

### Recipe 1: Committing

You can do all this through the Terminal, via text commands, but I recommend using JupyterLab's built-in GitHub support.

1. In the top menubar, find the "Git" menu, click on it, and make sure the item "Simple staging" is checked. If not, select it to turn it on.
    - This setting should be remembered hereafter.

1. Click on the Git icon in the left-hand border. That's the one that looks like a diamond containing a couple of dots connected by branching lines (subway map??).
    - When you do, the File Browser panel should be replaced by one that says, at the top, "Current Repository" and the name of your repo.

1. That panel has two sub-panels, with side-by-side tabs labeled "Changes" and "History". If "Changes" isn't selected already, click that.
    - You should see a list of all files in the project that have been added, modified, or removed since your last commit. 

1. Make sure the checkboxes are checked for all the files you want to commit.
    - If you've created any new files, those won't be checked by default. Check them unless they're "throwaway" files you don't care about keeping in the repo. This adds them to the list of files to be tracked by git.

1. In the "Summary" box near the bottom of the panel, type a brief note like "Finished Exercise 04" (or whatever is appropriate).
    - This will help you figure out which snapshot you might want to compare or roll back to, should the need arise.

1. Adding a "Description" is optional.
    - Write one if you want to add a comment providing more detail about what's changed for this commit.

1. Then, click the big blue `Commit` button at the bottom (not the three-dots button on its right).
    - This performs the actual commit, storing the snapshot info in the repo.

1. If you are shown a "Who is committing?" dialog, fill in your name and UNCG email address and click "OK".
    - JupyterHub should remember your identity thereafter, and not demand this every time you commit.

_Save point created!_

### Recipe 2: Pushing

However, this new commit (snapshot) is only local, as is all the hard work you've done on the repo. Time to _push_ it to GitHub.

1. Look at the very top of the Git panel, up above the words "Current Repository". You should see a row of three little icons: a cloud with a down-arrow, a cloud with an up-arrow, and a circular-arrow.
    - These mean "pull", "push" and "sync" respectively.
    - If you hover your mouse pointer over any of them, a tooltip should appear to tell you what it does.
    - The "push" icon (the middle one) should have an orange dot next to it. That means the local repo has committed changes that haven't yet been pushed.

2. Click the "push" icon.
    - The dot should disappear, and a "Successfully pushed" message should briefly appear in the bottom-right corner of the JupyterLab window.

_Relax, content in the knowledge that your work is now safely protected on GitHub's massive server farms._
___
