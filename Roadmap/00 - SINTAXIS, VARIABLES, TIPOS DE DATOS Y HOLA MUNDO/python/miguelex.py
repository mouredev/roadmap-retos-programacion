# Documentación https://www.python.org/

# Comentario de una línea

"""
Comentario
de varias
líneas
"""

lenguaje = "Python" 

# Python no tiene una forma para declarar constante. En su defecto,
# se usa una convención de nombrar las constantes con mayúsculas.

PI = 3.1416 

# Tipos primitivos
entero = 1
flotante = 1.1
cadena = "Ejemplo de cadena"
booleano = True
caracter = 'A'
nulo = None

# Imprimir por consola
print(f"Hola {lenguaje}!!!") 
print(f"""Tipos primitivos:
      Entero {entero} <= nombre de la clase: {entero.__class__.__name__}
      Flotante {flotante} <= nombre de la clase: {flotante.__class__.__name__}
      Cadena {cadena} <= nombre de la clase: {cadena.__class__.__name__}
      Booleano {booleano} <= nombre de la clase: {booleano.__class__.__name__}
      Caracter {caracter} <= nombre de la clase: {caracter.__class__.__name__}
      Nulo {nulo} <= nombre de la clase: {nulo.__class__.__name__}
      """)