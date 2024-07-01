# cadenas de caracteres

# Operaciones con cadenas de caracteres

# crear cadena

mi_cadena = "una cadena de texto"
print(mi_cadena)

# longitud de una cadena

print(f"La cadena tiene una longitud de {len(mi_cadena)} caracteres")

# concaterar cadenas

mi_nombre = "Pedro"
mi_apellido = "Pérez"
mi_segundo_apellido = "Gracia"
espacio = " "

mi_nombre_completo = mi_nombre + espacio + mi_apellido + espacio + mi_segundo_apellido

print (mi_nombre_completo)

# repetición

print(mi_nombre * 3)

# indexación
print (mi_nombre[0])
print (mi_nombre[2])
print (mi_nombre[4])

# slicing (quedarse con una parte de la cadena)
print(mi_nombre[0:5])
print(mi_nombre[3:5])
print(mi_nombre[1:])
print(mi_nombre[:3])

# busqueda
print("p" in mi_nombre)
print("P" in mi_nombre)

# reemplazo
print(mi_nombre.replace("P", "X"))

# División
print(mi_nombre.split("d"))

print(mi_nombre_completo)
print (mi_nombre_completo.split(espacio))








