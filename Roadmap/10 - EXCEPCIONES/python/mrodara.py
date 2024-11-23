#################### EXCEPCIONES EN PYTHON ############################

'''
Una excepción o un error de ejecución se produce durante la ejecución del programa. 
Las excepciones se pueden manejar para que no termine el programa.
'''

# Excepción de división por cero
try:
    a = 10/0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Finalizó la ejecución")

my_list = [i for i in range(5)]

try:
    print(my_list[5]) # Genera un IndexError
except IndexError:
    print(f"Índice fuera de rango, mostramos el último elemento de la lista: {my_list[-1]}")

# Definir una excepción propia
'''
Para crear un tipo de excepción personalizada en Python, podemos definir una nueva clase que herede 
de la clase base de excepciones. 
Esto permite generar errores específicos para ciertos casos en tu aplicación.
'''
class MyException(Exception):
    def __init__(self, message: str = "Error personalizado") -> None:
        super().__init__(message)
        
try:
    raise MyException("Este es un error personalizado")
except MyException as e:
    print(f"Captura de la excepción: {e}")
    
#################### FIN EXCEPCIONES EN PYTHON ############################

#################### EXTRA ############################

def my_exception_managment(value1 : int = 0, value2 : int = 0, value3: tuple = (), boolvalue: bool = True) -> None:
    try:
        return value1 / value2
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        
    try:
        value2 + value3
    except TypeError:
        print("No se puede sumar un entero con un string")
    
    try:
        print(value4)
    except NameError:
        print("La variable no está definida")# No se puede acceder a una variable no definida
    finally:
        print("Finalizó la ejecución")
    
my_exception_managment(10, 0, (1, 2, 3), True)

#################### FIN EXTRA ############################