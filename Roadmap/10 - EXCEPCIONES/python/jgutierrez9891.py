## Ejercicio

numbera = int(input("Ingrese el primer número: "))
numberb = int(input("Ingrese el segundo número: "))
try:
    resultado = numbera / numberb
    print("El resultado es: " + str(resultado))
except ZeroDivisionError:
    print("Error: División por cero no está permitida.")
except Exception as e:
    print("Ocurrió un error: " + str(e))
finally:
    print("Operación finalizada.")

## Dificultad Extra
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise CustomError("El número no es positivo.")
    return True

try:
    num = int(input("Ingrese un número positivo: "))
    if check_positive(num):
        print("El número es positivo.")
except CustomError as ce:
    print("Error personalizado: " + ce.message)
except ValueError:
    print("Error: Entrada inválida, por favor ingrese un número entero.")
except Exception as e:
    print("Ocurrió un error: " + str(e))
finally:
    print("Verificación finalizada.")
