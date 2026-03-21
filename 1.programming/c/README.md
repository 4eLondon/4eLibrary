<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="80"/>
  <h1>C</h1>

  ![Purpose](https://img.shields.io/badge/purpose-systems%20%26%20embedded-A8B9CC)
  ![Difficulty](https://img.shields.io/badge/difficulty-hard-F44336)
  ![Typing](https://img.shields.io/badge/typing-static-2196F3)
  ![Execution](https://img.shields.io/badge/execution-compiled-795548)
  ![Paradigm](https://img.shields.io/badge/paradigm-procedural-607D8B)
</div>

---

## What is C

C is one of the oldest and most influential programming languages in
existence. Created by Dennis Ritchie at Bell Labs in the early 1970s, it
was used to write the original Unix operating system and has been the
foundation of countless languages since — including C++, Java, Python, and
Rust. C gives you direct access to memory and hardware with minimal
abstraction between your code and what the computer actually does.

---

## Difficulty

**Hard.** C does not protect you from yourself. There is no garbage
collector, no bounds checking on arrays, and no safety net. You are
responsible for every byte of memory you allocate and for freeing it when
you are done. Mistakes cause crashes, security vulnerabilities, and subtle
bugs that are extremely difficult to track down. It is one of the most
educational languages to learn precisely because it forces you to
understand what is actually happening.

---

## What C is used for

| Field | Details |
|-------|---------|
| **Operating systems** | Linux, Windows, and macOS kernels are written in C. If you want to understand how operating systems work, C is essential. |
| **Embedded systems** | Microcontrollers, IoT devices, and hardware drivers run C because it produces tiny, fast executables with no overhead. |
| **Compilers and interpreters** | CPython (the main Python runtime) is written in C. So is the V8 JavaScript engine. |
| **Databases** | SQLite, PostgreSQL, and MySQL are written in C. |
| **Game development** | Many game engines use C for performance-critical components. |
| **Security research** | Understanding C is essential for exploit development, reverse engineering, and vulnerability research. |

---

## Key features

- **Direct memory access** — pointers let you work directly with memory addresses
- **Minimal runtime** — almost no overhead between your code and the hardware
- **Portable** — C code can run on virtually any platform with a C compiler
- **Fast** — one of the fastest languages available, comparable to Assembly in optimised builds
- **Foundation language** — understanding C makes every other language easier to understand

---

## Limitations

- **No memory safety** — buffer overflows, use-after-free, and null pointer dereferences are common mistakes
- **Manual memory management** — you must allocate and free memory yourself
- **No built-in data structures** — no lists, dictionaries, or sets in the standard library
- **Verbose** — tasks that are one line in Python can take 20 lines in C
- **Undefined behaviour** — many mistakes do not produce errors but cause unpredictable results

---

## What knowing C gets you

- A deep understanding of how computers actually work
- Strong foundation for learning C++, Rust, and systems programming
- Roles in embedded systems, OS development, and security research
- Credibility as a programmer who understands the fundamentals

---

## How to run C

**Terminal:**
```bash
gcc filename.c -o output    # compile
./output                    # run
```

Install GCC on Linux: `sudo apt install gcc`
Windows users need MinGW or WSL.

**GUI (VS Code):**
Install the C/C++ extension from Microsoft. Use the play button or the
integrated terminal with the `gcc` command.

---

## File naming for this folder

```
1.variables.c
2.user-input.c
3.conditionals.c
4.loops.c
5.functions.c
6.arrays.c
7.pointers.c
8.error-handling.c
9.file-io.c
10.structs.c
11.memory.c
12.preprocessor.c
```
