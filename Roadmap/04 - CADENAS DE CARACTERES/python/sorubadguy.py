"""
Cadenas de caracteres
"""
cadena = "Hola Soy una cadena de caracteres"
cadena2 = '  yo tambien lo soy    '
cadena3 = """--soy una
cadena escrita en
varias lineas--
"""
cadena4 = "soy"

print(cadena)
print(cadena2)
print(cadena3)
print(cadena[3])
print(len(cadena)) #tamaño de la cadena
print("una" in cadena) #compruebo si una cadena esta en la cadena
print("sde" in cadena)
print(cadena4 in cadena)
print(cadena[3:13]) #Selecciono un rango de caracteres dentro de la cadena
print(cadena[:13]) #muestro desde el inicio hasta el caracter indicado
print(cadena[13:]) #mustro desde el caracter indicado hasta el final de la cadena
print(cadena[-8:]) #Al utilizar numeros negativos como indice, empieza a contar posiciones desde el final
print(cadena.upper()) #Todos los caracterse pasan a ser mayusculas
print(cadena.lower()) #Todos los caracteres pasan a ser minusculas
print(cadena2.strip()) #quita los espacion en blanco del principio de la cadena
print(cadena.replace("a", "t")) #reemplaza todas las coincidencias con el primer parametro con el segundo
print(cadena.split(" ")) #devuleve una lista de substrings separadas por el caracter dado
print(cadena.split("a"))

cadena5 = cadena2 + cadena3
print(cadena5)

costo = 34
print(f"el costo del producto es de {costo:.3f}") #puedo indicar en cuantos decimales puedo mostrar de un numero
print("puedo usar el simbolo \\ para evadir la \"funcionalidad\" de un caracter en especifico")

#Metodos
print("\n\n")
print("convierte la primer letra de la cadena en mayuscula".capitalize()) #convierte la primer letra de la cadena en mayuscula
print("CONVIERTE TODO EL TEXTO EN MINUSCULA".casefold())
centrar = "centra el contenido \"X\" caracteres"
print(centrar.center(50))
print(centrar.center(50, "_"))
print("Muestra la cantidad de ocurrencias en un string de un valor especifico".count("un"))
print("codifica caracteres especiales: Ståle".encode())
print("devuelve True si termina con el valor especificado".endswith("cado"))
print("devuelve True si termina con el valor especificado".endswith("valor"))
print("Especifica el valor de las t\ta\tb\tu\tl\ta\tc\ti\to\tn\te\ts".expandtabs(5))
print("busca un valor especifico y devuleve en que posicion se encontro".find("valor")) #En caso de no encotrar ocurrencias devuelve -1
print("da formato a un texto {costo:.2f}".format(costo = 50))
print("busca un valor especifico y devuleve en que posicion se encontro".index("valor")) #En caso de no encontrar ocurrencias devuelve un error
print("TrueS1T0d0sLosCaracteresSonAlfanumericos".isalnum())
print("TrueSiTodosLosCaracteresPertenecenAlAlfabeto".isalpha())
print("True si todos l0s c4ract3res corresponden con los valores ascii".isascii())
print("345".isdecimal()) #solo permite numeros decimales, es decir del 0 al 9
print("3\u00B2 ","\u00B2".isdigit()) #Permite decimales, aunque estos sean por ejemplo decimales
print("True_si_es_un_identificado_valido".isidentifier()) #Se considera identificador si solo posee caracteres alfanumericos, es decir, (0-9) (a-z) o "_"
print("true si todos los carecteres estan en minusculas".islower())
print("2234567".isnumeric()) #devuelve true si todos sus caracteres son numeros
print("true si la cadena es imprimible".isprintable())
print("              ".isspace()) #True si todos los caracteres de la cadena son " " espacios
print("True Si Corresponde Con La Norma De Titulos".istitle()) #todas las palabras deben comenzar con una mayuscula y seguir con minusculas
print("TRUE SI TODAS LAS LETRAS DE LA CADENA SON MAYUSCULAS".isupper())
lista_nombres = ("lucas", "pedro", "gaston")
print("#".join(lista_nombres)) #concatena con el caracter indicado un elemento iterable
print("ljust()".ljust(30), "devuelve una version justificada hacia la izquiera")
print("CONVIERTE TODO EN MINUSCULAS".lower())
print("quita los espacios","            que se encuentren              ".lstrip(), "a la izquierda")
centrar = "Me van cambiar las letras \"a\" por letras \"T\""
mapa = str.maketrans("a", "t") #genera un mapa de caracteres
print(centrar.translate(mapa)) #translate intercambia la primera letra del mapa de caracteres por la segunda
print("Retorna una tupla con 3 resultados:lo que esta antes de la cadena indicada, la cadena, y lo que esta despues".partition("indicada"))
print("Reemplaza un caracter especifico por otro".replace("e","j"))
print("devuelve la ultima posicion en la que se encontro el string dado".rfind("s"))
print("devuelve la ultima posicion en la que se encontro el string dado".rindex("s")) #da error en caso de no encontrarlo
print("justifica hacia la derecha".rjust(40))
print("Realiza lo mismo que particion, salvo que usa la ultima ocurrencia en el string".rpartition("l"))
print(cadena.rsplit(" ", 2))
print("quita los espacio", "                  de               ".rstrip(), "la derecha")
print(cadena3.splitlines()) #genera una lista a partir de las lineas de un strin
print("True si el estring comienza con la cadena dada".startswith("Tr"))
print("InViErTe MaYuScUlAs Y mInUsCuLaS".swapcase())
print("convierte todas las primeras letras en mayusculas".title())
print("rellena los strigns con 0 hasta que\n".zfill(10), "llegan a\n".zfill(10), " \"X\" caracteres".zfill(25))

