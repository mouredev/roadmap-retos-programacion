; https://nasm.us/

; ====================================================================
; Ejercicio 04 - Cadenas de texto
; ====================================================================
;
; En ensamblador, existen sólo 5 instrucciones para el manejo de cadena de caracteres (strings)
; que son: MOVS, LODS, STOS, CMPS y SCAS.
; Cada una de las cuales tiene distintas variantes. Explico que hace cada una con un ejemplo.
;
; MOVS viene de MOV String. Sus variantes son MOVSB, MOVSW, MOVSD, MOVSQ, donde B viene de BYTE, W de WORD, D de DOUBLE WORD y Q de QUAD WORD.
; (recordemos que BYTE son 8 bits, WORD 16 bit, DOUBLEWORD 32 y QUADWORD 64).
; Esta instrucción mueve datos de una parte de la memoria a otra, y dependiendo de que variante se usa mueve los datos de 8 en 8 bits, de 16 en 16 etc...
; Esta misma lógica aplica para CMPS, con sus variantes CMPSB, CMPSW, CMPSD, CMPSQ
; CMPS viene de CMP Strings. Compara dos valores residentes en memoria, modificando RFLAGS acorde al resultado.
; LODS viene de LOAD String. Esta instrucción carga en el registro RAX desde la memoria. Se puede usar de dos maneras, sin operandos: usa como puntero a memoria
; al registro RSI. Si se usa alguna de sus variantes, entonces siempre se usa el registro RSI.
; STOS Viene de STORE String. Al contrario de LODS, esta instrucción guarda en memoria el valor de RAX. Si se usa STOSB entonces el valor almacenado es el registro AL,
; si se usa STOSW, se usa AX, etc...
; SCAS es igual a CMPS sólo que compara un valor en memoria con el registro RAX. Igual que las demas instrucciones, dependiendo de la variante, compara contra AL, AX, EAX, RAX.
; El resto, deberemos implementarlo por nuestra cuenta.
;
; Debo mencionar que NASM tiene 2 macros que se pueden usar para "manipular" cadenas de caracteres, aunque no me parecen muy útiles y sólo las voy a mencionar por completitud:
; %strlen <etiqueta> <string literal> crea una etiqueta con el largo en bytes de la cadena <string literal>. Aunque no se puede usar para calcular el largo de cadenas
; que tengamos guardadas en memoria, por lo que no la veo muy util.
; %substr <etiqueta> <string_literal> <index> crea una etiqueta con el valor del <string_literal> en la posicion <index>
; un ejemplo sería %substr mi_caracter "xyz" 1. En este caso se crea una etiqueta "mi_caracter" con el valor "x". Si en lugar de 1 usamos el 2, "mi_caracter" valdría "y".
; de nuevo, esta macro sólo funciona con cadenas de texto literales y no le podemos pasar cadenas que tengamos almacenadas en memoria.
;
; NOTA: tanto RDI como RSI son los registros que usan estas instrucciones usan para operar.
; el registro RDI es el registro de indice de destino, de ahí viene el DI: Destination Index. La R es la nomenclatura que se usa en x64. Existe tambien EDI, de 32 bits y DI de 16 bits
; al igual, el registor RSI es el registro de indice de fuente: SI de Source Index.
; De manera que siempre se usa RSI como el puntero a la memoria de la que vamos a leer, y RDI donde vamos a escribir.








SYS_write: equ 1  ; syscall para escribir.
SYS_exit: equ 60  ; syscall para terminar la ejecucion.

STDIN:  equ 0      ; entrada estandar, en este caso la consola.
STDOUT: equ 1     ; salida estandar, en este caso la consola.
STDERR: equ 2     ; salida de errores, en este caso también se muestra por consola.

global _start
extern printf
section .text

; Vamos a crear una función que nos devuelva el largo de un string.
; Le pasamos en RDI el puntero al string y nos devuelve en RAX el largo.
; Recordemos que todos los strings los vamos a terminar con un byte nulo.
strlen:
  xor rax, rax
