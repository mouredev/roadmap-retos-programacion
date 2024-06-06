# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
# *   lenguaje de programación que has seleccionado.
    # https://www.python.org/

# * - Representa las diferentes sintaxis que existen de crear comentarios
# *   en el lenguaje (en una línea, varias...).
    #   Python realmente no tiene una sintaxis multilineas, pero 
    #ignorará string que no estan asignados a una variable

"""
    Comentario
    multi
    linea
    Ignorado por python puesto que no esta asignado a una variable
"""

# * - Crea una variable (y una constante si el lenguaje lo soporta).

cont = 0
myNombre = "Jose"

# * - Crea una variable global (y una constante si el lenguaje lo soporta).

global x
x = "Mundial"

#* - Crea variables representando todos los tipos de datos primitivos
#*   del lenguaje (cadenas de texto, enteros, booleanos...).

varString = str("Es es una string")
varInt = int(10)
varFloat = float(3.41)
#cualquier String es true a menos que esté vacia
varBooleanTrue = bool("Hello")
#cualquier String es true a menos que esté vacia
varBooleanFalse = bool("")

varText = str("¡Hola, [y el nombre de tu lenguaje]!")
print(varText) 