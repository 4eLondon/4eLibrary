# Programming Languages

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white)
![Lua](https://img.shields.io/badge/Lua-2C2D72?logo=lua&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnubash&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?logo=csharp&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=mysql&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white)
![Assembly](https://img.shields.io/badge/Assembly-6E4C13?logoColor=white)

This folder contains notes, snippets, and projects for general-purpose
programming languages. Each language has its own folder with the same
three sub-folders inside.

---

## Sub-folders

| Folder      | What goes here                                                        |
| ----------- | --------------------------------------------------------------------- |
| `concepts/` | Notes and explanations — how the language works, saved as `.md` files |
| `snippets/` | Short ready-to-use code blocks, saved in the language's file type     |
| `projects/` | Small working programs that demonstrate real usage                    |

---

## Languages — easiest to hardest

| Order | Language       | Why it sits here                                                                                              |
| ----- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| 1     | **Python**     | Reads almost like plain English. Minimal setup. The best first language.                                      |
| 2     | **JavaScript** | Runs in the browser with no setup. Immediate visual feedback.                                                 |
| 3     | **TypeScript** | JavaScript with types. Learn JS first, then come here.                                                        |
| 4     | **PHP**        | Designed for the web. Simple to get running, widely used in older codebases and CMS platforms like WordPress. |
| 5     | **Lua**        | Small and simple. Good second language if you came from game scripting.                                       |
| 6     | **Bash**       | Straightforward for simple scripts, gets tricky fast with complex logic.                                      |
| 7     | **Java**       | More verbose and strict. Requires understanding classes from the start.                                       |
| 8     | **C#**         | Similar to Java. Powerful but a steeper initial setup.                                                        |
| 9     | **Go**         | Clean and simple but introduces compiled language concepts early.                                             |
| 10    | **SQL**        | Different way of thinking — declarative rather than step by step.                                             |
| 11    | **C**          | Manual memory management. No safety net. Foundational but demanding.                                          |
| 12    | **C++**        | C with more complexity on top. One of the steeper learning curves here.                                       |
| 13    | **Rust**       | Hardest on this list. The compiler is strict by design. Rewarding once it clicks.                             |
| 14    | **Assembly**   | As low-level as it gets. You are writing instructions the CPU understands directly.                           |

---

## Topics to cover per language

Work through these in order when adding content for a language.

1. Variables and data types
2. User input and output
3. Conditionals (if, else, switch)
4. Loops (for, while)
5. Functions
6. Arrays and lists
7. Dictionaries and key-value pairs
8. Error handling
9. File I/O (reading and writing files)
10. Object-oriented programming (classes, objects, inheritance)
11. Modules and imports
12. Concurrency (threads, async)

---

## File naming convention

Name files using a number prefix so they sort in order of difficulty.
Use lowercase and hyphens.

```
1.variables.py
2.user-input.py
3.conditionals.py
4.loops.py
5.functions.py
```

Same pattern for every language — just swap the extension:

```
1.variables.js      JavaScript
1.variables.ts      TypeScript
1.variables.cs      C#
1.variables.java    Java
1.variables.php     PHP
1.variables.go      Go
1.variables.c       C
1.variables.cpp     C++
1.variables.rs      Rust
1.variables.lua     Lua
1.variables.sh      Bash
1.variables.sql     SQL
1.variables.asm     Assembly
```

Concept files in `concepts/` follow the same pattern but use `.md`:

```
1.variables.md
2.user-input.md
```

---

## How to run code

### Terminal vs GUI — what is the difference

**Terminal** — you write code in any text editor, save the file, then run it
by typing a command. You are in full control and can see exactly what is
happening. No plugins, no buttons — just you and the command. Closer to how
things work in the real world.

**GUI (editor or IDE)** — an application like VS Code or IntelliJ that
combines the editor, terminal, and run button in one place. Handles a lot of
setup for you and adds autocomplete, error highlighting, and debugging tools.
Easier to start with but can hide what is actually happening under the hood.

Both are valid. Learning the terminal first gives you a stronger foundation.

---

### Python

**Terminal:**

```bash
python3 filename.py
```

**GUI (VS Code):** Install the Python extension. Click the play button (▷) top right, or right-click and select `Run Python File`.

---

### JavaScript

**Terminal:**

```bash
node filename.js
```

**GUI (VS Code):** Install Code Runner. Press `Ctrl+Alt+N` (`Cmd+Alt+N` on Mac). Output appears in the terminal panel below.

---

### TypeScript

**Terminal:**

```bash
tsc filename.ts       # compiles to filename.js
node filename.js      # runs the compiled file
```

Install the compiler first: `npm install -g typescript`

**GUI (VS Code):** Built-in TypeScript support. Use the integrated terminal and run the same two commands.

---

### PHP

**Terminal:**

```bash
php filename.php
```

**GUI (VS Code):** Install PHP Intelephense. Run using the integrated terminal or Code Runner extension.

---

### Java

**Terminal:**

```bash
javac Filename.java   # compile
java Filename         # run — no .java extension
```

**GUI (IntelliJ IDEA):** Click the green play button next to `main` or press `Shift+F10`.

**GUI (VS Code):** Install Extension Pack for Java. Play button appears above `main`.

---

### C#

**Terminal:**

```bash
dotnet new console -n ProjectName
cd ProjectName
dotnet run
```

**GUI (Visual Studio):** Press `F5` to build and run.

**GUI (VS Code):** Install C# Dev Kit. Use the play button or `dotnet run` in the terminal.

---

### Go

**Terminal:**

```bash
go run filename.go        # compile and run
go build filename.go      # compile only
./filename                # run the compiled file
```

**GUI (VS Code):** Install the Go extension. Use the play button or integrated terminal.

---

### SQL

**Terminal:**

```bash
sqlite3 database.db
sqlite3 database.db < file.sql
```

**GUI (DB Browser for SQLite):** Open a database, write SQL in the Execute SQL tab, press play.

**GUI (DBeaver):** Connect to your database, write your query, press `Ctrl+Enter`.

---

### C

**Terminal:**

```bash
gcc filename.c -o output
./output
```

**GUI (VS Code):** Install the C/C++ extension. Use the play button or integrated terminal. Windows users need MinGW or WSL.

---

### C++

**Terminal:**

```bash
g++ filename.cpp -o output
./output
```

**GUI (VS Code):** Same as C — install the C/C++ extension.

**GUI (CLion):** Press `Shift+F10`. Handles compilation automatically.

---

### Rust

**Terminal:**

```bash
rustc filename.rs        # single file
./filename

cargo new project-name   # full project
cargo run
```

**GUI (VS Code):** Install rust-analyzer. Use `cargo run` in the terminal or the play button above `fn main()`.

---

### Lua

**Terminal:**

```bash
lua filename.lua
```

**GUI (VS Code):** Install the Lua extension. Use the integrated terminal or Code Runner.

---

### Bash

**Terminal:**

```bash
bash filename.sh
chmod +x filename.sh
./filename.sh
```

**GUI (VS Code):** Install ShellCheck for linting. Run using the integrated terminal.

---

### Assembly

**Terminal:**

```bash
nasm -f elf64 filename.asm -o filename.o
ld filename.o -o output
./output
```

Install NASM: `sudo apt install nasm`

**GUI (VS Code):** Install ASM Code Lens for syntax highlighting. Compilation must be done manually in the integrated terminal — no play button for Assembly.
