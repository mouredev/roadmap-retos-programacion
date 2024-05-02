"""
/*
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
 * - Anagramas
 * - Isogramas
 */"""
 
def anagrama():
    tx1 = input("Ingrese la primera palabra: ").lower()
    txt2 = input("Ingrese la segunda palabra: ").lower()

    if len(sorted(tx1)) == len(sorted(txt2)):
        return f"La palabra {tx1}y la palabra {txt2}:\nSon un anagrama."
    else:
        return f"La palabra {tx1} y la palabra {txt2}:\nNo son anagrama."
    
print(anagrama())