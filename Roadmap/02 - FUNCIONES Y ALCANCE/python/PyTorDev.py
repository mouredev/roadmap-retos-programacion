"""
/*
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


# Declaración sin parametros
def funcion_nombre1():
  nombre = "Aitor"
  apellido = "Lopez"
  espacio = " "
  num_funcion = str(1)
  nombre_completo = nombre + espacio + apellido + espacio + num_funcion
  print(nombre_completo)

# Llamada a la función
funcion_nombre1()

# Funcion con retorno
def funcion_nombre2():
  nombre = "Aitor"
  apellido = "Lopez"
  espacio = " "
  num_funcion = str(2)
  nombre_completo = nombre + espacio + apellido + espacio + num_funcion
  return nombre_completo

print(funcion_nombre2())

# Funcion con parametros

def funcion_nombre3(nombre, apellido):
  espacio = " "
  num_funcion = str(3)
  nombre_completo = nombre + espacio + apellido + espacio + num_funcion
  return nombre_completo

print(funcion_nombre3("Aitor", "Lopez")) 

# Funcion con parametros por defecto
def funcion_nombre4(nombre = "Aitor", apellido = "Lopez"):
  espacio = " "
  num_funcion = str(4)
  nombre_completo = nombre + espacio + apellido + espacio + num_funcion
  return nombre_completo

print(funcion_nombre4())
print( funcion_nombre4("Manuel", "Salas"))

# Funcion con numero arbitraio de parametros
def arbit_function(*args):
  nombre = "Aitor"
  apellido = "Lopez"
  espacio = " "
  num_funcion = str(1)
  nombre_completo = nombre + espacio + apellido + espacio + num_funcion
  print(nombre_completo)

# Función como parametro de otra función
def num_cuadrado(n):
  return n * n

def ejecutando_funcion(f, x):
  return f(x)

print(ejecutando_funcion(num_cuadrado, 3))

#Ejemplo de tres funciones ya creadas
print("Imprime en consola el argumento dado")
# nombre = input("Muestra este mensaje en consola, detiene la ejecución y guarda en la variable numbre lo que introduce el usuario")
print(type("Devuelve el tipo del valor que recibe como argumento"))

#Variable local vs global

my_global = "Esta es una variable global"

def my_local():
  my_local = "Aqui declaro una var local, que solo es accesible desde dentro de la misma funcion"
  print(my_local)

def prueba_loc_glob(x):
  print(x)

my_local()
prueba_loc_glob(my_global)
# prueba_loc_glob(my_local) Esto da error, porque no se ppuede acceder a la varable local declarada dentro de una funcion

# Extra
def imprime_num(n1 = input("Introduce el numero de inicio"), n2 = input("Introduce el numero final")):
  n1 = int(n1)
  n2 = int(n2) + 1
  for i in range (n1, n2):
    if (i % 3 == 0 and i % 5 == 0):
      print("FizzBuzz")
    elif (i % 5 == 0):
      print("Buzz")
    elif (i % 3 == 0):
      print("Fizz")
    else:
      print(i)

imprime_num()