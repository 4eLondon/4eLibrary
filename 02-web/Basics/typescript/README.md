<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" width="80"/>
  <h1>TypeScript</h1>

  ![Purpose](https://img.shields.io/badge/purpose-typed%20web%20development-3178C6)
  ![Difficulty](https://img.shields.io/badge/difficulty-intermediate-FF9800)
  ![Typing](https://img.shields.io/badge/typing-static-2196F3)
  ![Execution](https://img.shields.io/badge/execution-compiled%20to%20JS-9C27B0)
  ![Paradigm](https://img.shields.io/badge/paradigm-multi--paradigm-607D8B)
</div>

---

## What is TypeScript

TypeScript is JavaScript with types. It is a superset of JavaScript developed
by Microsoft, meaning all valid JavaScript is also valid TypeScript. It adds
a type system on top of JS that catches errors at compile time before your
code ever runs. It compiles down to plain JavaScript so it runs anywhere JS
does. Released in 2012, it has become the standard choice for any serious
JavaScript project.

---

## Difficulty

**Intermediate.** You should learn JavaScript first and feel comfortable with
it before moving to TypeScript. Once you understand JS, TypeScript is a
natural step up — the syntax is almost identical and the type system becomes
intuitive quickly. The compiler errors are excellent and guide you toward
fixing problems.

---

## What TypeScript is used for

| Field | Details |
|-------|---------|
| **Large-scale web apps** | TypeScript shines in big projects where plain JS becomes hard to maintain. Types make refactoring safe and code easier to understand. |
| **Frontend frameworks** | React, Vue, and Angular all have first-class TypeScript support. Most modern frontend projects use it by default. |
| **Backend with Node.js** | All the same use cases as JavaScript on the server, with the added safety of types. |
| **Libraries and SDKs** | Most modern npm packages ship TypeScript type definitions so your editor knows exactly what each function expects and returns. |
| **Team projects** | Types act as documentation — other developers can see exactly what a function needs without reading its implementation. |

---

## Key features

- **Static typing** — define what type a variable, parameter, or return value should be and the compiler enforces it
- **Interfaces** — describe the shape of objects so your code is self-documenting
- **Enums** — named constants that make code easier to read
- **Generics** — write reusable code that works with multiple types safely
- **Great tooling** — VS Code was built for TypeScript and has exceptional autocomplete and error detection
- **Gradual adoption** — you can add TypeScript to an existing JS project file by file

---

## Limitations

- **Compile step** — you cannot run TypeScript directly, it must be compiled to JavaScript first
- **Added complexity** — type errors can be confusing when you are starting out
- **Not always necessary** — for small scripts or solo projects, plain JavaScript is often simpler and faster to write
- **Type definitions** — some older npm packages do not have types, requiring workarounds

---

## What knowing TypeScript gets you

- A significant advantage when applying for frontend or full-stack roles
- The ability to work on large codebases confidently
- Fewer bugs in production — the compiler catches whole classes of errors before they reach users
- Better IDE support than any other JavaScript variant

---

## Key tools to know

| Tool | What it does |
|------|-------------|
| `tsc` | The TypeScript compiler — converts `.ts` to `.js` |
| `ts-node` | Run TypeScript directly without compiling first |
| `eslint` + `typescript-eslint` | Linting and code style enforcement |
| `zod` | Runtime type validation |
| `prisma` | Type-safe database ORM |

---

## How to run TypeScript

**Terminal:**
```bash
tsc filename.ts       # compile to JavaScript
node filename.js      # run the compiled file
```

Install the compiler first:
```bash
npm install -g typescript
```

Run without compiling using ts-node:
```bash
npx ts-node filename.ts
```

**GUI (VS Code):**
Built-in TypeScript support. Use the integrated terminal for the same commands above.

---

## File naming for this folder

```
1.variables.ts
2.user-input.ts
3.conditionals.ts
4.loops.ts
5.functions.ts
6.arrays.ts
7.interfaces.ts
8.error-handling.ts
9.generics.ts
10.classes.ts
11.modules.ts
12.async.ts
```
