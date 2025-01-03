# Función sin parámetros ni retorno
numero1 = 3
numero2 = 5
cadena = "esto es una cadena"

def suma_sin_params_ni_retorno():
    suma = numero1 + numero2
    print("La suma sin parámetros ni retorno es ", suma)

# Función con parámetros pero sin retorno
def suma_con_params_sin_retorno(numero1, numero2):
    suma = numero1 + numero2
    print("La suma con parámetros pero sin retorno es ", suma)


# Función con parámetros y retorno
def suma_con_params_y_retorno(numero1, numero2):
    suma = numero1 + numero2
    return suma

# Funciones dentro de funciones
def funcion_dentro_funcion(numero1, numero2):
    def resta(suma):
        resta = suma - 67
        print(resta)
    suma = numero1 + numero2
    resta(suma)
    
    return suma

# Variables Locales
def suma_con_variables_locales(numero1, numero2):
    numero1 = 43
    numero2 = 54

    suma = numero1 + numero2
    return suma

def suma_con_variables_globales(numero1, numero2):
    suma = numero1 + numero2
    return suma


suma_sin_params_ni_retorno()
suma_con_params_sin_retorno(numero1, numero2)
print("La suma con parámetros y retorno es ", suma_con_params_y_retorno(numero1, numero2))

print(funcion_dentro_funcion(numero1, numero2))
print("esto es una función de pintar por la consola")
print("Esto es una función que da la longitud de una variable, esta es ", len(cadena))

print("Esto es una suma con variables Locales ", suma_con_variables_locales(numero1, numero2))
print("Esto es una suma con variables Globales ", suma_con_variables_globales(numero1, numero2))

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
cadena1 = "esto es la cadena 1"
cadena2 = "esto es la cadena 2"

def funcion_extra(cadena1, cadena2):
    contador = 0

    for i in range(1, 101):
        
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1, cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            contador += 1
    return contador

contador = funcion_extra(cadena1, cadena2)
print("el numero de veces que se ha impreso el numero es", contador)

def saludar(*names):
    for name in names:
        print(f"Hola: {name}!!")

saludar('pepe', 'juan', 'antonio', 'jose', 'pepita', 'cristina', 'angel')

def datos_usuario(**usuario): # es un diccionario
    for key, value in usuario.items():
        print(f"Hola su {key} es {value}")

datos_usuario(nombre='juan', apellidos='castro', edad=34, ciudad="Madrid", codigo_postal=28016)