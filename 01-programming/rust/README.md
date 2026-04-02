<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-original.svg" width="80"/>
  <h1>Rust</h1>

  ![Purpose](https://img.shields.io/badge/purpose-systems%20programming-000000)
  ![Difficulty](https://img.shields.io/badge/difficulty-hard-F44336)
  ![Typing](https://img.shields.io/badge/typing-static-2196F3)
  ![Execution](https://img.shields.io/badge/execution-compiled-795548)
  ![Paradigm](https://img.shields.io/badge/paradigm-multi--paradigm-607D8B)
</div>

---

## What is Rust

Rust is a systems programming language focused on three goals — speed, safety,
and concurrency. It achieves memory safety without a garbage collector through
a unique ownership system enforced at compile time. Developed at Mozilla and
first released in 2015, it has been voted the most loved language in Stack
Overflow's developer survey every year since 2016.

---

## Difficulty

**Hard.** Rust has one of the steepest learning curves of any mainstream
language. The borrow checker — the system that enforces memory safety — will
reject code that works in other languages until you understand its rules.
This is frustrating at first but the compiler's error messages are excellent
and guide you toward the correct solution. Once it clicks, it is deeply
rewarding.

---

## What Rust is used for

| Field | Details |
|-------|---------|
| **Systems programming** | Operating systems, device drivers, embedded systems — anywhere you need direct control over hardware. |
| **WebAssembly** | Rust compiles to WebAssembly better than almost any other language, enabling near-native performance in the browser. |
| **CLI tools** | Fast, reliable command-line tools. Many modern Unix tools are being rewritten in Rust (ripgrep, bat, fd). |
| **Game engines** | Growing presence in game development where performance and control are critical. |
| **Networking** | High-performance web servers and network services. |
| **Cybersecurity** | Memory-safe systems code that eliminates entire classes of vulnerabilities. |

---

## Key features

- **Memory safety without GC** — the ownership system prevents null pointers, dangling references, and data races at compile time
- **Zero-cost abstractions** — high-level code compiles to the same performance as hand-written low-level code
- **Fearless concurrency** — the type system prevents data races between threads
- **Excellent tooling** — Cargo (package manager + build tool) is one of the best in any language
- **Expressive type system** — enums, pattern matching, and traits make complex logic clean and safe
- **No runtime** — no garbage collector, no virtual machine, just your code and the OS

---

## Limitations

- **Steep learning curve** — the borrow checker requires a new way of thinking about code
- **Slow compilation** — Rust projects can take longer to compile than other languages
- **Verbose** — some simple tasks require more code than in higher-level languages
- **Smaller ecosystem** — the library ecosystem is growing fast but is still smaller than Python or JavaScript

---

## What knowing Rust gets you

- Roles in systems programming, embedded development, and high-performance computing
- The ability to write software that is both fast and provably safe
- Strong fundamentals in memory management that make you a better programmer in any language
- A highly respected and increasingly in-demand skill

---

## Key tools and crates to know

| Tool / Crate | What it does |
|-------------|-------------|
| `cargo` | Build system and package manager — used for everything |
| `serde` | Serialisation and deserialisation (JSON, TOML, etc.) |
| `tokio` | Async runtime for building network applications |
| `clap` | Command-line argument parsing |
| `reqwest` | HTTP client |
| `axum` / `actix-web` | Web frameworks |

---

## How to run Rust

**Terminal:**
```bash
rustc filename.rs     # compile a single file
./filename            # run

cargo new project     # create a full project
cargo run             # compile and run
cargo build           # compile only
```

**GUI (VS Code):**
Install the rust-analyzer extension. Use `cargo run` in the integrated
terminal or the play button above `fn main()`.

---

## File naming for this folder

```
1.variables.rs
2.user-input.rs
3.conditionals.rs
4.loops.rs
5.functions.rs
6.vectors.rs
7.hashmaps.rs
8.error-handling.rs
9.file-io.rs
10.structs.rs
11.traits.rs
12.concurrency.rs
```
