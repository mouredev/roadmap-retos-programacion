
lista: list = ["Jose", "Juan", "Miguel"]
print(lista)

# Inserción
lista.append("Samuel")
print(lista)

# Borrado
lista.remove("Jose")
print(lista)

# Actualización
lista[2] = "Albert"
print(lista)

# Ordenación
lista.sort()
print(lista)

# EXTRA

def agenda():
    lista = list

    while True:
        print("¿Que operación quieres hacer?")
        print("1. Nuevo Contacto\t2. Actualizar contacto\n3. Buscar contacto\t4. Eliminar contacto")

        opcion = int(input())

        if opcion == 1:


        


agenda()