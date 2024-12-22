# Script a Calculation

___
## Problem to Solve

> **I want to use a particular calculation multiple times, perhaps with different givens, and/or have a permanent record of it.**

Up until now, we've been using the IPython console as a kind of scientific calculator on steroids. This makes sense for quick one-off calculations. However, it has two major drawbacks:

1. Repeating the same calculation with different given values is tedious and error-prone, and
2. Constructing more complicated, multi-step calculations is awkward and error-prone, especially when repeated trying-fixing-trying again or debugging cycles are required.

The solution: Write your lines of python code in a _script file_, using a text editor of some kind. Then, send the whole file to the python interpreter (from IPython or a terminal console) to execute. The interpreter will still work through your code one line at a time, just as if you'd entered them into an IPython session console.

The biggest difference is that you won't see the results of bare python expressions. If you want your script to give you some results, you'll need to use the `print()` statement.

___
## Recipe, Part 1: Create the Script File

Python scripts are just sequences of python commands, saved in a file with a `.py` extension. You can write and edit them in any text editor, but it's easiest to work in one that's meant for coding and provides useful functionality like auto-indentation and syntax coding. _JupyterLab_ is a great choice for this.

1. In _JupyterLab_, open the left-side File Browser (if not already open).

2. In the File Browser, navigate to the folder where you want to save your script file. You can create folders and subfolders for this, if you wish, using the new-folder button at the top of the File Browser.

3. If the Launcher is not open, open it by clicking the `+` button at the top of the File Browser or in the tab bar above the main panel.

4. In the Launcher, click the "Python File" button down in the "Other" section. The Launcher should be replaced by a blank window with a tab that says "untitled.py".

5. You can immediately give the file a more sensible name by saving it (cmd/ctrl-S or "Save Python File" from the JupyterLab File menu) and specifying a name. Give it a meaningful name, but don't use spaces or special characters other than the underscore, and make sure to keep the `.py` ending. You should see it show up in the File Browser.

6. It's a good habit to immediately put a comment line (or several) at the top of the file, briefly stating what the script's purpose is. That could be as simple as something like `# Calculations for PHY 325 HW 3 Problem 2`.

    - In python code, any line beginning with a `#` (possibly preceded by empty space) is considered a "comment" for humans only, and is ignored by the python interpreter.

You now have a python script! Admittedly, it doesn't do anything yet, so…

___
## Recipe, Part 2: Write the Script

The short version: Just write python code in the file, as you would type it into an interactive python/ipython session. When you run the script, the lines in the file will be sent to the python interpreter one at a time, in the order they appear. If the very last non-empty line is an expression that would return a result (rather than, say, a variable assignment), that result will be shown as the "result" of the script.

The longer version, showing good script organization habits:

1. **Begin the script with an informative comment**, as described above. Think about explaining "WTH is this script for?" to anyone (including far-future you) that might look at it, as well as any assumptions that might not be obvious from the code. And, if this might be shared or distributed, include your name and a date and such.

2. **Next, import any needed modules**, or functions from modules. Putting all the import statements at the top makes it easy for someone to see what your code's "dependencies" are. As you start writing bigger, more sophisticated programs with nonstandard third-party modules, this becomes increasingly important.

3. **Define variables for any physical or other "standard" constants**, like the local or universal gravitational constants, the speed of light, etc. End the line with a comment that includes the units, like these:

    - `G = 6.67430e-11  # m**3 / (kg s**2)`
    - `c = 2.99792458e8  # m/s`

4. **Define variables for any situation-specific given values**, also with explicit units in a comment. If the physical meaning of the variable is not obvious from its name, say what it is in the comment.

    - `m1 = 2.5    # kg, mass of upper block`
    - `m2 = 2.5    # kg, mass of lower block`
    - `mu_k = 0.3  # coefficient of kinetic friction between lower block and tabletop`

    Note that you can use some extra space characters to make the comments align nicely.

