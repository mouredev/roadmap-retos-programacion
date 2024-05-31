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

