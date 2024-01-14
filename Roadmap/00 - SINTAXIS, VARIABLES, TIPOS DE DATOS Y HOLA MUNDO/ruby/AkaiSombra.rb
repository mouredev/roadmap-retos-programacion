
# Author: Nicolas Romero https://github.com/AkaiSombra

=begin
 * EJERCICIO:
 * 1. Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2. Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3. Crea una variable (y una constante si el lenguaje lo soporta).
 * 4. Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
=end

# Ejercicio 1:

# Sitio oficial de Ruby: https://www.ruby-lang.org/en/

# Ejercicio 2:

# Comentario de una linea en Ruby

=begin
Comentario de varios lineas
en Ruby
=end

# Ejercicio 3:

# Variable

parecido = "Python"

# Al igual que Python Ruby no tiene Const
# Pero si escribimos una variable en mayusculas
# se toma como constante pero solo a nivel de semantica

LENGUAJE = "Ruby"

# Ejercico 4:
# Datos primitivos

# Entero(int)
int_number = 2024

# Numero con punto flotante(float)
float_number = 3.14

# Cadena de texto(string)
string = "Cadena de texto"

# Booleanos (bool)

boolean_true = true
boolean_false = false

# Simbolos (Symbol)
simbolo = :Symbol


# Nulo (Null)
valor_nulo = nil

# Ejercicio 5:

puts "¡Hola, #{LENGUAJE}!"
