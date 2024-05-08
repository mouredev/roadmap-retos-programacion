# Reto 02 - Funciones y alcance
from builtins import print, len, type, range, str

# Funcion sin parametros y llamada a funcion

def arrancar_moto():
    print("Kikiki, chak, broooooom broom")

arrancar_moto()

# Funcion con parametros y llamada a funcion

def seguridad_moto(guantes, casco):
    if(guantes and casco):
        print("Listo para salir.")

seguridad_moto(True, True)

# Funcion con parametros, valor de retorno y llamada a funcion

def tiempo_ruta(distancia, velocidad):
    return distancia / velocidad

print(tiempo_ruta(150, 89.5))

# Funcion dentro de funcion

def numero_favorito(numero):

    def repetir_numero_favorito(veces):
        return (numero * veces)
    
    print(f'Tu numero favorito {numero} repetido varias veces es ' + str(repetir_numero_favorito(numero)))

numero_favorito(49)

# Funciones existentes
flag = True
print(type(flag))

mensaje = "Mi moto funciona muy bien."
print(len(mensaje))
print(mensaje.lower())
print(mensaje.upper())
x = range(0, 11)
print(x)

# Variables locales y globales
variable_global = "Soy una variable global."

def caja_de_variables():
    variable_local = "Soy una variable local."
    print(variable_global)
    print(variable_local)

caja_de_variables()

# Ejercicio extra
def imprimeNumeros(texto1, texto2):
    numero = 0
    
    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 == 0):
            print(texto1 + texto2)
        elif(i % 3 == 0):
            print(texto1)
        elif(i % 5 == 0):
            print(texto2)
        else:
            print(i)
            numero += 1

    return numero

a = imprimeNumeros("Mult3", "Mult5")
print(a)