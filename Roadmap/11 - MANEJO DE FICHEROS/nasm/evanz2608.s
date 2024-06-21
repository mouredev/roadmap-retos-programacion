; https://nasm.us

; =======================================================
; Ejercicio 11 - MANEJO DE FICHEROS
; =======================================================
;
; Para manejar ficheros en ensamblador, necesitamos hacer una llamada al sistema que lo gestione por nosotros,
; de manera que será el propio sistema el que creará, abrirá y cerrará el fichero que nosotros queramos.
; Evidentemente, al ser código dependiente del sistema operativo, el proceso será distinto en linux, windows, mac, etc...
; como yo estoy en linux de 64 bits, mi código está escrito para esta plataforma, y no funcionará en otros OS ni en linux de 32 bits.
;
; Una vez abierto el fichero, el sistema nos devolverá un file descriptor que usaremos para luego poder escribir y leer en él, y una vez
; hemos terminado, vamos a hacer ótra llamada al sistema para que cierre el fichero.
; Al momento de abrir un archivo, necesitámos pasarle al sistema el nombre del archivo a abrir, un integer a modo de "flags", que le indíca cómo debe de ser
; abierto el fichero (abrir para sólo lectura, sólo escritura, lectura/escritura, si debe crearlo en caso de no existir, etc..) y por último, el modo (cuando
; especificámos la flag O_CREAT, el fichero será creado si no existe, y el modo se usa para setear los permisos que tendrá el fichero nuevo. Es ignorado si el fichero
; existe).
;
;   - File descriptor: https://es.wikipedia.org/wiki/Descriptor_de_archivo


SYS_read:   equ 0
SYS_write:  equ 1
SYS_open:   equ 2
SYS_close:  equ 3
SYS_lseek:  equ 8
SYS_exit:   equ 60
SYS_unlink: equ 87
STDIN:      equ 0
STDOUT:     equ 1
STDERR:     equ 2
FLAGS:      equ 0q1102
MODE:       equ 0q0666
SEEK_SET:   equ 0
SEEK_CUR:   equ 1
SEEK_END:   equ 2


global _start
extern printf
extern memset
section .text

_start:
  call ejercicio

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall

; ========================
; Ejercicio
; ========================

ejercicio:
  mov rax, SYS_open
  mov rdi, filepath
  mov rsi, FLAGS
  mov rdx, MODE
  syscall
  cmp rax, 0
  js .fail_open
  mov qword [fd], rax
  mov rax, SYS_write
  mov rdi, [fd]
  lea rsi, [content]
  mov rdx, content_len
  syscall
  mov rax, SYS_lseek
  mov rdi, [fd]
  mov rsi, 0
  mov rdx, 0
  syscall
  mov rax, SYS_read
  mov rdi, [fd]
  lea rsi, [read_buffer]
  mov rdx, content_len
  syscall
  mov rax, SYS_close
  mov rdi, [fd]
  syscall
  lea rdi, [success_msg]
  lea rsi, [read_buffer]
  call printf
  jmp .done
.fail_open:
  lea rdi, [fail_msg]
  lea rsi, [filepath]
  call printf
.done:
  ret

printstring:
  mov rbx, rdi
  xor r12, r12
.print_char:
  cmp byte [rbx + r12], 0x00
  je .print_done
  mov rax, SYS_write
  mov rdi, STDOUT
  lea rsi, [rbx + r12]
  mov rdx, 1
  syscall
  inc r12
  jmp .print_char
.print_done:
  ret

section .rodata
  filepath: db "evanz2608.txt", 0x00

  content: db "Franco", 0x0A, "31", 0x0A, "Ensamblador, C/C++"
  content_len: equ $-content
  fail_msg: db "Failed to open/create file [%s]", 0x0A, 0x00
  success_msg: db "File content:", 0x0A, "%s", 0x0A, 0x00
  LF: db 0x0A

section .bss
  fd: resq 1
  read_buffer: resb content_len + 1
