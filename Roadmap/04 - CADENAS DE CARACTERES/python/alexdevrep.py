'''
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
 */
'''

# Creamos una cadena de caracteres (String)

mi_string = "Soy una cadena de caracteres"
print(mi_string)

# Operaciones con cadenas de caracteres 

# Acceso a caracteres
print(mi_string[5])

#Creación de subcadenas
print(mi_string[0:15])

# Longitud de una cadena de caracteres y interpolación de caracteres
print(f'Mi cadena tiene {len(mi_string)} caracteres')

# Concatenación de una cadena de caracteres
mi_string3 = mi_string + " " + "y estoy descubriendo que puedo hacer en python!"
print(mi_string3)

#Repetición de la cadena de caracteres
mi_string4 = "Hola python!  " * 3
print(mi_string4)

# Conversión de la cadena a mayúsculas
mi_string1 = mi_string.upper()
print(mi_string1)

# Conversión de la cadena a minúsculas
mi_string2 = mi_string.lower()
print(mi_string2)

#Repetición de la cadena de caracteres
mi_string4 = "Hola python!  " * 3
print(mi_string4)

#División de una cadena de caracteres
mi_string5 = mi_string3.split('estoy')
print(mi_string5)

#Reemplazo de caracteres
mi_string = mi_string.replace('c', 'k')
print(mi_string)

#Recorriendo una cadena de caracteres
num = 0
while num < len(mi_string):
    print (mi_string[num])
    num =num + 1

#Unión de cadenas 
cadena= ("soy","una","cadena","de","caracteres")
mi_string = "/".join(cadena)
print(mi_string)

#Verficacion de un elemento en una cadena de caracteres

mi_string = "soy una cadena de caracteres"
print(mi_string.isdecimal())
print(mi_string.isdigit())
print(mi_string.isalnum())
print(mi_string.isalpha())
print(mi_string.isascii())
print(mi_string.isidentifier())
print(mi_string.islower())
print(mi_string.isnumeric())


#Dificultad extra
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''
palabra4 = input("Introduce la primera palabra a al sistema: ")
palabra5 = input("Introduce la segunda palabra al sistema: ")
palabra4invertida = palabra4[::-1].lower
palabra5invertida = palabra5[::-1].lower
def palindromo(palabra4invertida , palabra5invertida): # Un palíndromo es una palabra que puede leerse de la misma forma de izquierda a derecha que de derecha a izquierda
       
       if palabra4invertida == palabra4:
         print(f'La palabra {palabra4} es un palíndromo')
       else :
         print (f'La palabra {palabra4} no es un palíndromo')

       if palabra5invertida == palabra5:
         print(f'La palabra {palabra5} es un palíndromo')
       else :
         print (f'La palabra {palabra5} no es un palíndromo')
        

def Anagrama(palabra4,palabra5): #Es una palabra que si se ordena de otra manera da lugar a otra palabra distinta roma//amor 

    if sorted(palabra4) == sorted(palabra5):
         print ("Estas palabras son un anagrama")
    else :
         print ("Estas palabras no son un anagrama")


def Isograma (palabra4,palabra5): # Un isograma es una palabra que no tiene letras repetidas
   
   if len(set(palabra4)) == len(palabra4):
        print ("Esta palabra es un isograma")
   else:
    print("Esta palabra no es un isograma")

   if len(set(palabra5)) == len(palabra5):
        print ("Esta palabra es un isograma")
   else:
        print("Esta palabra no es un isograma")
   

palindromo(palabra4invertida,palabra5invertida)
Anagrama(palabra4,palabra5)
Isograma(palabra4,palabra5)
