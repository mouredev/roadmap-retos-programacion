# Funciones sin parametro ni retorno:

def saludar():
    print("¡Hola comunidad!")
    
saludar() # funcion que impreme un saludo

def imprimir_numeros():
    for i in range(1,6):
        print(i)

imprimir_numeros() # imprime numero del 1 al 5

# Funcion con parametro

def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Bonifacio") # saluda con un argumento

# Funcion con parametros

def sumar(a, b):
    resultado = a + b
    print(f"La suma {a} y {b} es {resultado}")

sumar(11, 28)

# Funcion con parametros predeterminados

def informacion_personal(nombre = "Desconocido", edad = 0, cuidad= "Desconocida"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Cuidad: {cuidad}")
    
informacion_personal() # sin parametros imprime valores predeterminados
informacion_personal("Fridolina") # con un parametro
informacion_personal("Fridolina", 30) # con dos parametro
informacion_personal("Fridolina", 30, "Kungsbacka") # con tres parametro

# Funcion con retorno

def crear_saludo(nombre):
    return f"¡Hola, {nombre}!"

c_saludo = crear_saludo("Yonaiker")
print(c_saludo)

# Funcion con varios retornos
def mayor_y_menor(numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return mayor, menor

numeros = [11, 15, 18, 22, 25, 28]
mayor, menor = mayor_y_menor(numeros)
print("El numero mayor: ",mayor)
print("El numero menor:", menor)

# Funcion con parametros y retorno
def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(11, 28)
print("El resultado de es:", resultado_suma)

# Funcion con parametros posionales variables
def saludo_variable(*nombres):
    for nombre in nombres:
        print(f"¡Hola, {nombre}!")

saludo_variable("Comunidad", "Bonifacio", "Frionilda", "Yonaiker")

# Funcion con parametros de palabra clave
def info_person_variable(**args):
    for clave, valor in args.items():
        print(f"{clave}: {valor}")

info_person_variable(nombre = "Bonifacio", edad = 23)

info_person_variable(nombre = "Frionilda", edad = 30, pais = "Suecia", equipo = "FC Barcelona")


# Extra

def imprime_numeros (texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
            contador += 1
        elif numero % 3 == 0:
            print(texto1)
            contador += 1
        elif numero % 5 == 0:
            print(texto2)
            contador += 1
        else:
            print(numero)
    return contador

nro_veces = imprime_numeros ("Fizz", "Buzz")
print("El numero que se ha impreso el número en lugar de los textos es: ", nro_veces)