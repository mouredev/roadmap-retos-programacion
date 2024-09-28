# URL OFCIAL DE PYTHON: https://www.python.org/

# COMENTARIO DE UNA LINEA: COLOCAR # A LA IZQUIERDA
# lo que se encuentre hacia la derecha del hashtag sera omitido por el interprete python

''' 
    COMENTARIO EN VARIAS LINEAS (1 de 2):
        se demarca tanto al principio como al final tres comillas
        pudiendo ser simples...

'''
"""
    COMENTARIO EN VARIAS LINEAS (2 de 2):
        ...como comillas dobles, el resultado sera el mismo.
        Todo lo que se encuentre dentro del bloque de comillas
        sera omitido por el interprete de python
"""
'''
    CONSTANTES Y VARIABLES
    
    * constantes: no existe como tal una forma de declarar constante en python, aunque se puede
    respetar una convencion al identificar nombre de varia en mayuscula como si fuera 
    un valor inmutable. Sin embargo, existen algunas constantes propias del lenguaje,
    como por elemplo: True o False

    * variables: python tiene 4 tipos de variables primitivas (referidas a aquellas que
    no pueden dividirse en partes mas peque#as). No es necesario declararlas como sucede
    en otros lenguajes, aunque se puede indicar cual sera su configuracion inicial,
    lo cual servira de referencia para evitar inconvenientes con su uso. Ademas, los IDE
    podran monitorear mejor el codigo.
    Sin embargo, al ser un lemguaje de tipado dinamico, una vez que se han creado, 
    las mismas pueden ser modificadas en el mismo proceso de ejecucion. Pueden ser nombradas
    en cualquier estilo aunque se recomienda que sean facil de identificar al leer el codigo:

    Los tipos de variables primitivas serian:
    variables numericas: int, float
    alfanumericas: str
    booleanas: bool
'''
CONSTANTE = 10
variable_numerica_entera = 5
variable_numerica_flotante = 5.5
variable_alfanumerica = "Hola"
variable_booleana = True

lenguaje_usado = "python"

print (f"Hola mundo, esta es mi primer reto en {lenguaje_usado} ")
