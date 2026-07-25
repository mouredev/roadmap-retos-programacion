#!/bin/bash

: "
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */
"

# La pagina oficial de bash es https://gnu.org/software/bash

# Para comentar una sola línea se usa el símbolo  "#"
# Bash ignora todas las líneas que comiencen con este símbolo excepto la primera línea que define el script y se llama shebang

: "
Para comentar varias líneas
se puede usar el símbolo de dos
puntos seguido de comillas dobles
"

# Constante
declare -r PI=3.14159

# Variable
lenguaje="Bash"

# Tipos de datos primitivos

string="Hola mundo"
integer=73
boolean=true    #no existe un tipo booleano nativo
float=1.6180339887

# Imprimir por terminal

echo "$string, esto de aqui es $lenguaje"
