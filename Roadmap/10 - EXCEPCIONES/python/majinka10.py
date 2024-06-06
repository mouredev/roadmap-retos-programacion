lista = [3]

# De manera general
def removerElemento(lista, elemento):
    try:
        lista.remove(elemento)
        print(f'Se pudo remover el elemento: {elemento}')
    except Exception as e:
        print(f'Ha ocurrido: {e}')

removerElemento(lista, 3)
removerElemento(lista, 3)
    
# De manera específica
def division(a:int, b: int) -> int:
    try:
        print(a/b)
    except ZeroDivisionError:
        print(f'No se puede dividir entre cero {ZeroDivisionError}')
    
division(10, 2)
division(5, 0)

# Ejercicio EXTRA
print("\nFunción que procesa parámetros o lanza excepciones\n")

class InvalidRoot(Exception):
    def __init__(self, mensaje = "InvalidRoot"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def operaciones(numero) -> int:
    try:
        if numero < 0:
            raise InvalidRoot("El número no puede ser negativo.")
        elif numero == 0:
            raise ValueError("El número no puede ser cero.")
        elif isinstance(numero, float):
            raise ValueError("El número no puede ser flotante.")
        else:
            print("El parámetro se procesó correctamente.")
    except (ValueError, InvalidRoot) as e:
        print(f'Excepción de valor: {e}')
    except Exception as e:
        print(f"Error inesperado: {e}")
    else: 
        print("No se produjo ningún error.")
    finally:
        print("La ejecución ha finalizado.\n")

operaciones(-3.5)
operaciones(0)
operaciones(5.7)
operaciones(3)