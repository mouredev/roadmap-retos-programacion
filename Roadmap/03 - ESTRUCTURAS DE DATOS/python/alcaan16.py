"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
 """
agenda= {}


def my_agenda(opcion=0):

    def insertar():
        name = input("introduce el nombre del contacto: ")
        telefono = input("introduce el telefono del contacto: ")
        if telefono.isdigit and len(telefono) > 1 and len(telefono) <= 11:
            agenda[name] = telefono
        else:
            print("el numero no es valido")

    while True:

        print("\n******************")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        print("******************")

        opcion = input("\nIntroduce la opcion deseada: " )

        match opcion:
            case "1":
                print("1. Buscar contacto")
                if len(agenda) == 0:
                    print("no hay contactos")
                else:
                    buscar = input("introduce el nombre a buscar: ")
                    if buscar in agenda:
                        print (f"el numero de telefono del contacto {buscar} es: {agenda[buscar]}")
                    else:
                        print(f"no existe el contacto {buscar}")
            case "2":
                print("2. Insertar contacto")
                insertar()
            case "3":
                if len(agenda) == 0:
                    print("no hay contactos")
                else:
                    print("3. Actualizar contacto")
                    buscar = input("introduce el nombre del contacto a modificar: ")
                    if buscar in agenda:
                        insertar()
                    else:
                        print(f"no existe el contacto {buscar}")                   
            case "4":
                if len(agenda) == 0:
                    print("no hay contactos")
                else:
                    print("4. Eliminar contacto")
                    buscar = input("introduce el nombre a eliminar: ")
                    if buscar in agenda:
                        del agenda[buscar]
                    else:
                        print(f"no existe el contacto {buscar}")
            case "5":
                print("5. Salir")
                break
            case _:
                print ("Introduce una opcion valida. Desde el 1 al 5")
my_agenda()