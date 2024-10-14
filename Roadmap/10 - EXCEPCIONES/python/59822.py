''' Try/ Except /Finally

# Try / Except / Finally es una estructura que permite manejar errores 
# en tiempo de ejecución, es decir, cuando el programa ya está en ejecución.
'''

def division(x: float, y: float):
    return x / y

try:
    resultado = division(10, 0)
    print(resultado)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa")
    
# Ejemplo
# En este ejemplo se muestra como se puede manejar un error en tiempo de ejecución

def saludo(x : str):
    return "Hola " + x

try:
    hola = saludo(2)
    print(hola)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa")
    
def contraseña(x: str):
    if len(x) < 10:
        raise ValueError("La contraseña debe tener más de 9 caracteres")
    
''' Extra '''
class Ortography(Exception):
    def __init__(self, text: str):
        self.text = text
        
def oracion(x: str):
    if x[-1] != ".":
        raise Ortography("El texto no termina en punto")
    if (x.isnumeric):
        raise Ortography("El texto no puede ser un número")
    if len(x) < 1:
        raise Ortography("El texto no puede estar vacío")
    
try:
    oracion(0/0)
except Exception as e:
    print("Revisar la info del problema")
finally:
    print("Fin del programa")