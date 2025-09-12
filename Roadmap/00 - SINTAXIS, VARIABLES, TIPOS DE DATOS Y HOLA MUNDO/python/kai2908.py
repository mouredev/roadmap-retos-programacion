# https://www.python.org/

# comentario en python

"""
este comentario es un poco mas extenso.
lo realizo para descubrir los limites del
comentario
"""

'''
tambien se pueden realizar
de esta manera

'''

_variable = "mi variable de texto"
_variable = "nuevo valor de mi variable de texto"

# Las constantes las voy a representar con mayusculas 

CONSTANTE = "mi constante"

# datos primitivos de python

# tipo: int (numeros enteros) 

edad = 25
cantidad_personas = 100
print(f"en 10 años tendras: {edad + 10}") # resultado: 35

# float (numero decimal)

precio = 20.99
tasa_interes = 0.6
print(f"el precio final es: {precio * (1 + tasa_interes)}") # resultado: 33.584

# tipo: str (cadena de texto)

nombre = "ariel"
saludo = "hola"
print(F"{saludo} {nombre}") # resultado: hola ariel

# varios ejemplos de booleanos

# tipo: bool (booleano) — verdadero o falso

es_verdad = True
es_falso = False
print(es_verdad and es_falso) # resultado: False ( para que "and" de "True" ambos deben de ser verdaderos)
print(es_verdad or es_falso) # resultado: True (para que "or" de "False" ninguno deben de ser "True")
print(not es_falso) # resultado: True ("not" invierte el resultado, por lo cual lo que "False" pasa a ser "True")
print(not es_verdad) # resultado: False (en este caso, "not" invierte el resultado "true" y lo convierte en "False")

print(type(precio))
print(type(nombre))
print(type(es_falso))
print(type(edad))

lenguaje = "python" 
print(f"¡hola {lenguaje}") #
   
