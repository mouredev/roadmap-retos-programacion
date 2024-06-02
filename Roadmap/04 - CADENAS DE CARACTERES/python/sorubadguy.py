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
print("345".isdecimal())
print("34.5".isdigit())