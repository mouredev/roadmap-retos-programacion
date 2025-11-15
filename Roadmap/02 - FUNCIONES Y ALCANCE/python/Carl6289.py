# Función sin parámetros ni retorno
def mensaje():
    print("Esto es una función sin parámetros ni retorno")
mensaje() # Llamada de la función
print()

# Función con uno o varios parámetros
print("Función con uno o varios parámetros:")
def camisetas(color, cantidad):
    mensaje_camisetas = f"De las camisetas color {color}, quedan disponibles un total de {cantidad} camisetas"
    print(mensaje_camisetas)
camisetas("negro", 13) # Llamada de la función
print()

# Función con retorno
print("Función con retorno:")
def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma 
resultado = sumar_numeros(72, 33) # Llamada de la función
print(f"El resultado de la suma es: {resultado}")
print()

# Funciones dentro de funciones
print("Funciones dentro de funciones:")
def funcion_externa(nombre):
    saludo = "¡Hola,"
    def funcion_interna():        
        saludo_completo = f"{saludo} {nombre}!"
        print(saludo_completo)
    funcion_interna()
funcion_externa("Carlos")
print()

# Funciones ya creadas en el lenguaje
print("Funciones ya creadas en el lenguaje:")
print("Ejemplo con la funcion len()")
cadena = "Hola Python"
print(f"La variable cadena tiene una longitud de: {len(cadena)}")
lista = [10, 20, 30]
print(f"La variable lista tiene una longitud de: {len(lista)}")
print()

# Ejemplo con la funcion type()
print("Ejemplo con la funcion type()")
numero = 14
animales = ["Jirafa", "Hipopotamo", "Raton"]
print(f"La variable numero es del tipo: {type(numero)}")
print(f"La variable animales es del tipo: {type(animales)}")
print()

# Ejemplo con la funcion input()
print("Ejemplo con la funcion input()")
# edad = input("Escribe tu edad: ") <--- Comentado para que no interfiera con el resto de la ejecución del ejercicio
print()

# Ejemplo con la funcion int()
print("Ejemplo con la funcion int()")
minutos = 103.6
print(f"Han transcurrido {int(minutos)} minutos")
print()

# Ejemplo con la funcion str()
print("Ejemplo con la funcion str()")
tiene_hijos = True
print(f"Tiene hijos: {str(tiene_hijos)}")
print()

# Ejemplo con la funcion float()
print("Ejemplo con la funcion float()")
litros = 6
print(f"Litros: {float(litros)}")
print()

# Ejemplo con la funcion abs()
print("Ejemplo con la funcion abs()")
num_negativo = -8
print(f"El número negativo ahora es: {abs(num_negativo)}")
print()

# Ejemplo con la funcion sum()
print("Ejemplo con la funcion sum()")
lista_numeros = [23, 19, 58, 36, 14]
print(f"La suma de los números en la lista es: {sum(lista_numeros)}")
print()

# Ejemplo con la funciones max() y min()
print("Ejemplo con la funciones max() y min()")
print(f"El número mas grande de la lista es: {max(lista_numeros)}")
print(f"El número mas pequeño de la lista es: {min(lista_numeros)}")
print()

# Variable LOCAL y GLOBAL en una función
print("Variable LOCAL y GLOBAL en una función:")
color = "Azul" # Variable global
def mostrar_color():
    color = "Rojo" # Variable local
    print(f"La variable local es: {color}")
mostrar_color()
print(f"La variable global es: {color}")
print()

# Dificultad extra
print("DIFICULTAD EXTRA:")
texto_1 = "múltiplo de tres"
texto_2 = "múltiplo de cinco"
def numeros_1_100(texto_1, texto_2):
    contador = 0    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: 
            print(f"{texto_1} y {texto_2}")
        elif i % 3 == 0:
            print(f"{texto_1}")
        elif i % 5 == 0:
            print(f"{texto_2}")
        else:
            print(i)
            contador += 1
    return contador
veces_numero = numeros_1_100(texto_1, texto_2)
print(f"El número se imprimió {veces_numero} veces")