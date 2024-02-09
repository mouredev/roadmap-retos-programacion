#* DIFICULTAD EXTRA (opcional):
 #* Crea una agenda de contactos por terminal.
 #* - Debes implementar funcionalidades de búsqueda, inserción, actualización
 #*   y eliminación de contactos.
 #* - Cada contacto debe tener un nombre y un número de teléfono.
 #* - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 #*   y a continuación los datos necesarios para llevarla a cabo.
 #* - El programa no puede dejar introducir números de teléfono no númericos y con más
 #*   de 11 dígitos (o el número de dígitos que quieras).
 #* - También se debe proponer una operación de finalización del programa.
 #*/

agenda = {
    "Ivan" : 625325408,
    "Juan" : 634728376,
    "Blanca" : 623746342,
    "Pepe" : 637289476,
    "David" : 671829354
}

def buscar(nombre):
    if nombre not in agenda:
        return "El contacto no existe"
    
    return agenda[nombre]

def insertar(nombre, telefono):
    agenda[nombre] = telefono

def actualizar(nombre, telefono):
    agenda[nombre] = telefono

def eliminar(nombre):
    agenda.pop(nombre)


while True:
    print("Que operacion desea realizar:")
    print("1. BUSCAR")
    print("2. INSERTAR")
    print("3. ACTUALIZAR")
    print("4. ELIMINAR")
    print("5. SALIR")
    opcion_elegida = int(input())

    if opcion_elegida == 1:
        nombre = input("Introduzca el nombre del contacto: ").capitalize()
        print(buscar(nombre))

    elif opcion_elegida == 2:
        nombre = input("Introduzca el nombre del nuevo contacto: ").capitalize()
        telefono = input("Introduzca el telefono: ")

        if len(telefono) > 9 or not telefono.isdigit():
            print("Error al introducir el telefono")
        else:
            insertar(nombre, telefono)

    elif opcion_elegida == 3:
        nombre = input("Introduzca el nombre del contacto que quiera actualizar: ").capitalize()
        telefono = input("Introduzca el nuevo telefono: ")
        actualizar(nombre, telefono)

    elif opcion_elegida == 4:
        nombre = input("Introduzca el nombre del contacto que quiera eliminar: ").capitalize()
        eliminar(nombre)

    elif opcion_elegida == 5:
        print("Salió del programa")
        break
