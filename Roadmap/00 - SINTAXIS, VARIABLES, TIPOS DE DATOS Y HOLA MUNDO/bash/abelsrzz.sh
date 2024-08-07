#!/bin/bash
: '

No hay una página oficial de bash así que coloco la página de Wikipedia.
- https://es.wikipedia.org/wiki/Bash

'

# Esto es un comentario de una sola línea

: '
Esto es un comentario multi línea.
'

: << EOF

Esto también es un comentario multi línea.

EOF

declare constante="constante"
echo "Esto es una $constante"

cadena="cadena"
echo "Esto es una $cadena"

int=1
echo "Este ese mi int número $int"

array=("Esto" " es" " un" " array")
echo "${array[@]}"

bool_1=true
bool_2=false

echo "Existen booleanos $bool_1 y $bool_2"


echo "Hola Bash!"

