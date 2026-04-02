<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/elixir/elixir-original.svg" width="80"/>
  <h1>Elixir</h1>

  ![Purpose](https://img.shields.io/badge/purpose-concurrent%20systems-4B275F)
  ![Difficulty](https://img.shields.io/badge/difficulty-intermediate-FF9800)
  ![Typing](https://img.shields.io/badge/typing-dynamic-FF9800)
  ![Execution](https://img.shields.io/badge/execution-compiled%20to%20BEAM-9C27B0)
  ![Paradigm](https://img.shields.io/badge/paradigm-functional-607D8B)
</div>

---

## What is Elixir

Elixir is a dynamic, functional language built on top of the Erlang virtual
machine (BEAM). Created by José Valim in 2011, it was designed to bring modern
syntax and developer-friendly tooling to the proven concurrency and fault-
tolerance model that Erlang built over decades in telecoms. Elixir inherits
Erlang's ability to run millions of lightweight processes simultaneously while
adding a clean, Ruby-inspired syntax and a rich macro system. It is the
language behind the Phoenix web framework, one of the fastest and most
scalable web frameworks available.

---

## Difficulty

**Intermediate.** Elixir is approachable if you have some programming
experience, but it requires a shift in thinking. There is no shared mutable
state — data is immutable and programs are built by passing data through
functions. Pattern matching replaces much of what other languages do with
conditionals and loops. These concepts take adjustment but become very
powerful once they click.

---

## What Elixir is used for

| Field | Details |
|-------|---------|
| **Web development** | Phoenix is a high-performance web framework known for handling massive concurrency with low latency. Used by companies like Discord and Bleacher Report. |
| **Real-time systems** | Elixir's process model makes it ideal for chat apps, live dashboards, multiplayer games, and anything needing persistent connections (via Phoenix LiveView/Channels). |
| **Distributed systems** | Built-in tools for clustering nodes, message passing, and process supervision make distributed architecture straightforward. |
| **Fault-tolerant backends** | The "let it crash" philosophy and OTP supervision trees allow systems to recover from failures automatically. |
| **Data pipelines** | Broadway and GenStage provide abstractions for building concurrent, back-pressured data ingestion pipelines. |

---

## Key features

- **Immutable data** — values never change in place; functions always return new data
- **Pattern matching** — destructuring and control flow are unified into one powerful construct
- **Processes** — lightweight, isolated units of execution; millions can run simultaneously
- **OTP** — a battle-tested framework for building fault-tolerant, self-healing applications
- **Macros** — Elixir is built on a macro system, allowing the language itself to be extended
- **Pipe operator** — `|>` chains function calls cleanly, making data transformations readable

---

## Limitations

- **Niche ecosystem** — fewer libraries than Python, JavaScript, or Java
- **Not for CPU-heavy work** — the BEAM is optimised for concurrency, not raw computation
- **Functional learning curve** — thinking without mutable state is an adjustment for most developers
- **Small job market** — Elixir roles exist but are fewer than mainstream languages

---

## What knowing Elixir gets you

- Backend roles at companies building high-concurrency or real-time systems
- A deep understanding of functional programming and immutable data
- Exposure to the Actor model, one of the most important concurrency paradigms
- The ability to build systems that are genuinely fault-tolerant by design

---

## How to run Elixir

**Terminal:**
```bash
elixir filename.exs
```

**Interactive REPL:**
```bash
iex
```

**GUI (VS Code):**
Install the ElixirLS extension. Use the integrated terminal or run via `iex`.

---

## File naming for this folder

```
1.variables.exs
2.user-input.exs
3.pattern-matching.exs
4.conditionals.exs
5.loops-recursion.exs
6.functions.exs
7.lists-tuples.exs
8.maps.exs
9.strings.exs
10.error-handling.exs
11.processes.exs
12.modules.exs
13.structs.exs
14.pipe-operator.exs
```
