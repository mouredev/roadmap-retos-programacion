#!/bin/env bash

# EJERCICIO:
#  - Crea un comentario en el código y coloca la URL del sitio web oficial del
#    lenguaje de programación que has seleccionado.
#  - Representa las diferentes sintaxis que existen de crear comentarios
#    en el lenguaje (en una línea, varias...).
#  - Crea una variable (y una constante si el lenguaje lo soporta).
#  - Crea variables representando todos los tipos de datos primitivos
#    del lenguaje (cadenas de texto, enteros, booleanos...).
#  - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
#  ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
#  debemos comenzar por el principio

# Los comentarios en bash se indican con "#" al comienzo de línea.
# NO hay comentarios multilínea => se simulan con líneas consecutivas inicializadas con "#".

typeset -r URL_OFICIAL_BASH="https://www.gnu.org/software/bash/"
echo "Con "'${URL_OFICIAL_BASH}'" muestro el contenido de la CONSTANTE URL_OFICIAL_BASH = ${URL_OFICIAL_BASH}"

typeset -i entero=1
echo "Con "'${entero}'" muestro el contenido de la VARIABLE entero = ${entero}"

cadena="bash"
echo "Con "'${cadena}'" muestro el contenido de la VARIABLE cadena = ${cadena}"

echo 'bash NO tiene variable booleanas => se debe operar con "test expr" y ver si retorna ($?) 0 True o 1 False'
echo "test "'${entero}'" == 1; echo "'$?'" <= devuelve 0 = True" 
echo "test "'${entero}'" == 2; echo "'$?'" <= devuelve 1 = False"

echo "bash no tiene aritmética de punto flotante => se debe usar una función y asignar a una variable de cadena."
echo "flotante="'$(bc -l <<< 10/3)'"; echo "'${flotante} <= devuelve 3.3333333333333' 

echo "Hola ${cadena}"
echo "Aprende BASH en la web oficial: ${URL_OFICIAL_BASH}"
