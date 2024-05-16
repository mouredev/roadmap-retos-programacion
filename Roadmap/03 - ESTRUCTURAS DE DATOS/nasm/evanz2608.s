; https://nasm.us


SYS_exit: equ 60
SYS_read: equ 0
SYS_write: equ 1
SYS_open   equ 2
SYS_close  equ 3
STDIN: equ 0
STDOUT: equ 1
STDERR: equ 2

O_CREAT:   equ 0q0100
O_RDWR:    equ 2
MODE:      equ 0q0666

%macro get_offset 1
  mov rax, %1
  mov rdx, Contact_size
  mul rdx
%endmacro

%define get_field(offset, field) Contacts + offset + Contact. %+ field

extern memset
extern printf
global _start

section .text
_start:

  mov rdi, CLEAN_MSG
  call printstring
  mov rdi, printf_mask
  mov rsi, [Contacts_index]
  mov rdx, [Contacts_capacity]
  call printf

  mov rdi, MENU_MSG
  call printstring

  mov rdi, option
  mov rsi, 1
  call readstring

  cmp byte [option], '1'
  je .insert_contact
  cmp byte [option], '2'
  je .search_contact
  cmp byte [option], '3'
  je .update_contact
  cmp byte [option], '4'
  je .delete_contact
  cmp byte [option], '5'
  je .save_list
  cmp byte [option], '6'
  je _exit
  jmp .bad_option

.save_list:
  mov rax, SYS_open
  lea rdi, [filepath]
  mov rsi, O_CREAT
  or rsi, O_RDWR
  mov rdx, MODE
  syscall
  cmp rax, 0
  jb .failed
  mov [fd], rax

  mov rax, SYS_write
  mov rdi, [fd]
  lea rsi, [Contacts]
  mov rdx, Contact_size * CONTACT_MAX
  syscall

  mov rax, SYS_close
  mov rdi, [fd]
  syscall
  jmp _start
.failed:
  mov rdi, FAILED_MSG
  call printstring
  jmp _exit

.insert_contact:
  mov rdi, CLEAN_MSG
  call printstring
  mov rdi, INSERT_MENU
  call printstring
  cmp byte [Contacts_capacity], CONTACT_MAX
  jae .array_full
  mov rdi, NAME_MSG
  call printstring
  get_offset [Contacts_capacity]
  lea rdi, [get_field(rax, name)]
  mov rsi, 0x00
  mov rdx, NAME_LEN
  call memset
  get_offset [Contacts_capacity]
  lea rdi, [get_field(rax, name)]
  mov rsi, NAME_LEN
  call readstring
  mov rdi, PHONE_MSG
  call printstring
  get_offset [Contacts_capacity]
  lea rdi, [get_field(rax, phone)]
  mov rsi, PHONE_LEN
  call readstring
  mov rax, [Contacts_capacity]
  mov [Contacts_index], rax
  inc rax
  mov [Contacts_capacity], rax
  jmp .insert_done
.array_full:
  mov rdi, FULL_ARRAY_MSG
  call printstring
.insert_done:
  jmp _start

.search_contact:
  mov rdi, CLEAN_MSG
  call printstring
  mov rdi, SEARCH_MENU
  call printstring
  mov rdi, NAME_MSG
  call printstring
  mov rdi, input_buffer
  mov rsi, NAME_LEN
  call readstring
  mov [Input_length], rax
  xor rbx, rbx
  mov qword [Contact_found], 0
.loop_search:
  cld
  get_offset rbx
  lea rdi, [get_field(rax, name)]
  lea rsi, [input_buffer]
  mov rcx, [Input_length]
  repe cmpsb
  je .search_found
  inc rbx
  cmp rbx, [Contacts_capacity]
  jl .loop_search
  jae .search_not_found
.search_found:
  mov [Contact_found], rbx
  mov rdi, FOUND_MSG
  call printstring
  mov rdi, NAME_MSG
  call printstring
  get_offset [Contact_found]
  lea rdi, [get_field(rax, name)]
  call printstring
  mov rdi, LINEFEED
  call printstring
  mov rdi, PHONE_MSG
  call printstring
  get_offset [Contact_found]
  lea rdi, [get_field(rax, phone)]
  call printstring
  mov rdi, LINEFEED
  call printstring
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start
.search_not_found:
  mov rdi, NOT_FOUND_MSG
  call printstring
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start

.update_contact:
  mov rdi, CLEAN_MSG
  call printstring
  mov rdi, UPDATE_MENU
  call printstring
  mov rdi, NAME_UPDATE_MSG
  call printstring
  mov rdi, input_buffer
  mov rsi, 0x00
  mov rdx, NAME_LEN + 1
  call memset
  mov rdi, input_buffer
  mov rsi, NAME_LEN
  call readstring
  mov [Input_length], rax
  xor rbx, rbx
  mov qword [Contact_found], 0
.update_search:
  cld
  get_offset rbx
  lea rdi, [get_field(rax, name)]
  lea rsi, [input_buffer]
  mov rcx, [Input_length]
  repe cmpsb
  je .update_found
  inc rbx
  cmp rbx, [Contacts_capacity]
  jl .update_search
  jae .update_not_found
