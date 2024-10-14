### 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

## Ejercicio
  
# - Crea un comentario en el codigo y coloca la URL del sitio web oficial del
#   lenguaje de programacion que has seleccionado.

# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una linea, varias...).

# - Crea una variable (y una constante si el lenguaje lo soporta).

# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...).

# - Imprime por terminal el texto: "!Hola, [y el nombre de tu lenguaje]!"

## Solucion

# - La documentacion oficial del lenguaje R se encuentra en: https://cran.r-project.org/

# - A diferencia de otros lenguajes, R solo permite añadir comentarios mediante
#   el operador #. Si se quiere realizar comentarios de varias lineas, la solucion
#   es simple, poner # en cada linea (como lo estamos haciendo en este caso).

# - Para crear una variable en R, se pueden utilizar dos operadores, los cuales
#   son equivalentes, es decir, no hay diferencia en utilizar uno u otro. El mas
#   utilizado es <-, que representa una flecha y asigna lo que esta en la derecha
#   al nombre que pongamos a la izquierda. El otro es operador es el famoso =, 
#   utilizado en la mayoria de lenguajes.
#   Los nombres permitidos por las variables en R deben cumplir algunas condiciones:
#   1.No pueden ser palabras reservadas del sistema.
#   2.No pueden iniciar por numeros o guion bajo (_).
#   3.Debe iniciar por una letra o un punto (.) y continuar con combinaciones de
#   letras, numeros, punto, y guion bajo (_). No pueden contener espacios o guion
#   medio (-).
#   4.Los nombres de las variables son sensibles a mayusculas (var != Var).
#   Finalmente, aplicando el operador <-
myVar <- "Hello World!"
#   Y, aplicando el operador =
myVar2 = 5*4
#   En R las constantes se tratan igual que las variables, con los mismos operadores.
#   No es comun declarar constantes y hay algunas que vienen por defecto: pi, 
#   month.abb, month.name, LETTERS, letters.

# - En R, los tipos de datos mas basicos que existen son:
# 1. numeric
c(10, 10.5, 105, 1)
# 2. integer
c(1L, 10L, 105L) # En donde la letra "L" declara que es un entero
# 3. complex
c(9 + 8i, 5i) # En donde la letra "i" declara la parte imaginaria
# 4. character (a.k.a string)
c("s", "R", "Hello", "12 + 4")
# 5. logical (a.k.a boolean)
c(TRUE, FALSE)

# la funcion class() permite evaluar el tipo (clase) de un objeto
class(c(10, 10.5, 105, 1))
class(c(1L, 10L, 105L))
class(c(9 + 8i, 5i))
class(c("s", "R", "Hello", "12 + 4"))
class(c(TRUE, FALSE))

# - En R se puede imprimir de dos maneras, simplemente escribiendo el identificador,
#   numero u objeto en la consola y dar enter. Tambien esta la funcion print() que
#   cumple la misma funcion.
'Hola, R!'
print("Hola, R!")
