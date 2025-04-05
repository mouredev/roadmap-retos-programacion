"""/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
    *Palabra o frase cuyas letras están dispuestas de tal manera 
    que resulta la misma leída de izquierda a derecha que de derecha a izquierda
 * - Anagramas
    * - Un Anagrama consiste en formar una palabra reordenando TODAS
    *   las letras de otra palabra inicial.
    * - NO hace falta comprobar que ambas palabras existan.
    * - Dos palabras exactamente iguales no son anagrama.
 * - Isogramas
    *palabra o frase en la que cada letra aparece el mismo número de veces.
    *el orden indica el numero de veces
 */"""

def anagrama (var_1, var_2):
    if var_1.lower() == var_2.lower():
        #print ("las palabras son iguales")
        return False
    return sorted(var_1.lower()) == sorted (var_2.lower())

def isograma (var_1):
    contador={}
    for char in var_1:
        if char in contador.keys():
            contador[char] +=1
        else:
            contador[char] =1
    print (contador)
    orden=0
    for i in contador.values():
        if orden == 0:
            orden = i
        if orden != i:
            return print (f"{var_1} NO es una palabra isograma\n")
    return print (f"{var_1} es una palabra isograma de orden {orden}\n")
            


print ("\nlas palabras son anagramas?")
print (anagrama("Caso", "saco"))

print ("\nes una palabra isograma?")
isograma("Casoo")
isograma("saco")