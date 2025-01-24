"""
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 *
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 """
import random


def generar_clave():
    """
    Se genera la clave que debe descubrir el usuario, y solo tiene 4 caracteres
    """

    letras = ["A", "B", "C"]
    numeros = [1, 2, 3]
    union = letras + numeros

    return random.sample(union, k=4)


def validar_clave(clave, ingreso):
    """
    Evalua caracter por caracter para saber su estado si es correcto, presente o incorrecto
    """
    valida_caracter = []

    def evaluar(valor):

        if valor in clave and (ingreso.index(str(valor)) == clave.index(valor)):
            valida_caracter.append('Correcto')
        elif valor in clave:
            valida_caracter.append('Presente')
        else:
            valida_caracter.append('Incorrecto')

    for valor in ingreso:

        if valor.isdigit():
            numero = int(valor)
            evaluar(numero)
        else:
            evaluar(valor)

    return valida_caracter


def main():
    """
    Se le solicita al usuario ingresar una contraseña para realizar su validación
    """
    clave = generar_clave()
    i = 0

    mensaje = '''\n\tDebes ayudar al viejo pascuero; se le olvidó la contraseña del almacén.
        Tienes que descubrir la contraseña, la cual \033[1;37;47mestá compuesta por letras de la A a la C \033[0;m 
        \033[1;37;47my por números del 1 al 3.\033[0;m Tiene una longitud de 4 caracteres.
        A continuación, se solicitará que ingreses la clave, tienes solo 10 intentos.
        '''
    print(mensaje)

    while i < 10:
        i += 1
        print(f'\n\tIntento {i} |{"»"*40}')
        clave_ingresada = input(
            '\n\t• Ingresa la clave(de 4 Caracteres):').upper()

        if len(clave_ingresada) > 5:
            print(
                '\n\nError, desperdiciaste una oportunidad, recuerda ingresa solo 4 Caracteres\n')
        else:

            validacion = validar_clave(clave, clave_ingresada)

            print(f'\n\t{validacion}\n')

            if i == 10 and (validacion.count("Correcto") != 4):
                print(
                    '\n\tLamentablemente, finalizaron los intentos para descubrir la contraseña del almacén')
                print(
                    '\n\tPor lo tanto, el viejo pascuero no puede entregar los regalos.')

            elif validacion.count("Correcto") == 4:
                print(
                    '\n\t¡Felicitaciones! Lograste adivinar la clave, pueden abrir el almacén\n')
                break


if __name__ == '__main__':
    main()
