# Execute Interactive Python
___

## Problem to Solve

> **I want to execute python commands interactively (perhaps to do a one-off calculation or just try things out).**
___

## Recipe


___
# Old Version

___
## Recipe to Solve It

_This is another "procedural" recipe._

### Part A, Version 1: Starting IPython from _JupyterLab_

If you are logged into Beskar and looking at the _JupyterLab_ interface…

1. If no "Launcher" tab is open in the main JupyterLab window, **open the Launcher** by clicking on the `+` button to the right of whatever tab(s) is/are open. A tab labeled "Launcher" should appear in the main window.

    -  Alternatively, you can click on the blue `+` button at the top of the File Browser in the left sidebar. If the sidebar is collapsed or is showing something else, view the File Browser by clicking on the folder icon in the very left window border.

2. **Launch an IPython console** by clicking on the button labeled "Python 3 (ipykernel)" **in the Console section**, _<u>not the identical button in the Notebook section above it</u>_. The Launcher tab should disappear, replaced by a tab labeled "Console N" (where `N` is some number). You now have an active IPython session.

3. **Type python expressions and statements into the input box** at the bottom of the pane, and hit Shift-Enter (or possibly just Enter) to send them to the python interpreter for execution.

    - You can decide whether you want to use Shift-Enter or just Enter to execute statements. Click the Settings menu in the JupyterLab browser window, pick "Console Run Keystroke" from the menu that appears, and select the option you prefer.
    - If you use "Enter" to execute code, you can use Shift-Enter to insert a line break for multiline input.


### Part A, Version 2: Starting IPython from the terminal

If you are working on your own computer or are logged into a different server, you can use IPython without JupyterLab. The visual appearance is different, but the functionality is equivalent.

1. Open a terminal window in whatever way is appropriate for your operating system.

    - In JupyterLab, you can do this by opening the Launcher (see Version 1 above) and clicking on the "Terminal" button in the "Other" section at the bottom.
    - On a Mac or Linux machine, launch the Terminal app or an equivalent application. (I prefer the "Warp" app.)
    - On Windows, you can use the Command Prompt or PowerShell.

2. At the terminal's command line, type `ipython` and hit Enter.

3. If you get a message like "command not found: ipython", either your computer doesn't have IPython installed, or it's in a "virtual environment" that you don't have activated. Resolving that is beyond the scope of this recipe. For PHY 351, just use _JupyterLab_ on Beskar and you should be fine.


### Part B: Do the calculation

1. Enter and execute a succession of python expressions and statements to accomplish your goals. (Details about how to do this are coming in future recipes, especially [the next one](calc-interactively.md).) The window above the input box/prompt will show you your IPython session's prior history of commands and their results. JupyterLab and most terminal programs will let you scroll back through that history, at least for a while.


### Part C: Save, if desired

If you want, you can save your IPython session's history to a file so that you have a record of what you did. 

1. **Execute `%save filename.txt`**, replacing `filename` with something meaningful to your situation.

    - This will save all your inputs and python's responses, for the entire IPython session.
    - You can save just a subset of the history by specifying the line numbers along with the `%save` command. For example, if you want to save lines 12 through 30, you would type `%save filename.txt 12-30`.

2. **Locate your history file** and, if desired, move it somewhere more convenient. By default, it gets saved in the "current working directory".

    - If you're using the JupyterLab interface, the "current working directory" will be whatever directory is currently displayed in the JupyterLab File Browser.
    - If you're using a terminal, it will be the directory your terminal was "in" when you launched IPython.
    - If you're thinking ahead, navigate the JupyterLab File Browser or terminal to the folder/directory you'll want your history file to be stored in before launching IPython.

Technically, it is possible to **reload a stored session** by re-running all commands in a history file. However, this is tricky and unreliable, because any errors in the file — from times that you entered something wrong and then redid or fixed it — will cause the re-running process to halt. In general, I recommend re-doing rather than restoring prior work if you need to resume an IPython session. (For anything complex enough to make this annoying, see the [Scripts](scripts.md) recipe.)


### Part D, Version 1: Quitting IPython from _JupyterLab_

1. **Close the console tab** by clicking the "X" at the right side of the "Console N" tab.

3. **Kill the background interpreter** by clicking on the square-within-a-circle icon in JupyterLab's far left border (it says "Running Terminals and Kernels" if hovered over) and clicking "Shut Down All" next to "KERNELS". (Or, expand the Kernels section, hover over the line for "Console N", and click the "X" that appears to its right.)

### Part D, Version 2: Quitting IPython from the terminal

1. **Enter and execute `quit`** at the console prompt. This will return you to the terminal's command line. (Unfortunately, if you do this within the JupyterLab IPython console, it'll quit and then automatically restart the console — quite annoying.)

___

## Comments

Again, this may look long and complicated, but it's the work of a few seconds once you're comfortable firing up JupyterLab or a terminal session. The result is an easy-access calculator that is superior in most ways to whatever handheld calculator or phone calculator app you might generally use.
