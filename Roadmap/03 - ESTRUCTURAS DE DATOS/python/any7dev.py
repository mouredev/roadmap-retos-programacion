""" /*
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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */ """

# LISTAS
lista = [1, 2, 3, 4] # También -> lista = list("1234")
print(lista)

# Insercción al final de la lista
lista.append(5)
print(lista)
# Insercción en índice indicado
lista.insert(2, 2.5)
print(lista)
# Insercción de lista
lista.extend([0, 7, 8])
print(lista)

# Actualizar elemento
lista[6] = 6
print(lista)

# Borra elemento dado
lista.remove(2.5)
print(lista)
# Borra elemento según posición
del lista[4]
print(lista)
# Borra el último elemento de la lista
lista.pop()
print(lista)

# Invierte la lista
lista.reverse()
print(lista)
# Ordena la lista
lista.sort()
print(lista)

# Borra toda la lista
lista.clear()
print(lista)


# TUPLAS
tupla = (1, 2, 3) # También -> tupla = 1, 2, 3
print(tupla)


# SETS (CONJUNTOS)
conjunto = {1, 7, 6, 5, 8, 2} # También -> conjunto = set([1, 7, 6, 5, 8, 2])
print(conjunto)

# Añade elemento al final
conjunto.add(9)
print(conjunto)
# Añade varios elementos y si está, no hace nada
conjunto.update([9, 3, 5, 4])
print(conjunto)

# Eliminar elemento dado
conjunto.remove(6)
print(conjunto)
# Eliminar elemento dado y no hace nada si no existe
conjunto.discard(6)
print(conjunto)
# Elimina elemento aleatorio
conjunto.pop()
print(conjunto)
# Borra todo el set
conjunto.clear()
print(conjunto)


# DICCIONARIOS
diccionario = {"Nombre": "Ana", "Edad": 37, "Teléfono": 412567} # También -> diccionario = dict([("Nombre", "Ana"), ("Edad", 37), ("Teléfono", 412567)])
print(diccionario)                                                         # diccionario = dict(Nombre= "Ana", Edad= 37, Teléfono= 412567)

# Actualizar elemento
diccionario["Teléfono"] = 421576 
print(diccionario)
# Si no existe, se crea
diccionario["Dirección"] = "Calle Rumbo"
print(diccionario)
# Actualizar elemento
diccionario.update({"Teléfono": 423576}) 
print(diccionario)
# Si no existe, se crea
diccionario.update({"Profesión":"Estudiante"})
print(diccionario)

# Borra la clave indicada con su valor
diccionario.pop("Edad")
print(diccionario)
# Borra de forma aleatoria un elemento
diccionario.popitem()
print(diccionario)
# Borra el diccionario
diccionario.clear()
print(diccionario)



# DIFICULTAD EXTRA
def menu():
    while True:
        print(f"\n\t1-Mostrar Agenda\n\t2-Buscar contacto\n\t3-Insertar o actualizar contacto\n\t4-Borrar contacto\n\t5-Salir")    
        opcion = input(f"\nEscribe el número de la opción a realizar: ")
        match opcion:
            case "1": 
                  mostrar()
            case "2":
                  buscar()
            case "3": 
                  insertar()
            case "4": 
                    borrar()
            case "5": 
                print(f"Saliendo de la agenda\n")
                break                   
            case _: 
                  print("Opción incorrecta")

def mostrar():
    if not agenda:
        print(f"Agenda Vacía {agenda}")
    else:
        for clave, valor in agenda.items():
            print(f"{clave}-{valor}")

def buscar():
    if not agenda:
        print(f"Agenda Vacía {agenda}")
    else:
        contacto = input("Dime el nombre a buscar: ")
        contacto = agenda.get(contacto, "Contacto no encontrado")     
        print(f"\t\t\t {contacto}")      

def insertar():
    while True:
        nombre = input(f"Dime el nombre: ")
        if nombre and not nombre.isnumeric():
            if nombre in agenda:
                print("Contacto encontrado, lo vas a actualizar")
            else:
                print("Vas a crear un nuevo contacto")
            while True:
                telefono = input(f"Teléfono: ")
                if telefono and telefono.isnumeric() and len(telefono) == 9:
                    agenda[nombre] = telefono
                    break
                else:
                    print("Error: No se cumplen las validaciones. El teléfono debe ser número entero y tener 9 dígitos")
            break
        else:
            print("Error: No se cumplen las validaciones. El contacto debe tener un nombre no numérico")
        
def borrar():
    if not agenda:
        print(f"Agenda Vacía {agenda}")
    else:
        nombre = input(f"Dime el nombre: ")
        agenda.pop(nombre, "Contacto no encontrado")     
        
                     

if __name__ == '__main__':
    global agenda
    agenda = {}
    menu()
