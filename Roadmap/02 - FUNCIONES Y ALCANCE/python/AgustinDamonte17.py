# -----------------------------
# Función sin parámetros ni retorno
# -----------------------------
def saludar():
    print("Hola, mundo!")

saludar()
print()

# -----------------------------
# Función con parámetros
# -----------------------------
def saludar_nombre(nombre):
    print(f"Hola, {nombre}!")

saludar_nombre("Agustín")
print()

# -----------------------------
# Función con varios parámetros y retorno
# -----------------------------
def sumar(a, b):
    return a + b

resultado = sumar(5, 7)
print("Resultado de sumar(5, 7):", resultado)
print()

# -----------------------------
# Función dentro de función
# -----------------------------
def funcion_externa(x):
    def funcion_interna(y):
        return y * 2
    print("Resultado de funcion_interna:", funcion_interna(x))

funcion_externa(4)
print()

# -----------------------------
# Uso de funciones ya creadas en Python
# -----------------------------
numeros = [4, 2, 8, 1]
print("Lista original:", numeros)
print("Lista ordenada con sorted():", sorted(numeros))
print("Longitud con len():", len(numeros))
print("Máximo con max():", max(numeros))
print()

# -----------------------------
# Variables GLOBAL y LOCAL
# -----------------------------
variable_global = "Soy global"

def prueba_variables():
    variable_local = "Soy local"
    print("Dentro de la función:")
    print("Local:", variable_local)
    print("Global (accedida):", variable_global)

prueba_variables()

print("\nFuera de la función:")
print("Global:", variable_global)
# print(variable_local)  # Esto daría error si lo descomentás
print()

# -----------------------------
# DIFICULTAD EXTRA
# -----------------------------
def fizzbuzz_personalizado(palabra1, palabra2):
    contador_numeros = 0
    for i in range(1, 101):
        texto = ""
        if i % 3 == 0:
            texto += palabra1
        if i % 5 == 0:
            texto += palabra2
        if texto:
            print(texto)
        else:
            print(i)
            contador_numeros += 1
    return contador_numeros

print("Ejecutando FizzBuzz personalizado:")
veces_impreso_numero = fizzbuzz_personalizado("Fizz", "Buzz")
print(f"Números impresos (sin Fizz ni Buzz): {veces_impreso_numero}")
