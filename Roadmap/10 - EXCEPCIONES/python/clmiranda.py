# EXCEPCIONES

# Uso de try-except
try:
    name = input("Ingresa tu nombre: ")
    age = int(input("Ingresa tu edad: "))
    print(f"Tu nombre es {name} y tienes {age} años")
except ValueError:
    print("No se ha ingresado un número para la edad")


# División entre 0
try:
    division = 35 / 0
    print(f"El resultado es {division}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
finally:
    print("Bloque que siempre se ejecuta")



# Ejercicio - Dificultad Extra

class MyOwnException(Exception):
    def __init__(self, message):
        self.message = message

def operations(numbers : list):
    if len([i for i in numbers if isinstance(i, str)]) >= 1:
        raise MyOwnException("Todos los elementos de la lista deben ser enteros")
    if not all(numbers):
        raise ZeroDivisionError()
    if len(numbers) < 4:
        raise ValueError()
    
    return sorted(numbers, reverse=True)

try:
    print(operations([15, 87, 23, 49, 7]))
except MyOwnException as own:
    print(own)
except ZeroDivisionError:
    print("Ningun valor de la lista puede ser 0")
except ValueError:
    print("Se requiere un mínimo de 4 elementos")
except Exception as e:
    print(f"Ha sucedido un error inesperado: {e}")
else:
    print("No ocurrió ningún error en la ejecución")
finally:
    print("La aplicación ha finalizado su ejecución")