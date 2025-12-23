#!/bin/bash

# https://www.gnu.org/software/bash/

#esto es un comentario simple en bash

: '
 esto es un
 comentario de
 varias lineas
'

saludo="Hola Mundo!" #string
a=1                  #integer
b=2.7182             #float
c=true               #boolean
d='o'                #char
e=("Hola" "Bash""!") #array
readonly pi=3.1416   #constante

echo "${e[*]}"       #imprimir en bash
printf "Hola Mundo!"

: '
 echo imprime en consola, el "$" llama a una variable, 
 'e' es el array, los '{}' hace que echo imprima todo lo que este dentro 
 y [*] imprime todo lo que este dentro del array
'
