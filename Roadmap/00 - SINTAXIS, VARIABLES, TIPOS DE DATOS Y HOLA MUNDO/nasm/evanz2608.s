;	https://www.nasm.us/

; IMPORTANTE
; =============================================================================================
; Aclarar que NASM es uno de los ensambladores que existen y no el lenguaje en si,
; aunque cada ensamblador define una sintaxis, en ensamblador las instrucciones son las mismas,
; y solo cambian cosas que no son especificas del lenguaje ensamblador en si.
;
; La sintaxis que se usa es la de Intel, y se escribe codigo para 64 bits en Linux.
; =============================================================================================






; Los comentarios inician con punto y coma.

%if 0
	No existen comentarios multilinea como tal, pero se pueden usar macros como esta
	que el ensamblador ignorará a la hora de procesar el archivo porque al evaluar la macro
	0 es false, y por lo tanto esto no se incluirá, al igual que un comentario
%endif ;0


section .data
	; las "variables" en ensablador son simples porciones de memoria que reservamos para su uso
	; no tienen tipo, y van dentro de la seccion .data

	mi_variable: db 0										; mi_variable reserva 1 byte inicializado a 0.
	mi_segunda_variable: dw 0						; aquí reservamos 2 bytes, lo que se llama word, también inicializado a 0
																			; Se puede usar dq para reservar 4 bytes, y dq para reservar 8 bytes.

	mi_array: db 0, 1, 2, 3, 4					; Puesto que las variables son porciones de memoria, podemos definir arrays separando cada valor con una coma.

	mi_segundo_array: times 20 dw 0			; Reservamos 20 words, lo que serían 40 bytes y los inicializamos a 0.

	mi_string: db "Cadena de texto"			; Se pueden inicializar variables con cadenas de texto y el tamaño sería igual a la cantidad de caracteres
																			; que contenga la cadena, y cada caracter será tratado como un byte. 


section .rodata
	mi_constante: equ 10								; Para las "constantes" usamos la seccion .rodata (read only data) y usamos EQU para definirles un valor.
																			; Decir que las constantes son meros nombres para el valor que definamos.

	hello: db "Hola, NASM!", 0x0A				; para imprimir por consola el texto. (0x0A es el caracter para salto de línea. En otros lenguajes se puede denotar como '\n')
	hello_len: equ $-hello							; calculamos el largo del texto a imprimir.



section .text					; la seccion donde ira nuestro codigo.
global _start					; declaramos el punto de entrada de nuesto programa. Similar a la funcion main de algunos lenguajes.

_start:								; y aquí la implementamos
	; Imprimimos por pantalla el texto "Hola mundo"
	mov rax, 1
	mov rdi, 1
	lea rsi, [hello]
	mov rdx, hello_len
	syscall

	; y salimos de nuestro programa.
	mov rax, 60
	mov rdi, 0
	syscall
