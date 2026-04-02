section .data
    prompt db "Enter your name: ", 0
    greet  db "Hello, ", 0

section .bss
    buffer resb 64

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, 17
    syscall

    mov rax, 0
    mov rdi, 0
    mov rsi, buffer
    mov rdx, 64
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, greet
    mov rdx, 7
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 64
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
