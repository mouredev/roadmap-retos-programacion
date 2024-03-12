# #04 CADENAS DE CARACTERES
## Ejercicio

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
 */
 '''
 
 #CADENAS DE CARACTERES
cadena = "Hola Mundo"

#Funciones de cadena
print(cadena[0]) #H
print(cadena[1:4]) #ola
print(len(cadena)) #10
print(cadena + " " + "Cruel") #Hola Mundo Cruel
print(cadena * 3) #Hola MundoHola MundoHola Mundo
print(cadena.lower()) #hola mundo
print(cadena.upper()) #HOLA MUNDO
print(cadena.replace("Hola", "Adios")) #Adios Mundo
print(cadena.split(" ")) #['Hola', 'Mundo'] 
print(" ".join(cadena)) #H o l a   M u n d o
print(cadena.find("Mundo")) #5
print(cadena.count("o")) #2

#Programa que analiza dos palabras diferentes y realice comprobaciones
def menu():
    print("Introduce la primera palabra:")
    palabra1 = input()
    print("Introduce la segunda palabra:")
    palabra2 = input()
    return palabra1, palabra2

#Funcion Palindromo que significa que se lee igual de izquierda a derecha que de derecha a izquierda
def palindromo(palabra1, palabra2):
    if palabra1 == palabra1[::-1]: #[::-1] invierte la cadena y comprueba si es palindromo
        print("La palabra", palabra1, "es un palindromo") 
    else:
        print("La palabra", palabra1, "no es un palindromo")
    if palabra2 == palabra2[::-1]:
        print("La palabra", palabra2, "es un palindromo")
    else:
        print("La palabra", palabra2, "no es un palindromo")
        
#Funcion Anagrama que significa que las letras de una palabra se pueden reordenar para formar otra palabra
def anagrama(palabra1, palabra2): 
    if sorted(palabra1) == sorted(palabra2):#sorted ordena la cadena y comprueba si es un anagrama
        print("La palabra", palabra1, "es un anagrama de", palabra2)
    else:
        print("La palabra", palabra1, "no es un anagrama de", palabra2)

#Funcion Isograma que significa que no tiene letras repetidas
def isograma(palabra1, palabra2):
    if len(palabra1) == len(set(palabra1)) and len(palabra2) == len(set(palabra2)):#set elimina los elementos duplicados
        print("La palabra", palabra1, "es un isograma")
    else:
        print("La palabra", palabra1, "no es un isograma")
    if len(palabra2) == len(set(palabra2)):
        print("La palabra", palabra2, "es un isograma")
    else:
        print("La palabra", palabra2, "no es un isograma")

def main():
    palabra1, palabra2 = menu()
    palindromo(palabra1, palabra2)
    anagrama(palabra1, palabra2)
    isograma(palabra1, palabra2)
    
main()#Llamada a la funcion main  
    
     
 