5. **Calculate intermediate values and chunks of complicated expressions**, storing them in variables and building up the calculation step by step. Again, include comments for anything not self-explanatory.

    - `I = (2/5) * M * R**2  # kg m**2, moment of inertia of the sphere`
    - `A = 1 / r1 + 1 / r2  # denominator of net potential expression`

6. **Use `print()` to display result(s)**, using f-string format codes as you see fit. See the recipe [Print Formatted Output](print.md) for details.

    - `x_f, v_f, m.degrees(angle_f)` (assuming your script already assigned values to the variables `x_f`, `v_f`, and `angle_f`)

7. **Save your edits.** It's probably wise to do this every so often as you work, just in case.

___
## Recipe, Part 3: Run the Script

You can run the script directly from within an active IPython session, or from the system command line in a terminal.

### Method A: From IPython

1. If you're in _JupyterLab_, you can easily **open an IPython session** with the correct working directory by right-clicking (or double-tapping or whatever) on the script file's title tab at the top of the editor, and selecting "Create Console for Editor".

    - You should get a "Select Kernel" dialog. 

2. **Choose "Python 3 (ipykernel)". Click "Select".**

    - A new pane should pop open, probably in the bottom half of the window.

    - If you wish, you can grab the console by its tab and drag it to the right of the screen (to split vertically instead of horizontally), or right next to the script file's tab (to let you switch back and forth between the tabs, giving each a full window of space).

3. This is a normal ipython session, so you can do the usual interactive python things there. And, you can run your python script (or any python script, really) by entering the magic command `%run your_filename.py`, replacing the `your_filename` bit with whatever you named your file.

    - You should see the result of your script appear in the IPython console, exactly as if you'd typed the lines in, one at a time. (Except that you won't see the results of any expressions except the last in the script.)

    - Any variables you've defined in the script are now defined in the IPython session, with whatever values the script assigned to them, so you can continue the calculation, or explore their values, or whatever you might want to do with them.

___
## Recipe, Part 4: Modify the Script

If you discover an error, or you want to run it with different givens, or you're dissatisfied with what the script outputs, or you want to extend it — immediately, or days or months later — doing that is far easier than if you'd been working interactively in the console.

1. **Edit the script** in the editor window in whatever way you wish.

2. **Save changes** via the usual method (cmd/ctrl-S or "Save Python File" from the _JupyterLab_ File menu).

3. **Run the script** as in Recipe Part 3.

___
## Recipe, Part 5: Quitting

When you're done (at least for a while):

1. **Close the IPython console** by clicking the `x` in the tab. The pane should disappear.

2. **Open the "Running Terminals and Kernels" panel** (in place of the File Browser panel) by clicking the "square in circle" button in the far left border of the _JupyterLab_ window (which says "Running Terminals and Kernels" when you hover over it).

3. **Kill the ipython kernel by clicking on the "Shut Down All" words to the right of the "KERNELS" section header in that panel.
    - If you have other running kernels that you don't want to kill, you can instead open the KERNELS section by clicking on the word KERNELS, finding the line with your script's filename and an alphanumeric code like `(1c7e3b30)` following it, mousing over it. and clicking the "X" that appears to its right.

It's easy to forget to kill the kernel, since there's no visual reminder that its running once you've closed the pane. Nothing terrible will happen if you forget, but it will hang around and take up memory on the server and generally cruft things up, so please try to remember.

___
## Recipe, Part 6: Resuming

If, some time later, you wish to re-run and perhaps modify or extend your script, no problems!

1. Locate the script in the File Browser and reopen it by double-clicking on it.

2. Edit as you wish.

3. Launch an IPython console for it, as described above in Recipe Part 3 (method A or B).

4. Run, modify, and rerun it as you did in Recipe Parts 3 and 4.

5. When done, quit as in Recipe Part 5.

___
## An Example

*Whew!* That took a lot longer to describe than it actually takes to do. Let's look at an example.

