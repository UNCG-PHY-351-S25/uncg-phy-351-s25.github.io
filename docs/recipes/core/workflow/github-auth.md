# Authorizing with GitHub from Beskar

Rather than typing in a password every time you need your working computer to talk to GitHub, GitHub uses a credential system that lets you authorize your computer once and then remembers the authorization. Let's get that set up.

This process is rather bizarre and finicky, so please ask for help if you're at all confused — and follow the instructions very, very carefully. Fortunately, you should only have to do it once, or at least once every so often.

1. **Log into Beskar** (if necessary).

1. **Open a Terminal**.

1. **Navigate to your home directory** (if necessary).

1. **Execute `gh auth login`**. ("gh" means "github"). That will start a several-step interaction that will guide you through the process, albeit not very clearly. The steps are…

1. **Choose `GitHub.com`** to log into. (This should be what comes up as the default choice, so you can just hit return to accept it.)

1. **Choose `HTTPS`** for the protocol. (Ditto.)

1. **Enter `Y`** when asked "Authenticate Git with your GitHub credentials?" (Ditto.)

1. **Choose `Login with a web browser`**. (Ditto.)

1. **Write down the "one-time code"** shown, or just make sure not to close this terminal or browser tab yet so you can get back to it.

1. **Press `Enter`**.
    - It will try and fail to open a web browser, because this is running on _my_ server and can't control _your_ web browser. So, when you get the failure message:

1. **Select and copy the URL** it shows.

1. **Open a NEW browser tab/window and paste in that URL**. Go there.

1. **Sign into GitHub** again, if necessary. You may need to enter an authentication code that GitHub emails or texts to you.

1. **Enter your one-time code** when asked. You'll probably want to go back to the tab with the Terminal session, copy the code, return here, and paste it in.

1. **Agree to authorize GitHub CLI** when asked whether to do so.

1. **Return to the Terminal session** and you should now see some output ending in "✓ Logged in as" and your GitHub username. Success!

If what you experience differs from this, let Prof. Beatty know ASAP.

**Note:** At any time in the future, you can check whether you're still logged into GitHub by executing `gh auth status` at any Terminal prompt.
