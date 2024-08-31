"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
 """

 #FUNCIÓN SIN PARÁMETROS NI RETORNO:
def funcionS ():
    print("Hola Python")

funcionS()  #llamar a la función

#FUNCIÓN CON RETORNO:
def funcionC ():
   return "Hola Python"

print(funcionC()) 

#FUNCIÓN CON PARÁMETROS:
def funcionP (nombre):
    print(f"Hola {nombre}")

funcionP("Ruth")

#FUNCION CON VARIOS PARÁMETROS:
def funcionVP (nombre, edad):
    print(f"Mi nombre es {nombre} y tengo {edad} años")

funcionVP("Ruth", "34")

#FUNCIÓN CON ARGUMENTO PREDETERMINADO:
def funcionAP (nombre="Python"):
    print(f"Hola {nombre}")

funcionAP()
funcionAP("Ruth")

#FUNCION CON ARGUMENTOS Y RETORNO:
def funcionCR (nombre, edad):
    return f"{nombre}, {edad}"

print(funcionCR("Ruth", "34"))

#FUNCION CON NÚMERO VARIABLE DE ARGUMENTOS:
def funcionVA(*names):
    for name in names:
        print(f"Hola {name}")

funcionVA ("Ruth", "Patricia", "Rebecca")

#FUNCIONES CON UN NÚMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE
def funcion_key (**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

funcion_key(
    language="Python",
    name="Ruth",
    edad= 34
)

#FUNCIONES DENTRO DE FUNCIONES:
def funcion_externa():
    def funcion_interna():
        print ("Función Interna: Hola Python!")
    funcion_interna()

funcion_externa()

#FUNCIONES DEL LENGUAJE (BUILT-IN):
print(len("Ruth"))
print(type(34))
print("Ruth".upper())

#VARIABLES LOCALES Y GLOBALES:

global_var = "Python"

def hello_python():
    local_var= "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print (local_var) No se puede acceder desde fuera de la función

hello_python()

"""
EXTRA
"""

def fizzBuzz(texto1, texto2)-> int:
    count =0
    for number in range(1, 101):
        if number %3==0 and number%5==0:
            print(texto1 + texto2)
        elif number %3==0:
            print(texto1)
        elif number%5==0:
            print(texto2)
        else :
            print (number)
            count +=1
    return count

print(fizzBuzz("Fizz", "Buzz"))