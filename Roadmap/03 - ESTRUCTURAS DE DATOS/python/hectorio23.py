# Autor: Héctor Adán 
# GitHub: https://github.com/hectoiro23

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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''

contacts = []

def menu():
    while True:
        print("************ Sistema de Gestion de contactos *************")
        print("[1] - Busqueda de Contactos")
        print("[2] - Insercion de Contactos")
        print("[3] - Actualizacion de Contactos")
        print("[4] - Eliminacion de Contactos")
        print("[5] - Imprimir todos los contactos")
        print("[6] - Terminar el programa")

        choose = input("Escoge una opcion: ")

        if choose == '1':
            buscar_contacto()
        elif choose == '2':
            agregar_contacto()
        elif choose == '3':
            actualizar_contacto()
        elif choose == '4':
            eliminar_contacto()
        elif choose == '5':
            imprimir_contactos()
        elif choose == '6':
            print("Programa terminado. Adios.")
            break
        else:
            print("Opcion invalida. Intentalo de nuevo.")
        print("\n\n")

def buscar_contacto():
    patron = input("Ingresa el registro que quieras buscar (nombre/telefono): ")
    print("\n")

    encontrado = False
    for nombre, telefono in contacts:
        if nombre == patron or telefono == patron:
            print(f"Registro encontrado: {nombre} <- {telefono}")
            encontrado = True
            break

    if not encontrado:
        print("Dato no encontrado")

def agregar_contacto():
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    telefono = input("Ingresa el numero de telefono del nuevo contacto: ")

    if len(telefono) > 11 or not telefono.isdigit():
        print("Numero de telefono invalido. Debe tener hasta 11 digitos y ser numerico.")
        return

    contacts.append((nombre, telefono))
    print("Contacto agregado exitosamente.")

def actualizar_contacto():
    nombre = input("Ingresa el nombre del contacto que quieres actualizar: ")

    encontrado = False
    for i, (nombre_contacto, telefono_contacto) in enumerate(contacts):
        if nombre_contacto == nombre:
            nuevo_telefono = input(f"Ingresa el nuevo numero de telefono para {nombre}: ")

            if len(nuevo_telefono) > 11 or not nuevo_telefono.isdigit():
                print("Numero de telefono invalido. Debe tener hasta 11 digitos y ser numerico.")
                return

            contacts[i] = (nombre_contacto, nuevo_telefono)
            print("Contacto actualizado exitosamente.")
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingresa el nombre del contacto que quieres eliminar: ")

    for i, (nombre_contacto, telefono_contacto) in enumerate(contacts):
        if nombre_contacto == nombre:
            del contacts[i]
            print("Contacto eliminado exitosamente.")
            return

    print("Contacto no encontrado.")

def imprimir_contactos():
    print("\n\n")
    for nombre, telefono in contacts:
        print(f"{nombre} <- {telefono}\n\n")

if __name__ == "__main__":
    menu()
