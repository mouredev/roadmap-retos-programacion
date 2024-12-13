# Función para limpiar la pantalla
def limpiar_pantalla():
    print("\033[H\033[J")


def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) <= 11


def agregar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono: ")

    if not validar_telefono(telefono):
        print("Número de teléfono no válido.")
        return

    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")


def buscar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a buscar: ")
    if nombre in agenda:
        print("Nombre: {}, Teléfono: {}".format(nombre, agenda[nombre]))
    else:
        print("Contacto no encontrado.")


def actualizar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a actualizar: ")
    if nombre in agenda:
        telefono = input("Introduce el nuevo número de teléfono: ")

        if not validar_telefono(telefono):
            print("Número de teléfono no válido.")
            return

        agenda[nombre] = telefono
        print("Contacto actualizado correctamente.")
    else:
        print("Contacto no encontrado.")


def eliminar_contacto(agenda):
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado correctamente.")
    else:
        print("Contacto no encontrado.")


def main():
    agenda = {}

    while True:
        limpiar_pantalla()
        print("--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

        input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
