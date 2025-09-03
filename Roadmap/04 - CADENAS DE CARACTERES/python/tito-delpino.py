#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

cadena = 'Esto es una cadena'
cadena2 = ' Esto es otra cadena '

caracter = cadena[10] # accedemos al caracter en indice 10
print(caracter)
subcadena = cadena[5:15] # accede a una subcadena entre los indices indicados
print(subcadena)
longitud = len(cadena) # damos valor a la variable con la longitud de cadena
print(longitud)
concatenacion = cadena + ' ' + cadena2 # concatenamos cadenas
print(concatenacion)
mayus = cadena.upper() # converion a mayusculas
print(mayus)
minus = cadena.lower() # conversion a minusculas
print(minus)
primera_mayus = cadena.title() # primera letra de cada palabra en mayus
print(primera_mayus)
solo_inicio_mayus = cadena.capitalize() # solo primera letra del string en mayus
print(solo_inicio_mayus)
print(cadena * 3) # repeticion
print('a' in cadena) # a existe en cadena, printeara True
remplazo = cadena.replace('a', 'e') # remplazamos las 'a' por 'e' dentro de la cadena
print(remplazo)
division = cadena.split('t') # corta en elementos en el valor indicado,crea lista con las partes
print(division)
eliminacion_espacios = cadena2.strip() # elimina los espacios al inicio y fin de la cadena
print(eliminacion_espacios)
cantidad = cadena.count('a') # cuenta las veces que esta lo indicado en el string
print(cantidad)
formateo = 'String1:{}, string2:{}'.format(cadena, cadena2) # da formato al la salida
print(formateo)
interpolacion = f'String1:{cadena}, string2:{cadena2}' # da formato al la salida interpolando tipos de datos
print(interpolacion)
lista = [cadena, ',', cadena2, '!']
print(" ".join(lista)) # unifica en un mismo string los varoles de una lista separados por el valor indicado

cadena = 'sdfsdf'
print(cadena.isalpha()) # cheque si el string es alfanumerico
print(cadena.isalnum()) # chequea si el strin es numerico


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas

word1 = 'Sierra'
word2 = 'Nevada'
