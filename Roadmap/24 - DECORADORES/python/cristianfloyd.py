# EJERCICIO:
# Explora el concepto de "decorador" y muestra cómo crearlo
# con un ejemplo genérico.
from functools import wraps
from typing import Callable, Any

def mi_decorador(funcion_original):
    def nueva_funcionalidad():
        print("Estoy antes de la ejecución de la función original")
        funcion_original()
        print("Estoy después de la ejecución de la función original")

    return nueva_funcionalidad


@mi_decorador
def funcion_original():
    print("\tEstoy dentro de la función original")


@mi_decorador
def funcion_original_2():
    print("\tEstoy dentro de la función original 2")


@mi_decorador
def funcion_original_3():
    print("\tEstoy dentro de la función original 3")


funcion_original()
funcion_original_2()
funcion_original_3()


#
# DIFICULTAD EXTRA (opcional):
# Crea un decorador que sea capaz de contabilizar cuántas veces
# se ha llamado a una función y aplícalo a una función de tu elección.




class ContadorDeLlamadas:
    """
    Decorador que cuenta cuantas veces se ha llamado a una funcion.
    """
    def __init__(self, funcion: Callable[..., Any]) -> None:
        wraps(funcion)(self)
        self.funcion = funcion
        self.contador: int = 0
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.contador += 1
        print(f"Llamada #{self.contador} a '{self.funcion.__name__}'")
        return self.funcion(*args, **kwds)
        

@ContadorDeLlamadas
def saludar(nombre: str) -> None:
    print(f"Hola, {nombre}!")

@ContadorDeLlamadas
def multiplicar(a: int, b: int) -> int:
    return a * b


print("-" * 100)
print("Testeando el decorador contador de llamadas")
print("-" * 100)
saludar("Cristian")
saludar("Floyd")
saludar("Cristian")

print(f"Total de llamadas: {saludar.contador}")

print("-" * 100)
print("Testeando el decorador contador de llamadas con una funcion que retorna un valor")
print("-" * 100)
print(f"Resultado de la multiplicacion de 2 y 3: {multiplicar(2, 3)}")
print(f"Resultado de la multiplicacion de 4 y 5: {multiplicar(4, 5)}")
print(f"Total de llamadas: {multiplicar.contador}")