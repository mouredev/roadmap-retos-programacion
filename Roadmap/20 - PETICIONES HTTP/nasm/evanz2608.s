; https://nasm.us

; ===================================================
; 20 - PETICIONES HTTP
; ===================================================


AF_INET: equ 2
SOCK_STREAM: equ 1

STDIN: equ 0
STDOUT: equ 1
STDERR: equ 2

SYS_read: equ 0
SYS_write: equ 1
SYS_socket: equ 41
SYS_connect: equ 42
SYS_sendto: equ 44
SYS_recvfrom: equ 45
SYS_sendmsg: equ 46
SYS_bind: equ 49
SYS_exit: equ 60

BUF_LEN: equ 2048


global _start
extern inet_addr
extern htons
section .text
_start:
  ; Creamos un socket, en este caso un socket TCP
  mov rax, SYS_socket
  mov rdi, AF_INET
  mov rsi, SOCK_STREAM
  mov rdx, 0
  syscall

  cmp rax, 0
  jl _exit
  mov dword [sockfd], eax

; 93.184.215.14 - IP de http://example.com
; 80 - Puerto de escucha de solicitudes HTTP
  lea rdi, [example_url]
  call inet_addr
  mov dword [servaddr + sockaddr_in.sin_addr], eax
  mov rdi, 80
  call htons
  mov word [servaddr + sockaddr_in.sin_port], ax
  mov word [servaddr + sockaddr_in.sin_family], AF_INET
  mov rax, SYS_connect
  mov edi, dword [sockfd]
  lea rsi, [servaddr]
  mov rdx, sockaddr_in_size
  syscall

  test rax, rax
  js _exit

  mov rax, SYS_sendto
  mov edi, dword [sockfd]
  lea rsi, [request]
  mov rdx, request_len
  xor r10, r10
  xor r8, r8
  xor r9, r9
  syscall

  cmp rax, 0
  js _exit

.read_loop:
  mov rax, SYS_recvfrom
  mov edi, dword [sockfd]
  lea rsi, [recv_buffer]
  mov rdx, BUF_LEN
  mov r10, 0x100
  xor r8, r8
  xor r9, r9
  syscall

  test rax, rax
  js _exit
  jz _exit

  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [recv_buffer]
  mov rdx, BUF_LEN
  syscall
  jmp .read_loop

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall

section .data
  struc sockaddr_in
    .sin_family: resw 1
    .sin_port: resw 1
    .sin_addr: resd 1
    .sin_zero: resq 1
  endstruc
section .bss
  sockfd: resd 1
  servaddr: resb sockaddr_in_size
  recv_buffer: resb BUF_LEN

section .rodata
  request:  db "GET / HTTP/1.1", 0x0D, 0x0A
            db "Host: example.com", 0x0D, 0x0A
            db "Connection: close", 0x0D, 0x0A
            db 0x0D, 0x0A
  request_len: equ $-request

  example_url: db "93.184.215.14", 0x00
