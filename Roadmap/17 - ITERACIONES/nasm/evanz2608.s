; https://nasm.us

; ===================================================
; 17 - ITERACIONES
; ===================================================
;
; Existe en ensamblador, una forma de iteración que usa el registro RCX como contador
; y es la instrucción LOOP. La particularidad de este tipo de iteraciónes es que va en
; forma decreciente, donde se guarda en RCX el número de iteraciones que uno desea, y cada vez
; que se ejecuta la instrucción LOOP, se decrementa RCX y se comprueba si no es 0.
; En caso que no sea 0, LOOP salta a la etiqueta para ejecutar una vez mas el loop.
; Si RCX ES 0, loop no salta y la ejecución sigue.


STDIN: equ 0
STDOUT: equ 1
STDERR: equ 2

SYS_exit: equ 60


extern printf
global _start
section .text
_start:
; Iteraciones con LOOP

  sub rsp, 8    ; Alineamos el stack, para que luego del push podamos hacer el call a printf
  mov rcx, 10
loop_tag:
  push rcx      ; Cada vez que hacemos un call, rcx cambia su valor, por lo que debemos guardar en el stack.
  lea rdi, [number_mask]
  mov rsi, rcx
  call printf
  pop rcx       ; Y restauramos RCX a su valor antes del call
  loop loop_tag

  add rsp, 8
  lea rdi, [new_line]
  call printf

; Y ahora vamos a hacer una iteración con saltos condicionales.
  sub rsp, 8
  mov rcx, 1
jump_tag:
  push rcx
  lea rdi, [number_mask]
  mov rsi, rcx
  call printf
  pop rcx
  inc rcx
  cmp rcx, 10
  jle jump_tag

  add rsp, 8
  lea rdi, [new_line]
  call printf

; y estas son las únicas 2 formas de hacer iteraciones.

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall

section .rodata
  number_mask: db "%d ", 0x00
  new_line: db 0x0A, 0x00
