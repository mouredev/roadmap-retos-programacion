
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas

#Operaciones

s1 = "hola"
s2 = "PYTHON"

print(s1 + " " + s2)


#replicacion
print(s1 * 3)

#indexacion
print(s1[0]+s2[4]+s1[2]+s1[3])

#longitud
print("longitud cadena Python: " + str(len(s2)))

#slicing

print("slicing [2:5]= " + s2[2:5])
print("slicing [2:]: " + s2[2:])
print("slicing [0:2]: " + s2[0:2])
print("slicing [:2]: " + s2[:2])

#busqueda

print("a" in s1)
print("ho" in s1)
print("y" in s1)

#remplazo
print(s1.replace("o", "a"))

#division
print(s2.split("t"))
s3 = "pythonthon"
print(s3.split("t"))

#Mayusculas y minusculas
print(s1.upper())
print(s2.lower())
print("lio 7 master".title())
print("lio 7 master".capitalize())

#eliminacion de espacios al principio y fin

print(" leo limon ".strip() + "@dominio.com")

#busqueda al principio y al final
print(s1.startswith("py"))
print(s1.startswith("ho"))
print(s1.endswith("la"))
print(s1.endswith("hon"))

#busqueda de posición

print("Leonardo Limon @lio7master".find("li"))
print("Leonardo Limon @lio7master".find("lim"))
print("Leonardo Limon @lio7master".find("Lim"))
print("Leonardo Limon @lio7master".find("L"))
print("Leonardo Limon @lio7master".find("l"))

#busqueda de ocurrencia
print(s3.lower().count("h"))

#formato
print("Saludos: {}, lenguaje: {}".format(s1, s2))

#interpolacion
print(f"Saludos: {s1}, lenguaje: {s2}")

#Transformacion de lista de caracteres

print(list(s3))

#trsnformacion de lista en cadena

l1 = [s1, "", "", s2, "!"]

print(" ".join(l1))

#transformacion numerica
s4 = "1234567"
s4 = int(s4)
print(s4)


s5 = "1234567.89"
s5 = float (s5)
print(s5)

#comprobacion varias
s4 = "1234567"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


#EXTRA


def check(word1: str, word2: str):

    #palindromos -> Palabras/fraces que se leen igual de derecha a izquierda como izquierda a derecha.
    print(word1)
    print(word2[::-1]) #Esta sentencia invierte la posicion del strinf pero se pueden usar otras funciones

    print(f"{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palindromo?: {word2 == word2[::-1]}")

    #anagrama -> es una  palabra que resulta de reordenar todas las letras de otra palabra
    print(f"{word1} es un anagrama de {word2}?: {sorted(word1)== sorted(word2)}")

    #heterograma -> es una palabra o frase que no contiene ninguna letra repetida.
    #isograma -> en una palabra aparecen el mismo numero de veces cada letra, o en una frase cada palabra palabra.
    print(len(word1)) #la longitud total de la palabra 
    print(len(set(word1)))#el set por su concepto mismo no permite el guardar valores duplicados, por lo que nos permite contar las letras diferentes para este caso
    print(f"¿La palabra {word1} es un isograma? {len(word1)==len(set(word1))}")
    print(f"¿La palabra {word2} es un isograma? {len(word2)==len(set(word2))}")

    def isograma(word: str) -> bool:
        word_dict = dict()
        for charater in word:
            word_dict[charater] = word_dict .get(charater, 0) + 1

        isograma = True
        values =  list(word_dict.values())
        isograma_len = values[0]
        for word_count in word_dict.keys():
            if len(word_count) != isograma_len:
                isograma = False
                break
        return isograma
   
    print(f"¿La palabra {word1} es un isograma? (fun) {isograma(word1)}")
    print(f"¿La palabra {word2} es un isograma?(fun){isograma(word2)}")

check("radar", "python")
check("amor", "roma")
check("radar", "python")
