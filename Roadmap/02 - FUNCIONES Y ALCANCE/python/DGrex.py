"""
    EJERCICIO:
    Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje:
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    Comprueba si puedes crear funciones dentro de funciones.
    Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    Pon a prueba el concepto de variable LOCAL y GLOBAL.
    Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
"""

# Funcion sin parámetros ni retorno

def suma():
  num_one = 3
  num_two = 5
  print(F"Suma > {num_one} + {num_two} : {num_one + num_two}")

suma()

# Funcion con parametros

def resta(num1,num2):
  print(F"Resta > {num1} - {num2} : {num1 - num2}")

resta(5,3)

# Funcion con retorno

def multiplicacion(num1,num2):
  mensaje = f"Multiplicacion > {num1} * {num2}: {num1 * num2}"
  return mensaje

print(multiplicacion(2,5))

# Funcion dentro de una funcion

def funcion_one():
  num1 = 1
  def funcion_two(num2,num3):
    mensaje = f"suma > {num1} + {num2} + {num3}: {num1 + num2 + num3}"
    return mensaje
  print(funcion_two(3,6))


funcion_one()

# Funciones creadas en el lenguaje

#Funcion tipo de dato de una variable type()
nombre= "DGrex"
print(type(nombre)) # print() tambien es una funcion del lenguaje

# Funcion longitud
nombre= "DGrex"
print(len(nombre))

# Funcion conversión de valores
print(int("123")) # Texto a entero
print(float("123.45")) # Texto a decimal
print(str(123)) # Numero a texto

# Funciones valor maximo y minimo
numeros = [1, 2, 3, 4, 5]
print(max(numeros))# Valor maximo
print(min(numeros))# Valor minimo


# Variable local y global

# Variable global
variable_global = "Soy una variable global"

def variables():
    # Variable local
    variable_local = "Soy una variable local"
    # Imprimir la variable global
    print(variable_global)
    # Imprimir la variable local
    print(variable_local)

variables()

# Intentar imprimir la variable local fuera de la función causará un error
# print(variable_local)  # Esto causará un NameError: name 'variable_local' is not defined

"""
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
print("\nFuncion ejercicio extra\n")

def funcion(cadena_uno,cadena_dos):
  contador = 0
  for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
      print(f"{cadena_uno} y {cadena_dos}")
    elif num % 3 == 0:
      print(cadena_uno)
    elif num % 5 == 0:
      print(cadena_dos)
    else:
      print(num)
      contador +=1

  return contador

funcion("Fizz", "Buzz")
