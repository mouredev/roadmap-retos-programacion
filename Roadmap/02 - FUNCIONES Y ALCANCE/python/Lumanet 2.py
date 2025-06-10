# FUNCIONES
# Sin parámetros ni retorno
def saludo():
  print("Hola, soy Lumanet")
# Con uno o varios parámetros
def saludo_personal(nombre, apellido):
  print(f"Hola, soy {nombre} {apellido}")
# Con varios parámetros
def saludo_personal_multiple(*nombres):
  for nombre in nombres:
    print(f"Hola, soy {nombre}")
# Con retorno
def saludo_personal_retorno(nombre, apellido):
  return f"Hola, encantado, soy {nombre} {apellido}"

saludo()
saludo_personal("Marcos", "Lumanet")
saludo_personal_multiple("Marcos", "Lumanet", "Juan", "Pedro")
print(saludo_personal_retorno("Marcos", "Lumanet"))

def saludo_pregunta(nombre, apellido, pregunta):
  saludo_personal(nombre, apellido)
  print(f"{pregunta}")
  
saludo_pregunta("Marcos", "Lumanet", "¿Cómo estás?")

from datetime import datetime

def saludo_hora(nombre, apellido):
  hora = datetime.now().hour
  if hora < 12:
    print(f"Buenos días, soy {nombre} {apellido}")
  elif hora < 18:
    print(f"Buenas tardes, soy {nombre} {apellido}")
  else:
    print(f"Buenas noches, soy {nombre} {apellido}")
    
saludo_hora("Marcos", "Lumanet")

# Variables globales y locales
nombre = "Marcos"
def saludo_global():
  saludo = "Hola"
  print(f"{saludo}, soy {nombre}")
  
saludo_global()
# print(saludo) # ! No se puede acceder a la variable local de la función

"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def multiplos(p1, p2):
  c =0
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print(f"{p1} y {p2}")
    elif i % 3 == 0:
      print(p1)
    elif i % 5 == 0:
      print(p2)
    else:
      print(i)
      c += 1
  return c

# multiplos("Tres", "Cinco")
valor= multiplos("Tres", "Cinco")
print(valor)