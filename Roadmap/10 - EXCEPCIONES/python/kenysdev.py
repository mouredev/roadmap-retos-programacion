# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# EXCEPCIONES 
# -----------------------------------
# - Representan una forma de controlar el comportamiento de un programa
#   cuando se produce un error.
# - Lista de excepciones que pueden presentarse: 
#   (https://docs.python.org/3/library/exceptions.html) 
#____________________________________
# Capturar excepciones
a = 7; b = 0
try:
    r = a/b
except ZeroDivisionError:
    print("Error ..")

#____________________________________
# Cpturar diferentes exepciones
try:
    #r = int("uno") + 2
    r = 7 + "txt"
except ValueError:
    print("Error al convertir")
except TypeError:
    print("Error de tipos.")

#____________________________________
# Tratar multiples exepciones en el mismo bloque
try:
    #r = 7/0
    r =7 + "txt"
except (ZeroDivisionError, TypeError):
    print("Error Divicion o de tipos")

#____________________________________
# Cuando se desconoce el tipo de excepción
my_list = [1,2,3]
try:
    print(my_list[7])
except Exception:
    print("Excepción ..")

# saber que excepción ha ocurrido
try:
    r = int("uno") + 2
except Exception as ex:
    print("Excepción: ", type(ex))

#NOTA: todas las excepciones heredan de "Exception".

#____________________________________
# Uso de else
my_list = [1,2,3]
try:
    print(my_list[2])
    #print(my_list[7])
except IndexError:
    print("Indice fuera del rango")
else:
    print("No hay excepción")

#____________________________________
# Uso de finally
# - Se ejecuta siempre, haya o no una excepción
try:
    r = 5/0
except:
    print("Excepción")
finally:
    print("bloque finally")

#____________________________________
# Uso de raise para ejecutar una excepción
'''
raise ZeroDivisionError("Error Divicion")
raise IndexError
raise TypeError("..")
'''

# -----------------------------------
# Definiendo Excepciones
# -----------------------------------
# Para crear una excepción, solamente tenemos que 
# crear una clase que herede de la clase Exception.

class Custom_Exception(Exception):
    def __init__(self, msg="Error personalizado"):
        self.msg = msg
        super().__init__(self.msg)

# simulando error
try:
    raise Custom_Exception
    #raise Custom_Exception("Error")
except Custom_Exception as ex:
    print(type(ex))
    print(ex.args)
    print(ex.msg)
#____________________________________
# Pasar a la excepción un argumento en forma de diccionario.
class MyExeption(Exception):
    pass

try:
    raise MyExeption({"msg":"Mensaje", "info":"Informacion"})
except MyExeption as ex:
    dic = ex.args[0]
    print(dic)
    print(dic["msg"])
    print(dic["info"])

# -----------------------------------
# Ejercicio:
# -----------------------------------
"""
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado. 
"""

class OddNumberError(Exception):
    pass

def division(a, b):
    if b % 2 != 0:
        raise OddNumberError
    return (f"\n- El resultado es: {a/b}")

def operation(a, b):
    try:
        print(division(a, b))

    except TypeError as ex:
        print("\nError: No se permite texto. ->", type(ex))

    except ZeroDivisionError as ex:
        print("\nError: No es posible dividir entre 0.->", type(ex))

    except OddNumberError as ex:
        print("\nError: no dividir entre impares. ->", type(ex))

    else:
        print("- No hubo errores.")

    finally:
        print("- Operación terminada.")

print("\n___________\nEjercicio:")
operation(10, "uno")
operation(10, 0)
operation(10, 5)
operation(10, 2)
