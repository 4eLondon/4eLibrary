<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" width="80"/>
  <h1>Bash</h1>

  ![Purpose](https://img.shields.io/badge/purpose-scripting%20%26%20automation-4EAA25)
  ![Difficulty](https://img.shields.io/badge/difficulty-beginner%20to%20intermediate-FF9800)
  ![Typing](https://img.shields.io/badge/typing-dynamic-FF9800)
  ![Execution](https://img.shields.io/badge/execution-interpreted-9C27B0)
  ![Paradigm](https://img.shields.io/badge/paradigm-scripting-607D8B)
</div>

---

## What is Bash

Bash (Bourne Again SHell) is the default command-line shell and scripting
language on Linux and macOS. It is how you communicate with your operating
system through the terminal. Bash scripts let you automate sequences of
commands — things you would otherwise type manually — and string programs
together. It is not a general-purpose programming language and should not be
used for complex logic, but for automation tasks it is the most direct tool
available.

---

## Difficulty

**Beginner to intermediate.** Basic Bash — running commands, writing simple
scripts, automating file operations — is very approachable. The syntax
becomes unusual and tricky as scripts grow more complex. For anything
involving complex logic, string manipulation, or data processing, switching
to Python is a better choice.

---

## What Bash is used for

| Field | Details |
|-------|---------|
| **Automation** | Automating repetitive tasks — renaming files, moving directories, running backups, scheduling jobs. |
| **DevOps & CI/CD** | Almost every CI/CD pipeline (GitHub Actions, Jenkins, GitLab CI) runs Bash scripts to build, test, and deploy software. |
| **System administration** | Managing Linux servers, setting up environments, installing software, configuring services. |
| **Gluing tools together** | Connecting the output of one command to the input of another using pipes. |
| **Startup and init scripts** | Bash scripts control how software starts, stops, and is configured on Linux systems. |

---

## Key features

- **Direct OS access** — run any command available on your system
- **Pipes** — chain commands together: `cat file.txt | grep "error" | sort | uniq`
- **Environment variables** — read and set system-wide configuration values
- **File globbing** — pattern matching for filenames: `*.txt`, `file_{1..10}.log`
- **Job control** — run processes in the background, foreground, or in parallel
- **Available everywhere** — any Unix-like system has Bash or a compatible shell

---

## Limitations

- **Not a real programming language** — no proper data structures, no classes, limited error handling
- **Cryptic syntax** — string quoting rules, variable expansion, and array handling are inconsistent and confusing
- **Fragile at scale** — large Bash scripts become difficult to maintain and debug
- **Portability issues** — scripts written for Bash may not work on other shells (sh, zsh, fish)

---

## What knowing Bash gets you

- The ability to automate tasks on any Linux or macOS system
- Essential for DevOps, system administration, and cloud engineering roles
- Comfort in the terminal — a foundational skill for any developer
- The ability to write CI/CD pipeline scripts

---

## How to run Bash

**Terminal:**
```bash
bash filename.sh        # run directly
chmod +x filename.sh    # make executable
./filename.sh           # run as executable
```

**GUI (VS Code):**
Install ShellCheck for linting. Run using the integrated terminal.

---

## File naming for this folder

```
1.variables.sh
2.user-input.sh
3.conditionals.sh
4.loops.sh
5.functions.sh
6.arrays.sh
7.strings.sh
8.error-handling.sh
9.file-io.sh
10.pipes.sh
11.env-variables.sh
12.cron-jobs.sh
```
