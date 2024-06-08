; https://www.nasm.us/


; ======================================================================================================================
; #03 - Funciones.
; Testeado en Arch linux. No lo he testeado en otras distribuciones.
; Para ensamblar: nasm -f elf64 -o evanz1902.o evanz1902.s
; Para linkear y generar el ejecutable: ld -o evanz1902 evanz1902.o -lc --dynamic-linker=/lib64/ld-linux-x86-64.so.2
; ======================================================================================================================



extern printf       ; Se usa para llamar a la función printf de libc.

; ===========================================================================
; Sección de código, con permisos de lectura y ejecución
; ===========================================================================
section .text
global _start

; Como primer ejemplo, vamos a crear una función que imprima un string por pantalla,
; caracter por caracter, hasta que encuentre un byte núlo, en cuyo caso terminaremos de imprimir y saldremos.
; Va a recibir en RDI la dirección de un string y va a devolver en RAX la cantidad de bytes que ha escrito en la terminal.
;
mi_print:
  mov r8, rdi           ; r8 contendrá la dirección base del string que le pasemos.
  xor rbx, rbx          ; Limpiamos rbx para iterar sobre el string, hasta llegar al byte núlo.

.loop:                  ; Una etiqueta que vamos a usar para saltar hasta lleguemos al byte núlo. Empieza por punto porque es una etiqueta local a esta función.
  cmp byte [r8 + rbx], 0
  jz .end
  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [r8 + rbx]
  mov rdx, 1
  syscall
  inc rbx
  jmp .loop
.end:
  mov rax, rbx          ; Devolvemos cuantos bytes hemos escrito, almacenados en rbx. Por convención el valor se devuelve siempre en rax.
  ret                   ; Y retornamos a donde fue llamada esta función


; Función sin parámetros, sin valor de retorno.
; Vamos a llamar a nuestra primera función, imprimiremos por pantalla "Función sin parámetros.".
mi_funcion_sin_parametros:
  mov rdi, mi_string_2
  call mi_print
  ret

; Función que recibe 2 números en RDI, RSI, los suma e imprime su resultado por pantalla.
; En este caso vamos a usar el stack para almacenar los valores que recibimos.
; El stack lo podemos pensar como memoria para "variables locales".
; Dentro de la función creamos un stack frame, un espacio en el stack para nuestra función, que luego cuando la ejecución de la función termine,
; restauraremos a su estado anterior. De esta manera definimos una porción de memoria temporal que luego liberaremos para su posterior uso por cualquier
; parte de nuestro programa.
; Hay que tener en cuenta, que si bien es una memoria que podemos usar a nuestro antojo, debemos dejar RBP y RSP en su estado anterior, puesto que 
; cada función puede tener datos guardados en ella, ademas de que se guarda el punto de retorno en el stack, y si no lo restauramos, estaremos corrompiendo
; los datos que funciones anteriores tengan guardadas en el stack.
funcion_con_parametros:
  push rbp                    ; Guardamos RBP en el stack, para luego restaurar su valor.
  mov rbp, rsp                ; Apuntamos al final del stack.
  sub rsp, 32                 ; Y reservamos 32 bytes. Es importante notar que para poder llamar a funciones, el stack debe estar alineado a 16 bytes,
                              ; es por eso que reservamos 32 bytes a pesar de sólo usar 24 bytes. Si no fuerámos a llamar a ninguna función dentro de esta,
                              ; podríamos simplemente reservar 24 bytes.

  mov [rbp - 32], rdi         ; Guardamos el primer valor que le pasamos a la función en el stack.
  mov [rbp - 24], rsi         ; Lo mismo con el segundo. 

  add rdi, rsi                ; Sumamos ambos valores
  mov [rbp - 16], rdi         ; Y guardamos el resultado en el stack.

  lea rdi, [printf_mask]      ; Nos preparamos para llamar a printf
  mov rsi, [rbp - 32]         ; Cargamos en rsi, el primer valor que le pasamos a la función
  mov rdx, [rbp - 24]         ; El segundo valor
  mov rcx, [rbp - 16]         ; Y el resultado de la suma
  call printf

  add rsp, 32                 ; Restauramos RSP a su valor inicial. Ahora RSP apunta a donde guardamos RBP.
  pop rbp                     ; Y restauramos RBP a su valor anterior. Ahora tanto RBP como RSP apuntan al stack frame de la función desde donde
                              ; se llamó a esta función.
  ret                         ; Y retornamos.


