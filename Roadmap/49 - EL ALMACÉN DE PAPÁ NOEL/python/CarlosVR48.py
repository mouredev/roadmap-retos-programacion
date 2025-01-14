"""EJERCICIO:
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

clave_original = list()
clave_bak = list()
clave_Acertar = list()
contador = 10
salir = True

# Creamos la contraseña principal la longitus es de cuatro variables 
# 3 letras y 3 numeros . En total son seis digitos  

while len(clave_bak) <= 3:
    caracter = random.randint (1 , 6)
    
    if clave_bak.count(caracter) == 0:
        clave_bak.append(caracter)
    
for index in clave_bak:
    if index == 1:
        clave_original.append("A")
    elif index == 2:
        clave_original.append("B")
    elif index == 3:
        clave_original.append("C")
    elif index == 4:
        clave_original.append("1") 
    elif index == 5:
        clave_original.append("2") 
    elif index == 6:
        clave_original.append("3")            

# Funcion que coje cada valor de la clave_bak y los compara con cada valor
# de la clave_original.Dandoles el valor correspondiente.

def comparar():
    clave_Acertar.clear()

    for index in range(0,4):
        if clave_bak[index] == clave_original[index]:
            clave_Acertar.append("CORRECTO")
        else:
            if clave_original.count(clave_bak[index]) > 0:
                clave_Acertar.append("PRESENTE")
            else:
                clave_Acertar.append("INCORRECTO")

# Funcion para pedir los digitos por consola enmarcados en los valores dados
def valor(posicion):
    while True:
        numero = input (f"DIME EL DIGITO {posicion} ? ").upper()
        if numero == "A" or numero == "B" or numero == "C" or numero == "1" or numero == "2" or numero == "3":
            return numero
        else:
            print ("\nVALOR INCORRECTO\n")

while contador > 0 and clave_Acertar.count("CORRECTO") < 4:
    print ("\nLA CLAVE ES DE CUATRO DIGITOS LOS CUALES PUEDEN SER A , B , C , 1 , 2 Y 3 . SIN REPETIR\n")
    print (f"NUMERO DE POSIBILIDADES: {contador}\n")
    
    while salir:
        digito_uno = valor(1)
        digito_dos = valor(2)
        digito_tres = valor(3)
        digito_cuatro = valor(4)
        
        clave_bak.clear()
        clave_bak.append(digito_uno)
        clave_bak.append(digito_dos)
        clave_bak.append(digito_tres)
        clave_bak.append(digito_cuatro)
        
        if clave_bak.count("A") < 2 and clave_bak.count("B") < 2 and clave_bak.count("C") < 2 and clave_bak.count("1") < 2 and clave_bak.count("2") < 2 and clave_bak.count("3") < 2:
            salir = False
        else :
            print ("\nHAY DIGITOS REPETIDOS\n")

    comparar()
    contador = contador - 1
    print (f"\n{clave_Acertar}\n")
    salir = True

if contador == 0 and clave_Acertar.count("CORRECTO") < 4:
    print ("NO TIENES ACCESO !!!!")
else:
    print ("BIEN TIENES ACCESO !!!!")            