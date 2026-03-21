# Cybersecurity

This folder is a beginner-friendly introduction to cybersecurity. The focus
is on understanding how things work and how attacks happen so you can write
safer code and make better decisions. Work through the folders roughly in
the order listed — each one builds on the last.

Nothing here is about attacking systems. It is about understanding threats
so you can defend against them.

---

## Sub-folders

| Folder | What goes here |
|--------|----------------|
| `concepts/` | Notes and explanations saved as `.md` files |
| `snippets/` | Short code or command examples |
| `projects/` | Small practical exercises and walkthroughs |

---

## `internet/`

Before you can understand security you need to understand what you are
securing. This covers how data travels across the internet, what actually
happens when you type a URL into a browser, and what the difference between
HTTP and HTTPS is. Everything else in this folder builds on this foundation
so start here.

---

## `linux/`

Most security tools, servers, and hacking challenges run on Linux. This
covers the essential terminal commands, how the Linux file system is laid
out, how user permissions work, and how to get comfortable navigating and
managing a Linux system. You do not need to be an expert — just confident
enough to get around.

---

## `networking/`

How computers find and talk to each other. Covers IP addresses, DNS (how
domain names get turned into actual addresses), ports, firewalls, and the
protocols that hold everything together like TCP and UDP. Understanding
networking is the single biggest unlock for understanding security — most
attacks exploit something at this level.

---

## `attacks/`

An overview of the most common ways systems get compromised. Covers
phishing, social engineering, brute force, man-in-the-middle attacks,
and more. Everything here is explained from the perspective of recognising
and preventing these attacks, not carrying them out.

---

## `websec/`

The most common vulnerabilities found in websites and web apps. Covers
the OWASP Top 10 — the industry's standard list of the biggest web security
risks — including SQL injection, cross-site scripting (XSS), and broken
authentication. If you are building anything for the web this is essential
reading.

---

## `passwords/`

Why weak passwords are dangerous, how password cracking works, what hashing
means and why storing plain text passwords is catastrophic, and how
multi-factor authentication (MFA) adds a critical layer of protection.
Practical knowledge for developers and everyday users alike.

---

## `tools/`

An introduction to beginner-friendly security tools used in the industry.
Covers what each tool does and basic usage — not deep configuration.

| Tool | What it does |
|------|-------------|
| **Nmap** | Scans a network to find what devices and ports are active |
| **Wireshark** | Captures and lets you inspect live network traffic |
| **Burp Suite** | Intercepts and tests web app traffic — useful for finding web vulnerabilities |
