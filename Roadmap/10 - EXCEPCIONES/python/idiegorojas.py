# Excepciones

# Tipos de excepciones

# ZeroDivisionError: Ocurre cuando se intenta dividir entre cero.
# TypeError: Ocurre cuando se realiza una operación con tipos de datos incompatibles.
# ValueError: Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.
# FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
# IndexError: Ocurre cuando se intenta acceder a un índice fuera de rango en una lista.
# KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.

# Estructura basica
try:
    # Dividir por cero genera la excepcion 'ZeroDivisionError'
    resultado = 10 / 0
except ZeroDivisionError:
    # Codigo que se ejecuta si se da la excepcion 'ZeroDivisionError'
    print('Error: No se puede dividir entre cero.')
else:
    # Codigo que se ejecuta si no hay ninguna excepcion
    print('La divison se realizo correctamente.')
finally:
    # Codigo que siempre se ejecuta, haya o no excepciones
    print('Este bloque siempre se ejecuta.')

print('---------------------')

# Multiples excepciones
try:
    resultado = 10 / 0
except (ZeroDivisionError, TypeError, ValueError) as e:
    print(f'Error: {e}')


print('---------------------')


# Excepciones personalizadas
class MiErrorPersonalizado(Exception):
    pass


try:
    raise MiErrorPersonalizado('Este es un error personalizado.')
except MiErrorPersonalizado as e:
    print(e)

print('---------------------')


# Ejemplo:
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero.')
    except TypeError:
        print('Error: Los tipos de datos no son validos')
    else:
        print(f'El resultado de dividir {a} y {b} es: {resultado}')
    finally:
        print('Fin del bloque.')

dividir(3, 4)
dividir(3, 0)
dividir(3, 'a')

print('---------------------')

# Extra

class ValorInvalidoError(Exception):
    def __init__(self, mensaje="El valor proporcionado no es válido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_parametros(numero, texto):
    if not isinstance(numero, int):
        raise TypeError("El primer parámetro debe ser un número entero")
    
    if not isinstance(texto, str):
        raise TypeError("El segundo parámetro debe ser una cadena de texto")
    
    if numero < 0:
        raise ValorInvalidoError("El número debe ser positivo")
    
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío")
    
    return f"Número: {numero}, Texto: {texto}"


def probar_funcion():
    casos_prueba = [
        (10, "Hola"),          # Caso válido
        (-5, "Mundo"),         # Número negativo
        (15, ""),              # Texto vacío
        ("no_numero", "Test"), # Tipo incorrecto
    ]
    
    for numero, texto in casos_prueba:
        try:
            resultado = procesar_parametros(numero, texto)
            print(f"¡Éxito! {resultado}")
        except ValorInvalidoError as e:
            print(f"Error personalizado: {e}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            print("La ejecución de este caso ha finalizado")
        print("-" * 50)


if __name__ == "__main__":
    probar_funcion()