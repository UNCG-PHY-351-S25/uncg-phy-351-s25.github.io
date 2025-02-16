# Execute Interactive Python
___

## Problem to Solve

> **I want to execute python commands interactively (perhaps to do a one-off calculation or just try things out).**
___

## Recipe

_This is another "procedural" recipe. Don't worry, we'll get to actual code soon enough._

### Part A: Starting IPython

#### Version 1: From _JupyterLab_

Assuming you are logged into Beskar and looking at the _JupyterLab_ interface:

1. If no "Launcher" tab is open in the main JupyterLab window, **open the Launcher** by clicking on the `+` button to the right of whatever tab(s) is/are open. A tab labeled "Launcher" should appear in the main window.

    -  Alternatively, you can click on the blue `+` button at the top of the File Browser in the left sidebar. If the sidebar is collapsed or is showing something else, view the File Browser by clicking on the folder icon in the very left window border.

1. **Launch an IPython console** by clicking on the button labeled "Python 3 (ipykernel)" **in the Console section**, _<u>not the identical button in the Notebook section above it</u>_. The Launcher tab should disappear, replaced by a tab labeled "Console N" (where `N` is some number). You now have an active IPython session.


#### Version 2: From the terminal

If you are working on your own computer or are logged into a different server, you can use IPython without JupyterLab. The visual appearance is different, but the functionality is equivalent.

1. Open a terminal window in whatever way is appropriate for your operating system.

    - In JupyterLab, you can do this by opening the Launcher (see Version 1 above) and clicking on the "Terminal" button in the "Other" section at the bottom.
    - On a Mac or Linux machine, launch the Terminal app or an equivalent application. (I prefer the "Warp" app.)
    - On Windows, you can use the Command Prompt or PowerShell.

1. At the terminal's command line, type `ipython` and hit Enter.

1. If you get a message like "command not found: ipython", either your computer doesn't have IPython installed, or it's in a "virtual environment" that you don't have activated. Resolving that is beyond the scope of this recipe. For PHY 351, just use _JupyterLab_ on Beskar and you should be fine.


### Part B: Do the calculation

1. **Type a python expression or statement into the input box** at the bottom of the pane, and hit Shift-Enter to send them to the python interpreter for execution.
    - If you prefer, can change the "execute" keystroke to just Enter (rather than shift-Enter). Click the Settings menu in the JupyterLab browser window, pick "Console Run Keystroke" from the menu that appears, and select the option you prefer.
    - If you make "Enter" your execution keystroke, you can use Shift-Enter to insert a line break for multiline input.

1. **Continue executing python expressions and statements**, one after another.
    - When you define a variable in one statement, it will be available to subsequent statements.
    - The window above the input box/prompt will show you your IPython session's prior history of commands and their results.

1. **Press the up-arrow key to step back through your prior commands**.
    - You can re-execute one with (shift-)Enter, or modify it before executing. This often saves considerable typing.


### Part C: Save, if desired

If you want, you can save your IPython session's history to a file so that you have a record of what you entered. (The output, however, will not be saved. You'l have to re-execute the commands to see that.)

1. **Execute `%save filename.py`**, replacing `filename` with something meaningful to your situation.
    - This will save all your inputs and python's responses, for the entire IPython session.
    - You can save just a subset of the history by specifying the line numbers along with the `%save` command. For example, if you want to save lines 12 through 30, you would type `%save filename.py 12-30`.

1. **Locate your history file** and, if desired, move it somewhere more convenient. By default, it gets saved in the "current working directory".
    - If you're using the JupyterLab interface, the "current working directory" will be whatever directory is currently displayed in the JupyterLab File Browser.
    - If you're using a terminal, it will be the directory your terminal was "in" when you launched IPython.
    - If you're thinking ahead, navigate the JupyterLab File Browser or terminal to the folder/directory you'll want your history file to be stored in before launching IPython.
    - You can see what IPython thinks the current working directory is by executing the "magic command" `%pwd` (for "print working directory") at the IPython prompt.

Technically, it is possible to **reload a stored session** by re-running all commands in a history file. However, this is tricky and unreliable, because any errors in the file — perhaps from incorrect expressions that you later redid — will cause the re-running process to halt. In general, I recommend re-doing rather than restoring prior work if you need to resume an IPython session. (For anything complex enough to make this annoying, see the [Script a Calculation](../calculation/scripts.md) recipe.)


### Part D: Quitting IPython

#### Version 1: From _JupyterLab_

1. **Kill the python "kernel"** by choosing "Shut Down" from the Kernel menu.
    - The Console's tab must be the active one; if not, click on it or on the console pane.

1. **Close the console pane** by clicking the "X" at the right side of its tab.

1. **If you forgot to kill the kernel before closing the console pane**:
    - Click on the "Running Terminals and Kernels" icon in the left sidebar (looks like a square inside a circle).
    - Expand the "Kernels" section.
    - Click on the "X" that appears next to the "Console N" entry in the list of running kernels. Or, click the "Shut Down All" text and confirm in the dialog that appears.
    
#### Version 2: From the terminal

1. **Enter and execute `quit` or `exit`**  at the console prompt. This will return you to the terminal's command line.
    - Unfortunately, if you do this within the JupyterLab IPython console, it'll quit the kernel and then automatically restart it — quite annoying.

___

## Comments

Again, this may look long and complicated, but it's the work of a few seconds once you're comfortable firing up JupyterLab or a terminal session. The result is an easy-access calculator that is superior in most ways to whatever handheld calculator or phone calculator app you might generally use.
