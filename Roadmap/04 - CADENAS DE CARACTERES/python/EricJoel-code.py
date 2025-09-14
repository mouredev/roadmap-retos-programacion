# Cadenas de caracteres son secuencias de caracteres que se utilizan para representar texto en Python.

## Operaciones 

cadena1 = "Hola"
cadena2 = "Mundo"

# Concatenación
print(cadena1 + ", " + cadena2) 

# Repetición
print(cadena1 * 3)

#Indexación
print(cadena1[0])

#Longitud
print(len(cadena1))
print(len(cadena2))

#Slicing
print(cadena1[1:3]) # no incluye el índice final
print(cadena2[:3])  # desde el inicio hasta el índice 3 (no incluido)
print(cadena2[3:])  # desde el índice 3 hasta el final
print(cadena2[-1])  # último carácter
print(cadena2[-3:]) # últimos tres caracteres

#Busqueda
print(cadena1.find("o")) # índice de la primera ocurrencia de "o"
print(cadena2.find("x")) # devuelve -1 si no se encuentra

print("a" in cadena1) # True
print("x" in cadena2) # False

#Reemplazo
print(cadena1.replace("o", "a")) 
print(cadena2.replace("Mundo", "Python"))
print(cadena2) # la cadena original no cambia

#Division
print(cadena2.split("n")) # divide en una lista

#Recorrido
for char in cadena1:
    print(char)


