'''
/*
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
 */
 '''

#region Estructuras de datos
#region Listas
print("----------Listas----------")
lista = [1, 2, 3, 4, 5]
print(lista)
print(lista[3])
lista.append(6)
print(lista)
lista.pop(2)
print(lista)
lista.sort(reverse = True)
print(lista)
lista[0] = 10
print(lista)
lista.clear()
print(lista)
#endregion

#region Tuplas
print("----------Tuplas----------")
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(tupla[3])
print(tupla.count(3))
print(tupla.index(4))
#endregion

#region Diccionarios
print("----------Diccionarios----------")
diccionario = {"nombre": "Alejandro", "apellido": "Abascal", "edad": 31 }
print(diccionario)
print(diccionario["nombre"])
diccionario["edad"] = 32
print(diccionario)
diccionario["telf"] = 123456789
print(diccionario)
diccionario.pop("apellido")
print(diccionario)
diccionario.clear()
print(diccionario)
#endregion

#region Conjuntos
print("----------Conjuntos----------")
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.add(6)
print(conjunto)
conjunto.remove(3)
print(conjunto)
conjunto.clear()
print(conjunto)
#endregion
#endregion

#region DIFICULTAD EXTRA
agenda = { "Alejandro": 123456789, "Alvaro": 987654321 }
#region Funciones
def busqueda_contacto():
    nombre = input("Introduzca el nombre del contacto a buscar: ").capitalize()
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - {agenda[nombre]}\n")
    else:
        print(f"No se ha encontrado el contacto {nombre}\n")

def insertar_contacto():
    nombre = input("Introduzca el nombre del contacto a guardar: ").capitalize()
    telf = input("Introduzca el teléfono del contacto a guardar: ")
    if telf.isdigit() and len(telf) == 9:
        agenda[nombre] = telf
        print(f"Contacto guardado: {nombre} - {agenda[nombre]}\n")
    else:
        print("Número de teléfono no válido\n")

def actualizar_contacto():
    nombre = input("Introduzca el nombre del contacto a actualizar: ").capitalize()
    if nombre in agenda:
        telf = input("Introduzca el nuevo teléfono del contacto: ")
        if telf.isdigit() and len(telf) == 9:
            agenda[nombre] = telf
            print(f"Contacto actualizado: {nombre} - {agenda[nombre]}\n")
        else:
            print("Número de teléfono no válido\n")
    else:
        print(f"No se ha encontrado el contacto {nombre}\n")

def eliminar_contacto():
    nombre = input("Introduzca el nombre del contacto a eliminar: ").capitalize()
    if nombre in agenda:
        agenda.pop(nombre)
        print(f"Contacto {nombre} eliminado\n")
    else:
        print(f"No se ha encontado el contacto {nombre}\n")

def mostrar_agenda():
    print("\nTodos los contactos de la agenda: ")
    for nombre in agenda:
        print(f"{nombre} - {agenda[nombre]}")
    print("")

def main():
    print("\n\n\n\nBienvenido a la agenda de contactos\n")
    salir = False
    while not salir:
        print("1. Buscar contacto: ")
        print("2. Insertar contacto: ")
        print("3. Actualizar contacto: ")
        print("4. Eliminar contacto: ")
        print("5. Ver contactos: ")
        print("6. Salir\n")

        opcion = input("Qué quiere hacer: ")

        match opcion:
            case "1":
                busqueda_contacto()
            case "2":
                insertar_contacto()
            case "3":
                actualizar_contacto()
            case "4":
                eliminar_contacto()
            case "5":
                mostrar_agenda()
            case "6":
                print("\nHasta la proxima!")
                salir = True
            case _:
                print("Opción no válida\n")
#endregion
main()
#endregion