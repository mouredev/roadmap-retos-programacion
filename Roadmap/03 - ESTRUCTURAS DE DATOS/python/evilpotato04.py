#/*
# * EJERCICIO:
# * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# ======= LISTAS =======
genshin_impact_personajes = ["Lumine", "Paimon"]

genshin_impact_personajes.append("Amber") # agrega un elemento
print(genshin_impact_personajes)

genshin_impact_personajes.extend(["Kaeya", "Lisa"]) # agrega una lista de elementos
print(genshin_impact_personajes)

genshin_impact_personajes.insert(1, "Diluc") # agrega un nuevo elemento según el índice
print(genshin_impact_personajes)

genshin_impact_personajes.remove("Paimon") # elimina un elemento específico
print(genshin_impact_personajes)

genshin_impact_personajes.pop() # elimina el ultimo elemento
print(genshin_impact_personajes)

genshin_impact_personajes.pop(2) # elimina un elemento según el índice
print(genshin_impact_personajes)

genshin_impact_personajes.clear() # elimina a todos los elementos de la lista
print(genshin_impact_personajes)

# ------------
genshin_impact_personajes.extend(["Qiqi", "Noelle", "Xinyan"])

print(genshin_impact_personajes.count("Qiqi")) # cuenta cuántas veces un mismo elemento aparece

genshin_impact_personajes.reverse() # invierte el orden de los elementos
print(genshin_impact_personajes)

genshin_impact_personajes2 = genshin_impact_personajes.copy() # copia la lista
genshin_impact_personajes2.append("Paimon")
print(genshin_impact_personajes)
print(genshin_impact_personajes2)

# ------------
del genshin_impact_personajes2[2]    # elimina el elemento correspondiente al índice
print(genshin_impact_personajes2)

del genshin_impact_personajes2[1:3]  # elimina elementos dentro del periodo
print(genshin_impact_personajes2)

del genshin_impact_personajes2[:]    # otra manera de eliminar a todos los elementos de la lista
print(genshin_impact_personajes2)


# ======= TUPLAS =======
genshin_impact_ciudades = ("Mondstadt", 'Liyue', "Sumeru", "Inazuma", "Fontaine")

ciudad_1, ciudad_2, ciudad_3, ciudad_4, ciudad_5 = genshin_impact_ciudades

print(f"""
        ciudad 1: {ciudad_1},
        ciudad 2: {ciudad_2},
        ciudad 3: {ciudad_3},
        ciudad 4: {ciudad_4},
        ciudad 5: {ciudad_5},
      """)

# ======= DICCIONARIO =======
genshin_impact_arcontes = {
    "Barbatos": "Anemo Archon",
    "Morax": "Geo Archon",
    "Raiden Shogun": "Electro Archon",
    "Nahida": "Dendro Archon",
    "Focalors": "Hydro Archon",
    "Murata": "Pyro Archon",
    "Tsaritsa": "Cryo Archon"
}

del genshin_impact_arcontes["Barbatos"] # elimina el elemento correspondiente a la clave
print(genshin_impact_arcontes)

genshin_impact_arcontes["Barbatos"] = "Anemo Archon" # agrega un nuevo elemento

print("Focalors" in genshin_impact_arcontes) # devuelve True si la clave existe en el diccionario
print("Focalors" not in genshin_impact_arcontes) # devuelve True si la clave no existe en el diccionario

# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una agenda de contactos por terminal.
# * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# * - Cada contacto debe tener un nombre y un número de teléfono.
# * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
# *   los datos necesarios para llevarla a cabo.
# * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
# *   (o el número de dígitos que quieras)
# * - También se debe proponer una operación de finalización del programa.
# */

def open_lista(contactos):
    id_contacto = 1
    print("")
    for contacto in contactos:
        print(f"""      {id_contacto}. {contacto["apellido"]}, {contacto["nombre"]}: {contacto["e-mail"]}""")
        id_contacto += 1
    print("")

def insert_contacto(contactos):
    nombre = input("Insert new contact's name: ")
    apellido = input("Insert new contact's last name: ")
    email = input("Insert new contact's e-mail: ")

    contactos.append({ "nombre": nombre, "apellido": apellido, "e-mail": email })
    print("New contact was added!")
    print("")
    return contactos

def remove_contacto(contactos):
    email = input("Insert the e-mail to be removed: ")
    contactos_nuevos = contactos.copy()
    for contacto in contactos:
        if contacto["e-mail"] == email:
            contactos_nuevos.remove(contacto)
            print("The contact was removed!")
    print("")
    return contactos_nuevos

def agenda_de_contactos():
    print("========= EVIL POTATO AGENDA =========")
    contactos = [{ "nombre": "Samunta", "apellido": "Lemos", "e-mail": "samunta@evilpotato.com" }]

    while True:
        print(f"""
            To open the contact list, digit option 1
            To insert a new contact, digit option 2
            To remove some contact from list, digit 3
            To close the agenda, digit option 9
            """)
        opcion = input("What do you want to do? ")

        match opcion:
            case "1":
                open_lista(contactos)
            case "2":
                contactos = insert_contacto(contactos)
            case "3":
                contactos = remove_contacto(contactos)
            case "9":
                print("Thank you for using this aplication! Bye! <3 <3 <3")
                return
            case _:
                print("Invalid option! Please, digit a valid option (1, 2, 3 or 9)")

agenda_de_contactos()
