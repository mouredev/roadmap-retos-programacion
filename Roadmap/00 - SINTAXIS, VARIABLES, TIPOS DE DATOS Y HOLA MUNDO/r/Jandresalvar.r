## Ejercicio
  
# - Crea un comentario en el c??digo y coloca la URL del sitio web oficial del
#   lenguaje de programaci??n que has seleccionado.

# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una l??nea, varias...).

# - Crea una variable (y una constante si el lenguaje lo soporta).

# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...).

# - Imprime por terminal el texto: "!Hola, [y el nombre de tu lenguaje]!"

## Soluci??n

# - La documentaci??n oficial del lenguaje R se encuentra en: https://cran.r-project.org/

# - A diferencia de otros lenguajes, R solo permite a??adir comentarios mediante
#   el operador #. Si se quierem realizar comentarios de varias lineas, la soluci??n
#   es simple, poner # en cada linea (como lo estamos haciendo en este caso).

# - Para crear una variable en R, se pueden utilizar dos operadores, los cuales
#   son equivalentes, es decir, no hay diferencia en utilizar uno u otro. El m??s
#   utilizado es <-, que representa una flecha y asigna lo que est?? en la derecha
#   al nombre que pongamos a la izquierda. El otro es operador es el famoso =, 
#   utilizado en la mayor??a de lenguajes.
#   Los nombres permitidos por las variables en R deben cumplir algunas condiciones:
#   1.No pueden ser palabras reservadas del sistema.
#   2.No pueden iniciar por numeros o guion bajo (_).
#   3.Debe iniciar por una letra o un punto (.) y continuar con combinaciones de
#   letras, numeros, punto, y gu??on bajo (_). No pueden contener espacios o guion
#   medio (-).
#   4.Los nombres de las variables son sensibles a mayusculas (var != Var).
#   Finalmente, aplicando el operador <-
myVar <- "Hello World!"
#   Y, aplicando el operador =
myVar2 = 5*4
#   En R las constantes se tratan igual que las variables, con los mismos operadores.
#   No es com??n declarar constantes y hay algunas que vienen por defecto: pi, 
#   month.abb, month.name, LETTERS, letters.

# - En R se puede imprimir de dos maneras, simplemente escribiendo el identificador,
#   n??mero u objeto en la consola y dar enter. Tambi??n est?? la funci??n print() que
#   cumple la misma funci??n.
'??Hola, R!'
print("??Hola, R!")
