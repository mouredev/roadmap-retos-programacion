'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''

# Acceso a caracteres específicos:
cadena = 'Hola Mundo'
print(cadena[0])

# Subcadenas(Indexación)
print(cadena[:7])

# Longitud
print(len(cadena))

# Concatenación
cadena1 = 'Hola'
cadena2 = 'Mundo'

print(cadena1 + cadena2)
print(cadena1 + ' ' + cadena2 + '!')

# Repetición
print(cadena1 + cadena1 + cadena1)
print(cadena1 * 3)

# Slicing (porción)
print(cadena2[2:5])
print(cadena2[2:]) # Que empiece desde donde quiero hasta el final
print(cadena2[0:2])
print(cadena2[:2])

# Búsqueda
print("H" in cadena1)
print("M" in cadena1)

# Reemplazo
print(cadena1.replace("o", "a"))

# División
print(cadena1.split("l"))

# Mayúsculas y minúsculas
print(cadena1.upper())
print(cadena2.lower())
print('carlos buenrostro'.title())
print('carlos buenrostro'.capitalize())

# Eliminación de espacions al principio y al final
print('carlos buenrostro valverde'.strip() + ' ' + '@carlosbuenrostrovalverde')

# Búsqueda al principio y al final
print(cadena1.startswith('H'))
print(cadena1.startswith('M'))

# Búsqueda de posición
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.find('@'))
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.find('l'))
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.lower().find('v'))

cadena3 = 'Carlos Buenrostro Valverde @cbuenrostrovalverde'

# Búsqueda de ocurrencias
print(cadena3.lower().find('n'))

# Formateo
print('Saludo: {}, Dirigido: {}'.format(cadena1, cadena2) )
print(f'Saludo: {cadena1}, Dirigido: {cadena2}' )