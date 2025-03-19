"""
 EJERCICIO 02:
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

#*-------------------------------------------------------------------------------------------------------------#
"""
  - Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""

#Funciones
print("************************************************")

print("Función simple")
def hola():
    print("Hola")
hola()
print("************************************************")

#Funciones con parametros
print("Funciones con parámetros")
def suma(num1, num2):
  return num1 + num2

resultado = suma(45, 56)
print(resultado)

print("************************************************")

#Funciones con retorno
print("Funciones con retorno")
def cubo(numero):
  return numero ** 3

numero_ingresado = 6
resultado_cubo = cubo(numero_ingresado)
print(f"El cubo de {numero_ingresado} es {resultado_cubo}")

print("************************************************")
#*-------------------------------------------------------------------------------------------------------------#

"""
- Comprueba si puedes crear funciones dentro de funciones.
"""
#Funcion dentro de otra funcion
print("Función de otra Función")
def suma_lista(lista):
    def sumar_elementos(elementos):
        return sum(elementos)

    total = sumar_elementos(lista)
    print(f"La suma de los elementos es: {total}")

mi_lista = [1, 2, 3, 4, 5]
suma_lista(mi_lista)
print("************************************************")
#*-------------------------------------------------------------------------------------------------------------#

"""- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
"""
print("Funciones creadas en python")

lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print(f"La longitud de la lista es: {longitud}")
print("************************************************")
#*-------------------------------------------------------------------------------------------------------------#

"""
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""

#Variables Globales
print("Variables Globales")

var_global = 42
def variable_global():
    print(f"El valor de la variable global es: {var_global}")

variable_global() 

print("************************************************")

print("Variables Locales")

def saludar():
    mensaje = ""
    print(mensaje)

saludar()
print("************************************************")
#*-------------------------------------------------------------------------------------------------------------#

"""
DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def numeros(texto_uno,texto_dos):
  impresiones = 0
  for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
      print(f"{num} es un {texto_uno + texto_dos}")
    elif num % 3 == 0:
      print(f"{num} es un {texto_uno}")
    elif num % 5 == 0 :
      print(f"{num} es un {texto_dos}")
    else:
      print(f"El número {num} no es un múltiplo de 3 y 5")
      impresiones += 1
      
texto_a = "Multiplo de Tres"
texto_b = "Multiplo de Cinco"
resultado = numeros(texto_a, texto_b)
print("Número de impresiones:", resultado)

#*-------------------------------------------------------------------------------------------------------------#