.update_found:
  mov [Contact_found], rbx
  mov rdi, NAME_MSG
  call printstring
  get_offset [Contact_found]
  lea rdi, [get_field(rax, name)]
  mov rsi, NAME_LEN
  call readstring
  mov rdi, PHONE_MSG
  call printstring
  get_offset [Contact_found]
  lea rdi, [get_field(rax, phone)]
  mov rsi, PHONE_LEN
  call readstring
  mov rdi, UPDATED_MSG
  call printstring
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start
.update_not_found:
  mov rdi, NOT_FOUND_MSG
  call printstring
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start

.delete_contact:
  mov rdi, DELETE_MENU
  call printstring
  mov rdi, NAME_DELETE_MSG
  call printstring
  mov rdi, input_buffer
  mov rsi, 0x00
  mov rdx, NAME_LEN + 1
  call memset
  mov rdi, input_buffer
  mov rsi, NAME_LEN
  call readstring
  mov [Input_length], rax
  xor rbx, rbx
  mov qword [Contact_found], 0
.delete_search:
  cld
  get_offset rbx
  lea rdi, [get_field(rax, name)]
  lea rsi, [input_buffer]
  mov rcx, [Input_length]
  repe cmpsb
  je .delete_found
  inc rbx
  cmp rbx, [Contacts_capacity]
  jl .delete_search
  jae .delete_not_found
.delete_found:
  mov [Contact_found], rbx
.delete_move_loop:
  mov rbx, [Contact_found]
  cmp rbx, [Contacts_capacity]
  jae .delete_done
  get_offset rbx
  lea rdi, [Contacts + rax]
  inc rbx
  get_offset rbx
  lea rsi, [Contacts + rax]
  mov rcx, Contact_size
  rep movsb
  inc qword [Contact_found]
  cmp qword [Contact_found], CONTACT_MAX
  jl .delete_move_loop
  jmp .delete_done
.delete_not_found:
  mov rdi, NOT_FOUND_MSG
  call printstring
.delete_done:
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start

.bad_option:
  mov rdi, BAD_OPTION_MENU
  call printstring
  lea rdi, [rsp]
  mov rsi, 1
  call readstring
  jmp _start

_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall


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

readstring:
  enter 1, 0
  mov rbx, rdi
  mov r13, rsi
  xor r12, r12
.read_character:
  mov rax, SYS_read
  mov rdi, STDIN
  lea rsi, byte [rbp]
  mov rdx, 1
  syscall
  mov al, byte [rbp]
  cmp al, 0x0A
  je .read_done
  cmp r12, r13
  inc r12
  jae .read_character
  mov byte [rbx], al
  inc rbx
  jmp .read_character
.read_done:
  mov byte [rbx], 0x00
  mov rax, r12
  leave
  ret

section .rodata
  NAME_LEN: equ 50
  PHONE_LEN: equ 10
  CONTACT_MAX: equ 100
  CLEAN_MSG:
    db  0x1B, "[H", 0x1B, "[0J", 0x00
  MENU_MSG:
    db  "Agenda de Contactos", 0x0A
    db  " 1. Insertar contacto.", 0x0A
    db  " 2. Buscar contacto.", 0x0A
    db  " 3. Actualizar contacto.", 0x0A
    db  " 4. Eliminar contacto.", 0x0A
    db  " 5. Guardar lista.", 0x0A
    db  " 6. Salir.", 0x0A
    db  0x0A, "Seleccione una opcion: ", 0x00

  INSERT_MENU: db "Insertar contacto", 0x0A, 0x00
  SEARCH_MENU: db "Buscar contacto", 0x0A, 0x00
  UPDATE_MENU: db "Actualizar contacto", 0x0A, 0x00
  DELETE_MENU: db "Eliminar contacto", 0x0A, 0x00
  BAD_OPTION_MENU: db "Opcion incorrecta. Por favor elija una opcion valida.", 0x0A, 0x00

  NAME_MSG: db "  Nombre: ", 0x00
  NAME_UPDATE_MSG: db "  Nombre del contacto a actualizar: ", 0x00
  NAME_DELETE_MSG: db "  Nombre del contacto a eliminar: ", 0x00
  PHONE_MSG: db "  Telefono: ", 0x00
  FULL_ARRAY_MSG: db "No queda espacio suficiente para añadir mas contactos.", 0x0A, "Presione una tecla para continuar.", 0x00
  FOUND_MSG: db "Contacto encontrado", 0x0A, 0x00
  NOT_FOUND_MSG: db "Contacto no encontrado", 0x00
  UPDATED_MSG: db "Contacto actualizado", 0x00
  DELETED_MSG: db "Contacto eliminado", 0x00
  FAILED_MSG: db "Error al abrir el archivo.", 0x00
  LINEFEED: db 0x0A, 0x00
  printf_mask: db "Index: %d - Capacity: %d", 0x0A, 0x00
  filepath: db "./list.bin", 0x00

section .data
  struc Contact
    .name: resb NAME_LEN + 1
    .phone: resb PHONE_LEN + 1
  endstruc

  Input_length: dq 0
  option: dq 0
  Contacts_index: dq 0
  Contacts_capacity: dq 0
  Contact_found: dq 0
  offset1: dq 0
  offset2: dq 0
  fd: dq 0

section .bss
  input_buffer: resb NAME_LEN + 1
  Contacts: resb CONTACT_MAX * Contact_size
