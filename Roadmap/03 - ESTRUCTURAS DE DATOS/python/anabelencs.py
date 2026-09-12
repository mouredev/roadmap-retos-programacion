print("\n#03 ESTRUCTURAS DE DATOS")

'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''

print()
print("--- LISTAS [] ---")
print()

lista = ["X", "Python", "JavaScript", "HTML", "CSS"] # Con corchetes.
print(lista)
lista.append("React") # Función de Inserción. Va con paréntesis.
print(lista)
lista.remove("X") # Eliminación.
print(lista)
print(lista[0]) #Acceso. La primera posición es la 0.
lista[0]= "Lógica & Python" # Actualización.
print(lista)
lista.sort() # Ordenación. Por defecto en orden alfabético.
print(lista)
print(type(lista))


print()
print("--- TUPLAS () ---")
print()

# Las usamos cuando queremos que nuestras listas sean inmutables.
tupla = ("Ana", "Castillo", "@anabelencs") # Con paréntesis. No son modificables como las listas.
print(tupla)
print(type(tupla))
print(tupla[2]) # Acceso.
tupla = sorted(tupla) # Ordena y se guarda reordenada. Ojo: no se ordenan si hay datos de varios tipos (strings, numéricos...).
print(tupla) # Observar que se devuelve en la impresión en corchetes: se vuelve una lista.
print(type(tupla))
tupla_2 = ("Ana2", "Castillo2", "@anabelencs2")
print(tupla_2)
tupla_2 = tuple(sorted(tupla_2))
print(tupla_2)
print(type(tupla_2))


print()
print("--- SETS {} ---")
print()

# Es una estructura desordenada. No hay posiciones de datos.
# Buenos para guardar muchos datos, para recorrerlos, pero no para buscarlos. No acceso.
# Es para evitar duplicados. En la lista se pueden agregar dos datos iguales; en sets, no.
set = {"Ana", "Castillo", "@anabelencs", "dato_x"} # Con llaves.
# set: set = {"Ana", "Castillo", "@anabelencs", "dato_x"} # Lo mismo, pero especificando que es un set con los :.
print(set)
print(type(set))
set.add("ab@mail.com") # Inserción.
set.add("ab@mail.com") # Probando. No se inserta de nuevo porque ya está.
print(set)
set.remove("dato_x")
print(set)
set.update(["dato_5", "dato_6", "dato_7"]) # Para concatenar más datos al set. Se usan paréntesis y corchetes. 
# Update no cambia un dato específico de un set. Allí tocaría hacer remove y add.
print(set)
set = sorted(set) # Lo vuelve a convertir en una lista. Se puede convertir en un set pero, va a volver a desordenarse.
print(set)
print(type(set))


print()
print("--- DICCIONARIOS {clave: dato} ---")
print()

# dicc: dict = {"nombre": "Ana", "apellido": "Castillo", "usuario": "@anabelencs"} # Se puede poner así, o:
dicc: dict = {
    "nombre": "Ana", 
    "apellido": "Castillo", 
    "usuario": "@anabelencs"
}
print(dicc)
print(type(dicc))
print(dicc["nombre"]) # La estructura de los diccionarios no es propiamente ordenada. Entonces no hay acceso por posiciones, pero sí por clave.
dicc["correo"] = "ab@mail.com" # Inserción.
print(dicc)
dicc["nombre"] = "Ana Belén" # Actualización. Luce igual que inserción pero, como ya había un dato en "nombre", lo reemplaza.
print(dicc)
del dicc["apellido"] # Eliminación.
print(dicc)
# dicc = sorted(dicc) # Ordenación. Lo mismo; se ordena pero se convierte en una lista, sólo con las claves.
dicc = sorted(dicc.items()) # Ordenación con .items(). Lo hace con claves y datos, pero en forma de una lista que contiene tuplas: [(,),(,)]
print(dicc)
print(type(dicc))


print()
print("--- DIFICULTAD EXTRA ---")
print()

'''
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 '''

# input: para solicitarle un dato al usuario.
# match / case: parecido a usar if, elif y else pero más práctico en algunos casos, como este de la agenda.
# while True: para abrir un bucle infinito.
# break: para cerrar un bucle infinito.
# Otra forma de hacer el bucle infinito es, abrir con:
'''
is_on = True
while is_on: 
-- desarrollar todo --
y cerrar con:
is_on = False
'''

print("A G E N D A   T E L E F Ó N I C A")