We'll revisit the physics calculation from our earlier recipe [Use Python Functions](use-functions.md), showing how the same calculation might be laid out in a script. I'll focus on the contents of the script, letting you walk through the procedural steps around it. For convenience, here's the problem again:

**Problem:** An unpowered projectile is launched from the ground with an initial speed of 20 m/s at an angle of 50° above the horizontal. What are its speed and direction when it's height above the ground is 10 m?

**Solution:** Elementary kinematics allows one to derive expressions for the horizontal and vertical component of the projectile's velocity at any height $h$ (not greater than its maximum height, of course):

$$v_x(h) = v_{0,x} \qquad v_y(h) = \sqrt{v_{0,y}^2 - 2gh}$$

where $v_{0,x}$ and $v_{0,y}$ are the components of the projectile's initial velocity, $g$ is the acceleration due to gravity, and $h$ is the height above the ground. If $\theta_0$ represents the velocity's initial angle above horizontal, we can decompose the initial velocity vector into:

$$v_{0,x} = v_0 \cos(\theta_0) \qquad v_{0,y} = v_0 \sin(\theta_0)$$

We can use the expressions above to determine the components of the initial velocity vector, and then the velocity components at the given height. Once we know those, we can calculate the requested values by applying trig to find the magnitude and direction of the velocity vector at that height:

$$v(h) = \sqrt{v_x(h)^2 + v_y(h)^2} \qquad \theta(h) = \arctan\left(\frac{v_y(h)}{v_x(h)}\right)$$

**The script:**

A python script to do the numeric calculations for this might — if well-organized and commented — look something like this:

```python
# -------------------------------------------------------------------
# PHY 291 HW-2 Problem 3 -- Calculations
# -------------------------------------------------------------------

# Imports
from math import radians, degrees, sin, cos, sqrt, atan2

# Define constants
g = 9.806           # N/kg -- local gravitational constant

# Define givens
h = 10             # m -- height for which we want velocity
v0 = 20            # m/s -- initial speed
q0 = radians(50)   # degrees (converted) -- initial direction

# Calculate initial velocity components
v0x = v0 * cos(q0)
v0y = v0 * sin(q0)

# Calculate velocity components at height `h`
vx = v0x
vy = sqrt(v0y**2 - 2 * g * h)

# Calculate magnitude and direction
v = sqrt(vx**2 + vy**2)
q = atan2(vy, vx)

# Report out the result
print(f"At a height of {h} m, the final velocity is {v:.2f} m/s")
print(f"at an angle of {degrees(q):.2f} degrees above horizontal.")

# -------------------------------------------------------------------
```
Let's assume we named the file `hw02-p3.py`. Executing `%run hw02-p3.py` in an IPython console would produce the following output:

```text
At a height of 10 m, the final velocity is 14.28 m/s
at an angle of 25.80 degrees above horizontal.
```

Should we want to know the velocity at a different height, we could edit the script to change `h = 10` to a different number, and then re-run the script. _Easy peasy._

A few comments:

- You might think including all those section comments like "# Calculate magnitude and direction" is overkill and a waste of time, but it's actually helpful if you do it right: Write out the sequence of section comments **first**, like a kind of "outline" or "recipe" to follow. Then, fill in the code for each section. You can skip the import section at first, adding bits to it as you're writing other sections and realize the functions you'll need to import.
- I chose to import specific `math` module functions by name here, but there are enough that using the `import math as m` route would be reasonable too.
- I didn't use the comma trick to define related variables (like `vx` and `vy`) on one line, but you could.
- Note that I did **NOT** "hard-code" any of the given values into the calculations or the final print statements. For example, I used f-string variable insertion to include the height value, rather than just typing `At a height of 10 m`. This way, I only have to edit one number to change the whole calculation and output to use a different height. Had I hard-coded a result, I introduce the risk of forgetting to change it in all places — a very VERY common coding error.
