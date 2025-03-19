# https://www.python.org/

# Comentario de una sola linea

"""
Comentario multilínea
con comillas dobles
"""

'''
Comentario multilínea
con comillas simples
'''

variable_string: str = "Hola Python"
CONSTANTE: str = "Soy una constante"
entero: int = 1
decimal: float = 1.5
booleano: bool = True
lista: list = [1, 2, 3]
tupla: tuple = (1, 2, 3)
diccionario: dict = {"nombre": "Juan", "apellido": "Perez"}

print(variable_string)
print(f'CONSTANTE {type(CONSTANTE)}, {repr(CONSTANTE)}')
print(f'entero {type(entero)}, {repr(entero)}')
print(f'decimal {type(decimal)}, {repr(decimal)}')
print(f'booleano {type(booleano)} {repr(booleano)}')
print(f'lista {type(lista)}, {repr(lista)}')
print(f'tupla {type(tupla)}, {repr(tupla)}')
print(f'diccionario {type(diccionario)}, {repr(diccionario)}')

# Texto sin cambiar en main
