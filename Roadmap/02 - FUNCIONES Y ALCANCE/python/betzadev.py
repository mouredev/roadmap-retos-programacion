""" /*
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
 */ """

""" /// FUNCIONES EN PYTHON 🐍 /// """

# Función sin parámetros o retorno de valores:

def hola():
  print('Hola Python 🙋🏻‍♀️')

hola() #llamada a la función

# Función con un parámetro

def saludar_persona(nombre):
  print(f"¡Hola, {nombre}!")

saludar_persona("Carlos")  # Salida: ¡Hola, Carlos!


# Función con múltiples parámetros con una sentencia de retorno

def calcular_suma(num1, num2):
  suma = num1 + num2
  return suma

resultado = calcular_suma(5, 3)
print(f"La suma de 5 y 3 es: {resultado}")  # Salida: La suma de 5 y 3 es: 8

# Función con retorno y parámetros opcionales:

def multiplicar(num1, num2=1):
  producto = num1 * num2
  return producto

resultado1 = multiplicar(5)  # Salida: 5
resultado2 = multiplicar(3, 2)  # Salida: 6

print(f"El resultado de multiplicar 5 por 1 es: {resultado1}")
print(f"El resultado de multiplicar 3 por 2 es: {resultado2}")

# Funciones dentro de funciones (anidamiento):

def funcion_externa():
  def funcion_interna():
    print("Estoy dentro de la función interna")

  funcion_interna()  # Se llama a la función interna desde la externa

funcion_externa()  # Se llama a la función externa

# Ejemplo de funciones ya creadas en Python:

print("Hola mundo")  # Función print()
len("Esta es una cadena")  # Función len() para longitud de cadenas
abs(-5)  # Función abs() para valor absoluto
sum([1, 2, 3])  # Función sum() para sumar elementos de una lista

# Variables locales y globales:

def variable_global():
  global variable_global  # Se declara como variable global

  variable_global = 10  # Se modifica el valor de la variable global

variable_global = 5  # Se inicializa la variable global

def variable_local():
  variable_local = 20  # Variable local dentro de la función

  print(f"Variable local dentro de la función: {variable_local}")

variable_local()  # Se llama a la función local
print(f"Variable global después de llamar a la función local: {variable_global}")  # Salida: Variable global después de llamar a la función local: 10

# Dificultad extra:

def multiples_con_mensajes(texto1, texto2):
  contador_mensajes = 0  # Contador de mensajes impresos

  for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
      print(f"{texto1} {texto2}")
      contador_mensajes += 2
    elif numero % 3 == 0:
      print(texto1)
      contador_mensajes += 1
    elif numero % 5 == 0:
      print(texto2)
      contador_mensajes += 1
    else:
      print(numero)

  return contador_mensajes

resultado = multiples_con_mensajes("Azul", "Amarillo")
print(f"Se han impreso los mensajes {resultado} veces")
