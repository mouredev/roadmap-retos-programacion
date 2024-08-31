; https://nasm.us

; ================================================
; 15 - ASINCRONÍA
; ================================================
;
; Tal vez el ejercicio más difícil hasta el momento.
; En ensamblador, debemos de crear un thread cada vez que querramos correr código de manera
; asíncrona, y para eso usaré la syscall "fork".
; A diferencia de otros lenguajes, cada vez que creamos un thread con fork, se crea una cópia del proceso, y el thread continuará su ejecución
; en la instrucción siguiente al syscall.
; Por suerte, podemos diferenciar si estamos en el proceso padre, o en un proceso hijo gracias a que la llamada a fork,
; devuelve en RAX: 0 en el proceso hijo (thread ó child), y el PID del thread en el proceso padre,
; con lo que comprobando RAX, podemos saltar a una parte u ótra del código.
; Otra cuestión a tener en cuenta, es que el proceso padre va a finalizar independiente a si el thread terminó o no su ejecución, con lo que
; deberemos de indicarle al proceso padre que "espere" a que todos los threads creados finalizen antes de terminar.


SYS_write equ 1
SYS_nanosleep equ 35
SYS_fork equ 57
SYS_exit equ 60
SYS_wait4 equ 61
SYS_time equ 201
SYS_clock_gettime equ 228
SYS_waitid equ 247
STDIN equ 0
STDOUT equ 1
STDERR equ 2

%define WNOHANG 1
%define WEXITED 4
%define OPTIONS WNOHANG | WEXITED
%define get_month(index) [months + index]

global _start
extern printf
section .text

_start:
  mov rax, SYS_fork
  syscall
  cmp rax, 0
  je call_task


  mov rax, SYS_fork
  syscall
  cmp rax, 0
  je funcA
  mov rax, SYS_fork
  syscall
  cmp rax, 0
  je funcB
  mov rax, SYS_fork
  syscall
  cmp rax, 0
  je funcC
  
.loop:
  xor r8, r8
  mov r10, OPTIONS
  xor rdx, rdx
  xor rsi, rsi
  xor rdi, rdi
  mov rax, SYS_waitid
  syscall
  cmp rax, 0
  je .loop
  jmp funcD

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall


funcA:
  lea rdi, [mask2_start]
  lea rsi, [funcA_name]
  mov rdx, 1
  call printf
  mov qword [timer + ts.tv_sec], 1
  mov rax, SYS_nanosleep
  lea rdi, [timer]
  syscall
  lea rdi, [mask2_end]
  lea rsi, [funcA_name]
  call printf
  jmp _exit

funcB:
  lea rdi, [mask2_start]
  lea rsi, [funcB_name]
  mov rdx, 2
  call printf
  mov qword [timer + ts.tv_sec], 2
  mov rax, SYS_nanosleep
  lea rdi, [timer]
  syscall
  lea rdi, [mask2_end]
  lea rsi, [funcB_name]
  call printf
  jmp _exit

funcC:
  lea rdi, [mask2_start]
  lea rsi, [funcC_name]
  mov rdx, 3
  call printf
  mov qword [timer + ts.tv_sec], 3
  mov rax, SYS_nanosleep
  lea rdi, [timer]
  syscall
  lea rdi, [mask2_end]
  lea rsi, [funcC_name]
  call printf
  jmp _exit

funcD:
  lea rdi, [mask2_start]
  lea rsi, [funcD_name]
  mov rdx, 1
  call printf
  mov qword [timer + ts.tv_sec], 1
  mov rax, SYS_nanosleep
  lea rdi, [timer]
  syscall
  lea rdi, [mask2_end]
  lea rsi, [funcD_name]
  call printf
  jmp _exit

call_task:
  lea rdi, [task1_name]
  mov rsi, 3
  call task
  jmp _exit

task:
  enter 16, 0
  mov qword [rbp - 16], rdi
  mov qword [rbp - 08], rsi
  mov rax, SYS_clock_gettime
  xor rdi, rdi
  lea rsi, [epoch]
  syscall
  mov rdi, [epoch + ts.tv_sec]
  lea rsi, [date]
  call get_date
  lea rdi, [mask_start]
  mov rsi, [rbp - 16]
  mov rdx, [rbp - 08]
  mov rcx, [date + tm.tm_hour]
  mov r8, [date + tm.tm_min]
  mov r9, [date + tm.tm_sec]
  call printf
  mov rax, [rbp - 08]
  mov qword [timer + ts.tv_sec], rax
  mov qword [timer + ts.tv_nsec], 0
  mov rax, SYS_nanosleep
  lea rdi, [timer]
  xor rsi, rsi
  syscall
  mov rax, SYS_clock_gettime
  xor rdi, rdi
  lea rsi, [epoch]
  syscall
  mov rdi, [epoch + ts.tv_sec]
  lea rsi, [date]
  call get_date
  lea rdi, [mask_end]
  mov rsi, [rbp - 16]
  mov rdx, [date + tm.tm_hour]
  mov rcx, [date + tm.tm_min]
  mov r8, [date + tm.tm_sec]
  call printf
