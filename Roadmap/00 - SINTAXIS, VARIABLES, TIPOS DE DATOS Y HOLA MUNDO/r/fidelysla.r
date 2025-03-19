# ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
# - Recuerda que todas las instrucciones de participación están en el
#   repositorio de GitHub.
#
# Lo primero... ¿Ya has elegido un lenguaje?
# - No todos son iguales, pero sus fundamentos suelen ser comunes.
# - Este primer reto te servirá para familiarizarte con la forma de participar
#   enviando tus propias soluciones.
#
# EJERCICIO:
# - Crea un comentario en el código y coloca la URL del sitio web oficial del
#   lenguaje de programación que has seleccionado.
# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una línea, varias...).
# - Crea una variable (y una constante si el lenguaje lo soporta).
# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...).
# - Imprime por terminal el texto: '¡Hola, [y el nombre de tu lenguaje]!'
#
# ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
# debemos comenzar por el principio.

# ? Crea un comentario en el código y coloca la URL del sitio web oficial del
# ? lenguaje de programación que has seleccionado.

# https://www.r-project.org/


# ? - Representa las diferentes sintaxis que existen de crear comentarios
# ?   en el lenguaje (en una línea, varias...).

# Comentario de una linea

# "
# Comentarios de
# varias lineas
# (no recomendable)
# "

# ? - Crea una variable (y una constante si el lenguaje lo soporta).

my_variable <- "Hola"

MI_CONSTANTE <- 3.14

# ? - Crea variables representando todos los tipos de datos primitivos
# ?   del lenguaje (cadenas de texto, enteros, booleanos...).

my_char <- "Hola Mundo"
my_numeric <- 1.5
my_integer <- -20L
my_logical <- TRUE
my_complex <- 1 + 2i
my_raw <- charToRaw("ABC")
my_null <- NULL
my_na <- NA
my_nan <- NaN

# ? Imprime por terminal el texto: '¡Hola, [y el nombre de tu lenguaje]!'

sprintf("¡%s R!", my_variable)