.loop:
  cmp byte [rdi + rax], 0
  je .done
  inc rax
  jmp .loop
.done:
  ret



; Funcion que limpia el buffer apuntado por RDI.
; El largo se recibe en RSI
memset:
  test rsi, rsi
  jz .done
  mov rax, 0
  mov rcx, rsi
  cld
.next:
  stosb
  loop .next
.done:
  ret

; Función que invierte un string
; Recibe en RDI el puntero a la memoria donde se va a guardar el string invertido
; en RSI el string a invertir y en RCX la cantidad de bytes a invertir.
; La vamos a usar para computar los palindromos.
reverse:
  test rcx, rcx
  jz .done
  add rdi, rcx
  dec rdi
.next:
  cld
  lodsb
  std
  stosb
  loop .next 
.done:
  ret

; El entry point de nuestro programa
_start:
  ; Primero vamos a ver ejemplos de las instrucciónes antes mencionadas y sus variantes.
  ; para comparar, vamos siempre a imprimir por pantalla ambos strings.

.movs_rep:
  ; Empecemos con MOVS, vamos a copiar word1 en buffer1.
  ; RDI es el puntero a la memoria destino, y RSI es el puntero a la cadena fuente.
  lea rdi, [buffer1]
  lea rsi, [word1]
  movsb
  ; En este caso sólo copiamos 1 byte, con lo cual buffer1 contiene solamente "r".
  lea rdi, [printf_mask]
  lea rsi, [word1]
  lea rdx, [buffer1]
  call printf

  ; Existe un modificador que nos facilita el copiar múltiples bytes sin tener que crear un loop.
  ; REP va a repetir la última instrucción, y se tiene que cargar en RCX el número de repeticiones que queremos realizar.
  ; MOVS luego de copiar el byte, incrementa o decrementa tanto RDI como RSI 1 byte si usamos MOVSB, 2 bytes si usamos MOVSW, 4 con MOVSD y 8 con MOVSQ.
  ; El incremento o decremento depende de RFLAGS, en específico el Flag de Direccion (DF). Si esta en 1 decrementa, si está a 0 incrementa.
  ; Ahora vamos a copiar word1 completo a buffer1 usando REP y limpiando, (poniendo a 0) el flag de dirección para incrementar los punteros.

  lea rdi, [word1]
  call strlen
  mov rcx, rax
  lea rdi, [buffer1]
  lea rsi, [word1]
  cld
  rep movsb
  ; Ahora buffer1 contiene "radar", igual que word1. y rcx en este punto vale 0
  lea rdi, [printf_mask]
  lea rsi, [word1]
  lea rdx, [buffer1]
  call printf

  ; Ahora que tanto word1 como buffer1 contienen el mismo string, vamos a probar CMPS, para ver si son iguales.
  ; Del mismo modo que, REP MOVSB repite la operación de copia, podemos usar REP CMPSB para repetir la comprobación en todos los bytes del string.
  ; Existen 2 variantes de REP que nos son útiles en este caso. REPE y REPNE. También existen REPZ y REPNZ que son equivalentes a las 2 anteriores.
  ; REPE significa (REPeat while Equal) y, obviamente, REPNE es (REPeat while Not Equal).
  ; REPE va a repetir la instrucción hasta que la comparación no sea igual, ó hasta que RCX llegue a 0, por lo que es fácil comprobar strings.
  ; Un detalle a tener en cuenta, es que CMPSB modifica el flag zero (ZF) en cada iteración, con lo cual, podemos comprobar el flag
  ; luego de que termina la instrucción, en este caso JE viene de Jump Equal, que salta a .equal en caso de estar ZF en 1.

