#!/bin/bash
# URL del sitio web oficial de Bash: https://www.gnu.org/software/bash/

# Comentario de una línea
# Otra forma de comentario de una línea

: '
  Este es un comentario de
  varias líneas en Bash
'

# Declaración de variables y constante
variable="Hola, Bash"  # Variable
readonly constante="Valor constante"  # Constante

# Tipos de datos primitivos en Bash
entero=42  # Entero
flotante=3.14  # Flotante (representado como cadena)
booleano=true  # Booleano (representado como cadena)

# Imprimir por terminal
echo $variable
echo $constante
echo "Entero: $entero"
echo "Flotante: $flotante"
echo "Booleano: $booleano"