#FUNCIONES

"""Funciones definidas por el usuario """

#simple
def saludo():
  print('Buenos días')

saludo()

#con retorno

def despedida():
  return('Hasta luego')

print(despedida())  #cuando tengo return, es necesario imprimir la función para que sí aparezca el resulato

#con argumentos

def saludo_personal(nombre):
  print("Bienvenida",nombre)

saludo_personal("Sara")

#varios argumentos

def saludo_completo(saludo, nombre):
  print(f"{saludo} {nombre}")

saludo_completo("hola","sara")

#Con un argumento predeterminado

def capital(pais="Colombia",capital="Bogota"):
  return(f"La capital de {pais} es {capital}")

print(capital())

#con un número variable de argumentos

def inventario(*elementos):
  for elemento in elementos:
    print(f"nombre del elemento: {elemento}")

inventario("silla","mantel","cortina")

#con un número variable de argumentos y palabra clave

def informacion(**caracteristicas):
  for clave, caracteristica in caracteristicas.items():
    print(f"{clave}: {caracteristica}")

informacion(pais="Colombia", capital="Bogota", gentilicio="Colombianos",continente="Latinoamerica")

# una función dentro de otra función

def funcion_externa():
  def funcion_interna():
    print("Hola interno")
  funcion_interna()

funcion_externa()

"""
Ejemplo de funciones ya creadas
"""

#print()

print('Hola mundo')

#len()

print(len('Hola mundo'))

#sum()

print(sum({9,1,8}))

#min()

print(min({9,1,8}))

#max()

print(max({9,1,8}))

#type()

print(type(45.8))

#upper()

print("Hola".upper())

"""
Ejercicio extra
"""

def textonumero(texto1,texto2) -> int:
  count = 0
  for numero in range(1,101):
    if (numero % 3) == 0 and (numero % 5) == 0:
      print(texto1+texto2) 
    elif (numero % 5) == 0:
      print(texto2)
    elif (numero % 3) == 0:
      print(texto1)
    else: 
      print(numero) 
      count += 1
  return(count)

print(textonumero("Fizz","Buzz"))
