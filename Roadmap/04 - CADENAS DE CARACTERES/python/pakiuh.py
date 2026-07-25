'''
   EJERCICIO:
   Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
   en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
   - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
     conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
'''



#Acceso a caracteres específicos
cadena1 = "Gandalf fue el que manejó el destino de Frodo y de los hobits sin saberlo."
buscamos_o = cadena1.find("o")
cuantas_o = cadena1.count("o")
print(f'el texto "{cadena1}" tiene un total de caracter "o": {cuantas_o} veces y la primera "o" está en la posición {buscamos_o}. de un texto que tiene un total de {len(cadena1)} caracteres')
cadena2 =  'Y Aragorn también fue guiado opr Gandalf'
print(cadena1 + " " + cadena2) #concatencación

#subcadena
subcadena1 = cadena1[0:7]
print(subcadena1)

#repetición
repetir_gandalf = subcadena1 * 5
print(repetir_gandalf)

for letra in subcadena1: #recorrido
    print(letra)

cadena1_mayusculas = cadena1.upper() #mayusculas
print(cadena1_mayusculas)

cadena1_minusculas = cadena1.lower() #minusculas
print(cadena1_minusculas)

cadena1_reemplazada = cadena1.replace("Gandalf", "Saruman")
print(cadena1_reemplazada)

cadena1_primera_parte = cadena1[0:int(len(cadena1)/2)]
cadena2_segunda_parte = cadena1[int((len(cadena1)/2)):len(cadena1)]
print(cadena1_primera_parte)
print(cadena2_segunda_parte)

#interpolacion
for letra in "Gandalf":
    print(f"*{letra}",end='')
print("*")

'''
   DIFICULTAD EXTRA (opcional):
   Crea un programa que analice dos palabras diferentes y realice comprobaciones
   para descubrir si son:
   - Palíndromos #Una palabra o frase que se lee igual hacia adelante que hacia atrás.
   - Anagramas #Dos palabras o frases que tienen las mismas letras en distinta posición.
   - Isogramas #Una palabra o frase donde no se repite ninguna letra.
'''
def palindromo(palabra):#Una palabra o frase que se lee igual hacia adelante que hacia atrás.
    palabra_reversed =""
    for letra in reversed(palabra):
        palabra_reversed = palabra_reversed+letra
    if palabra_reversed == palabra:
        print(f"La palabra {palabra} es un palíndromo")
    else:
        print(f"La palabra {palabra} no es un palíndromo porque al revés es {palabra_reversed}")
palindromo("Pitufina")

def anagrama(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        print(f"Las 2 palabras {palabra1} y {palabra2} son palindromos")
    else:
        print(f"L2as 2 palabras {palabra1} y {palabra2} NO son palindromos")

anagrama("roma", "amor")

def isogramas(frase1):#Una palabra o frase donde no se repite ninguna letra.
    set_frase1 = set(frase1)
    if len(frase1) == len(set_frase1):
        print(f"La frase'{frase1}' es un isograma")
    else:
        print(f"La frase '{frase1}' NO es un isograma")

isogramas("centavo")