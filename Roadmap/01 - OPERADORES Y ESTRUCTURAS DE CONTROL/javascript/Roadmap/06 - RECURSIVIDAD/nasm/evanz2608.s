; https://nasm.us/

; ====================================================================
; Ejercicio 06 - Recursividad
; ====================================================================
;
; Simplemente aclarar que existen dos tipos de recursividad: Directa e Indirecta.
; La recursividad directa se da cuando una función se llama a sí misma, y la recursividad indirecta se da cuando una función A llama a una función B
; que a su vez llama a la función A.


SYS_read:   equ 0
SYS_write:  equ 1
SYS_exit:   equ 60
STDIN:      equ 0
STDOUT:     equ 1
STDERR:     equ 2


global _start
extern printf
section .text

_start:
  mov rdi, 100
  call recursion1

  lea rdi, [LF]
  call printf
  lea rdi, [LF]
  call printf

%define FIB_ELEM 30
  mov rdi, FIB_ELEM
  call fibonacci
  mov rdx, rax
  mov rsi, FIB_ELEM
  lea rdi, [fibonacci_mask]
  call printf

%define FACT_NUM 10
  mov rdi, FACT_NUM
  call factorial
  mov rdx, rax
  mov rsi, FACT_NUM
  lea rdi, [factorial_mask]
  call printf

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall

; En esta función, primero preparamos el stack para poder hacer el CALL tanto a printf, como a la próxima iteración
; de recursion1.
; En ensamblador, es necesario que es stack esté alineado a 16 bytes, y cada vez que se usa CALL, el stack se desalinea
; puesto que CALL guarda en el stack la dirección de retorno, y por consiguiente, se le resta 8 bytes a RSP.
; Como en este caso tenemos dos llamadas, el stack sigue alineado, pero nesecitamos crear un "STACK FRAME", para que cada llamada
; guarde su punto de regreso sin corromper el punto guardado por la llamada anterior.
recursion1:
  push rbp
  mov rbp, rsp
  sub rsp, 16
  mov rcx, rdi
  mov [rbp - 16], rcx
  lea rdi, [printf_mask]
  mov rsi, rcx
  call printf
  mov rcx, [rbp - 16]
  dec rcx
  mov rdi, rcx
  test rcx, rcx
  jz .done
  call recursion1
.done:
  add rsp, 16
  pop rbp
  ret

; RDI: posición del elemento de la sucesión de Fibonacci a calcular.
; NOTA: esta función es muy lenta. Se puede optimizar bastante puesto que para cada recursión calcula
; todos los numeros de fibonacci anteriores.
fibonacci:
  push rbp
  mov rbp, rsp
  sub rsp, 32
  mov [rbp - 32], rdi
  
  cmp rdi, 1
  mov rax, rdi
  jle .return
  sub rdi, 1
  call fibonacci
  mov [rbp - 16], rax
  mov rdi, [rbp - 32]
  sub rdi, 2
  call fibonacci
  add rax, [rbp - 16]
  jmp .return
.return:
  add rsp, 32
  pop rbp
  ret

; RDI: el número del cual se va a calcular el factorial.
factorial:
  push rbp
  mov rbp, rsp
  sub rsp, 32
  mov [rbp - 32], rdi
  cmp rdi, 1
  jg .calculate
  mov rax, 1
  jmp .return
.calculate:
  dec rdi
  call factorial
  inc rdi
  mul rdi
  jmp .return
.return:
  add rsp, 32
  pop rbp
  ret

section .data
  printf_mask: db "%d ", 0x00
  fibonacci_mask: db "El elemento [%d] de fibonacci es: %d", 0x0A, 0x00
  factorial_mask: db "El factorial de [%d] es: %d", 0x0A, 0x00
  LF: db 0x0A, 0x00

section .bss
