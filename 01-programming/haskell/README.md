<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/haskell/haskell-original.svg" width="80"/>
  <h1>Haskell</h1>

  ![Purpose](https://img.shields.io/badge/purpose-pure%20functional-5D4F85)
  ![Difficulty](https://img.shields.io/badge/difficulty-advanced-F44336)
  ![Typing](https://img.shields.io/badge/typing-static%20%26%20strong-2196F3)
  ![Execution](https://img.shields.io/badge/execution-compiled-9C27B0)
  ![Paradigm](https://img.shields.io/badge/paradigm-purely%20functional-607D8B)
</div>

---

## What is Haskell

Haskell is a purely functional, statically typed programming language with
lazy evaluation. It was designed by a committee of researchers in 1990 to
consolidate ideas from functional programming academia into a single,
principled language. Haskell enforces functional purity strictly — functions
have no side effects unless explicitly managed through a type system construct
called a monad. It is less commonly used in industry than mainstream languages
but is deeply influential: features now found in Python, Rust, Scala, and
Swift (type inference, pattern matching, immutability) have roots in Haskell.

---

## Difficulty

**Advanced.** Haskell is widely considered one of the harder languages to
learn. Its type system is powerful but demanding, and concepts like monads,
functors, and lazy evaluation have no direct equivalent in imperative
languages. It rewards patience — developers who learn Haskell often report
it permanently changes how they think about code, even in other languages.
Do not start here; come back to it after you are comfortable with at least
one functional language like Elixir or a typed language like Rust.

---

## What Haskell is used for

| Field | Details |
|-------|---------|
| **Compilers & parsers** | Haskell is a top choice for writing compilers, interpreters, and parsers. GHC itself is written in Haskell. |
| **Finance & trading** | Several financial firms (Standard Chartered, Jane Street) use Haskell for correctness-critical trading systems. |
| **Research & academia** | A common language in programming language theory, type theory, and formal verification research. |
| **Cryptography & security** | The strong type system and purity make it attractive for writing provably correct security-critical code. |
| **Developer tooling** | Tools like Pandoc (the document converter) and ShellCheck are written in Haskell. |

---

## Key features

- **Pure functions** — functions always return the same output for the same input, with no hidden side effects
- **Lazy evaluation** — expressions are only computed when their value is actually needed
- **Strong static typing** — the type system catches entire classes of bugs at compile time
- **Type inference** — the compiler deduces types automatically; explicit annotations are rarely required
- **Pattern matching** — concise, expressive deconstruction of data structures
- **Monads** — a structured way to handle side effects (I/O, state, errors) while keeping functions pure

---

## Limitations

- **Steep learning curve** — monads, typeclasses, and lazy evaluation are genuinely difficult concepts
- **Small job market** — Haskell roles are rare outside finance, academia, and niche tooling companies
- **Lazy evaluation surprises** — deferred computation can cause unexpected memory behaviour (space leaks)
- **Tooling complexity** — the build ecosystem (GHC, Cabal, Stack) has historically been difficult to set up

---

## What knowing Haskell gets you

- A fundamentally different and more rigorous way of thinking about programs
- Deep understanding of type systems, which transfers to Rust, TypeScript, and Scala
- The ability to reason about code correctness more formally
- Credibility and strong signal in compiler engineering and PL research roles

---

## How to run Haskell

**Terminal (compiled):**
```bash
ghc filename.hs -o output && ./output
```

**Terminal (interpreted):**
```bash
runghc filename.hs
```

**Interactive REPL:**
```bash
ghci
```

**GUI (VS Code):**
Install the Haskell extension (powered by HLS). Use the integrated terminal.

---

## File naming for this folder

```
1.variables.hs
2.functions.hs
3.pattern-matching.hs
4.lists.hs
5.tuples.hs
6.types-typeclasses.hs
7.higher-order-functions.hs
8.recursion.hs
9.maybe-either.hs
10.io.hs
11.functors.hs
12.monads.hs
13.modules.hs
14.custom-types.hs
```
