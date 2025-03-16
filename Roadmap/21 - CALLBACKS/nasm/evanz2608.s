; https://nasm.us

; ===================================================
; 21 - CALLBACKS
; ===================================================
;
; Las funciones, en ensamblador, son en realidad etiquetas que luego en el proceso de ensamblado y linkeado,
; son reemplazadas por una dirección de memoria a la que luego se salta para ejecutar el código desde ese lugar.
; Con lo cual, pasar una funcíon a otra función, es exactamente igual que pasarle otro parámetro cualquiera.
; La única diferencia en este caso, sería cargar esa dirección de memoria en algún registro, y hacer un call con ese registro
; como parámetro.
; Hay que tener en cuenta que los registros modifican constantemente su contenido, asi que lo mas prudente es almacenar la dirección de la
; función en algún lugar de la memoria para luego poder hacer el call. El lugar mas obvio es dentro del stack en la función que recibe la callback.

SYS_write equ 1
SYS_exit equ 60

STDOUT equ 1

global _start
section .text
_start:
  lea rdi, [funcion_callback]
  call funcion_principal

  lea rdi, [callback_con_parametros]
  lea rsi, [callback_param_msg]
  mov rdx, callback_param_msg_len
  call funcion_principal_con_parametros
_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall


; RDI = puntero a función callback
funcion_principal:
  enter 16, 0
  mov qword [rbp - 16], rdi       ; Almacenamos la dirección de la función callback
  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [func_msg]
  mov rdx, func_msg_len
  syscall
  mov rax, qword [rbp - 16]       ; Cargamos la dirección de la función callback en RAX
  call rax                        ; Y llamamos a la función
  leave
  ret


; Función que será pasada a otras funciones como parámetro.
funcion_callback:
  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [callback_msg]
  mov rdx, callback_msg_len
  syscall
  ret


; RDI = puntero a función callback
; RSI = primer parametro de la función callback
; RDX = segundo parametro de la función callback
funcion_principal_con_parametros:
  enter 32, 0
  mov [rbp - 32], rdi
  mov [rbp - 24], rsi
  mov [rbp - 16], rdx

  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [func_param_msg]
  mov rdx, func_param_msg_len
  syscall

  mov rax, [rbp - 32]
  mov rdi, [rbp - 24]
  mov rsi, [rbp - 16]
  call rax
  leave
  ret

; Función callback con un parámetro.
; Recibe en RDI un puntero a un string.
; y en RSI el largo del string
callback_con_parametros:
  mov rdx, rsi
  mov rsi, rdi
  mov rax, SYS_write
  mov rdi, STDOUT
  syscall
  ret

section .rodata
  func_msg: db "Hola desde una función normal", 0x0A
  func_msg_len: equ $-func_msg
  func_param_msg: db "Hola desde una función normal con callback con parametros", 0x0A
  func_param_msg_len: equ $-func_param_msg
  callback_msg: db "Hola desde una función callback!", 0x0A
  callback_msg_len: equ $-callback_msg
  callback_param_msg: db "Hola desde una función callback con parámetros!", 0x0A
  callback_param_msg_len: equ $-callback_param_msg
