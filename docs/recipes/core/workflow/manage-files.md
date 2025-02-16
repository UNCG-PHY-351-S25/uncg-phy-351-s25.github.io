# Manage Files on Beskar
___

## Problem to Solve

> **I want to view and/or reorganize the files and folders in my personal file space on Beskar.**
___

This "recipe" is actually a collection of tiny little snippet-recipes. In truth, it's really more of a cheat-sheet of commands to get you comfortable with both the JupyterLab File Browser and the system terminal's command-line interface (CLI). If you're already familiar with JupyterLab, or just quick to figure out GUI interfaces, Part A is probably unnecessary for you. If you're comfortable using the unix/linux command line, Part B is probably unnecessary. Refer to this or not as you see fit.
___

## Recipe Set A: Using the JupyterLab File Browser

> A note on terminology: When a recipe says "right-click", that means to click with your right mouse-button, or (on a Mac) option-click with a one-button mouse, or tap with two fingers on a trackpad, or do whatever it is you usually do to get a contextual (pop-up) menu to appear.


### Recipe 1: Hide and Display the File Browser

When you log into JupyterHub and are presented with the JupyterLab window, you should see some menu-type stuff across the top, a mostly-empty panel on the left, and a big area with a tab at the top that says "Launcher" and contains a collection of icon-like buttons in subsections named "Notebook", "Console", and "Other".

The panel on the left is the File Browser, and it's JupyterLab's version of the Mac Finder or the Windows File Explorer.

- Collapse it by clicking on the file-folder icon in the very left-hand border of the window.
- Re-expand it by clicking on that icon again.
- Switch to a different sidebar by clicking on one of the other icons in that left-hand border. (For now, no need to worry about what they do.)
- Switch back to the File Browser by — yeah, you guessed it.

### Recipe 2: Create a New File

1. Right-click on the empty space in the File Browser panel.
1. Choose "New File" from the contextual menu that appears.
    - A new file will be listed in the File Browser, with the name ready to be edited.
1. Type the filename you want, replacing the default "untitled".
1. If you want to create a plain-text file, leave the file name extension as `.txt`. If you want to create a different kind of file, change the extension too:
    - `.md` for a markdown file
    - `.py` for a Python script
    - `.csv` for a comma-separated values file (tabular data, e.g. for a spreadsheet to ingest)
    - Other file types can be created by other extension, but these are the ones you'll need most often.

### Recipe 3: View and/or Edit a File

