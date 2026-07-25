# Ejercicio 04
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Variables

v_cadena = "Hola"
v_cadena2 = "Python"
v_cadena3 = "elias bonnin"
v_cadena4 = "elias bonnin @hotmail"
v_cadena5 = "123456"
list_c = [v_cadena, ", ", v_cadena2, "! "]

# Concatenacion

print(v_cadena + ", " + v_cadena2 + "!")  # Concatenamos cadenas sumandolas, podemos agregar espacios en el medio

# Repeticion

print(v_cadena * 3)  # Repetimos la cantidad de veces de 3 en este caso

# Indexacion

print(v_cadena[0] + v_cadena[1] + v_cadena[2])

# Longitud

print(len(v_cadena2))

# Slicing (Particionar)

print(v_cadena2[2:6])  # Si queremos un slice Concetro

print(v_cadena2[2:])  # Imprime hasta el final si necesidad de decirlo

print(v_cadena2[:2])  # Imprime desde el inicio hasta el indice 2 si necesidad de aclararlo

# Busqueda

print("a" in v_cadena)  # Buscamos si una cadena de caracteres "a" esta contenida en otra cadena "v_cadena"

# Remplazo

print(v_cadena.replace("o", "a"))  # Remplazamos donde estaria la existencia de cadena "o" por una "a"

# Division

print(v_cadena2.split("t"))  # Dividimos en el lugar que eligamos"t" y eliminamos en el proceso el punto elegido

# Conversion Mayusculas y Minusculas y Primera letra Mayuscula

print(v_cadena.upper())  # Pone todo en Mayuscula
print(v_cadena.lower())  # Pone todo en Minuscula
print(v_cadena3.title())  # Pone todos los primeros caracteres en Mayuscula
print(v_cadena3.capitalize())  # Pone solo el PRIMER caracter en Mayuscula

# Eliminacion de espacios al principio y final

v_cadena3 = " elias bonnin "
print(v_cadena3.strip() + "Eliasdev")

# Busqueda a principio y al final

print(v_cadena.startswith("Ho"))  # Podemos ver si la cadena empieza por un determinado texto
print(v_cadena.startswith("Py"))

print(v_cadena.endswith("la"))  # Podemos ver si la cadena termina por un determinado texto

# Busqueda de posicion

print(v_cadena4.find("bonnin"))  # Nos dice la Posicion donde esta empezando esa cadena buscada
print(v_cadena4.lower().find("b"))  # Se queda con la primera ocurrencia de match

# Busqueda de ocurrencias

print(v_cadena4.lower().count("n"))  # Me dice cuantas "n" hay en una cadena

# Formatear

print("Saludo: {} , Lenguaje: {} !".format(v_cadena, v_cadena2))

# Interpolacion FSTRING

print(f"Saludo: {v_cadena} , Lenguaje: {v_cadena2} !")

# Transformacion en lista de caracteres

print(list(v_cadena3))

# Transformacion de lista en cadena

print("".join(list_c))  # Une o concatena una lista de caracteres por un criterio

# Transformaciones numericas

print(v_cadena5)
v_cadena5 = int(v_cadena5)
print(v_cadena5)
v_cadena5 = float(v_cadena5)
print(v_cadena5)

# Comprobaciones

print(v_cadena4.isalnum())  # alfanumero
print(v_cadena.isalpha())  # Solo alfabetico
print(v_cadena.isnumeric())  # Es numerico

# Extra

# Funcion


def Check(Palabra1, Palabra2: str):

    # Palindromo

    print(f"{Palabra1} es un palindromo? {Palabra1 == Palabra1[::-1]}")  # Con el slider el inverso de la palabra
    print(f"{Palabra2} es un palindromo? {Palabra2 == Palabra2[::-1]}")

    # Anagrama

    print(f"{Palabra1} es un anagrama? {sorted(Palabra1) == sorted(Palabra2)}")

    # Isograma

    def isograma(Palabra: str) -> bool:

        dic_palabras = dict()
        for Palabra in Palabra2:
            dic_palabras[Palabra] = dic_palabras.get(Palabra, 0) + 1

        isograma = True
        Valores_dic = list(dic_palabras.values())
        len_isograma = Valores_dic[0]
        for Palabra_count in Valores_dic:
            if Palabra_count != len_isograma:
                isograma = False
                break

        return isograma

    print(f"{Palabra1} es un isograma? {isograma(Palabra1)}")
    print(f"{Palabra2} es un isograma? {isograma(Palabra2)}")


Check("radar", "phytonphytonphytonphyton")
Check("amor", "roma")
