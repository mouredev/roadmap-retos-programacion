# Este es un comentario de una línea

'''
    Comentario de párrafos
    URL de python https://www.python.org 
'''

"""
    Truco usar constantes usar typing.Final
    Y verificar archivo con la librería mypy
    `mypy tu_archivo.py`
    para indicar si tienes constantes que intentaste editarlas
    las constantes sin esa librería si son el mismo tipo de dato
    te validará que es el correcto cosa que no es cierto xP
    
    Aprendido en Código Facilito 
    URL = https://codigofacilito.com/cursos/type-hints
    y encontré en youtube un short
    URL = https://www.youtube.com/shorts/fNMgJaDYxvk
"""
from typing import Final


MY_CONSTANT: Final[str] = 'esto es una constante'

my_variable: str = 'esto es un texto'

my_integer: int = 4

my_float: float = 5.23

my_bool: bool = True


print('Hola, Python!')