For most file types, JupyterLab has only the plain-text view, so you view and edit the file in that. For a few, it has a plain-text view for editing and a formatted view for "nice" viewing. In particular, "markdown" and "CSV" files have two different views. (Some file types, like PDFs images, can't be edited or perhaps even viewed through JupyterLab.)

1. To view or edit a file, double-click on it in the File Browser.
    - The file should open in a new tab in the right-hand panel.
    - Other, previously-open tabs (other than the Launcher) will remain, and you can switch back and forth by clicking on their tabs.
2. For a file type that has two views, double-clicking will open whatever JupyterLab considers to be the "default" view. To get the other,
    - Right-click on the file in the file browser, choose "Open With" from the contextual menu, and choose the view you want.
3. If a file has opened to an editable view, you can make changes right in the displayed text. All the normal text-editing tools are available: cut, paste, undo, redo, etc. (See the Edit menu for more.)
4. To save your changes, choose "Save" from the File menu, or use the ⌘S (Mac) or ctrl-S (Windows) keyboard shortcut.
5. To close the file, click on the "X" in the file's tab.
    - If you have unsaved changes, JupyterLab will prompt you to save them before closing.

### Recipe 4: Duplicate a File

1. Right-click on the file in the File Browser and select Duplicate.
    - A new copy, with something like `Copy1` appended to the name, will appear in the File Browser.

### Recipe 5: Rename a File and/or Change its Type

1. Right-click on the file in the File Browser and select Rename.
    - The file name will become editable.
    - Change it to what you wish.
    - You can change the file's type by changing the extension.
    - Hit return to save the new name.

### Recipe 6: Delete a File or Folder

> **Note:** **Unlike most of what you do on a computer, deleting a file or folder via the File Browser cannot be undone. _Be careful!_** Pause a moment to ensure you know what you're doing and that you really want to do it.

1. Right-click on the file or folder in the File Browser and select Delete.
    - A confirmation dialog will appear.
    - Click "Delete" to confirm.

JupyterLab will not let you delete a folder unless it's empty. You can either delete its contents one at a time (possibly tedious), or use the Terminal method described below in Recipe B.10.

### Recipe 7: Create a New Folder

1. Right-click on the empty space in the File Browser panel.
    - Alternatively, you can click on the new-folder icon (a small folder with a `+` in it) at the top of the File Browser.
    - A new folder will appear, with its name ready to be edited.
2. Change the folder name to what you wish.

### Recipe 8: Move a File

- Click and drag the file to the folder you want to move it into.
- Alternatively, you can right-click on the file, select Cut, navigate into the folder you want to move it to (even a deeply nested one, a parent folder, or a different child of the current folder's parent), right-click on the empty space in the File Browser, and select Paste.

### Recipe 9: View a Different Folder

- To navigate into a folder currently displayed in the File Browser, double-click on it.
- To navigate back up to a parent folder, click on the folder's name in the "breadcrumb" bar at the top of the File Browser.
    - If you seen `/ … /` in the breadcrumb bar, the sequence of parent-child-grandchild folders has been abbreviated. Click on the `/ … /` to navigate to one of the elided folders.
___

## Recipe Set B: Using the System Terminal Command Line

JupyterLab's "Terminal" gives you a no-graphics, no-mouse, command-line-only interface to the file system (and operating system) underlying JupyterHub. The Linux command line is a powerful thing, and we're only going to scratch the surface in this course.

- If you really want to nerd out on it, Google is your friend. You may want to start with [The Linux Command Line](https://linuxcommand.org/tlcl.php) by William Shotts.

Here is some basic functionality to get you going. (Terminology warning: "directory" means the same as "folder", but is the more conventional term in this context.)

### Recipe 1: Open the Terminal

1. If the main display area is NOT showing the Launcher, display it by revealing the File Browser (if necessary) and clicking the big blue "+" button at its top.
2. In the Launcher, click on the button labeled "Terminal" in the Other section.
    - A new tab should open, with a prompt like `jupyter-test_student@Beskar:~$` at the top.
3. Start typing commands after the prompt.

### Recipe 2: Show the Current Directory

The terminal is always "in" a specific directory (folder), and life gets very confusing if you get confused about which one. You'll probably start in your "home" directory (which is the top of your personal file space and contains everything on Beskar that's "yours"), but will eventually navigate into others. To check which one you're currently in:

- Look at the part of the prompt just before the `$`.
    - It will show your current directory. The symbol `~` is a short-hand for your home directory.

- Alternatively, or to see a more complete path, type `pwd` (for "print working directory") and hit return.
    - The system will print out the full file path starting from the system's ultimate "root directory". It will look something like this for your home directory: `/home/jupyter-test_student`.
    - (In Linux, the currently-active directory is often called the "working" directory.)

### Recipe 3: List the Files in a Directory

- To see a list of the files in the current directory, type `ls` (for "list") and hit return.
    - To get additional information, you can append one or more "options" to the command, like this: `ls -l`, `ls -lF`, etc. Personally, my go-to is `ls -lFh`.
    - For exhaustive documentation on the options available, execute `ls --help`.

- To see a list of files within one of the directories (folders) in your current folder, execute `ls <foldername>`, replacing `<foldername>` with the name of the folder you want to see.
    - For example, `ls data` will show you the files in a folder named `data`.
    - Folder names that contain spaces are inconvenient, and best avoided. If you have one, you can surround thename with quotes (`ls 'test folder'` or `ls "test folder"`), or "escape" the space by preceding it with a backslash (`ls test\ folder`).

- You can lists the contents of sub-sub-directories like this: `ls <foldername>/<subfoldername>`.
    - For example, `ls data/2023-10-02` will show you the files in a folder named `2023-10-02` inside a folder named `data`.

- You can even list the contents of the current directory's parent with the special `..` name that means `parent of`, like this: `ls ..`.
    - Or, list the contents of a sibling of the current folder with `../<siblingname>`.

- No matter what directory you're currently in, you can list the contents of the home directory via `ls ~`, the contents of one of its subfolders with `ls ~/subfoldername`, and so on.

Yes, Linux command-line stuff is arcane, but powerful and flexible.

### Recipe 4: View a Calendar

This one isn't very important, but it's a useful illustration of some of the very deep functionality available from the command line.

- To see a compact little calendar of the current month, enter `cal`.
- To see the calendar for a different month and year, enter `cal <month> <year>`, for example: `cal 10 2026` or `cal oct 2026` for October 2026.
- To see a calendar for an entire year, execute `cal <year>`, for example: `cal 2025`.
- For exhaustive documentation, execute `man cal`. (`man` means "manual".)

### Recipe 5: Reuse Prior Commands

To save typing, you can re-execute commands you've (reasonably) previously executed in the Terminal. You can even modify them before re-executing them.

1. At the system prompt, press the up-arrow key.
    - Your most recently-executed command will appear.
    - You can continue to step back through previous commands by pressing the up-arrow key again and again.
2. When you find the command you want to re-execute, press the return key.
    - If you want to modify it first, you can left-arrow and/or backspace and/or type to make changes. Then hit return.
3. If you decide that you don't want to use a prior command, you can clear the command line by typing control-C (hold down the control key and press the `C` key). That is generic Linux for "cancel that!"

### Recipe 6: Change the Current Directory

- Navigate into a subdirectory of the current directory by executing `cd <foldername>`, replacing `<foldername>` with the name of the subdirectory you want to enter.
    - For example, `cd data` will navigate into a folder named `data`.
- You can navigate directly into a sub-subdirectory, a parent directory, a sibling directory, and so on with the same "file path" methods as were shown above in Recipe 3: List the Files in a Directory (for the `ls` command).
- The `cd ~` shortcut is a super-convenient way to jump back to your home directory quickly.

### Recipe 7: Create a New Directory

- Create a new, empty directory within the current directory by executing `mkdir <foldername>`, replacing `<foldername>` with the name of the new directory you want to create.
    - For example, `mkdir data` will create a new folder named `data` within the current directory.

### Recipe 8: Rename a File or Directory

- Rename a file or directory by executing `mv <oldname> <newname>`, replacing `<oldname>` with the current name and `<newname>` with the new name you want.
    - For example, `mv oldfile.txt newfile.txt` will rename a file named `oldfile.txt` to `newfile.txt`.
    - `mv` stands for "move". This is really just a special case of moving a file to a different directory (see below).

### Recipe 9: Move a File or Directory

- Move a file from the current directory into one of its subdirectories with `mv <filename> <foldername>`, replacing `<filename>` with the name of the file you want to move and `<foldername>` with the name of the subdirectory you want to move it into.
    - For example, `mv oldfile.txt data` will move a file named `oldfile.txt` into a subdirectory named `data`.
    - The `mv` command knows that you want to move, rather than rename, because the destination is the name of an already-existing directory.
- Move a file from somewhere other than the current directory by specifying its "file path", as described above in Recipe 3: List the Files in a Directory.
    - For example, `mv ~/other_project/file1.py data` will move a file named `file1.py` from a directory named `other_project` that lives in your home directory, and put it in a directory named `data` within the current directory (whatever that might be).
- Move a file to somewhere else the same way, by prepending a path onto the destination name.
    - For example, undo the previous example with `mv data/file1.py ~/other_project`.
- The character `.` is a very convenient short-hand for "the current directory".
    - For example, move a file from elsewhere to the current directory with `mv ~/other_project/file1.py .`.

### Recipe 10: Copy a File or Directory

- Make a copy of a file by executing `cp <filename> <newfilename>`, replacing `<filename>` with the name of the file you want to copy and `<newfilename>` with the name you want to give the copy.
    - For example, `cp oldfile.txt newfile.txt` will create a copy of a file named `oldfile.txt` and call it `newfile.txt`.
- You can put the copy into a subdirectory (or, really, anywhere else) by prepending the new file's nanme with a path.
    - Example: `cp oldfile.txt data/newfile.txt` will create a copy of `oldfile.txt` and put it in the `data` subdirectory, calling it `newfile.txt`.
- To make a copy of a directory and all its contents, include the `-r` option, like this: `cp -r <foldername> <newfoldername>`.
    - For example, `cp -r data data_backup` will create a copy of the `data` directory and call it `data_backup`.

### Recipe 11: View the Contents of a File

- To display the contents of a text file, execute `cat <filename>`, replacing `<filename>` with the name of the file you want to view.
    - For example, `cat oldfile.txt` will display the contents of a file named `oldfile.txt`.
    - Why `cat`? Because the command's full purpose is to concatenate multiple files together. We're just using it as an easy way to dump out the contents of one.

### Recipe 12: Save the Output of a Command to a File

- To save the output of a command to a file, execute the command as normal, but append `> <filename>` to the end of it before hitting retutrn. (Replace `<filename>` with the name of the file you want to save the output to, of course.)
    - For example, `ls -lFh > filelist.txt` will save a detailed listing of the files in the current directory to a file named `filelist.txt`.
    - If the file already exists, it will be overwritten. If it doesn't exist, it will be created.
    - If you instead want to append the output to an existing file, use `>>` instead of `>`.


### Recipe 13: Delete a File or Directory

> **Note:** **Unlike most of what you do on a computer, deleting a file or folder via the command line cannot be undone. _Be careful!_** Pause a moment to ensure you know what you're doing and that you really want to do it.

- Delete a file by executing `rm <filename>`, replacing `<filename>` with the name of the file you want to delete.
    - For example, `rm oldfile.txt` will delete a file named `oldfile.txt`.
- Delete a directory and all its contents by executing `rm -r <foldername>`, replacing `<foldername>` with the name of the directory you want to delete.
    - For example, `rm -r data` will delete a directory named `data` and all its contents.
    - The `-r` option means "recursive", which means "and everything inside it".

### Recipe 14: Clear the Terminal

- Empty the terminal display of all prior commands and output by executing `clear`.
    - This does not undo the history of what's happened; it just removes the clutter from your view.
    - You can still up-arrow through the command history.

### Recipe 15: Quit the Terminal Session

- To quit the terminal session, execute `exit`.
    - This will close the current tab AND shut down the terminal process.

Warning: If you just close the Terminal display by clicking on the "X" in the tab bar, the process will still be running on the server, just out of sight. In that case:

1. In the far left window border, click the square-inside-a-circle icon to replace the File Browser with the  "Running Terminals and Processes" panel.
2. Down at the bottom, find the Terminals section, and click "Shut Down All", then agree to the confirmation dialog.
    - Alternatively, you can expand that section, find the terminal session listed under it, mouse over it, and click the "X" that appears to its right. This is useful if you have multiple terminals going, and only want to kill one of them.

___
