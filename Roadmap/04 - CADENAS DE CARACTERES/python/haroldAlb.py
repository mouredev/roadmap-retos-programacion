cadena_01= "Hola"
cadena_02= "Mundo"
cadena_03= "Que ase?"
cadena_04= "HAROLD"
cadena_05= "5.33,12,200.633,001,3,0.009"
cadena_06= ["Hola", "Harolito", "que", "ases?"]
cadena_07= "123456"
cadena_08= "3.1416"
### Acceso a caracteres específicos ###
print(cadena_01[2]) # Imprime el caracter en el índice 2 

### subcadenas ###


### longitud ###
print(len(cadena_01)) # retorna el número total de caracteres que tenga el string

### concatenación ###
print(cadena_01 + " " + cadena_02)

### repetición ###
print("#" * 10)

### recorrido ###
for c in cadena_03:
    print(c)

### conversión a mayúsculas ###
print(cadena_01.upper())

### conversión a minúsculas ###
print(cadena_04.lower())

### reemplazo ###
print("Harold que ases".replace("Harold", cadena_01))

### división ###
print(cadena_05.split(",")) # Divide la cadena en una lista de subcadenas separadas por el separador especificado

### unión ###
print(" ".join(cadena_06)) # Une lo elementos de una lista, en una sola cadena. El separador se indica al principio

### interpolación ###


### verificación ###


### slicing ###
print(cadena_04[3:])
print(cadena_04[-1:-len(cadena_04)-1:-1])

### busqueda ###
print("u" in cadena_02)
print("a " in cadena_02)

### busqueda al principio y al final ###
print(cadena_01.startswith("H"))
print(cadena_01.startswith("K"))
print(cadena_01.endswith("a"))
print(cadena_01.endswith("i"))

### busqueda de posición ###
print(cadena_03.lower().find("q")) # pasa las mayusculas a minusculas y busca la posición de la 'q'

### conversión a Integer ###
print(type(int(cadena_07)))
print(type(float(cadena_08)))

### EXTRA ###
"""
Un palíndromo es una palabra o frase que se lee igual en un sentido que en otro.
Un anagrama es cojer una palabra o frase, reordenarla y obtenes otra palabra o otra frase.
Un isograma es una palabra donde ninguna letra se repite, como "murciélago".
""" 
def comprobacion(palabra_1: str, palabra_2: str):
    # Palíndromo
    def palindromo(palabra):
        palabra_reb= palabra[::-1]

        if palabra == palabra_reb:
            print(f"{palabra} si es un palíndromo")
        else:
            print(f"{palabra} no es un palíndromo")

    # Anagrama
    def anagrama(palabra_1, palabra_2):
        count= 0
        aux= ""
        if len(palabra_1) == len(palabra_2):
            for p1 in palabra_1:
                for p2 in palabra_2:
                    if p1 == p2 and p2 not in aux:
                        count += 1
                aux= aux + p1
            if count == len(palabra_2):
                print(f"{palabra_1} y {palabra_2} SI son Anagrama")
            else:
                print(f"{palabra_1} y {palabra_2} no son Anagrama")
        else:
            print(f"{palabra_1} y {palabra_2} NO son Anagrama")

    # Solución Anagrama de Brais #

    def anagramaBrais(palabra_1, palabra_2):
        if sorted(palabra_1) == sorted(palabra_2): # Ordena las letras de cada string y las compara entre si. Si tienen las mismas letras es que son Anagramas.
            print(f"{palabra_1} SI es anagrama de {palabra_2}")
        else:
            print(f"{palabra_1} NO es anagrama de {palabra_2}")
    
    # Isograma
    def isograma(palabra):
        aux=""

        for p in palabra:
            if p not in aux:
                aux= aux + p
            else:
                break
        
        if palabra == aux:
            print(f"{palabra} SI es un isograma")
        else:
            print(f"{palabra} NO es un isograma")

    palindromo(palabra_1)
    palindromo(palabra_2)
    anagrama(palabra_1, palabra_2)
    anagramaBrais(palabra_1, palabra_2)
    isograma(palabra_1)
    isograma(palabra_2)



if __name__ == "__main__":
    word_1= input("Introduce la primera palabra: ")
    word_2= input("Introduce la segunda palabra: ")

    comprobacion(word_1, word_2)