leave
  ret

; RDI: fecha en segundos.
; RSI: puntero a struct tm
get_date:
  enter 16, 0
  mov [rbp - 16], rdi
  mov r15, rsi

  ; Segundos
  mov rax, [rbp - 16]
  xor rdx, rdx
  mov rbx, 60
  div rbx
  mov qword [imin], rax
  xor rdx, rdx
  mul rbx
  mov rbx, [rbp - 16]
  sub rbx, rax
  mov qword [r15 + tm.tm_sec], rbx

  ; Minutos
  mov rax, qword [imin]
  xor rdx, rdx
  mov rbx, 60
  div rbx
  mov qword [ihrs], rax
  xor rdx, rdx
  mov rbx, 60
  mul rbx
  mov rbx, qword [imin]
  sub rbx, rax
  mov qword [r15 + tm.tm_min], rbx

  ; Hora
  mov rax, qword [ihrs]
  xor rdx, rdx
  mov rbx, 24
  div rbx
  mov qword [iday], rax
  xor rdx, rdx
  mov rbx, 24
  mul rbx
  mov rbx, qword [ihrs]
  sub rbx, rax
  mov qword [r15 + tm.tm_hour], rbx

  ; Fecha
  add qword [iday], 365
  add qword [iday], 366
  mov rax, qword [iday]
  xor rdx, rdx
  mov rbx, ((4 * 365) + 1)
  div rbx
  mov qword [lday], rax
  mov qword [qday], rdx
  cmp qword [qday], 60
  jl .l1
  inc qword [lday]
.l1:
  mov rax, qword [iday]
  sub rax, qword [lday]
  xor rdx, rdx
  mov rbx, 365
  div rbx
  mov qword [iyrs], rax
  mov rdx, 365
  mul rdx
  mov rbx, qword [iday]
  sub rbx, rax
  sub rbx, qword [lday]
  mov qword [jday], rbx
  cmp qword [qday], 365
  ja .l2
  cmp qword [qday], 60
  jl .l2
  inc qword [jday]
.l2:
  lea rdi, [r15 + tm.tm_year]
  lea rsi, [iyrs]
  movsq
  add qword [r15 + tm.tm_year], 1968
  mov qword [r15 + tm.tm_mon], 13
  mov qword [mday], 366
.while:
  mov rax, qword [jday]
  mov rbx, qword [mday]
  cmp rax, rbx
  jae .end_while
  dec qword [r15 + tm.tm_mon]
  mov rax, [r15 + tm.tm_mon]
  mov rdx, 8
  mul rdx
  mov rbx, get_month(rax)
  mov qword [mday], rbx
  cmp qword [r15 + tm.tm_mon], 2
  jl .endif
  mov rax, [r15 + tm.tm_year]
  xor rdx, rdx
  mov rbx, 4
  div rbx
  test rdx, rdx
  jnz .endif
  inc qword [mday]
.endif:
  jmp .while
.end_while:
  mov rax, qword [jday]
  sub rax, qword [mday]
  inc rax
  mov qword [r15 + tm.tm_mday], rax
  inc qword [r15 + tm.tm_mon]
  leave
  ret


section .rodata
  months: dq 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
  task1_name: db "task1", 0x00
  mask_start: db "Task name: %s - Duration: %usecs - Start: %02u:%02u:%02u", 0x0A, 0x00
  mask_end: db "Task name: %s - End: %02u:%02u:%02u", 0x0A, 0x00

  mask2_start: db "Function [%s] STARTED. Duration :%02u seconds", 0x0A, 0x00
  mask2_end: db "Function [%s] FINISHED.", 0x0A, 0x00

  funcA_name: db "Function A", 0x00
  funcB_name: db "Function B", 0x00
  funcC_name: db "Function C", 0x00
  funcD_name: db "Function D", 0x00

section .data
  struc ts
    .tv_sec: resq 1
    .tv_nsec: resq 1
  endstruc

  struc tm
    .tm_sec:  resq 1  ; segundos [0 - 60]
    .tm_min:  resq 1  ; minutos [0 - 59]
    .tm_hour: resq 1  ; hora [0 - 23]
    .tm_mday: resq 1  ; día del mes [1, 31]
    .tm_mon:  resq 1  ; mes [0 - 11] (enero = 0)
    .tm_year: resq 1  ; año
    .tm_wday: resq 1  ; día de la semana [0 - 6] (domingo = 0)
    .tm_yday: resq 1  ; día del año [0 - 365]
  endstruc

section .bss
  timer: resb ts_size
  epoch: resb ts_size
  date: resb tm_size
  imin: resq 1
  ihrs: resq 1
  iday: resq 1
  lday: resq 1
  qday: resq 1
  iyrs: resq 1
  jday: resq 1
  mday: resq 1
