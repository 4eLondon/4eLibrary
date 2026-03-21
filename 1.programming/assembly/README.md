<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="80"/>
  <h1>Assembly</h1>

  ![Purpose](https://img.shields.io/badge/purpose-low%20level%20%26%20systems-6E4C13)
  ![Difficulty](https://img.shields.io/badge/difficulty-very%20hard-B71C1C)
  ![Typing](https://img.shields.io/badge/typing-untyped-607D8B)
  ![Execution](https://img.shields.io/badge/execution-assembled-795548)
  ![Paradigm](https://img.shields.io/badge/paradigm-imperative-607D8B)
</div>

---

## What is Assembly

Assembly language is as close to the hardware as you can get while still
writing human-readable code. Each instruction maps almost directly to a
machine code instruction that the CPU executes. There is no single Assembly
language — each processor architecture (x86, x86-64, ARM, RISC-V) has its
own instruction set. These notes use x86-64 NASM syntax on Linux, which is
the most common starting point for learning.

---

## Difficulty

**Very hard.** There are no variables in the traditional sense, no loops
beyond jumps and labels, no functions beyond call stacks managed by hand.
You work directly with CPU registers, memory addresses, and system calls.
A single bug can cause a crash with no helpful error message. Assembly is
not learned for everyday use — it is learned to deeply understand how
computers work.

---

## What Assembly is used for

| Field | Details |
|-------|---------|
| **Reverse engineering** | Disassembled binaries are read as Assembly. Essential for malware analysis, CTF challenges, and vulnerability research. |
| **Exploit development** | Writing shellcode and understanding how exploits manipulate program execution requires Assembly knowledge. |
| **Compiler development** — understanding what compilers produce helps you write better high-level code and optimise for performance. |
| **Embedded systems** — critical timing code, bootloaders, and device firmware sometimes requires Assembly for precise control. |
| **OS development** — the very first code that runs when a computer boots is Assembly. |
| **Performance optimisation** — hand-written Assembly SIMD intrinsics can outperform compiler output for specific operations. |

---

## Key concepts

- **Registers** — small, extremely fast storage inside the CPU (rax, rbx, rcx, rdi, rsi, etc.)
- **Mov** — the most common instruction: move data between registers and memory
- **Stack** — a region of memory used to store temporary values and function call information
- **System calls** — how Assembly programs communicate with the OS to do I/O, exit, etc.
- **Labels and jumps** — how loops and conditionals are implemented at the Assembly level
- **Sections** — `.text` for code, `.data` for initialised data, `.bss` for uninitialised data

---

## Limitations

- **Architecture specific** — x86-64 Assembly does not run on ARM without being rewritten
- **Extremely verbose** — simple tasks in Python take dozens of lines in Assembly
- **No portability** — tied completely to the hardware it was written for
- **Almost never used for new applications** — compilers produce Assembly-quality output for most use cases

---

## What knowing Assembly gets you

- Deep credibility in security research and reverse engineering
- A fundamental understanding of how CPUs, memory, and operating systems actually work
- Skills valued in malware analysis, vulnerability research, and low-level systems work

---

## How to run Assembly (x86-64 NASM, Linux)

**Terminal:**
```bash
sudo apt install nasm          # install assembler
nasm -f elf64 filename.asm -o filename.o   # assemble
ld filename.o -o output        # link
./output                       # run
```

**GUI (VS Code):**
Install ASM Code Lens for syntax highlighting. All compilation must be
done in the integrated terminal — there is no play button for Assembly.

---

## File naming for this folder

```
1.hello-world.asm
2.registers.asm
3.arithmetic.asm
4.conditionals.asm
5.loops.asm
6.stack.asm
7.functions.asm
8.memory.asm
9.system-calls.asm
10.strings.asm
```
