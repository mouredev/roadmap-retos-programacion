

#  EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */




   # aplicacion de " + " y print

# saludos= "Hola"
# nombre="pedrito por acá"
# saludo_completo=saludos + "," + nombre 
# print(saludo_completo)  #Hola,pedrito por acá


#    # uso de " * "

# repetir= saludos*4
# print(repetir)  #HolaHolaHolaHola


#    # imprimir un carcter  específico 
# palabra= "carpintero"
# eliminar_caracter=palabra[4]
# print(eliminar_caracter)   #limina el caracter de la posicion 4 >>> "i"


#    #subcadena
# texto="programacion"
# limitado=texto[0:6]
# print(limitado)    #imprime "progra"


#    #numero de caracteres
# palabron="contadores publicos"
# contador=len(palabron)
# print(contador)   #imprime el numero de caracteres >> 19


#    #immrpimir mayusculas "upper"o minusculas "lower" 
# saludito = "Saludos Totales en Proceo"
# mayusculas = saludito.upper()
# minusculas = saludito.lower()
# print(mayusculas)  # Salida: SALUDOS TOTALES EN PROCEO
# print(minusculas)  # Salida: saludos totales en proceo


#     #reemplazar " texto en cadena"  .replace( " a "  " b "  " c ")
# escrito = "aqui vamos, en proceso continuo"
# nuevo_ = escrito.replace("aqui", "desde" "cero" "de" "nuevo")
# print(nuevo_)  
# print(escrito)  # Salida: aqui vamos, en proceso continuo


    # encontrar " posicion " (numero de carcateres antes de la palabra) de una plabra en una cadena de texo con .find("  ")
# cadena1= "aqui vamos, en proceso continuo"
# posicion = cadena1.find("proceso")
# print(posicion)  # Salida: 15 (son los caracteres antes de inciciar "proceso")


# #  dividir una cadena en subcadena (lista con elementos separados por ,)
# cadena2 = "aqui vamos, en proceso continuo, por ahora"
# subcadena = cadena2.split(", ")
# print(subcadena)  # Salida:['aqui vamos', 'en proceso continuo', 'por ahora']


      #Quitar espacios en blanco al inicio y al final de la cadena con .strip()
# cadena3 = "   aqui vamos, en proceso continuo, por ahora   "
# subcad = cadena3.strip()
# print(subcad)  # imprime:aqui vamos, en proceso continuo, por ahora





