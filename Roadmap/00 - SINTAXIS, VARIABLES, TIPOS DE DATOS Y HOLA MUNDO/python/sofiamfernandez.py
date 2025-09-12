# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO by sofiamfernandez 
# url del sitio oficial https://www.python.org/

#Diferentes sintaxis de comentarios en Python:  

#Comentario en línea

"""
Esto es un bloque
comentado o un
comentario 
en bloque
"""

#VARIABLES

nombre_de_usuario = "Pepe Hongo"
print(nombre_de_usuario)

#CONSTANTES : En Py no existen las constantes pero nos referimos a las variables que no cambian con el nombre en mayúsculas

DIAS_DE_LA_SEMANA = 7
print(DIAS_DE_LA_SEMANA)

#TIPOS DE DATOS BASITOS

entero       = 77                          #int
flotante     = 7.4                         #float
complejos    = 10.3j                       #complex
cadenas      = "Pepe", "Pepa", "Pig"       #str
booleano     = True , False                #bool
diccionario  = {
  "Nombre": "Pepe",
  "Edad": 27,
  "Documento": 1003882
}                                           #dict
lista        = ["Paula", 14, True]          #list
tupla        = ("Paula", 14, 7.8 , False)   #tuple
conjunto     = {3, 4, 5, "Jimena", 3.21}    #set
rango        = range(5,10)                  #range
binario      = bytes(45)                    #bytes

#IMPRIMIR POR TERMINAL 
nombre_de_lenguaje = "Python"
print("Hola " + nombre_de_lenguaje)

