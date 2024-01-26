'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
'''

# el clásico string:
hola = "Hola Mundo!"
print(hola)

# subcadena, acceso a caracteres específicos
subcadena = hola[0:4]
print(subcadena)

# longitud de la cadena
print(f"La cadena {hola} tiene {len(hola)} caracteres")

# concatenación
test_concatenar = "Hola" + " " + "Mundo!" + "(concatenado)"
print(test_concatenar)


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''