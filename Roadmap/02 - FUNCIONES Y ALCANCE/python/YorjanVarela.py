#función basica en python 

print("hola mundo") #imprime cosas en pantalla 

#función sin parametro ni retorno 

def saludar():
    print("¡Hola!")

saludar()  # Salida: ¡Hola!

#funciónes con uno o varios paramatros

def sumar(a, b):
    resultado = a + b
    print("La suma es:", resultado)

sumar(3, 5)  # Salida: La suma es: 8

#función con retorno

def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 6)
print(resultado)  # Salida: 24

#función dentro de otra función o función aninada

def funcion_externa(x):
    def funcion_interna(y):
        return x * y
    return funcion_interna

# Crear una función interna específica
multiplicar_por_5 = funcion_externa(5)

# Usar la función interna
resultado = multiplicar_por_5(3)
print(resultado)  # Salida: 15

#funciónes que ya vienen con el lenguaje 


valor_absoluto = abs(5) 
print(valor_absoluto) 

length = len("hola")
print(length)

type = type("hola")
print(type)



#entre muchas otras que harian el codigo infinito  pero son muchas y muy utiles cuya finalidad es evitar que escribamos el codigo desde cero.

#variables local y globales

# Variable global
mensaje = "Hola, mundo!"

def mi_funcion():
    # Variable local
    nombre = "Juan"
    print(mensaje)  # Podemos acceder a la variable global
    print(nombre)  # Solo podemos acceder a nombre dentro de la función

mi_funcion()
print(mensaje)  # Podemos acceder a mensaje fuera de la función
# print(nombre)  # Esto daría error, porque nombre solo existe dentro de mi_funcion()



#Ejercicio extra

def my_function(a, b):
    for i in range(1, 101): 
        if i % 3 == 0 and i % 5 == 0:
            print(a, b)
        elif i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        else:
            print(i)
    
print(my_function("hola", "mundo"))