#============================
# 49 El almacen de Papá Noel
#============================

import random
import sys

# Funcion que comprueba errores

def validar_cadena(cadena):

    if len(cadena) != 4:
        return "Error: La cadena debe tener exactamente 4 caracteres."

    errores = []

    for char in cadena:
        if char not in "ABC123":
            errores.append(f"'{char}'")

    if len(set(cadena)) != len(cadena):
        errores.append("Los caracteres no deben repetirse")

    if errores:
        return f"Error: {', '.join(errores)}. Solo se permiten A, B, C, 1, 2, y 3, y sin repeticiones."

    return "La cadena es válida."

# Funcion que comprueba la contraseña ingresada

def comprobar_psw(psw_in, psw):

    for x, y in zip(psw_in, psw):

        if x == y:
            print(f'\n{x}: Correcto')
        elif x in psw:
            print(f'\n{x}: Presente')
        else:
            print(f'\n{x}: Incorrecto')

# Generar una cadena aleatoria de 4 caracteres

psw = ''.join(random.sample('ABC123', k=4))

# Inicio de juego

print('''
    \n¡Bienvenido Papá Noel, es hora de repartir regalos!
    \nPara abrir al almacén de juguetes digita la clave de ingreso
(tienes 10 intentos).
    \nPista: La clave son 4 dígitos alfanuméricos con letras de la A la C
y números del 1 al 3, en mayúsculas y sin repeticiones.
    ''')

# Inicio de bucle

intento = 0

while intento < 10:

    intento += 1
    print(f'\nIntento n.° {intento}:')

    psw_in = input('\nIngresa contraseña: ')
    resultado = validar_cadena(psw_in)

    if resultado == "La cadena es válida.":
        pass
    else:
        print(resultado)
        continue

    if psw_in == psw:
        print('''
        \n La contraseña es correcta.
        \n¡Felicidades, a repartir juguetes!
        ''')
        sys.exit()
    else:
        print(f'''
        \nLa contraseña es incorrecta. Pero descuida, te doy unas pistas:
        ''')
        comprobar_psw(psw_in, psw)

print('''
        \n¡Oh, no. Papá Noel has olvidado la contraseña!
Ya no te quedan más intentos.
      ''')

