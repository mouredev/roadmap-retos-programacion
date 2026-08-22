"""
* EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
*   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

cadena = "hola cómo estás"
print(cadena.upper()) # Conversión a mayúsculas

cadena = "ESPAÑA BICAMPEONA"
print(f"Conversión a minúsculas: {cadena.lower()}, contador de palabras: {len(cadena)}") # Conversión a minúsculas ; cuenta el espacio como caracter

cadena_de_perdedores = " A LA PRÓXIMA ARGENTINA"

cadena_ground_truth = cadena + cadena_de_perdedores + " " + "RETIRAMOS A LIONEL" # Concatenación
print(cadena_ground_truth)

for i in cadena_de_perdedores: # Recorrido
    print(i)

print(cadena_de_perdedores * 3) # Repetición

ganadores_del_mundial = cadena[0] + cadena[1] + cadena[2] + cadena[3] + cadena[4] + cadena[5] # Indexación
print(ganadores_del_mundial)

ganadores_del_mundial = cadena[0:6] # Slicing (Porción) ; La posición 6 no se incluye!
print(ganadores_del_mundial)

print("ESPAÑA" in ganadores_del_mundial) # Búsqueda
print("ARGENTINA" in ganadores_del_mundial)

print(cadena_de_perdedores.replace("ARGENTINA", "FRANCIA")) # Reemplazo

cadena_trozeada = (cadena_ground_truth.split(" ")) # División en lista

print(type(cadena_trozeada))

(cadena_trozeada.append("WE ARE THE BEST"))
print(cadena_trozeada)

cadena_minus = cadena.lower()
print(cadena_minus.title()) # Primera letra de cada palabra en mayúscula
print(cadena_minus.capitalize()) # Únicamente la primera letra en mayúscula en toda la cadena

print(" marcos tudela     ".strip()) # Eliminación de espacios al principio y al final 

print("ferran torres".startswith("fe")) # Búsqueda al principio
print("ferran torres".endswith("rres")) # Búsqueda al final

print("Cabo verde casi se carga a Argentina".lower().find("carga")) # Posición de la c

facto_mundialista = "Cubarsí balón de oro cabros"

print(facto_mundialista.lower().count("c")) # Contador de ocurrencias

print(list(facto_mundialista)) # Transformación de caracteres a lista

lista = [cadena, cadena_de_perdedores, " dale wachin", " !"]
print("".join(lista)) # Transformación de lista en cadena de texto
print(" ciao!".join(lista))

#Comprobaciones Varias

cadena_alfanumérica = "HolaCola123"

print(cadena_alfanumérica.isalnum()) # Es alfanumércia ? 
print(cadena_alfanumérica.isalpha()) # Es alfa ? 

print(sorted("hola"))
"""
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""

def analizador_de_palabras():

    def comprobar_palindroma(palabra: str) -> bool:

        recorrido_izqda_dcha=""
        recorrido_dcha_izqda=""
        es_palindroma = False

        for letra in palabra.lower():
            recorrido_izqda_dcha+= letra

        for letra in palabra[::-1].lower(): # Coges toda la palabra, pero lee al revés, también válido con reversed()
            recorrido_dcha_izqda+= letra
    
        if recorrido_dcha_izqda == recorrido_izqda_dcha:
            es_palindroma = True
        
        return es_palindroma
    
    def comprobar_anagrama(palabra_1: str, palabra_2: str) -> bool:
        es_anagrama = False

        if sorted(palabra_1) == sorted(palabra_2):
            es_anagrama = True

        return es_anagrama

    def comprobar_isograma_primer_orden(palabra: str) -> bool:
        es_isograma = False

        if len(set(palabra)) == len(palabra):
            es_isograma = True

        return es_isograma
    
    def comprobar_isograma_segundo_orden(palabra: str) -> bool:
        
        if not palabra:
            return True

        diccionario = dict()

        # En programación: en Python, las líneas con = se ejecutan siempre de DERECHA a IZQUIERDA.
        for letra in palabra:
            diccionario[letra] = diccionario.get(letra, 0) + 1 

        lista_diccionario = list(diccionario.values())
        valor_referencia = lista_diccionario[0]

        for valor in diccionario.values():
            if valor_referencia != valor:
                return False
        
        return True
        

    print("")
    print("Introduce una palabra: ")
    palabra_1 = input()
    print("\nIntroduce otra palabra: ")
    palabra_2 = input()

    # ---- PALINDROMAS -----

    resultado_1_palindroma = comprobar_palindroma(palabra_1)
    resultado_2_palindroma = comprobar_palindroma(palabra_2)

    print(f"\nLa palabra 1 ha dado {resultado_1_palindroma} en el test de palundrismo\n")
    print(f"La palabra 2 ha dado {resultado_2_palindroma} en el test de palundrismo\n")

    # ---- ANAGRAMAS -----

    resultado_anagrama = comprobar_anagrama(palabra_1, palabra_2)

    print(f"El test anagrámico ha dado {resultado_anagrama}\n")

    # ---- ISOGRAMAS -----

    resultado_1_isograma = comprobar_isograma_primer_orden(palabra_1)
    resultado_2_isograma = comprobar_isograma_primer_orden(palabra_2)

    print(f"La palabra 1 ha dado {resultado_1_isograma} en el test isográmico")
    print(f"\nLa palabra 2 ha dado {resultado_2_isograma} en el test isográmico\n")

    resultado_1_segundo_orden = comprobar_isograma_segundo_orden(palabra_1)
    resultado_2_segundo_orden = comprobar_isograma_segundo_orden(palabra_2)
    print(f"La palabra 1 ha dado {resultado_1_segundo_orden} en el test isográmico de segundo orden\n")
    print(f"La palabra 1 ha dado {resultado_2_segundo_orden} en el test isográmico de segundo orden\n")


analizador_de_palabras()