#CADENAS DE CARACTERES

mi_cadena = "El amor no duele "

#Acceso a caracteres específicos
print(mi_cadena[3])

#Subcadenas
print(mi_cadena[3:7])

#Longitud
print(len(mi_cadena))

#Concatenación
otra_cadena = " vive y deja vivir"
print(mi_cadena +"," + otra_cadena)

#Repetición
print(mi_cadena * 3)

#Recorrido
for letra in mi_cadena:
    print(letra)

#Conversión a mayúsculas y minúsculas
print(mi_cadena.upper())
print(otra_cadena.lower())

#Reemplazo
print(otra_cadena.replace("vivir","gozar"))

#División
print(mi_cadena.split())

# Unión
print(".".join(otra_cadena))

#Interpolación
nombre = "Homero"
edad = 102
print(f" Hola mi nombre es {nombre}, tengo {edad} años, soy un lolo")

#Verificación
print("amor" in mi_cadena)
print("love" in mi_cadena)

#Eliminación de espacios
print(otra_cadena.strip())

#Capitalización
print(otra_cadena.title())
