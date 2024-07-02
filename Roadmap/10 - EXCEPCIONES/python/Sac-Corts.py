### Ejercicio ###

# Try | Except | Finally

try:
    numero1 = int(input("Introduce un número: "))
    numero2 = int(input("Introduce un número: "))
    resultado = numero1 + numero2
    print(resultado)
except:
    print("Solamente puedes ingresar números enteros.")
finally:
    print("Saludos")


### Ejercicio Extra ###

# Definir la excepción personalizada
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Definir la función que puede lanzar excepciones
def procesar_parametros(param):
    if not isinstance(param, int):
        raise TypeError("El parámetro debe ser un entero")
    elif param < 0:
        raise ValueError("El parámetro no puede ser negativo")
    elif param == 42:
        raise CustomException("El parámetro no puede ser 42")
    else:
        return f"El parámetro es {param}"

# Capturar las excepciones desde el lugar donde se llama a la función
def main():
    parametros = [10, -5, "string", 42, 15]
    
    for param in parametros:
        try:
            resultado = procesar_parametros(param)
            print(resultado)
        except TypeError as e:
            print(f"Se ha producido un TypeError: {e}")
        except ValueError as e:
            print(f"Se ha producido un ValueError: {e}")
        except CustomException as e:
            print(f"Se ha producido una CustomException: {e}")
        except Exception as e:
            print(f"Se ha producido una excepción inesperada: {e}")
        else:
            print("No se ha producido ningún error")
        finally:
            print("La ejecución ha finalizado para el parámetro actual")

print(main())