# Sin parámetros
def saludar() -> None:
    print("Hola")

# Un parámetro
def saludar_a(nombre: str) -> None:
    print(f"Hola, {nombre}")

# Múltiples parámetros
def sumar(a: int, b: int) -> int:
    return a + b

# Con retorno
def cuadrado(n: int) -> int:
    return n ** 2

# Función anidada
def externa() -> None:
    def interna() -> None:
        print("soy interna")
    interna()

# Scope
variable_global: str = "global"

def demo_scope() -> None:
    variable_local: str = "local"
    print(variable_global)
    print(variable_local)

saludar()
saludar_a("Franco")
print(sumar(3, 4))
print(cuadrado(5))
externa()
demo_scope()

# Reto extra: FizzBuzz como función que retorna la cantidad de números impresos
def fizzbuzz(inicio: int, fin: int) -> int:
    count: int = 0
    for n in range(inicio, fin + 1):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
        count += 1
    return count

total = fizzbuzz(1, 20)
print(f"Números impresos: {total}")
