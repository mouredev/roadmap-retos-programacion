#los string en pyhton o cadenas de texto es una estrucutura de terxto mas en la que se guardan caracteres
#por ende esta cadena de texto se puede iterar y se pueden hacer operacion con esta

"""OPERACIONES BASICAS CON STRINGS"""
#concatenacion de cadenas de texto 

text_1 = "hola "
text_2 = "python"

print(text_1+" "+text_2)

#repeticion de cadenas de texto

text_1 = "hola "
text_2 = "python "

print(text_1*3 +" "+text_2*2)

#acceder a caracteres de una cadena por medio de la indexacion 

text = "esto es una cadena de text"

print(text[0])


#slicing en cadenas de texto, al ser un tipo de estructura de dato tambien se puede hacer slicin

text = "python es mejor que java"

print(text[0:17])

#saber la longitud de un string con len()

text = "python"
print(f"python tiene una longitud de {len(text)}")

#verificar si una cadena tiene un caracter n ["n" in "str"]

text = ("a,b,c,d,e,f,h,i,j,k")

print("a" in text)

#comparar si una cadena es igual a otra cadena

print("hola" == "hola")

"""METODOS DE ANALISIS Y BUSQUEDA CON STRINGS"""

# .find(substring) busca el primer conjunto de caracteres en la cadena de texto si no 
# lo encuentra devuelve -1 si lo encuentra devuelve el indice

text = "mi sueño es viajar mucho"

print(text.find("z"))
print(text.find("sueño "))

# .index(substring) busca el indice de donde comienza el str a encontrar pero si no 
# lo encontra lanza error
text = "mi sueño es viajar mucho"

print(text.index("z"))
print(text.index("sueño "))

# .count(substring) return the times of the substring find in the string
text = "sueño sueño sueño hola sueño otra vez sueñoooo"

print(text.count("sueño "))

# .startwhith(substring) compare the substring with the string start

texto =  "pythonn es el mejor"

print(texto.startswith("python"))


"""DIVISION Y UNION DE CADENDAS DE TEXTO"""

# .split("division") retorna una lista con las palabras de la cadena de texto
# palabra = grupo de caracteres sin separador

text = "esto es una cadena de letras , y va a seperar todo esto."

print(text.split("z"))


# .rsplit("division") retorna una lista con palabras de la cadena de texto pero recorre de derecha a izquierda
# palabra = grupo de caracteres sin separador

text = "esto es una cadena de letras , y va a seperar todo esto."

print(text.rsplit(" ", 2))


# .partition() devuelve una tupla con 3 elementos, [str antes del separador,separador ,str despues del separador]

text = "esto es :una cadena de letras : y va a seperar todo :esto."

print(text.partition(":"))


# .join(lista) convierte una lista en un str separando los elementos por el str que llamo el metodo

list_name = ["hola","me","llamo", "daniel"]
print(" ".join(list_name))

"""ALINIACION Y FORMATO"""

# .center(n) centra una cadena de texto en un ancho de n caracteres

texto = "texto centrado"

print(texto.center(100))

# .ljust(n) alinea a la izquierda una cadena de texto en un ancho de n caracteres

texto = "texto alineado a la izquierda"

print(texto.ljust(100))


# .rjust(n) alinea a la derecha una cadena de texto en un ancho de n caracteres

texto = "texto alineado a la izquierda"

print(texto.rjust(100))

# .zfill(n) 

texto = "relleno con 0"

print(texto.zfill(100))




#Ejercicio Extra



def word_type(word_one :str, word_tow:str) -> str:
    """Retorna una str con el tipo de las palabras:
    Palindromo, Anagramas, Isogramas"""
    word_one, word_tow = word_one.lower(), word_tow.lower()
    
    def is_polindromo(word)->bool:
        if word == word[::-1]:
            return True
        return False
    
    def is_isograma(word)->bool:
        views = []
        for key, char in enumerate(word):
            if word[key] in views:
                return False
            views.append(char)
        return True
    def is_anagrama(word_one: str, word_tow: str)->bool:
        word_one = sorted(word_one)
        word_tow = sorted(word_tow)
        if word_one == word_tow:
            return True
        else:
            return False

    print(f"la palabra {word_one} es un polindromo?: {is_polindromo(word_one)}")
    print(f"la palabra {word_tow} es un polindromo?: {is_polindromo(word_tow)}")

    print(f"la palabra {word_one} es un isograma?: {is_isograma(word_one)}")
    print(f"la palabra {word_tow} es un isograma?: {is_isograma(word_tow)}")
    
    print(f"la palabra {word_one} es un anagrama de la palabra {word_tow}?: {is_anagrama(word_one,word_tow)}")



word_type("murciélago","oso")
