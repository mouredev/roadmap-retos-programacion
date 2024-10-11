#!/bin/bash

# URL del sitio web oficial de Bash: https://www.gnu.org/software/bash/

# COMENTARIOS

# Esto es un comentario de una linea.

: '
Este es un comentario 
de varias lineas
'


# VARIABLES

variable=0                          # variable
readonly constant="Mi constante"    # constante

function my_function {
local variable_local=0            # variable local
}

# TIPOS DE DATOS

variable="String"                   # String
variable=1                          # Int
variable=("rojo" "verde" "azul")    # Array
variable=true                       # Boolean

declare -A dictionary
dictionary[valor]='valor1'          # diccionario

# Hola mundo
echo "Hola, Bash!"                  # echo sirve para imprimir en la terminal

# Para llamar a una variable se usa el simbolo $[nombre de la variable]
variable="Hola Bash"
echo $variable                      