.cmps_rep:
  lea rdi, [word1]
  call strlen
  mov rcx, rax
  lea rdi, [word1]
  lea rsi, [buffer1]
  repe cmpsb
  je .equal     ; si la comparación falla, la ejecución continua en la siguiente instrucción, si no falla, entonces saltamos a .equal.
  lea rdi, [not_equal_mask]
  lea rsi, [buffer1]
  lea rdx, [word1]
  call printf
  jmp .lods_stos
.equal:
  lea rdi, [equal_mask]
  lea rsi, [buffer1]
  lea rdx, [word1]
  call printf
  jmp .lods_stos

.lods_stos:
  ; Vamos ahora con LODS. Esta instrucción carga en RAX, un valor en la memoria apuntada por RSI.
  ; Usada en conjunto con STOS sirven para iterar en un string y manipular cada caracter uno por vez.
  ; Un ejemplo sería convertir minúsculas a mayúsculas.

  ; primero voy a copiar word1 en buffer1 para no destruir el valor en word1.
  lea rdi, [word1]
  call strlen
  mov rcx, rax
  lea rdi, [buffer1]
  lea rsi, [word1]
  cld
  rep movsb

  ; Para pasar un caracter en minuscula a mayuscula, vamos a setear el bit 6 del byte a 0. Esto porque entre un caracter en minuscula y el mismo en mayuscula solo es
  ; este bit.
  ; Un ejemplo: el valor del caracter ascii "A" es 0x41, en binario: 0b01000001 y el valor de "a" es 0x61, en binario 0b01100001

  ; Ahora que tengo el string copiado en buffer1, vamos a iterar cada byte, cambiar este bit cuando sea necesario, y guardarlo de nuevo en buffer1.
  lea rdi, [buffer1]
  call strlen
  mov rcx, rax
  lea rsi, [buffer1]
  mov rdi, rsi
  cld
%define BIT_MASK 0b11011111
.next:
  lodsb             ; Cargo en al, el siguiente byte, (LODSB incrementa RSI al igual que MOVSB).
  and al, BIT_MASK  ; Si el bit 6 es 0, lo dejo en 0, si es uno, lo cambio a 0.
  stosb             ; y guardo el byte en la posicion de memoria apuntada por RDI. (STOS incrementa RDI al igual que MOVSB)
  loop .next        ; Repito hasta que rcx sea 0. (antes del loop, cargamos en rcx el largo de buffer1).

  ; Una vez terminamos, imprimo. Ahora buffer1 debería contener "RADAR" y word1 "radar".
  lea rdi, [printf_mask]
  lea rsi, [word1]
  lea rdx, [buffer1]
  call printf


; ============================================================================
; Ejercicio extra
; ============================================================================

; Para el ejercicio extra voy a crear unas funciones mas abajo.

  lea rdi, [buffer1]
  mov rsi, 0
  mov rdx, BUFFER_LEN
  call memset
  lea rdi, [word1]
  call strlen
  mov rcx, rax
  lea rdi, [buffer1]
  lea rsi, [word1]
  mov rdx, rcx
  call palindromos

  lea rdi, [buffer2]
  mov rsi, 0
  mov rdx, BUFFER_LEN
  call memset
  lea rdi, [word2]
  call strlen
  mov rcx, rax
  lea rdi, [buffer2]
  lea rsi, [word2]
  mov rdx, rcx
  call palindromos

  lea rdi, [word1]
  lea rsi, [word2]
  call anagramas

  lea rdi, [word2]
  call isogramas
  lea rsi, [word2]
  jz .is_isogram
  jmp .is_not_isogram

.is_isogram:
  lea rdi, [is_isogram_mask]
  call printf
  jmp _exit

.is_not_isogram:
  lea rdi, [is_not_isogram_mask]
  call printf

; Terminamos la ejecución.
_exit:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall


; ============================================================================
; Funciones para el ejercicio extra
; ============================================================================

; RDI: puntero destino
; RSI: puntero fuente
copy:
  enter 16, 0
  mov [rbp - 8], rdi
  mov [rbp - 16], rsi

  mov rdi, rsi
  call strlen
  mov rcx, rax

  mov rdi, [rbp - 8]
  mov rsi, [rbp - 16]
  cld
  rep movsb
  leave
  ret
  
