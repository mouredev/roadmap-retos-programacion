"""
Sitio Oficial de python ---> https://www.python.org/
"""

# Este es un comentario de una sola linea

"""
Este es
un comentario
de varias lineas
"""

#Variables y Constantes
radio = 13.45   # Esta es una variable de tipo Float
PI = 3.14159    # Esta es una constante <--- por CONVENCIÓN
"""
En python no existen las constantes hablando de manera estricta,
aunque por convención se suele declarar variables con MAYUSCULAS
para indicar que son constantes a las cuales no se les deberia cambiar
su valor una ves declarada.
"""

#Tipos de Datos Primitivos

str_var = "hola mundo" #Variable string (texto) (str)
int_var = 12345         #Variable integger (numeros enteros) (int)
float_var = 1.2345      #Variable floating number (numero de punto floatante) (float)
complex_var = 123j      #Variable complex (numeros complejos) (complex)

list_var = [1, 2, 3, 4, 5]  #Variable list (list)
tuple_var = (1, 2, 3, 4, 5) #Variable tupla (tuple)
dict_var = {
    "marco": "polo",
    "user": "macova96",
    "language": "python"
}   #Variable dictionary (Conjunto de datos de clave y valor) (dict)

bool_var = True #Variable booleana (datos de tipo True False) (bool)


language ="Python"
print(f"¡Hola {language}!")