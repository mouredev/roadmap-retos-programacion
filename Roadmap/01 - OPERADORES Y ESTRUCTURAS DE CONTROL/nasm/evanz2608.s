; https://www.nasm.us/


; ======================================================================================================================
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


_start:
; IMPORTANTE:
; Todas las instrucciones en ensamblador pueden recibir 0, 1, o 2 parametros, donde:
;     instruccion destino, fuente
; destino puede ser un registro o una direccion de memoria. (variable que se accede con [variable])
; fuente puede ser un registro, una direccion de memoria o un valor inmediato
; pero NO SE PUEDE usar dos direcciones de memoria como destino y fuente a la vez. Ej:
;     mov qword [var_integer], qword [mi_float]
; no está permitido.
; Como se ve, cuando se accede a la memoria, se debe especificar el tamaño que se espera y deben coincidir los dos operandos. Ej
; RAX es un registro de 64 bits (8 bytes), y cuando se escribe su valor en memoria, se usa qword [variable] para indicar que vamos a escribir 8 bytes.
; EAX hace referencia a los primeros 32 bits (4 bytes) del registro rax, y se usaría dword [variable] para indicar que escribimos 4 bytes.




; Operación de asignación. Para asignar un valor a una variable definida en la sección .data, usamos la instrucción mov
  mov qword [var_integer], 10

; imprimimos el valor en [var_integer]
; para entender como se imprime por pantalla, le pasamos a printf los parametros que espera
;   printf(const char* fmt, ...)
; Para entender como se pasan parametros en ensamblador: https://www.ired.team/miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame
  lea rdi, [mask_string]
  lea rsi, [int_string]
  mov rdx, [var_integer]
  xor rax, rax
  call printf


; Lo mismo que antes, pero usando un registro. Movemos 10 a rax, y luego escribimos en [var_integer] el valor en rax. (rax = 20 en este caso).
  mov rax, 20
  mov qword [var_integer], rax
; y volvemos a imprimr el valor en [var_integer]
  lea rdi, [mask_string]
  lea rsi, [int_string]
  mov rdx, [var_integer]
  xor rax, rax
  call printf


; Operaciones aritmeticas. Usamos add para sumar, sub para restar, mul para multiplicar y div para dividir.
  mov rax, 10                 ; rax = 10
  mov qword [var_integer], 10  ; var_integer = 10
  add qword [var_integer], rax ; Sumamos. El resultado se guarda en var_integer.

; imprimimos en pantalla el resultado.
  lea rdi, [mask_string]
  lea rsi, [suma]
  mov rdx, [var_integer] 
  xor rax, rax
  call printf

  sub qword [var_integer], 5 ; restamos 5 al resultado.
; imprimimos en pantalla el resultado.
  lea rdi, [mask_string]
  lea rsi, [resta]
  mov rdx, [var_integer] 
  xor rax, rax
  call printf

; Como dije antes, RAX es un registro de 64 bits, que está subdividido en registros más pequeños. Dejo una referencia: https://www.jamieweb.net/info/x86_64-general-purpose-registers-reference/

; Tanto la instrucción MUL como DIV, trabajan de una manera un tanto particular:
; El primer parametro se debe cargar en el registro RAX.
; luego se llama a la instrucción con el segundo parametro, que puede ser un registro o un valor guardado en memoria.
; El resultado se devuelve en RDX:RAX.
; Al multiplicar, se puede dar el caso que el resultado sea tan grande que no entre en un solo registro, por lo que se usan dos registros para devolver el valor, de la siguiente forma:
; RDX:RAX = resultado.
; en RAX estan los primeros 64 bits del resultado (bits 0-63), y en RDX los siguientes (bits 64- 127). Si el resultado cabe en 64 bits, entonces RDX será 0 y el resultado estará en RAX.
; Se pueden usar los registros de 32 bits también y siguen la misma regla, el resultado estará en EDX:EAX, aunque se debe tener en cuenta que en tal caso
; se deberá usar un registro de 32 bits para el segundo operando también.

  mov rax, 10
  mov rbx, 3
  mul rbx     ; rax * rbx. En este caso el resultado es RDX = 0, RAX = 30.
; imprimimos en pantalla el resultado.
  lea rdi, [mask_string]
  lea rsi, [multiplicacion]
  mov rdx, rax
  xor rax, rax
  call printf


; En este caso utilizamos los registros de 32 bits. Se usa el registro ebx puesto que todos los parametros deben ser del mismo tamaño.
  mov eax, 20
  mov ebx, 10
  mul ebx     ; eax * ebx. El resultado es EDX = 0, EAX = 200
; imprimimos en pantalla el resultado.
  lea rdi, [mask_string]
  lea rsi, [multiplicacion]
  mov rdx, rax
  xor rax, rax
  call printf


