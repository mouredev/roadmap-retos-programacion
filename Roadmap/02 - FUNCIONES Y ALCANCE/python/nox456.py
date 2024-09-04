# Función sin parámetros ni retorno
def saludar():
    print("Holaaa!!")

saludar()

# Función con parámetros contados y retorno
def suma(num1,num2):
    return num1 + num2

print(suma(5, 2))

# Función con parámetros variables y retorno
def multiplicar(*nums):
    resultado = 1
    for i in nums:
        resultado = resultado * i
    return resultado

print(multiplicar(2,5,10,5))

# Funciones anidadas
def accion(nombre):
    def comer(comida):
        print(f"{nombre} está comiendo {comida}")
    def jugar(juego):
        print(f"{nombre} está jugando {juego}")

    comer("pizza")
    jugar("Fallout (juegazo)")

accion("Gabriel")

# Función predefinida por el lenguaje
nombre = "Gabriel"
print(f"La longitud el nombre es {len(nombre)}")

# Variable local
num = 5
def mostrarNum(num):
    print(f"Número es: {num}")
    num = 10
    print(f"(Dentro de la función) el número es: {num}")

mostrarNum(num)
print(f"(Fuera de la función) el número sigue siendo: {num}")

# Variable global
edad = 19
def mostrarEdad():
    global edad
    print(f"La edad inicialmente es {edad}")
    edad = 20
    print(f"(Dentro de la función) Ahora la edad es {edad}")

mostrarEdad()
print(f"(Fuera de la función) la edad también es {edad}")

# DIFICULTAD EXTRA

def contar(texto1,texto2):
    count = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            count += 1
    return count

print(f"La veces que se imprimió el número fueron: {contar("hola", "adios")}")

