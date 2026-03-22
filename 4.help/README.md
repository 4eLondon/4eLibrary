# Git

![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

A reference for using Git — both in the terminal and inside VS Code.
Git is a version control system. It tracks changes to your files over time
so you can see what changed, undo mistakes, and collaborate without
overwriting each other's work.

---

## Terminal vs GUI — what is the difference

**Terminal** — you type Git commands directly. You are in full control and
can see exactly what is happening at every step. Every action is explicit —
nothing happens unless you type it. This is the most universal way to use
Git because it works the same everywhere regardless of what editor or OS
you are on.

**GUI (VS Code)** — VS Code has Git built in. Instead of typing commands
you click buttons in the Source Control panel on the left sidebar. It
handles the most common actions — staging, committing, pushing, pulling —
without you needing to remember a single command. It is faster for everyday
work once you understand what each button is actually doing underneath.

The important thing to understand is that **VS Code's Git UI and the terminal
are doing the exact same thing**. When you click commit in VS Code it runs
`git commit` behind the scenes. Learning the terminal first means you always
know what is happening, even when you are using the GUI.

VS Code also has an integrated terminal (`Ctrl+`` `) where you can type Git
commands directly. This is useful for commands the GUI does not expose —
like creating branches or managing remotes — but it is not the main way
of using Git in VS Code. The Source Control panel is.

![Terminal vs VS Code side by side](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/terminal-vscode.png)

---

## Setup

### Install Git

**Linux:**

```bash
sudo apt install git
```

**Mac:**

```bash
brew install git
```

**Windows:**
Download from [git-scm.com](https://git-scm.com). The installer also gives
you Git Bash, a terminal that works the same as Linux/Mac.

![Git Windows installer](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-install-windows.png)

### Configure your identity

Run these once after installing. Git attaches your name and email to every
commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Set up Git in VS Code

VS Code detects Git automatically if it is installed. No extension needed
for basic use. Open a repo folder and the Source Control icon (the branching
icon on the left sidebar) becomes active.

For a better experience install the **GitLens** extension — it adds inline
blame, history views, and more detail to the built-in Git panel.

![VS Code Source Control sidebar](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-sidebar.png)

---

## Core concepts

| Term                  | What it means                                                                     |
| --------------------- | --------------------------------------------------------------------------------- |
| **Repository (repo)** | A folder Git is tracking. All history lives here.                                 |
| **Commit**            | A saved snapshot of your changes with a message describing what you did.          |
| **Branch**            | A separate line of work. Changes on one branch do not affect others until merged. |
| **Remote**            | A copy of the repo hosted somewhere else — usually GitHub.                        |
| **Push**              | Send your local commits up to the remote.                                         |
| **Pull**              | Bring commits from the remote down to your local copy.                            |
| **Merge**             | Combine the changes from one branch into another.                                 |
| **Stage**             | Mark specific changes to be included in the next commit.                          |
| **Clone**             | Download a remote repo to your machine for the first time.                        |

![Git flow diagram](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-flow-diagram.png)

---

## Terminal workflow

### Starting out

Clone an existing repo:

```bash
git clone https://github.com/username/repo-name.git
```

Or initialise Git in an existing folder:

```bash
git init
```

![Git clone in terminal](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-clone-terminal.png)

---

### Checking the status of your work

See what files have changed and what is staged:

```bash
git status
```

See the actual changes line by line:

```bash
git diff
```

![Git status output](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-status-terminal.png)

---

### Saving changes

Stage a specific file:

```bash
git add filename.py
```

Stage everything that has changed:

```bash
git add .
```

Commit with a message:

```bash
git commit -m "Add for loop snippet to python/snippets"
```

![Git add and commit](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-add-commit-terminal.png)

---

### Syncing with the remote

Push your commits to GitHub:

```bash
git push origin branch-name
```

Pull the latest changes from GitHub:

```bash
git pull origin branch-name
```

![Git push output](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-push-terminal.png)

---

### Branches

Create a new branch without switching to it:

```bash
git branch branch-name
```

Switch to an existing branch:

```bash
git checkout branch-name
```

Create and switch in one step:

```bash
git checkout -b branch-name
```

See all branches:

```bash
git branch
```

Push a new branch up to GitHub:

```bash
git push origin branch-name
```

![Git branch list](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-branch-terminal.png)

---

### History

See a log of all commits:

```bash
git log
```

See a compact one-line version:

```bash
git log --oneline
```

![Git log output](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-log-terminal.png)

---

### Undoing things

Unstage a file you accidentally staged:

```bash
git restore --staged filename.py
```

Discard changes to a file and revert it to the last commit:

```bash
git restore filename.py
```

> **Note:** `git restore` only affects uncommitted changes. Once something
> is committed, ask the repo owner before trying to undo it — reverting
> commits incorrectly can affect everyone.

---

## VS Code workflow

### Opening the Source Control panel

Click the branching icon in the left sidebar or press `Ctrl+Shift+G`.
This is where all your Git actions live in VS Code.

![VS Code Source Control panel](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-source.png)

### Seeing what changed

Any file you have modified appears in the **Changes** list automatically.
Click a file to open a diff view showing exactly what was added or removed —
green lines were added, red lines were removed.

![VS Code diff view](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-diff.png)

### Staging changes

Hover over a file in the Changes list and click the **+** icon to stage it.
To stage everything at once click the **+** next to the Changes heading.

![VS Code staging a file](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-stage.png)

### Committing

Type your commit message in the box at the top of the Source Control panel
and press `Ctrl+Enter` (or click the tick ✓). This commits everything that
is staged.

![VS Code commit message](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-commit.png)

### Pushing and pulling

At the bottom left of VS Code you will see the current branch name and two
small arrows — one pointing up (push) and one pointing down (pull). Click
them to sync with GitHub.

![VS Code push pull bar](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-pull-push.png)

### Switching branches

Click the branch name in the bottom left corner of VS Code. A dropdown
appears where you can switch to any existing branch.

![VS Code branch switcher lead](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-branch-switcher-lead.png)


![VS Code branch switcher](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-branch-switcher.png)

### When to use the terminal inside VS Code

The Source Control panel handles the most common actions. Use the integrated
terminal (`Ctrl+`` `) when you need to do something the panel does not expose:

```bash
git branch branch-name          # create a branch without switching
git push origin branch-name     # push a new branch for the first time
git log --oneline               # view commit history
git restore --staged filename   # unstage a specific file
```

![VS Code integrated terminal](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/5.assets/images/git-vscode-terminal.png)

---

## Quick reference

| Action           | Terminal                  | VS Code                             |
| ---------------- | ------------------------- | ----------------------------------- |
| See what changed | `git status`              | Source Control panel                |
| Stage a file     | `git add filename`        | Click **+** next to the file        |
| Stage everything | `git add .`               | Click **+** next to Changes         |
| Commit           | `git commit -m "message"` | Type message and press `Ctrl+Enter` |
| Push             | `git push origin branch`  | Click the up arrow bottom left      |
| Pull             | `git pull origin branch`  | Click the down arrow bottom left    |
| Switch branch    | `git checkout branch`     | Click branch name bottom left       |
| View history     | `git log --oneline`       | GitLens extension or terminal       |