; La división funciona de manera muy similar a MUL: Ya que se puede dar que el dividendo sea mas grande que el registro que vayamos a usar, se pasa
; en los registros combinados RDX:RAX para 64 bits, EDX:EAX en 32 bits, y el divisor debe ser un registro del mismo tamaño, u un valor en memoria también del
; mismo tamaño. El resultado se devuelve de la siguiente forma: RAX = cociente, RDX = resto.

  mov rdx, 0    ; limpiamos rdx, de esta manera rdx:rax = 100
  mov rax, 100
  mov rbx, 12
  div rbx       ; rax / rbx. El resultado es RAX = 8 (cociente), RDX = 4 (resto).
; imprimimos en pantalla el resultado.
  lea rdi, [mask_div]
  mov rsi, rax
  call printf

  mov edx, 0    ; limpiamos edx, de esta manera rdx:rax = 100
  mov eax, 200
  mov ebx, 12
  div ebx       ; eax / ebx. El resultado es EAX = 16 (cociente), EDX = 8 (resto).
; imprimimos en pantalla el resultado.
  lea rdi, [mask_div]
  mov rsi, rax
  call printf

; Existen dos instrucciones más, imul e idiv. Ambas funcionan de la misma manera sólo que tienen en cuenta el signo de los operandos.
; voy a poner un ejemplo sólo con idiv.

  mov rdx, 0
  mov rax, -100
  mov rbx, 2
  idiv rbx
; imprimimos en pantalla el resultado.
  lea rdi, [mask_div]
  mov rsi, rax
  call printf

; Ahora, para trabajar con números decimales (float), se usa la fpu (floating point unit) del procesador.
; La fpu tiene 8 registros: st0 - st7 que se comportan como un stack, con lo cual para cargar datos debemos hacer un "push"
; en el siguiente ejemplo se explica con comentarios todo el codigo.
; Vamos a usar qword para nuestras variables, o lo que es lo mismo, el tipo double de C/C++. Si usaramos dword, serían float de C/C++.
; Existen varias instrucciones que operan en la fpu: fmul, fadd, fdiv, etc... Funcionan todas de manera muy similar
; Ademas de la fpu, existen otros registros (xmm0 - xmm15) que se usan para el manejo de valores decimales y tenemos acceso a ellos de la misma manera
; que accedemos a los registros de uso general.

  fninit                    ; Inicializamos la fpu para evitar inconsistencias.
  fld qword [var_float1]    ; Cargamos en st0 el valor de var_float1. Sólo se pueden cargar datos desde la memoria
  fld qword [var_float2]    ; Cargamos en st0 el valor de var_float2. El valor de st0 se pasa a st1 y se carga en st0 el nuevo valor.
  faddp                     ; (Add and pop) Suma st0 con st1. El resultado se guarda en st0 y st1 ahora queda vacío.
  fstp qword [var_result]    ; Guarda el valor de st0 en var_result y hace un "pop", con lo cual ahora el stack de la fpu queda vacío.
; imprimimos en pantalla el resultado.
  movsd xmm0, [var_result]
  lea rdi, [mask_float]
  call printf


; Operadores de comparación y condicionales:
;
; Referencia de todas las instrucciones de salto que hay: https://www.felixcloutier.com/x86/jcc
;
; Para comparaciones tenemos dos instrucciones: cmp y test. Son prácticamente iguales y se usan en conjunto con los saltos para 
; crear estructuras de control. cmp y test comparan dos valores, y modifican la flags del procesador, que luego usaremos para controlar el flujo
; de ejecución con saltos condicionales. Hay que tener en cuenta que las operaciones aritméticas también modifican los flags y por lo tanto, a la hora de saltar,
; hay que tener esto en cuenta, ya que se pueden usar las instrucciones de salto en conjunto con estas operaciones directamente sin usar cmp o test.
; Para poder controlar donde vamos a continuar la ejecución debemos conocer la dirección de memoria donde esté la próxima instrucción que querramos ejecutar,
; aunque sería muy engorroso tener que calcular esas direcciones a mano. Para eso usamos las etiquetas, o labels que podemos definir en cualquier parte de nuestro programa
; y luego saltar a ellas. NASM calculará las direcciones cuando ensamblemos el programa y reemplazará las etiquetas con los offsets correspondientes.
; Para declarar una etiqueta basta con escribir un nombre seguido de ":". Esto definirá una etiqueta a la que podremos saltar desde cualquier lado de nuestro programa.
;
; Vamos a declarar algunas etiquetas y saltar a ellas como prueba.

  mov rax, 20
  mov rbx, 10
comparacion_rax_rbx:        ; definimos una etiqueta para volver a ella luego de las comparaciones
  cmp rax, rbx              ; cmp hará una resta entre los operandos y modificará los flags del cpu acorde al resultado.
  ja mayor                  ; ja = Jump if Above. En este caso, saltará a "mayor" sólo si rax es mayor que rbx. Existe también jae = Jump if Above or Equal.
  je iguales                ; je = Jump if Equal. Este salto condicional saltará a la etiqueta "iguales" si rax y rbx son iguales.
  jne distintos             ; jne = Jump if Not Equal. Este salto condicional saltará a la etiqueta "distintos" si rax y rbx son distintos.

  jmp fin_de_saltos         ; jmp = Jump. Es una instrucción de salto incondicional, por lo que siempre saltará. En este caso, como en ensamblador las instrucciones
                            ; ejecutan de manera secuencial, si no saltamos a "fin_de_saltos", el programa volvería a ejecutar el código que hay debajo, por lo que
                            ; tenemos que saltarlo sí o sí para continuar nuestra ejecución. Es aquí donde se ve la utilidad de jmp.
                            ; En este caso, nunca se ejecutará este salto, ya que lo vamos a hacer en "distintos", de lo contrario estaríamos en un bucle infinito ya que
                            ; no existe forma de escapar de estas tres comparaciones a la vez, lo que muestra que hay que tener cuidado a la hora de hacer saltos sin
                            ; tener en cuenta esta posibilidad.