"""
Extra
"""
def palindromo(palabra1: str, palabra2: str):
    
    if(palabra1[:] == palabra2[::-1]):
        print(f"{palabra1} y {palabra2} son palindromos entre si")
    else:
        print(f"{palabra1} y {palabra2} no son palindromos entre si")

        if(palabra1[:] == palabra1[::-1]):
            print(f"{palabra1} es palindromo")

        if(palabra2[:] == palabra2[::-1]):
            print(f"{palabra2} es palindromo")

def anagrama(palabra1: str, palabra2: str):

    palabra1 = palabra1.replace(" ", "")
    palabra2 = palabra2.replace(" ", "")

    if(len(palabra1) == len(palabra2)):
        palabra1_ordenada = []
        palabra2_ordenada = []
        palabra1_ordenada = list(palabra1)
        palabra2_ordenada = list(palabra2)
        palabra1_ordenada.sort()
        palabra2_ordenada.sort()

        if(palabra1_ordenada == palabra2_ordenada):
            print(f"{palabra1} y {palabra2} son anagramas")
        else:
            print(f"{palabra1} y {palabra2} no son anagramas")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas")

def isograma(palabra1: str, palabra2: str):
    contador1 = {}
    contador2 = {}
    iso = False
    for i in range(0,len(palabra1)):
        if(palabra1[i] not in contador1):
            contador1[palabra1[i]] = palabra1.count(palabra1[i])

    for i in range(0,len(palabra2)):
        if(palabra2[i] not in contador2):
            contador2[palabra2[i]] = palabra2.count(palabra2[i])

    if(len(contador1) == len(contador2)):
        for i in contador1:
            if(i in contador2 and contador1[i] == contador2[i]):
                iso = True
            else:
                iso = False
                break;
    
    if iso:
        print(f"{palabra1} y {palabra2} son isogramas")
    else:
        print(f"{palabra1} y {palabra2} no son isogramas")

def palabras(palabra1: str, palabra2: str):
    isograma(palabra1, palabra2)
    anagrama(palabra1, palabra2)
    palindromo(palabra1, palabra2)

palabras("cara", "arca")