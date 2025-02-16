# Clone a Repo to Beskar
___

## Problem to Solve

> **I want to copy my fork of a course level repo from GitHub to Beskar so that I can start working on it in JupyterHub.**
___

## Recipe

1. **On GitHub, go to the main page of the repo** that you want to clone. For an assignment repo, make sure you're looking at your fork, not at the instructor's original.
    - If you are reading this on the GitHub site: to keep these instructions visible as you go, right-click on the repo name (e.g., `A-01-username`) at the very top of the window, and choose "Open in new tab".
        - Or, if you've got loads of screen real estate, "Open in new window" so you can put them side-by-side.
    - Do make sure you're looking at **your** fork, not at the original!

1. **Click the big green "Code" button** near the top of the repo main page.
    - That should reveal a popup dialog.

1. **Select the "Local" tab** in that dialog if it's not already selected.

1. **Select the "GitHub CLI" sub-tab**.

1. **Click the two-rectangles "copy" icon** to the right of the text box that contains something analogous to `gh repo clone UNCG-PHY-351-S25/A-01-username`.
    - A little tooltip that says "Copied!" should appear, briefly.

1. **Open a Terminal** (or switch to an already-open one) in your Beskar browser tab.

1. **Verify that you are, in fact, in your home directory** or life will get very awkward.

1. **Paste the copied text in as a terminal command** and hit return to execute it.

1. **List the directory's contents** and you should see a new subdirectory with the name of your repo.

