#Strings en python

palabra = "Esto es una string"

palabra2 = " Esto es otra string"

#Longitud de una string
print(len(palabra))

#Concatenar
print(palabra + palabra2)

#Repetir palabra 
print(palabra *3)

#Acceder a una string
print(palabra[0])

#Convertir a mayúsculas, minísculas y capitalizar la primera
print(palabra.upper())
print(palabra.capitalize())
print(palabra.lower())

#Substrings
print(palabra.count("Esto"))

#Reemplazar
print(palabra.replace("Esto", "Hola"))

#Separar 
print(palabra.strip(" "))

#Juntar
print(palabra.split())

