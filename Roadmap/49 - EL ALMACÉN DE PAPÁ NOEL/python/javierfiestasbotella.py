'''
/*
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
 */
'''
import random

fabrica=['a','b','c','1','2','3']
def crea_contraseña(l):
    password=''
    while len(password)<4:
        digito=random.choice(l)
        if digito not in password:
            password+=digito
    return password

password_1=crea_contraseña(fabrica)
print(password_1)

intento=0
while intento <10:
    sol=input('Escribe la Contraseña: ')
    if sol==password_1:
        print('Bien Acertaste PapáNoél Ganó')
        break
    else:
        buena = [letra for letra in password_1 if letra != ' ']
        mala = [letra for letra in sol if letra != ' ']
        for i in range(len(password_1)):
            if sol[i]==password_1[i]:
                print(sol[i], 'Correcto')
            elif sol[i] in password_1:
                print(sol[i], 'Presente')
            else:
                print(sol[i], 'Incorrecto')
    intento+=1
if intento==10:
    print('Lo siento no lo conseguiste')