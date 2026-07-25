#=======================================================================================================================
# 49 El almacen de Papá Noel
#=======================================================================================================================

# Importar librerias
import random
import re

# Expresion regular para password
pattern = r'^(?!.*(.).*\1)[ABC123]{4}$'

# Generar password aleatorio
psw = ''.join(random.sample('ABC123', k=4))

# Inicio de juego
print('''
    \n¡Bienvenido Papá Noel, es hora de repartir regalos!
    \nPara abrir al almacén de juguetes digita la clave de ingreso
(tienes 10 intentos).
    \nPista: La contraseña debe contener 4 caracteres sin repeticiones y solo acepta
los valores A,B,C,1,2 y 3.
    ''')

# Inicio de bucle

intento = 0

while intento <= 10:

    # Iniciar contador
    intento += 1

    # Si se excedio de 10 intentos terminar el juego
    if intento > 10:
        print('''
            \n¡Oh, no. Papá Noel has olvidado la contraseña!
    Ya no te quedan más intentos.
          ''')
        break

    # Solicitar el ingreso de un password
    print(f'\nIntento n.° {intento}:')
    psw_in = input('\nIngresa contraseña: ').upper()

    # Comprobar si el passwor ingresado es valido
    if bool(re.match(pattern, psw_in)):
        pass
    else:
        print('''
        \nLa contarseña ingresada no es válida. La contraseña debe contener 4
caracteres sin repeticiones y solo acepta los valores A,B,C,1,2 y 3.
        ''')
        continue

    # Si el password fue valido comprobar si es el correcto
    if psw_in == psw:
        print('''
        \n La contraseña es correcta.
        \n¡Felicidades, a repartir juguetes!
        ''')
        break
    else: # Si el password es incorrecto dar las pistas por cada caracter
        print(f'''
        \nLa contraseña es incorrecta. Pero descuida, te doy unas pistas:
        ''')
        for x, y in zip(psw_in, psw):
            if x == y:
                print(f'\n{x}: Correcto')
            elif x in psw:
                print(f'\n{x}: Presente')
            else:
                print(f'\n{x}: Incorrecto')
        print('\n¡Vuelve a intentarlo, Papá Noel!')