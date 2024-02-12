""" * EJERCICIO:

 *  Crea ejemplos de funciones básicas que representen las diferentes
 *  posibilidades del lenguaje:
 *  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 *  Comprueba si puedes crear funciones dentro de funciones.
 *  Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 *  Pon a prueba el concepto de variable LOCAL y GLOBAL.
 *  Debes hacer print por consola del resultado de todos los ejemplos.
 *  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

"""

# Funciones sin parámetros ni retorno

def saludo(): # Definición de la función 
    print("Hola, ¿Cómo estás?")

saludo() # Llamada a la función para que se ejecute

# Funciones con parámetros y retorno

def suma(numero1, numero2): # Definición de la función que recibe dos parámetros
    return numero1 + numero2

print(f"la suma de los parametros es {suma(5, 6)}") # Llamada a la función con dos parámetros

# Funciones con multiples parámetros y retorno

def suma_multiples_parametros(*args): # Definición de la función que recibe multiples parámetros
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(f"la suma de los parametros es {suma_multiples_parametros(5, 6, 7, 8, 9)}") # Llamada a la función con multiples parámetros

# Funciones con funciones dentro

def funcion_dentro(saludo1): # Definición de la función que contiene otra función
    def funcion_dentro_dentro(saludo2):  
        print(f"{saludo2} una funcion dentro de funcion")
    funcion_dentro_dentro(saludo1)

funcion_dentro("Esta es")

### Funciones ya creadas en el lenguaje ###

# Función map

def cuadrado(numero): # Definición de la función que eleva al cuadrado un número
    return numero * numero

lista = [1, 2, 3, 4, 5]
resultado = map(cuadrado, lista) # La función map devuelve un objeto map, por lo que se debe convertir a lista para poder visualizar el resultado
print(list(resultado)) 

# Función filter

def es_par(numero): # Definición de la función que devuelve True si el número es par
    if numero % 2 == 0:
        return True
    else:
        return False

lista = [1, 2, 3, 4, 5]
resultado = filter(es_par, lista) # La función filter devuelve un objeto filter, por lo que se debe convertir a lista para poder visualizar el resultado
print(list(resultado)) # imprime [2, 4] que son los números pares de la lista

# Función reduce

from functools import reduce # Se debe importar la función reduce

def suma(numero1, numero2): # Definición de la función que suma dos números
    return numero1 + numero2

lista = [1, 2, 3, 4, 5]
resultado = reduce(suma, lista) # La función reduce devuelve un objeto reduce, por lo que se debe convertir a lista para poder visualizar el resultado
print(resultado) # imprime 15 que es la suma de todos los números de la lista

# Variable global
variable_global = "Soy una variable global"

def mi_funcion():
    # Variable local
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)

mi_funcion()

print(variable_global) # Esto se puede hacer porque variable_global es una variable global
# print(variable_local)  # Esto dará un error porque variable_local no es accesible fuera de la función


"""
DIFICULTAD EXTRA (opcional):
  Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
  La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  La función retorna el número de veces que se ha impreso el número en lugar de los textos 
  Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
  Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
"""

from num2words import num2words # Se debe instalar la librería num2words para poder utilizarla con el comando "pip install num2words"

numero = 123
palabras = num2words(numero, lang='es') # Convierte el número a palabras en español
print(palabras)  # imprime "ciento veintitrés"

def extra():
  contador = 0
  for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
      palabras = num2words(i, lang='es')
      print(palabras)
    elif i % 3 == 0:
      palabras = num2words(i, lang='es')
      print(palabras)
    elif i % 5 == 0:
      palabras = num2words(i, lang='es')
      print(palabras)
    else:
      print(i)
      contador += 1
  return contador

resultado = extra()
print(f"Número de veces que se ha impreso el número en lugar de los textos: {resultado}")