# Ejemplo de función sin parámetros ni retorno
def saludar():
    print("Hola, este es un saludo desde una función sin parámetros ni retorno.")

# Ejemplo de función con un parámetro
def saludar_persona(nombre):
    print(f"Hola, {nombre}, este es un saludo personalizado.")

# Ejemplo de función con varios parámetros
def sumar(a, b):
    print(f"La suma de {a} y {b} es {a + b}.")

# Ejemplo de función con retorno
def multiplicar(a, b):
    return a * b

# Ejemplo de función dentro de otra función
def funcion_externa():
    print("Esta es la función externa.")

    def funcion_interna():
        print("Esta es la función interna.")
    
    funcion_interna()

# Ejemplo de uso de una función ya creada en el lenguaje
def ejemplo_funcion_nativa():
    numeros = [1, 2, 3, 4, 5]
    print(f"El máximo de la lista {numeros} es {max(numeros)}.")

# Ejemplo de variable LOCAL y GLOBAL
global_variable = "Soy una variable global"

def ejemplo_variables():
    local_variable = "Soy una variable local"
    print(local_variable)
    print(global_variable)

# Llamadas a las funciones para mostrar los resultados
saludar()
saludar_persona("José")
sumar(3, 5)
resultado = multiplicar(4, 6)
print(f"El resultado de la multiplicación es {resultado}.")
funcion_externa()
ejemplo_funcion_nativa()
ejemplo_variables()

# Modificando la variable global
def modificar_global():
    global global_variable
    global_variable = "He sido modificada desde una función"
    print(global_variable)

modificar_global()

#dificultad extra
def fizzbuzzito():
    for i in range(1,101):
        if i %3==0 and i%5==0:
            print("Fizzbucito")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzzito")
        else:
            print(i)
fizzbuzzito()
