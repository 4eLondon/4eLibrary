# Web

![HTML](https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)

![Vue](https://img.shields.io/badge/Vue-4FC08D?logo=vuedotjs&logoColor=white)
![Svelte](https://img.shields.io/badge/Svelte-FF3E00?logo=svelte&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white)
![Astro](https://img.shields.io/badge/Astro-BC52EE?logo=astro&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?logo=express&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)

![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?logo=tailwindcss&logoColor=white)
![Sass](https://img.shields.io/badge/Sass-CC6699?logo=sass&logoColor=white)

This folder covers everything needed to build things for the internet —
from the basics of how a page is structured all the way to backend servers,
APIs, and styling tools.

---

## Sub-folders

| Folder      | What goes here                                           |
| ----------- | -------------------------------------------------------- |
| `concepts/` | Notes and explanations saved as `.md` files              |
| `snippets/` | Short ready-to-use code blocks in the relevant file type |
| `projects/` | Small working examples that show things in action        |

---

## `basics/`

The foundation of all web development. Learn these before touching any
framework or tool — everything else builds on top of them.

| Folder          | What it covers                                                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `html`          | The skeleton of every web page. Defines structure — headings, paragraphs, buttons, images, and links. Without HTML there is no page.      |
| `css`           | Makes things look good. Colours, fonts, spacing, and layout. Flexbox and grid are the two most important layout tools to learn.           |
| `javascript`    | Makes pages interactive. Clicking buttons, fetching data, updating content without reloading — all of that happens here.                  |
| `accessibility` | Making sure sites work for everyone including people using screen readers or keyboards. Good accessibility also improves search rankings. |

---

## `frameworks/`

Pre-built tools that give you a head start when building sites and apps.
They handle the repetitive parts so you can focus on what makes your project
unique. All are JavaScript-based and all produce HTML and CSS in the end.

| Folder   | What it is                                                                                                                    |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `react`  | The most popular UI framework. Build small reusable components and React handles updating the page when data changes.         |
| `vue`    | Similar to React but generally easier to pick up. More structured and approachable out of the box.                            |
| `svelte` | Does its work at build time so almost no extra code reaches the browser. Very fast and lightweight.                           |
| `nextjs` | React plus routing, server-side rendering, and backend code all in one project. The default choice for full-stack React work. |
| `astro`  | Built for content-heavy sites like blogs and docs. Sends almost no JavaScript to the browser by default.                      |

---

## `backend/`

The part of a web app the user never sees. Runs on a server, handles data,
processes logins, and sends information to the frontend.

| Folder    | What it is                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------ |
| `nodejs`  | JavaScript on the server. The runtime that Express and many other tools are built on.                        |
| `express` | Lightweight framework on top of Node.js. Handles routing and requests. Simple by design.                     |
| `fastapi` | Python framework for building APIs. Generates its own documentation and is one of the faster Python options. |
| `django`  | Fully loaded Python framework. Database layer, user auth, and admin panel all included out of the box.       |

---

## `apis/`

How two pieces of software talk to each other. When a frontend needs data
from a backend, or an app connects to an external service, it goes through
an API.

| Folder       | What it is                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `rest`       | The standard approach. Data lives at URLs and you use HTTP actions (GET, POST, PUT, DELETE) to interact with it.                            |
| `graphql`    | The client asks for exactly the data it needs in one request. Useful when different parts of an app need different slices of the same data. |
| `websockets` | A live open connection between browser and server. Used for real-time features — chat, live dashboards, multiplayer tools.                  |

---

## `auth/`

Authentication (confirming who someone is) and authorisation (what they can
do). Covers sessions, JWTs, OAuth (sign in with Google etc.), and the rules
that matter most — never store passwords in plain text, never write your own
encryption.

---

## `styling/`

Tools that make writing CSS easier and more maintainable as a project grows.

| Folder     | What it is                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| `tailwind` | Small pre-built CSS classes applied directly in HTML. No separate stylesheet to manage. Very popular in modern projects. |
| `modules`  | Scopes styles to the component that uses them so nothing accidentally affects anything else.                             |
| `sass`     | CSS with variables, nesting, and reusable chunks called mixins. Compiles to plain CSS.                                   |
