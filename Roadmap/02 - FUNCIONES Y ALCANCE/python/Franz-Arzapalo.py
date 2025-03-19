"""
EJERCICIO: #02 FUNCIONES Y ALCANCE

- Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
  DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# 1. Crea ejemplos de funciones básicas que representen las diferentes
#    posibilidades del lenguaje:
#    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

"""
Antes de definir una funcion podemos recapitular de forma que en retos anteriores vimos funciones nativas como range() o como bin()
y es eso las funciones nativas son las funciones que ya estan en python de forma determinada o preinstalada pero nosotros tambien 
podemos crear nuestras propias funciones con el comando def para definir la funcion esto nos pedira un nombre para la funcion y de forma
opcional un parametro que ira entre parentesis terminando con los dos puntos para pasar a definir la accion que se ejecutara.
"""

# Definir una funcion basica sin parametros con "def":

def ejemplo ():
    print("Ejemplo")

# para usar la funcion se tiene que nombrar y usar el parentesis.:

ejemplo()

# Definir una funcion basica con parametro:

def ejemplo1 (lenguaje):
    print (f"Hola, {lenguaje}!")

ejemplo1("Python")

# Hasta ahora estas funciones no tenian retorno pero se podian ver resultados gracias a la funcion print().

# Definir una funcion basica con parametro y retorno.

def ejemplo2 (Nombre):
    return f"Hola {Nombre}"

print(ejemplo2("Franz"))    

# A simple vista no parece relevante este cambio pero es por la necesidad de imprimir el cambio para verlo en la consola.
# Las funciones nos sirven para ahorra timepo y codigo pues cunado vamas a repetir las mismas acciones con cambios puntuales
# el tener una funcion para automatizar esos cambios es bastante util.
# Return sirve especificamente para sacar el resultado de la funcion de dentro de la funcion no la imprime pero ahi esta.

# Definir una funcion basica con mas de un parametro y retorno:

def ejemplo3 (Lenguaje, Nombre):
    return f"Hola {Nombre}, {Lenguaje} es increible!"

print(ejemplo3("Python", "Franz"))

# De esta forma podemos poner mas parametros en la funcion.
# El orden en el que se definen los parametros son el mismo orden en el que se tienen que ingresar dichos parametros para su uso correcto.

# Asignar valores predeterminados a los parametros de una funcion:

def ejemplo4 (numero=", no ingreso un numero"):
    return f"Su numero es {numero}"

print(ejemplo4())

# De esta forma si no se ingresa parametros en la funcion se ejecutara con el valor definido si esto no se hace y se ejecuta una funcion
# sin parametros aparecera un error en la consola y se dentra la ejecucion de todo codigo que le siga.

# Definir una funcion con mas de un retorno:

def ejemplo5 ():
    return "uno", "dos"

numero1, numero2 = ejemplo5()

print(numero1)
print(numero2)

# Definiendo las variables separadas por comas se podra separar mas de un valor que retorne una funcion.

# Podemos tambien hacer funciones que utilicen el mismo parametro pero que se introduscan mas variables para ese parametro:

def ejemplo6 (*names):
    for name in names:
        print(f"¡Hola, {name}!")
    print(type(names))
ejemplo6("Python", "Franz", "Erick", "Arzapalo")

# Con el bucle for podemos separar una gran cantidad de valores que se pongan en un parametro.
# Pero lo mas importante es el * puesto antes del parametro esto combierte los valores que se ingrese en un grupo de valores conocido
# como tuplas esto varia en otros leguajes pero en python es una herramienta muy util.(Esto es conocido como *args refiriendose a arguments)

# Ahora el siguiente nivel del tipo de funcion anterior es crear un funcion con un palabra clave y un valor de la misma forma con
# una cantidad de valores variables para el parametro.

def ejemplo7 (**names):
    for keys, value in names.items():
        print(f"{keys}, ({value}!)")
ejemplo7(lenguaje="Python", name="Franz", numero=14, serie="the office", pelicula="harry potter")

# En el bucle usamos .items() para poder acceder a los valores de cada clave porque cuando se trabaja con diccionarios de no usar el items
# solo se trabajaria con las claves pero como se trabaja con esta es bastante util el tener un valor como con las tuplas pero ahora el
# tener cada valor un nombre nos facilita de gran manera trabajar de otra forma esto simplifica el trabajo.

# Comentarios en funciones:
def comentada ():
    """
    Esta es una funcion que se usara como ejemplo para demostrar lo 
    importante y util que puede ser comentar una funcion de esta forma.
    """
    return "Funcion comentada"

help(comentada)
print(comentada.__doc__)

# De esta forma se llama al comentario dentro de un funcio y si esta ha sido comentada con su funcion apoyara de gran manera a otra 
# persona que quiera leer el codigo osea es una buena practica el comentar las funciones de esta forma.

# Anotacion en funciones:

def ejemplo8 (x:int) -> int:
    return x*5
print(ejemplo8("Franz"))

# De esta forma se anota en un funcion el tipo de parametro que se quiere o se necesita para el correcto funcionamiento de la funcion
# pero solo lo hacer notar como se dice no afecta ni inpone esa regla por ello ne no cumplirse y la funcio puede funcionar sin
# la necesidad de se cumpla la notacion se ejecutara de forma normal.

# 2. Comprueba si puedes crear funciones dentro de funciones.

"""
En python se pueden crear funciones dentro de otras funciones la principal caracteristica de estas funcion son que no funcionan afuera
de la funcion en la que fureron definidas son como funciones temporales.
"""

def funcion_mayor ():
    def funcion_menor ():
        print("Esta es la funcion menor")
    print("Esta es la funcion mayor")
    funcion_menor()
funcion_mayor()

# funcion_menor() # No la reconoce porque fue llamada fuera de la funcion principal.

# 3. Utiliza algún ejemplo de funciones ya creadas en el lenguaje (built-in).

# https://docs.python.org/es/3.8/library/functions.html 
# Documentacion de funciones nativas python.

"""
Built-in o tambien conocidas como funciones nativas son funciones definidas o preinstaladas en el lenguaje en este caso python,
son muchas pero muy utiles solo veremos 3:
"""

print(len("Franz")) # 5
# len hace un conteo de objetos en este caso el numero de letras.
# Nos puede ayudar por ejemplo para saber el numero de iteraciones que podriamos tener usando el bucle for.
# Ojo solo funciona con grupos de obejtos como el bucle for no con integers o floats.

print(type(x:=3+4j)) # <class 'complex'
# Type retorna el tipo de variable que se le ingresa en este caso complex por que es un numero complejo.
# Nos puede ayudar mas cuando no sabemos de que tipo es una variable talvez que no encontras definida o que no sabemos como termina despues de una operacion.

print("python".upper()) # PYTHON
# upper() convierte todos los caracteres de una cadena de texto a mayusculas.
# Solo puede trabajar con strings.

# 4. Pon a prueba el concepto de variable LOCAL y GLOBAL.

Variable_global = "Global"

def ejemplo9 ():
    Variable_local= "Local"
    print(f"Variable globa ({Variable_global}), Variable local ({Variable_local})")

print(Variable_global)
# print(Variable_local) no se puede llamar fuera de la funcion

ejemplo9()

# 5. Debes hacer print por consola del resultado de todos los ejemplos.
#  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades) (cumplida)

# 6. Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def FizzBuzz (Cadena1, Cadena2):
    count=0
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(Cadena1+Cadena2)
        elif n % 3 == 0:
            print(Cadena1)
        elif n % 5 == 0:
            print(Cadena2)
        else:
            print(n)
            count+=1
    return(count)

print(FizzBuzz("Fizz", "Buzz")) 

# Fin.