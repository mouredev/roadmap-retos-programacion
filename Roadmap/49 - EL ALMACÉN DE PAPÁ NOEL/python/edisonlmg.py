#============================
# 49 El almacen de Papá Noel
#============================

import random
import sys

# Funcion que comprueba errores

def errores(psw_in):



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

    while True:

        psw_in = input('\nIngresa contraseña: ')

        if errores(psw_in):

            print('''
            \nLos caracteres ingresados no son correctos.
            \nInténtalo de nuevo...
            ''')

    if psw_in == psw:

        print('''
        \n La contraseña es correcta.
        \n¡Felicidades, a repartir juguetes!
        ''')

        exit()

    else:

        print(f'''
        \nLa contraseña es incorrecta. Pero descuida, te doy unas pistas:
        \n{comprobar_psw(psw_in, psw)}
        ''')

print('''
        \n¡Oh, no. Papá Noel has olvidado la contraseña!
Ya no te quedan más intentos.
      ''')

