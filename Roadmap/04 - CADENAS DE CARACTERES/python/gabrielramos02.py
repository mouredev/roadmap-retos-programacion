# #04 CADENAS DE CARACTERES

# Acceso a caracteres
ejemplo = "ejemplo"
print(ejemplo[1])  # Accede al elemtento en la segunda posicion del string

#  Repeticion
print(
    ejemplo.count("e")
)  # count.() devuelve la cantidad de caracteres que son iguales al pasado por parametros

# Longitud
print(
    len(ejemplo)
)  # len() devuelve la cantidad de elementos que tenga el objeto pasado por parametros

# Concatenacion
print(ejemplo + " concatenacion")

# Recorrido
for i in ejemplo:  # Recorre cada uno de los elementos del string
    print(i)

# Conversion a mayuscula
print(ejemplo.capitalize())  # solo la inicial
print(ejemplo.upper())  # todas las letras
ejemplo = ejemplo.upper()  # convertimos todas a mayusculas para los siguientes ejemplos
print(ejemplo.lower())  # todas son minusculas

# Remplazo
reemplazado = ejemplo.replace("EJEMPLO", "ejemplo de reemplazo")
print(reemplazado)

# Division
print(ejemplo.split(","))


# Dificultado extra

def verificar(palabra1: str, palabra2: str):
    if palabra1.lower() == palabra2.lower():
        print("Las palabras son iguales")
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    def es_palindromo():
        if len(palabra1) == len(palabra2):
            return palabra1.lower() == palabra2.lower()[::-1]
        else: return False
    print("Palindromo: ",es_palindromo())
          
    def es_anagrama(): 
        list_palabra1 = list()
        list_palabra2 = list()
        for index in palabra1:
            list_palabra1.append(index)
        for index in palabra2:
            list_palabra2.append(index)
        list_palabra1.sort()
        list_palabra2.sort()
        #print(list_palabra1)
        #print(list_palabra2)

        return list_palabra1 == list_palabra2
    
    print("Anagrama: ",es_anagrama())


verificar("roma","amor")