palindromos:
  enter 32, 0
  mov rcx, rdx
  mov [rbp - 0], rdi
  mov [rbp - 8], rsi
  mov [rbp - 16], rcx
  call reverse
  mov rdi, [rbp - 0]
  mov rsi, [rbp - 8]
  mov rcx, [rbp - 16]
  cld
  repe cmpsb
  je .is_palim
  mov rdx, [rbp - 0]
  mov rsi, [rbp - 8]
  lea rdi, [is_not_palim_mask]
  call printf
  jmp .done
.is_palim:
  mov rdx, [rbp - 0]
  mov rsi, [rbp - 8]
  lea rdi, [is_palim_mask]
  call printf
.done:
  leave
  ret

; Una forma fácil de saber si dos palabras son anagramas, es ordenar sus letras, y comparar ambas cadenas ordenadas.
; Si son iguales, entonces ambas palabras son anagramas, de lo contrario, no lo son.
; Puesto que en un anagrama, no importa si las letras son mayusculas o minusculas, pero a la hora de ordenarlas si,
; primero vamos a convertir todas las letras a minusculas, y luego recién ordenamos y comparamos.
; Recibe en RDI y RSI los punteros a los strings a comparar.
anagramas:
  enter 32, 0
  mov [rbp - 8], rdi
  mov [rbp - 16], rsi
  lea rdi, [buffer1]
  mov rsi, BUFFER_LEN
  call memset
  lea rdi, [buffer2]
  mov rsi, BUFFER_LEN
  call memset
  mov rdi, [rbp - 8]
  call lowercase
  mov rdi, [rbp - 16]
  call lowercase
  lea rdi, [buffer1]
  mov rsi, [rbp - 8]
  call copy
  lea rdi, [buffer1]
  call sort
  lea rdi, [buffer2]
  mov rsi, [rbp - 16]
  call copy
  lea rdi, [buffer2]
  call sort
  lea rdi, [buffer1]
  lea rsi, [buffer2]
  mov rcx, BUFFER_LEN
  cld
  repe cmpsb
  je .is_anagram
  lea rdi, [is_not_anagram_mask]
  mov rsi, [rbp - 8]
  mov rdx, [rbp - 16]
  call printf
  jmp .done
.is_anagram:
  lea rdi, [is_anagram_mask]
  mov rsi, [rbp - 8]
  mov rdx, [rbp - 16]
  call printf
.done:
  leave
  ret

; Para saber si una palabra es un isograma, podemos contar cuantas veces aparece cada letra, y luego comparar cada resultado
; Inicializamos un array de 25 bytes a 0, convertimos la palabra a minusculas y luego, cargamos cada letra en RAX, le restamos 0x61
; y usamos el resultado como indice para incrementar el array en esa posicion.
; NOTA: Los caracteres en minuscula en ascii empiezan con "a" = 0x61, "b" = 0x62 ... "z" = 0x7A. Al restarle 0x61, tenemos que "a" - 0x61 = 0
; "b" - 0x61 = 1 ... "z" - 0x61 = 25. Luego usamos este resultado como indice. Esta es la razon por la que vamos a convertir en minusculas primero.
; Por ultimo, compararemos el array con el primer valor distinto de 0 que encontremos. Si todos los demás valores del array son 0 ó igual al primer valor hallado,
; entonces tenemos un isograma.
; Pongo un ejemplo de cómo se vería el array con un isograma.
;
; Palabra: "diez"
;             a b c d e f g h i j k l m n o p q r s t u v w x y z
; Alphabet:   0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

