#!/bin/bash

: '
Página oficial de Bash: https://www.gnu.org/software/bash/
'

# Los comentarios de una línea se hacen con el signo gato (numeral o hash)

: '
Se colocan con el comando ":", un espacio y comilla simple para abrir,
Luego se coloca una comilla de cierre para terminar el comentario
'

<<Document
Otra manera de tener comentarios multilínea es con lo que se denominan
HereDocuments, que básicamente son una manera de decirle a bash que lo que está
entre el comienzo del documento, que se declara con "<<" y un nombre, y el cierre,
que se declara con el nombre del documento solo en una línea, se procesa como una
sola unidad
Document

readonly constante="x3mboy" #Y los comentarios dentro de línea se hacen igual con el signo gato

nombre=$constante
cadena="Hola"
entero=1
flotante=1.1
booleano=true

echo $cadena" "$nombre
echo "Numero entero: "$entero
echo "Numero real: "$flotante
echo "Variable booleana: "$booleano

echo "Hola Bash!"
