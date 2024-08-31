# Web oficial de Python: https://www.python.org/
# Web para aprender Python: https://www.learnpython.org/es/

#Comentario de una sola linea

"""
Comentario de varias lineas
"""

#Variables
#Una variable es un contenedor de informacion
variable = "Hola Mundo"
variable = 10

#Constante 
#Es un contenedor de informacion que no puede cambiar su valor, en Python no existen las constantes, pero se llego a una convencion de que se usaran mayusculas para identificarlas
PI = 3.1416

#Variables de todos los tipos de datos primitivos
cadena = "Hola soy una cadena de texto"
entero = 99
flotante = 4.2
booleano = True

#Variables de todos los tipos de datos complejos o estructurados
lista = [10,20,30,40,50]
tupla = (100,200,300,400,500)
my_set = {"Hola", "Mundo", "!"}
diccionario = {
    "nombre":"Victor",
    "apellido":"Robles",
    "curso":"Master en Python"
}
rango = range(9)
complejo = 7j + 3

#Byte 
#Es un tipo de dato que se utiliza para trabajar con datos binarios
dato_byte = b"Probando"
dato_normal = "Probando"

#Imprimir por consola
print(f"La variable declarada con byte es: {dato_byte}")
print(f"La variable declarada normal es: {dato_normal}")
print(f"El primer caracter del byte es: {dato_byte[0]}")
print(f"El primer caracter del normal es: {dato_normal[0]}")

#No se puede modicar dato_byte
try:
    dato_byte[0]="p"
except TypeError as e:
    #Captura el error y lo muestra
    print(f"Error: {e}")
 
print(f"La variable declarada con byte no se puede modificar individualmente {dato_byte}")

#Imprimir hola mundo
print(f"¡Hola, Python!")