; Como vemos, en este caso, todas las letras de la palabra solo aparecen una vez, y el resto está a 0.
; Comprobamos ahora desde el primer valor, si es cero seguimos, si es distinto de cero, lo almacenamos y seguimos comprobando
; ahora con el valor 1 (el primero distinto de cero que encontramos). Si no hay otro valor distinto de 0 que sea distinto de 1, entonces tenemos un isograma
; Si encontráramos cualquier otro valor distinto, entonces ya no sería un isograma. 
; Como ejemplo pongamos:
;

; Palabra: "jueves"
;             a b c d e f g h i j k l m n o p q r s t u v w x y z
; Alphabet:   0 0 0 0 2 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0
;
; Vemos como "e" aparece dos veces, y el resto sólo 1 vez.

; RDI = puntero al string a comprobar
isogramas:
  mov r12, rdi
  call lowercase
  mov rdi, r12
  mov rsi, r12
  call strlen
  mov rcx, rax
  xor r12, r12
  xor rax, rax
.count_loop:
  lodsb
  sub al, 0x61
  inc byte [alphabet + rax]
  cmp r12b, byte [alphabet + rax]
  jae .count_continue
  inc r12
.count_continue:
  dec rcx
  test rcx, rcx
  jnz .count_loop
  xor rcx, rcx
.compare_loop:
  movzx rbx, byte [alphabet + rcx]
  inc rcx
  cmp rbx, 0
  je .compare_loop
  cmp rbx, r12
  jne .compare_fail
  cmp rcx, 25
  jae .compare_done
  jmp .compare_loop
.compare_fail:
  mov rax, 1
  jmp .done
.compare_done:
  mov rax, 0
.done:
  ret


; Función que ordena un array de bytes de menor a mayor.
; Recibe en RDI el puntero al array a ordenar y en RSI el puntero donde almacenar
; el array ordenado. La vamos a usar para computar los anagramas.
sort:
  enter 16, 0
  call strlen
  mov rcx, rax
.outer_loop:
  dec rcx
  test rcx, rcx
  jz .end_sort
  mov rsi, rdi
  mov r12, rcx
.inner_loop:
  mov al, byte [rsi]
  mov bl, byte [rsi + 1]
  cmp al, bl
  jbe .no_swap
  mov byte [rsi], bl
  mov byte [rsi + 1], al
.no_swap:
  inc rsi
  dec r12
  jnz .inner_loop
  jmp .outer_loop
.end_sort:
  leave
  ret


; Función que convierte todos los caracteres de un string a minusculas.
; Recibe en RDI un puntero al string.
lowercase:
%define MIN_MASK 0b00100000
  enter 16, 0
  mov [rbp - 8], rdi
  call strlen
  mov rcx, rax
  mov rsi, [rbp - 8]
  mov rdi, rsi
  cld
.loop:
  lodsb
  or al, MIN_MASK
  stosb
  loop .loop
  leave
  ret
  

section .rodata
  BUFFER_LEN: equ 20
  
section .data
  word1: db "Radar", 0x00
  word2: db "Ensamblador", 0x00


  printf_mask: db "word1: %s", 0x0A, "word2: %s", 0x0A, 0x00
  equal_mask: db "word1 es igual a word2", 0x0A, "  word1: %s", 0x0A, "  word2: %s", 0x0A, 0x00
  not_equal_mask: db "word1 es distinta a word2", 0x0A, "  word1: %s", 0x0A, "  word2: %s", 0x0A, 0x00
  is_palim_mask: db "%s es palindromo. Su inverso es: %s", 0x0A, 0x00
  is_not_palim_mask: db "%s no es palindromo. Su inverso es: %s", 0x0A, 0x00
  is_anagram_mask: db "%s es anagrama de %s", 0x0A, 0x00
  is_not_anagram_mask: db "%s no es anagrama de %s", 0x0A, 0x00
  is_isogram_mask: db "%s es isograma.", 0x0A, 0x00
  is_not_isogram_mask: db "%s no es isograma.", 0x0A, 0x00

section .bss
  buffer1: resb BUFFER_LEN
  buffer2: resb BUFFER_LEN
  alphabet: resb 25
