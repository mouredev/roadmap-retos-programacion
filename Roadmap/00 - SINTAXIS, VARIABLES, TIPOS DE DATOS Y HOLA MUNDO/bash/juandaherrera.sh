# Página principal de Bash: https://www.gnu.org/software/bash/

# Comentario de una línea

: '
Comentario
de varias líneas
'

# Variables
myVariable="Juan David" # Esta es una variable que puede cambiar
myVariable="Juan David Herrera"

readonly MY_CONSTANT="API_KEY" # Esta es una constante que no puede cambiar

# Tipos de datos primitivos en Bash
myInt=25 # Número entero
myFloat=1.33 # Número con punto flotante (Nota: Bash no diferencia entre int y float)
myBool=true # Booleano (Nota: Bash no tiene un tipo de dato booleano nativo)
myString="Mi cadena de texto" # Cadena de texto
myOtherString='Mi otra cadena de texto' # Otra forma de representar cadenas de texto
myLanguage="Bash" # Nombre del lenguaje

echo "¡Hola, $myLanguage!"

# Bash no tiene una función incorporada para determinar el tipo de una variable.
# Por lo general, todo se trata como una cadena de texto.
