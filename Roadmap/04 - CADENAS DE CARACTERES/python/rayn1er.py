# /*
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
#  *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
#  *   interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */

string = 'Hola'
string_2 = 'Mundo'

print(string + ' ' + string_2) # Podemos utilizar el operador + para concatenar 2 o mas cadenas de texto
print(string * 3) # podemos utilizar * para multiplicar la cadena de texto
string_2 += ' de Python' # += para agregar texto
print(string_2)
string_3 = string + string_2
print(len(string_3)) # len para calcular obtener el numero de caracteres
print(string_3.find("Mundo")) #find para encontrar el indice de inicio de la subcadena
print(string.find("naruto")) # find devolvera -1 si no se encuentra la subcadena
print(string_3.lower()) # lower para convertir todas las letras a minusculas
print(string_3.upper()) #upper para convertir todas las letras a mayusculas
print(string_3.replace('Python','Java')) # replace para reemplazar un valor por otro
print(string_3[2:6]) # se puede crear subcadena utilizando corchetes con los indices desde el comienzo hasta el final
string_4 = 'Hola con \"Secuencia de escape"' # permite representar caracteres no imprimibles
print(string_4)
string_5 = 'Hola\t mundo' #se puede usar \t para una tabulacion
print(string_5)
string_6 = "Hola\nmundo" # y \n para un salto de linea
print(string_6)
print(string_6.startswith('H')) #Para saber si empieza con una letra 
print(string_6.endswith("O")) # para saber si termina con una letra

#Ejercicio

def palindromo(string: str): 
    
    if string == string[::-1]: 
        return f'{string} es palindromo'
    else:
        return f'{string} No es palindromo'

print(palindromo("alomomola"))
print(palindromo("ratatta"))

def anagrama(string: str, string2 : str):
    
    if sorted(string) == sorted(string2):
        return f'{string} es anagrama de {string2}'
    else:
        return f'{string} no es anagrama de {string2}'

print(anagrama("japones", 'esponja'))
print(anagrama("amada", 'mirada'))

def isograma(string):
    check = {}
    isograma = True
    for i in string:
        check[i] = string.count(i)

    max_value = max(check.values())
    
    for i in check.values():
        if i != max_value:
            isograma = False
   
    
    if isograma:
        return f"{string} es un isograma"
    else:
        return f"{string} no es un isograma"

    return max_value
    
    
print(isograma("pythonpythonpython"))