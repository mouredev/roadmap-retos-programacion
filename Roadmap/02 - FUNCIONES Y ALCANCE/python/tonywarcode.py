#función sin parámetros de entrada ni parámetros de salida

def say_hello():
    print("Hola Python")

say_hello()

#funció con retorno

def retorno_hello():
    return "Hola Python2"


retrorno_h = retorno_hello()  #guardar en variable
print(retorno_hello())  #o imprimir


#pasando un argumento de entrada

def say_hello2(nombre):
    print("Hola", nombre)
    print(f"holas,{nombre}!")

say_hello2("Python3")


#varios argumentos con retorno

def suma(a, b):
    return a+b

print(suma(10, 15))

#con longitud variable

def suma1(*numeros):
    print(type(numeros))
    total = 0
    for i in numeros:
        total += i
    return total

print(suma1(1, 2, 3, 4, 5))

#con longitud variable y clave valor

def suma(**numeros):
    suma = 0
    for key, value in numeros.items():
        print(key, value)
        suma += value
    return suma

print(suma(a=9, b=20, c=21, d=0))

#funciones dentro de funciones

def funcion1():
    def funcion2():
        print("dentro de la funcion 2")
    funcion2()

funcion1()

#documentacion que hace una funcion o como usarla

def mi_funcion_suma(a, b):
    """
    Descripción de la función. Como debe ser usada,
    que parámetros acepta y que devuelve
    """
    return a+b

help(mi_funcion_suma)

#funciones del lenguaje
print("¡Hola, Python!") #imprime 

print(len("Hola python"))  #longitud del objeto

print(type([1, 2, 3, "green"]))  #tipo de dato

print("hola, python".upper()) #pone en mayusculas

print(range(20))  #rango de numeros

#variable LOCAL y GLOBAL

v_global = "Python"
print(v_global)

def hi_var_global():
    v_local= "Me encanta"
    print(v_local ,v_global)

hi_var_global()
#print(v_local) no se puede acceder a la variable de dentro de la función

'''
* DIFICULTAD EXTRA (opcional):
'''
def print_numeros_con_texto(texto1, texto2):
    # Inicializa un contador para los números impresos directamente
    contador_numeros = 0
    
    # Itera sobre los números del 1 al 100
    for i in range(1, 101):
        # Si el número es múltiplo de 3 y de 5, imprime la concatenación de texto1 y texto2
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        # Si el número es múltiplo de 3, imprime texto1
        elif i % 3 == 0:
            print(texto1)
        # Si el número es múltiplo de 5, imprime texto2
        elif i % 5 == 0:
            print(texto2)
        # Si el número no es múltiplo de 3 ni de 5, imprime el número
        else:
            print(i)
            # Incrementa el contador de números impresos directamente
            contador_numeros += 1

    # Retorna el número de veces que se imprimieron los números directamente
    return contador_numeros

# Ejemplo de uso de la función con los textos "Max" y "Mix"
num_cont = print_numeros_con_texto("Max", "Mix")

# Imprime el número de veces que se imprimieron números en lugar de textos
print(f"El número de veces que se imprimieron los números en lugar de los textos es: {num_cont}")

