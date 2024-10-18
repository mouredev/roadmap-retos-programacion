
#1. Funciones básicas
#a) Función sin parámetros ni retorno
def saludo():
    print("Hola, bienvenido al programa")

saludo()
#b) Función con un parámetro
def saludo_personalizado(nombre):
    print(f"Hola, {nombre}, bienvenido al programa")

saludo_personalizado("Mercedes")
#c) Función con varios parámetros
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es {resultado}")

sumar(5, 3)
#d) Función con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print(f"El resultado de la multiplicación es {resultado}")
#e) Función dentro de otra función
def funcion_externa():
    print("Esta es la función externa")

    def funcion_interna():
        print("Esta es la función interna")
    
    funcion_interna()

funcion_externa()

#2. Uso de funciones ya creadas (funciones integradas en Python)
numeros = [3, 6, 9, 12]
print(f"Números originales: {numeros}")
numeros_duplicados = list(map(lambda x: x * 2, numeros))
print(f"Números duplicados: {numeros_duplicados}")

#3. Variables locales y globales
# Variable global
mensaje = "Hola desde el ámbito global"

def imprimir_mensaje():
    # Variable local
    mensaje = "Hola desde el ámbito local"
    print(mensaje)

imprimir_mensaje()  # Imprime el mensaje local
print(mensaje)  # Imprime el mensaje global

#4. Dificultad extra: Función que recibe dos cadenas y retorna un número
def extra(cadena1, cadena2):
    contador_numeros = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + " " +cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            contador_numeros += 1
    return contador_numeros

resultado = extra("cadena1", "cadema2")
print(f"Se ha impreso el número en lugar de texto {resultado} veces.")