def agendaplay():

    agendadict = {}

    def contacto_existente():
        nombre = input("Introduzca el nombre del contacto: ")
        while nombre not in agendadict:
            nombre = input("El contacto introducido no existe. Introduzca el nombre de un contacto existente: ")
        return nombre
        
    def telefono_correcto():
        telefono = input("Introduzca el número de teléfono (8 dígitos, sin guiones): ")
        while not telefono.isdigit() or len(telefono) != 8:
            telefono = input("El número de teléfono no es válido. Introduzca el número de teléfono (8 dígitos, sin guiones): ")
        return telefono

    while True:

        print("\nMENÚ DE ACCIONES:")
        print("1. Buscar un número telefónico")
        print("2. Agregar un contacto nuevo")
        print("3. Actualizar un contacto existente")
        print("4. Eliminar un contacto")
        print("5. Salir")
        
        accion = input("Indique la acción que desea realizar: ")

        match accion:

            case "1": #Buscar
                print("\nBUSCANDO UN CONTACTO:")
                nombre = contacto_existente()
                telefono = agendadict[nombre]
                print(f"El número de teléfono de {nombre} es {telefono}.")
                input("Presione Enter para volver al Menú...")

            case "2": #Agregar
                print("\nAGREGANDO UN CONTACTO:")
                nombre = input("Introduzca el nombre del contacto: ")
                telefono = telefono_correcto()
                agendadict[nombre] = telefono
                print(f"Se guardó el contacto de {nombre}; su teléfono es {telefono}.")
                input("Presione Enter para volver al Menú...")
                    
            case "3": #Actualizar
                print("\nACTUALIZANDO UN CONTACTO:")
                nombre = contacto_existente()
                telefono = telefono_correcto()
                agendadict[nombre] = telefono
                print(f"Se actualizó el contacto de {nombre}; su teléfono es {telefono}.")
                input("Presione Enter para volver al Menú...")

            case "4": #Eliminar
                print("\nELIMINANDO UN CONTACTO:")
                nombre = contacto_existente()
                del agendadict[nombre]
                print(f"Se eliminó el contacto de {nombre}.")
                input("Presione Enter para volver al Menú...")

            case "5":
                print("\nAdiós.\n")                
                break

            case _:
                print("\nOpción inválida.")
                input("Presione Enter para volver al Menú...")       

agendaplay()


'''
INTENTO 2

print("A G E N D A   T E L E F Ó N I C A")

def menu():

    print()
    print("Menú de acciones:")
    print("1. Buscar un número telefónico")
    print("2. Agregar un contacto nuevo")
    print("3. Actualizar un contacto existente")
    print("4. Borrar un contacto")
    print("5. Salir")
    print()

    accion_loc = int(input("Indique la acción que desea realizar:"))

    while accion_loc > 5 or accion_loc < 1:
        print("Opción inválida.")
        accion_loc = int(input("Indique una opción del 1 al 5:"))

    return accion_loc

accion = menu()

agenda:dict = {"nombre":"telefono"}
#agenda ["nombre"] = nombre
#agenda ["telefono"] = telefono

if accion == 2:
    print()
    nombre:str = input("Introduzca el nombre del contacto:")
    #print(f"El nombre es {nombre}.")
    telefono:int = input("Introduzca el número de teléfono (8 dígitos, sin guiones):")
    while len(telefono) != 8:
        print("El número de teléfono no es válido.")
        telefono:int = input("Introduzca el número de teléfono (8 dígitos, sin guiones):")
    #print(f"El teléfono es {telefono}.")
    print()
    print(f"Se guardó el contacto de {nombre}, su teléfono es {telefono}.")
    agenda[nombre] = telefono
    print()
    input("Presione Enter volver al Menú...")

accion = menu()

if accion == 1:
    nombre:str = input("Escriba el nombre del contacto:")
    if nombre in agenda:
        telefono = agenda [nombre]
        print(f"El número telefónico de {nombre} es {telefono}")
    else:
        print("El contacto no existe.")
        nombre:str = input("Escriba el nombre del contacto:")
    input("Presione Enter volver al Menú...")

accion = menu()
'''  
    

'''
INTENTO 1

nuevo = input("Desea agregar un contacto nuevo? Y/N:")
if nuevo == "y":
    nombre:str = input("Introduzca el nombre:")
    print(f"El nombre es {nombre}.")

    telefono:int = input("Introduzca el número de teléfono (8 dígitos, sin guiones):")
    while len(telefono) != 8:
        print("El número de teléfono no es válido.")
        telefono:int = input("Introduzca el número de teléfono (8 dígitos, sin guiones):")
    print(f"El teléfono es {telefono}.")

    agenda:dict = {"nombre":"telefono"}
    agenda ["nombre"] = nombre
    agenda ["telefono"] = telefono
    print(f"Contacto nuevo: {agenda}")

elif nuevo =="n":
    print("bye")
'''