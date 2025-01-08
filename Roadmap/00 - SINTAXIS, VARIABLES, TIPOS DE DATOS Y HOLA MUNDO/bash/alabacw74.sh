#!/bin/bash

# 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
# alabacw74

# Sitio oficial
# https://www.gnu.org/software/bash/manual/bash.html

# Este es un comentario de una linea y los comentarios multilinea no estan
# sustentados de manera directa pero podemos hacerlo como aqui.

# Variables
saludo="Hola a todos yo soy $USER"
echo $saludo

# Constantes
declare -r MI_CONSTANTE="2024-01-15"
echo $MI_CONSTANTE

# En bash las variables no se tratan como en otros lenguajes de alto nivel,
# los valores de las  variables son trabajados como cadenas de texto. Si se
# desea trabajar con numeros es necesario hacer una expansión aritmetica

# Enviar por pantalla
echo "¡Hola, bash!