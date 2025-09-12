# funcion decoradora que recibe otra funcion como parametro
def decorador(funcion):
    # crear otra funcion
    def f():
        print('Antes de ejecutar la función') # hacer algo antes
        funcion() # ejecutar la funcion recibida como argumento
        print('Después de ejecutar la función') # hacer algo después
    
    # retornar funcion f
    # f = funcion decoradora + funcion recibida como argumento
    return f

# decorar la funcion saludo
@decorador
def saludo():
    print('Hola!')

# ejecutar la funcion con el decorador aplicado
saludo()

print("\n")

# ---- DIFICULTAD EXTRA ----

from random import choice, randint

def contador(funcion):
    # *args: argumentos posicionales variables
    # **kwargs: diccionario de argumentos variables
    def f(*args, **kwargs):
        f.contador += 1
        return funcion(*args, **kwargs)

    # a la funcion le añado una propiedad contador
    f.contador = 0
    return f

@contador
def sumatoria(m, M):
    return sum(range(m, M))

@contador
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

for _ in range(10):
    bin_choice = choice([0, 1])
    if bin_choice:
        m = randint(-10, 10)
        M = abs(m) * 2
        print(f"Sumatoria de {m} a {M}: {sumatoria(m, M)}")
    else:
        n = randint(0, 10)
        print(f"Factorial de {n}: {factorial(n)}")

print()
print(f"Cantidad de sumas: {sumatoria.contador}")

# el factorial se ejecuta mas veces porque es recursivo
print(f"Cantidad de factoriales: {factorial.contador}")