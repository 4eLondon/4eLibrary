<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg" width="80"/>
  <h1>Go</h1>

  ![Purpose](https://img.shields.io/badge/purpose-backend%20%26%20systems-00ADD8)
  ![Difficulty](https://img.shields.io/badge/difficulty-intermediate-FF9800)
  ![Typing](https://img.shields.io/badge/typing-static-2196F3)
  ![Execution](https://img.shields.io/badge/execution-compiled-795548)
  ![Paradigm](https://img.shields.io/badge/paradigm-concurrent-607D8B)
</div>

---

## What is Go

Go (also called Golang) is a compiled, statically typed language created by
Google in 2009. It was designed to be simple, fast to compile, and excellent
at handling concurrency. The language is intentionally minimal — it has very
few features compared to something like C++ — which makes it fast to learn
and easy to read. It is now one of the most popular languages for building
backend services, cloud tooling, and CLIs.

---

## Difficulty

**Intermediate.** Go has a small number of concepts to learn and very clean
syntax. If you already know one other language, Go is relatively quick to
pick up. The main adjustment is learning Go's approach to concurrency
(goroutines and channels) and its lack of some features you might expect
(no generics until Go 1.18, no traditional OOP).

---

## What Go is used for

| Field | Details |
|-------|---------|
| **Backend services** | Go powers backend infrastructure at Google, Uber, Dropbox, and Twitch. Fast, efficient, and easy to deploy. |
| **Cloud & DevOps tools** | Docker, Kubernetes, and Terraform are all written in Go. It is the dominant language in the cloud-native ecosystem. |
| **CLI tools** | Produces single static binaries with no dependencies — ideal for distributable command-line tools. |
| **Networking** | Excellent for high-performance network servers and proxies. |
| **Microservices** | Low memory footprint and fast startup times make it a popular choice for containerised services. |

---

## Key features

- **Goroutines** — lightweight threads built into the language, making concurrency straightforward
- **Fast compilation** — one of the fastest compilers of any language
- **Static single binary** — compiles to a single executable with no runtime dependencies
- **Built-in tooling** — formatter, test runner, and package manager all come with the language
- **Simple syntax** — a small number of keywords and concepts keeps the language readable
- **Strong standard library** — networking, HTTP, JSON, and more all built in

---

## Limitations

- **Verbose error handling** — Go requires explicit error checks after every function call, which adds repetition
- **No generics (pre-1.18)** — older Go code lacks the flexibility generics provide
- **Not great for GUIs** — not a natural fit for desktop or frontend applications
- **Less expressive** — the intentional simplicity means some abstractions require more code

---

## What knowing Go gets you

- Backend and infrastructure engineering roles, especially in cloud-native companies
- The ability to build fast, reliable services that are easy to deploy
- Strong credibility in DevOps and platform engineering
- A foundation in concurrent programming

---

## Key packages to know

| Package | What it does |
|---------|-------------|
| `net/http` | Built-in HTTP server and client |
| `encoding/json` | JSON encoding and decoding |
| `fmt` | Formatted I/O |
| `os` | Operating system interface |
| `gin` | Fast HTTP web framework |
| `gorm` | ORM for database interaction |

---

## How to run Go

**Terminal:**
```bash
go run filename.go        # compile and run
go build filename.go      # compile to executable
./filename                # run the compiled file
```

**GUI (VS Code):**
Install the Go extension. Use the play button or `go run` in the integrated terminal.

---

## File naming for this folder

```
1.variables.go
2.user-input.go
3.conditionals.go
4.loops.go
5.functions.go
6.slices.go
7.maps.go
8.error-handling.go
9.file-io.go
10.structs.go
11.interfaces.go
12.goroutines.go
```
