"""
Operaciones
"""

string1 = "Hola"
string2 = "Python"


#Concatenacion
print(string1 + " " + string2 + "!")

#Repeticion 
print(string1 * 3)

#Indexacion
print(string1[0] + string1[1] + string1[2] + string1[3])

#longitud
print(len(string1))

#slicing (porcion)
print(string2[2:6])
print(string2[2:])

#Busqueda
print("Ho" in string1)

#Remplazo
print(string1.replace("o","a"))

#Division
print(string2.split("t"))

#Mayusculas y minusculas
print(string1.upper())
print(string1.lower())
print("hola a todos".title())
print("hola a todos".capitalize())

#Eliminacion de espacios
print("   Hola python    ".strip())

#Busqueda al principio y al final
print(string1.startswith("Ho"))
print(string1.startswith("Py"))
print(string1.endswith("Ho"))
print(string1.endswith("Ho"))

#Busqueda de posicion
print("Hola como estan todos?".find("estan"))

#Busqueda de ocurrencias
print(string1.lower().count("o"))

#Formateo de cadena
print("Saludo: {}, lenguaje: {}!".format(string1, string2))

#Interpolacion
print(f"Saludo: {string1}, lenguaje: {string2}!")

#Transformacion en lista
print(list(string1))

#Transformacion en string
lista1 = ["h","o","l","a"]
print("".join(lista1))

#transformaciones numericas
string3 = 123456789
string3 = int(string3)  #ENTERO
print(type(string3))  
string3 = float(string3)  #DECIMAL
print(type(string3)) 

#Comprobaciones varias
print(string1.isalnum())
print(string1.isalpha())
print(string1.isnumeric())



#DIFICULTAD EXTRA


def texto_palindromo():

    print("elija su palabra a comprobar")
    texto = input("")

    texto_dividio_1 = []
    texto_dividio_2 = []

    if len(texto) % 2 == 0:
        for i in range(len(texto) // 2):
            letra = texto[i]
            texto_dividio_1.append(letra)

        for i in range(len(texto) -1, len(texto) // 2 -1, -1):
            letra = texto[i]
            texto_dividio_2.append(letra)
            
    else:
        for i in range(len(texto) // 2):
            letra = texto[i]
            texto_dividio_1.append(letra)

        for i in range(len(texto) -1, len(texto) // 2 , -1):
            letra = texto[i]
            texto_dividio_2.append(letra)
            
    if  texto_dividio_1 == texto_dividio_2:
        print("su texto es palindromo")
    else:
        print("su texto no es palindromo")



def texto_anagrama():
    print("elije tu palabra numero 1")
    palabra1 = input()
    lista_palabra1 = list(palabra1)
    lista_palabra1.sort()
    
    print("elije tu palabra numero 2")
    palabra2 = input()
    lista_palabra2 = list(palabra2)
    lista_palabra2.sort()
    
    if lista_palabra1 == lista_palabra2:
        print("TU PALABRA ES UN ANAGRAMAA!!!!")
    else:
        print("TU PALABRA NO ES UN ANAGRAMA :(")






def texto_isograma():
    print("elije tu palabra para ver si es un isograma")
    palabra = input()
    conteo = {}

    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

    apariciones_iniciales = next(iter(conteo.values()))
    valores = list(conteo.values())
    
    def fun():
        for i in valores:
            if apariciones_iniciales != i:
                return False
        return True
    
    fun()
    resultado = fun()
    

    if resultado == True:
        print("es un isograma")
    else:
        print("no es un isograma")
    
def menu():
    print("1----------palindromos")
    print("2----------anagrama")
    print("3----------isograma")
    print("4----------salir")


    opcion = input()
    

    if opcion == "1":
        texto_palindromo()
        menu()
    elif opcion == "2":
        texto_anagrama()
        menu()
    elif opcion == "3":
        texto_isograma()
        menu()
    elif opcion == "4":
        exit()        
    else:
        menu()



menu()



