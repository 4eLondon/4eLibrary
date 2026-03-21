; what: print hello world to the terminal
; lang: x86-64 nasm, linux
; tags: basics, output
; assemble: nasm -f elf64 1.hello-world.asm -o hello.o
; link:     ld hello.o -o hello
; run:      ./hello
section .data
    msg db "Hello, World!", 10
    len equ $ - msg
section .text
    global _start
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall
    mov rax, 60
    xor rdi, rdi
    syscall
