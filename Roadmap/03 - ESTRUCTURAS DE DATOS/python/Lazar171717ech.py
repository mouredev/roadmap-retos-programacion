## 1. ESTRUCTURAS DE DATOS ##

# Listas #
lista: list = [1, 3, 5, 7, 9] # Aquí creamos una lista. Esta contiene varios datos que pueden ser de distintos tipos

print(f"Esta es mi lista: {lista}")

lista.append(11) # Con el método append estamos añadiendo el dato que nosotros le demos.
print(f"Hemos añadido el 11: {lista}")

lista.remove(5) # Con el método remove estamos eliminando el dato que nosotros le demos.
print(f"Hemos eliminado el 5: {lista}")

lista[2] = 13 # Podemos asignar a contenidos de la lista otros datos mediante su posición.
print(f"Hemos cambiado la 3ra posición: {lista}")

lista.sort() # Con el método sort estamos ordenando los contenidos de la lista en orden numérico o alfabético.
print(f"Hemos ordenado la lista: {lista}")

# Tuplas #
tupla: tuple = (0, 2, 4, 6, 8) # A diferencia de las listas, las tuplas no se pueden variar.

print(f"Accedemos a la tupla: {tupla[3]}") # Estamos accediendo a los datos de la tupla

print(f"Podemos también concatenar varias tuplas: {tupla + (10, 12, 14)}") # Al igual que las listas.

# Diccionarios #
diccionario: dict = {1: 2, 3: 4, 5: 6, 7: 8} # Aquí guardamos varios datos y asociamos otro a cada uno de ellos.
# De esta manera, cuando hagamos referencia al primer dato dentro del diccionario, estaríamos haciendo referencia a su asociado.

print(f"Nos devuelve los valores asociados: {diccionario.values()}") 
print(f"Podemos acceder al diccionario de varias maneras: {diccionario.get(1)}, {diccionario[1]}")
print(f"Podemos eliminar del diccionario: {diccionario.pop(1)}") 
print(f"Podemos actualizar el diccionario: {diccionario.update()}")

print(diccionario)


## 2. RETO EXTRA ##


contactos: list = []

while True:
    commando: str = input("\nComandos:\nshow\nsearch\nadd\nchange\nexit\n> ")

    if commando == "show":

        for i in contactos:
            print(f"Nombre : {i[0]}, Teléfono: {i[1]}")

    elif commando == "search":

        busqueda: str = input("buscar > ")
        founded: bool = False
        for i in contactos:
            if busqueda in [i[0], str(i[1])]:
                print(f"Nombre : {i[0]}, Teléfono: {i[1]}")
                founded = True
        if not founded: print("No hay resultados")

    elif commando == "add":

        nombre: str = input("name\n> ")
        tel: str = input("tel\n> ")

        if tel.isdigit() and len(tel) == 11:
            tel: int = int(tel)
            contactos.append([nombre, tel])
            print(f"Usuario {nombre} añadido")

        else: print("Telefono erroneo")

    elif commando == "change":

        busqueda: str = input("buscar > ")
        founded: bool = False
        position: int = 0
        for i in contactos:
            if busqueda in [i[0], str(i[1])]:
                founded = True
                position = contactos.index(i)
        if not founded: print("No hay resultados")
        nombre: str = input("name\n> ")
        tel: str = input("tel\n> ")

        if tel.isdigit() and len(tel) == 11:
            tel: int = int(tel)
            contactos[position] = [nombre, tel]
            print(f"Usuario {nombre} actualizando")
        

    elif commando == "exit":
        print("Adiós!")
        break

    else: print("Comando desconocido")