; Función con parámetros y valor de retorno.
; Por convención, en linux x86-64 el valor de retorno siempre se carga en RAX.
; De esta manera, quien llama a una función, puede revirar el valor de RAX luego de la llamada.
; va a recibir dos números, y devolver la suma.
funcion_con_retorno:
  mov rax, rdi
  add rax, rsi
  ret


; =============================================================
; Ejercicio extra
; =============================================================

; Funciones auxiliares

; divide_counter recibe en rbx el divisor.
divide_counter:
  xor rdx, rdx
  mov rax, [counter]
  div rbx
  ret

; Y nuestra función.
ejercicio_extra:
  push rbp
  mov rbp, rsp

.main_loop:
  inc dword [counter]
  cmp dword [counter], 101
  je .end

  mov rbx, 3
  call divide_counter
  push rdx
  mov rbx, 5
  call divide_counter
  push rdx

  pop rbx
  pop rax

  cmp rax, rbx
  jne .test_individual

  cmp rax, 0
  je .print_ambos
  jne .print_number

.print_3:
  mov rdi, printf_str_mask
  mov rsi, string1
  call printf
  jmp .main_loop

.print_5:
  mov rdi, printf_str_mask
  mov rsi, string2
  call printf
  jmp .main_loop

.print_ambos:
  mov rdi, string1
  call mi_print
  mov rdi, string2
  call mi_print
  mov rdi, new_line
  call mi_print
  jmp .main_loop

.print_number:
  mov rdi, printf_num_mask
  mov rsi, qword [counter]
  call printf
  jmp .main_loop

.test_individual:
  test rax, rax
  jz .print_3
  test rbx, rbx
  jz .print_5
  jmp .print_number

.end:
  pop rbp
  ret



; Entry point de nuestro programa
_start:
  lea rdi, [mi_string]
  call mi_print       ; Y aquí llamamos a nuestra función.
  call mi_funcion_sin_parametros
  mov rdi, 10
  mov rsi, 20
  call funcion_con_parametros
  mov rdi, 30
  mov rsi, 20
  call funcion_con_retorno
  lea rdi, [printf_ret_mask]
  mov rsi, rax
  call printf

  call ejercicio_extra


; Terminamos la ejecucion
; Declaro una etiqueta en caso de querer salir prematuramente del programa. Si no se llama antes,
; _start llegará a este punto igualmente.
exit_proc:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall





; ===========================================================================
; Sección de datos inicializados con permisos de sólo lectura.
; ===========================================================================
section .rodata
  SYS_exit: equ 60
  SYS_write: equ 1
  STDOUT: equ 1
  mi_string: db "Hola desde una función!", 0x0A, 0x00
  mi_string_2: db "Función sin parámetros", 0x0A, 0x00
  printf_mask: db "Función con parámetros: %d + %d = %d", 0x0A, 0x00
  printf_ret_mask: db "Funcion con retorno: %d", 0x0A, 0x00
  printf_num_mask: db "%d", 0x0A, 0x00
  printf_str_mask: db "%s", 0x0A, 0x00

; Variables para el ejercicio extra
  string1: db "Fizz", 0x00
  string2: db "Buzz", 0x00
  new_line: db 0x0A, 0x00


; ===========================================================================
; Sección de datos inicializados con permisos de lectura y escritura.
; ===========================================================================
section .data
  counter: dd 0



; ===========================================================================
; Sección de datos no inicializados con permisos de lectura y escritura.
; ===========================================================================
section .bss
  var_result: resq 1
