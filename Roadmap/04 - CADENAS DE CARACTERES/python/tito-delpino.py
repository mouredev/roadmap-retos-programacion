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


def check_palabras(palabra1, palabra2):
    # Palindromo
    print(f'La palabra "{palabra1}" es palindromo? {palabra1 == palabra1[::-1]}')
    print(f'La palabra "{palabra2}" es palindromo? {palabra2 == palabra2[::-1]}')
    
    # Anagramas
    print(f'"{palabra1}" es anagrama de "{palabra2}"? {sorted(palabra1) == sorted(palabra2)}')

    # Isogramas
    def isograma(palabra):
        carac_palabra = dict()
        for carac in palabra:
            # el caracter se agregara al diccionario con valor 0 si no existe o sumara 1 al valor si existe
            carac_palabra[carac] = carac_palabra.get(carac, 0) +1
        isograma = True
        # creamos una lista con los valores obtenidos del diccionario
        valores = list(carac_palabra.values())
        # checkeamos de que tipo es el isograma
        long_isograma = valores[0]
        # Revisamos que todos los caracteres tengan el mismo conteo
        for conteo_carac in valores:
            if conteo_carac != long_isograma:
                # si algun caracter tiene conteo distinto, no es isograma
                isograma = False
                break
        return isograma


    print(f'"{palabra1}" es un isograma? {isograma(palabra1)}')
    print(f'"{palabra2}" es un isograma? {isograma(palabra2)}')




check_palabras('amor', 'ramo')
check_palabras('murcielago', 'reconocer')