#operaciones


s1 = "hola"
s2 = "python"

#concatenacion
print (s1 + ", " + s2 + "!")

#repeticion

print (s1 * 3)

#idexacion

print (s1[0] + s1[1] + s1[2] + s1[3])

#longitud

print(len(s1) + len(s2))

#slicing (porcion)

print( s2[2:5])
print( s2[2:])
print(s2[0:2])
print(s2[:2])

#busqueda

print ("a" in s1)

#reemplazo

print(s1.replace("o", "a"))

# Division

print(s2.split("t"))

# mayusculas y minisculas

print(s2.upper())
print(s2.lower())
print("simon torbett".title())
print("simon torbett".capitalize())

# elimicacion del espacio al principio y al finas

print(" simon torbett ".strip() + "lo lograras")

#busqueda al principio y al final

print(s1.startswith("ho"))
print(s1.startswith("py"))

s3 = "simon torbett"
# Busqueda de posicion

print("simon torbett @storbett".find("torbett"))

#busaqueda de ocurrencias

print(s3.lower().count("t"))

#formateo
print ("saludo: {}, lenguaje: {}!".format(s1, s2))

# interpolacion

print (f"saludo: {s1}, lenguaje: {s2}!")

# transformacion en lista de caracteres

print (list(s3))
       
# transformacion en lista en cadena 
l1 = [s1, ", ", s2, "!"]
print ("".join(l1))     

#transformacion numerica

s4 = "1234"
s4 = int(s4)
print (s4)

s5 = "1234.123"
s5 = float(s5)
print (s5)

#comparaciones varias
s4 = 1234
print (s1.isalnum())
print (s1.isalpha())


# extra


def check(palabra1: str, palabra2: str):

    #palindromos
    print (f"{palabra1} es un palindromo?: {palabra1 == palabra1[::-1]}") 
    print (f"{palabra2} es un palindromo?: {palabra2 == palabra2[::-1]}") 

    # Anagramas

    print (f"{palabra1} es un anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}") 

    # Isogramas 
    print (f"{palabra1} es un isograma?: {len(palabra1) == len(set(palabra1))}") 
    print (f"{palabra2} es un isograma?: {len(palabra2) == len(set(palabra2))}") 

    palabra_dict = dict()
    for palabra in palabra1:
        palabra_dict[palabra] = palabra_dict.get(palabra, 0) + 1

        isograma = True
        values = list(palabra_dict.values())
        isograma_len = values[0]
        for palabra_conteo in palabra_dict:
            if len(palabra_conteo) != isograma_len:
                isograma = False
                break

    print (isograma)
    print (palabra_dict)

check( "radar", "python")
# check( "amor", "roma")