distintos:                  ; Saltamos aquí cuando rax es distinto de rbx. Imprimimos un mensaje y preparamos rax y rbx para el próximo salto.
  lea rdi, [mask_jumps]
  lea rsi, [str_distintos]
  call printf
  jmp fin_de_saltos         ; Saltamos fuera de las comprobaciones, de lo contrario estaríamos en un bucle infinito.

iguales:                    ; Saltamos aquí cuando rax y rbx son iguales. Imprimimos un mensaje y preparamos rax y rbx para el próximo salto.
  lea rdi, [mask_jumps]
  lea rsi, [str_iguales]
  call printf
  mov rax, 10
  mov rbx, 20
  jmp comparacion_rax_rbx

mayor:
  lea rdi, [mask_jumps]
  lea rsi, [str_mayor]
  call printf
  mov rax, 20
  mov rbx, 20
  jmp comparacion_rax_rbx

fin_de_saltos:

; Con estas instrucciones, podemos crear fácilmente ciclos del estilo while, do while, etc...
; También podemos crear estructuras del estilo if (a == b), if (a == 0), if (a == b) else (), etc...
; Las etiquetas se pueden definir en cualquier parte dentro de la sección .text y vamos a poder saltar a ellas
; de manera que no es necesario que estén debajo del punto donde hacemos la comprobación.

; ===================================
; Ejercicio opcional
; ===================================

  lea rdi, [str_adicional]
  call printf


  mov byte [valor], 9    ; pongo [valor] en 9 porque lo primero que haré en bucle será incrementarlo.
bucle:
  add qword [valor], 1
  cmp qword [valor], 55
  je fin_de_bucle
  jmp es_par

imprimir:
  lea rdi, [mask_int]
  mov rsi, [valor]
  call printf
  jmp bucle

es_16:
  cmp qword [valor], 16
  jne es_multiplo
  jmp bucle

es_multiplo:
  mov rbx, 3
  mov rdx, 0
  mov rax, qword [valor]
  div rbx
  cmp rdx, 0
  jne imprimir
  jmp bucle

es_par:
  mov rbx, 2
  mov rdx, 0
  mov rax, qword [valor]
  div rbx
  cmp rdx, 0
  je es_16
  jmp bucle

fin_de_bucle:
  lea rdi, [mask_int]
  mov rsi, [valor]
  call printf
  lea rdi, [mask_nl]
  call printf
  jmp exit_proc

; Terminamos la ejecucion
exit_proc:
  mov rax, SYS_exit
  xor rdi, rdi
  syscall
; ===========================================================================
; Sección de datos inicializados con permisos de sólo lectura.
; ===========================================================================
section .rodata
  SYS_exit: equ 60
  mask_string: db "%s %u", 10, 0
  mask_div: db "Division: cociente: %i - resto: %i", 10, 0
  mask_float: db "Float: %.4f", 10, 0
  mask_jumps: db "Comparacion: RAX es %s que RBX", 10, 0
  mask_rcx_zero: db "Comparacion: RCX es igual a 0"
  mask_int: db "%u - ", 0
  mask_nl: db 0x0A

  int_string: db "var_integer:", 0
  suma: db "Suma:", 0
  resta: db "Resta:", 0
  multiplicacion: db "Multiplicacion:", 0
  str_distintos: db "distinto", 0
  str_iguales: db "igual", 0
  str_mayor: db "mayor que", 0
  str_mayor_igual: db "mayor o igual", 0
  str_menor: db "menor", 0
  str_menor_igual: db "menor o igual", 0
  str_zero: db "es igual a 0", 0
  str_not_zero: db "es distinto de 0", 0

  str_adicional: db 0x0A, 0x0A, 0x0A, "Ejercicio adicional", 0x0A, 0


; ===========================================================================
; Sección de datos inicializados con permisos de lectura y escritura.
;   No existe en ensamblador el concepto de tipo de datos, sólo son bytes que
;   reservamos para su uso.
;   
; ===========================================================================
section .data
  var_integer: dq 0
  var_float1: dq 100.0
  var_float2: dq 200.0
  valor: dq 0

; ===========================================================================
; Sección de datos no inicializados con permisos de lectura y escritura.
;   Aplica lo mismo que para la sección .data, solo que la memoria que usemos
;   en esta sección no va a ser inicializada y va a contener datos basura
;   hasta que escribamos en ella.
; ===========================================================================
section .bss
  var_result: resq 1
