![Banner](https://raw.githubusercontent.com/4eLondon/4eLibrary/main/05-assets/images/banner.png)

---

A shared reference for everything code. Notes, snippets, and small examples
covering programming languages, web development, and cybersecurity all in
one place so nothing gets lost and everything is easy to find.

Anyone can add to it. The rules below exist to keep it clean for everyone.

---

> **Contributors: always work on the `edit` branch, never `main`.**
> Run `git checkout edit` after cloning.

---

## Branches

This repo has three branches and three only. Do not create a new one without discussing it.

| Branch   | Purpose                                                        |
| -------- | -------------------------------------------------------------- |
| `main`   | The clean, stable version. Nobody pushes here directly — ever. |
| `edit`   | Where all new content goes. This is where you work.            |
| `hotfix` | Typos and wrong file locations only. Goes straight to main.    |

**When you clone the repo you will land on `main` automatically.**
Switch to `edit` before you do anything as main is strict about pushes into itself:

```bash
git checkout edit
```

When your changes are ready, push to `edit` and open a pull request.
Nothing gets into `main` without approval. GitHub will block it if you try.

---

## Before you start working

Every time you sit down to add something, run this first:

```bash
git pull origin edit
```

This pulls in any changes others have made since you last worked on the repo.
Skipping this is the number one cause of conflicts — you end up working on an
old version and your changes clash with someone else's.

---

## How to open a pull request

Once you have pushed your changes to `edit`, go to the repo on GitHub.

1. Click the **Pull requests** tab at the top
2. Click **New pull request**
3. Set the base branch to `main` and the compare branch to `edit`
4. Add a short title describing what you added
5. Click **Create pull request**

That sends it for approval. Once it is reviewed and approved it will be merged
into `main`. You do not merge it yourself.

---

## If you get a conflict

A conflict happens when two people edited the same file and Git cannot figure
out how to combine the changes. If you see a conflict message, stop what you are doing.
Do not try to fix it yourself. Let the repo owner know and they will sort it
out. Attempting to resolve a conflict without knowing what you are doing can
silently delete other people's work.

---

## What goes where

Three top-level folders exist — `languages`, `web`, and `cybersecurity`.
Each topic inside them has the same three sub-folders:

- `concepts/` — notes and explanations, written in markdown (`.md`)
- `snippets/` — short code blocks, saved as the language's file type (`.py`, `.js`, etc.)
- `projects/` — small working examples, can have their own folder inside

**Example:** A Python function you want to save goes in
`languages/python/snippets/` — not in the root or a new folder you made.

If you are unsure where something belongs, ask before adding it.

---

## File naming

Use lowercase and hyphens. No spaces, no capitals, no special characters.

```
for-loops.py        ✓
for-loops.md        ✓
For Loops FINAL.py  ✗
forLoops_v2.py      ✗
```

Concepts and notes are written in markdown. Save them as `.md`.
Code files use the extension for that language — `.py`, `.js`, `.rs`, and so on.

---

## Rules

**1. Never push directly to main.**
Main is protected. GitHub will block you if you try. Everything goes through
`edit` first and only reaches `main` after it has been approved. This was done
to keep things more organised and orderly and to prevent users messing up each
other's work.

**2. Do not create new branches.**
There are only three — `main`, `edit`, and `hotfix`. Use `edit` for all
additions and `hotfix` only for fixing small mistakes.

**3. Do not create new top level folders.**
The structure is already set. If you think something is missing,
open an issue and discuss it first. Anything in the projects directory
can have its own folder though.

**4. Do not rename or move existing folders.**
Other people's work depends on the current structure. Renaming breaks things.

**5. Keep files small and focused.**
One concept per file. One snippet per file. For example if you are covering
functions in Python ensure the file only talks about functions so things stay
digestible. This also helps save time as you can add tiny guides on a language
or concept rather than spending half the day on one file.

**6. Use comments.**
Since multiple people will be viewing a file it only makes sense to properly
comment things to help with readability. The entire purpose of this repo is to
be a guide so comments are a must.

**7. Name your files properly.**
Lowercase, hyphens instead of spaces, no capitals or special characters.
`for-loops.py` not `For Loops.py`. Concepts go in `.md` files, code goes in
the file type that matches the language.

**8. Write a clear commit message.**
Say what you added and where. `Add for loop snippet to python/snippets` is
good. A commit message like `stuff` is too vague and will only confuse everyone.

**9. If in doubt, ask.**
A quick question before you start saves everyone time and prevents mix ups.
Don't know if someone already covered a concept, just ask. You don't want to
waste time on something that is already done.

---

## Folder reference

| Folder           | What lives there                                 |
| ---------------- | ------------------------------------------------ |
| `languages/`     | Python, JavaScript, Rust, Go, C, and more        |
| `web/`           | Basics, frameworks, backend, APIs, auth, styling |
| `cybersecurity/` | Internet, networking, attacks, tools, and more   |
