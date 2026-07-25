#Functions

# 1. Función sin parámetros ni retorno
def saludar():
    print("¡Hola, bienvenido a Python!")

saludar()

# 2. Función con un parámetro
def saludar_nombre(nombre):
    print(f"¡Hola, {nombre}!")

saludar_nombre("Jhoao")

# 3. Función con múltiples parámetros
def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")

sumar(5, 3)

# 4. Función con retorno de valor
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print(f"El resultado de la multiplicación es: {resultado}")

# 5. Función con parámetros por defecto
def potencia(base, exponente=2):
    return base ** exponente

print(f"El cuadrado de 5 es: {potencia(5)}")
print(f"5 elevado a la 3 es: {potencia(5, 3)}")

# 6. Función con un número variable de argumentos (*args)
def sumar_varios(*numeros):
    return sum(numeros)

print(f"La suma de varios números es: {sumar_varios(1, 2, 3, 4, 5)}")

# 7. Función con argumentos nombrados (**kwargs)
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Jhoao", edad=30, ciudad="Bogotá")

# 8. Función lambda (función anónima con retorno)
doblar = lambda x: x * 2
print(f"El doble de 7 es: {doblar(7)}")

# 9. Función con una función dentro (función anidada)
def operacion(x):
    def cuadrado(n):
        return n ** 2
    return cuadrado(x)

print(f"El cuadrado de 6 es: {operacion(6)}")

# 10. Función generadora (yield)
def contar_hasta(n):
    for i in range(1, n+1):
        yield i

for numero in contar_hasta(5):
    print(numero)

#Dificultad extra

def print_numbers(string1,string2):
    def count_until(n):
        for i in range(1, n+1):
            yield i
            
    how_many = 0
    
    for numero in count_until(100):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{string1} and {string2}")
        elif numero % 3 == 0:
            print(string1)
        elif numero % 5 == 0:
            print(string2)
        else:
            print(numero)
            how_many += 1
    
    print(f"Total de números: {how_many}")

print_numbers("Fizz","Buzz")