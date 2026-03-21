; Project: echo input
; What it does: prints a prompt, reads input, then prints it back
; Run: nasm -f elf64 main.asm -o main.o && ld main.o -o echo && ./echo

section .data
    prompt      db "Enter your name: ", 0
    prompt_len  equ $ - prompt
    output_msg  db "You entered: ", 0
    output_len  equ $ - output_msg
    newline     db 10

section .bss
    buf resb 64

section .text
    global _start

_start:
    ; print prompt
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_len
    syscall

    ; read input into buf
    mov rax, 0
    mov rdi, 0
    mov rsi, buf
    mov rdx, 64
    syscall
    mov rbx, rax        ; save number of bytes read

    ; print "You entered: "
    mov rax, 1
    mov rdi, 1
    mov rsi, output_msg
    mov rdx, output_len
    syscall

    ; print what the user typed
    mov rax, 1
    mov rdi, 1
    mov rsi, buf
    mov rdx, rbx
    syscall

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall
