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

#-------------------------------------------------
#-------------- OPERACIONES BASICAS --------------
#-------------------------------------------------


#CONCATENAZIÓN ---> Unir 2 cadenas de diferentes variables
string_1 = "La hora es "
string_2 = "21:30"
concatenacion = string_1 + string_2
print(concatenacion)

#INDEXACIÓN ---> Acceder a un caracter especifico de una cadena por medio de su indice
string_3 = "Programacion"
caracter = string_3[5]
print(caracter)




#-------------------------------------------------
#-------------- METODOS CON CADENAS --------------
#-------------------------------------------------


#------ CAPITALIZE ---> Transforma la primera letra de una cadena en mayuscula
cadena_1 = "hola"
c1 = cadena_1.capitalize()
print(c1)

#------ CASEFOLD ---> Convierte una cadena a minusculas
cadena_2 = "HaY MuchAs MayusCuLas"
c2 = cadena_2.casefold()
print(c2)

#------ COUNT ---> Cuenta la cantidad de veces que se repite un elemento de las string
cadena_3 = "pelar manzanas, cocer manzanas, servir manzanas"
c3 = cadena_3.count("manzanas")
print(c3)

#------ FIND ---> Devuelve la cantidad de elementos que coincidan con un caracter a indicar
cadena_4 = "Bienvenido"
c4 = cadena_4.find("i")
print(c4)

#------ JOIN ---> Une todos los elementos de un grupo de elementos con un caracter de conexión
lista_1 = ["Esta", "es", "una", "cadena", "de", "una", "lista"]
c5 = " ".join(lista_1)
print(c5)

#------ PARTITION ---> Divide una cadena en 3 partes y devuelve una tupla
cadena_5 = "las cadenas pueden dividirse con el método partition"
c6 = cadena_5.partition("dividirse")
print(c6)

#------ RSTRIP ---> Nos permite eliminar los espacios vacios al final de una cadena
cadena_6 = "nombre        "
c7 = cadena_6.rstrip()
print("Mi", c7, "es Ignacio")


#------ SPLIT ---> Divide una cadena en sus diferentes palabras y las guarda en una lista
cadena_7 = "las cadenas pueden dividirse usando split"
c8 = cadena_7.split()
print(c8)

#------ RSPLIT ---> Crea una lista a partir de una cadena usando un separador especial
cadena_8 = "Mercedez Benz, Audi, Porsche, BMW, Volkswagen"
c9 = cadena_8.rsplit(", ")
print(c9)
print(c9[3])

#------ TITLE ---> Convierte el primer caracter de cada palabra de una string en mayusculas
cadena_9 = "diego, pablo, felipe, jose, maria, miguel"
c10 = cadena_9.title()
print(c10)

#------ SWAPCASE ---> Convierte mayusculas en minusculas y viceversa
cadena_10 = "Las Jerarquia Se Invierte"
c11 = cadena_10.swapcase()
print(c11)


#------ UPPER ---> Convierte todas las letras a myusculas
cadena_11 = "estoy gritando"
c12 = cadena_11.upper()
print(c12)

#------ REPLACE ---> Reemplaza todos los caracteres que conicidan con uno definido 
cadena_12 = "coincidencia"
c13 = cadena_12.replace("i", "a")
print(c13)


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''


#PALINDROMO: Palabra o frase cuyas letras están dispuestas de tal manera que resulta la misma leída de izquierda a derecha que de derecha a izquierda

cadena_original = input("Palindromo ?: ")
lista_letras = []
lista_2 = [] #Para obtener la cadena original sin espacios
counter = 0

cadena_Reversa = ""
cadena_notReversa = ""
cadena_aux = ""

#Transformar la cadena a lista
for l in cadena_original:
    #print(l)
    lista_letras.append(l)

#Quitar espacios a la cadena original e invertirla
for c in range(0, len(lista_letras)):
    cadena_aux = lista_letras[c]
    if cadena_aux == " ":
        continue
    elif cadena_aux != " ":
        cadena_Reversa = cadena_aux + cadena_Reversa

#Reconstruir la cadena original a partir de la cadena invertida sin espacios
for f in cadena_Reversa:
    lista_2.append(f)
    cadena_notReversa = lista_2[counter] + cadena_notReversa
    counter += 1

print(lista_2) #Lista
print(cadena_notReversa) #Cadena reconstruida sin espacios


print("Cadena Original: " + cadena_notReversa)
print("Cadena Reversa: " + cadena_Reversa)

if cadena_notReversa == cadena_Reversa:
    print("La cadena es un palindromo")
else:
    print("La cadena no es un palindromo")


#ANAGRAMA:

string_org_An = input("Cadena Original: ")
string_comp = input("Anagrama?: ")
counter = 0
charCounter = 0
list_strOrg = []
list_comp = []

for i in string_org_An:
    char1 = i.lower()
    list_strOrg.append(char1)

for h in string_comp:
    char2 = h.lower()
    list_comp.append(char2)

len_cadOrg = len(list_strOrg)
len_cadCom = len(list_comp)

if len_cadOrg == len_cadCom:
    print (len_cadOrg , "=", len_cadCom ) #Evaluamos si el largo de caracteres coincide
    for c in list_strOrg:
        charCounter = 0 #Char counter se actualiza aquí por cada vez que ingresa una nueva letra para ser coparada con las de la segunda cadena
        for d in list_comp:
            if (c == d):
                charCounter+=1
                counter+=1
                if charCounter == 2:
                    counter -= 1
                else:
                    print(c, " is in ", string_comp)
            else:
                continue

    if counter == len_cadOrg:
        print("Strings are anagramas")
    else:
        print("String are not anagramas")
        print(counter, " = ", len_cadOrg)
else:
    print("la cadena no es un anagrama") 


#ISOGRAMA: Palabra o frase donde cada letra aparece el mismo número de veces

isograma = input("Isograma: ")
isogramaToLower = isograma.lower()
lista_iso = []
letra = 0
contador = 0
caracterIsograma = {}

print(isogramaToLower)

for c in isogramaToLower:
    lista_iso.append(c)

for i in lista_iso:
    caracterIsograma[i] = 1
    # letra = i
    # lista_iso.remove(i)
    # for l in lista_iso:
    #     if letra == l:
    #         contador += 1
    #     else:
    #         continue
    # print(f"{letra}, {contador}")

    #caracterIsograma[i] = 1

print(caracterIsograma)

