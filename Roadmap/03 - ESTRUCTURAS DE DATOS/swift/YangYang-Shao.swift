/*
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

// Estructuras de datos en Swift
// Array 
var nameGatos = ["Ruru", "Matis", "Ruru", "Michi", "huahua"]
print(nameGatos)

// Insertar un elemento en el array
nameGatos.append("Sassi")
print(nameGatos)

// Borrar un elemento del array
nameGatos.remove(at: 2)
print(nameGatos)

nameGatos.removeLast()
print(nameGatos)

// Ordenar un array
nameGatos.sort()
print(nameGatos)

// Actualizar un elemento del array
nameGatos[0] = "Sasusu"
print(nameGatos)


// Dictionary
var animalTelefono = ["Ruru": "1234567890", "Matis": "0987654321", "Nanazu": "1112223333"]
print(animalTelefono)

// Insertar un elemento en el diccionario
animalTelefono["Sassi"] = "87936766783"
print(animalTelefono)

// Actualizar un elemento del diccionario
animalTelefono["Ruru"] = "0000000000"
print(animalTelefono)

// Borrar un elemento del diccionario
animalTelefono["Matis"] = nil //animnalTelefono.removeValue(forKey: "Matis")
print(animalTelefono)


// Set
var animalFamily: Set<String> = ["Ruruzi", "Meme", "Nana", "Meme"]
print(animalFamily)

// Insertar un elemento en el set
animalFamily.insert("Sassi")
print(animalFamily)

// Borrar un elemento del set
animalFamily.remove("Meme")
print(animalFamily)


// Tuple
var gatoInfo = (nombre: "Ruru", edad: 3, color: "Gris")
print(gatoInfo)
print("Nombre: \(gatoInfo.nombre), Edad: \(gatoInfo.edad), Color: \(gatoInfo.color)")

// Actualizar un elemento de la tupla
gatoInfo.edad = 4
print(gatoInfo) 


//Dificultad Extra
var agendaContactos = ["Ruyi": "1234567890", "Matis": "0987654321", "Nanazu": "1112223333", "Sassi": "87936766783"]

var continuar = true

while continuar {
    print("Selecciona una operación: (1) Buscar, (2) Insertar, (3) Actualizar, (4) Eliminar, (5) Finalizar")
    if let opcion = readLine() {
        switch opcion {

        case "1":
            print("Introduce el nombre del contacto a buscar:")
            if let nombreBuscar = readLine() {
                if let telefono = agendaContactos[nombreBuscar] {
                    print("El número de \(nombreBuscar) es: \(telefono)")
                } else {
                    print("Contacto no encontrado.")
                }
            }

        case "2":
            print("Introduce el nombre del contacto a insertar:")
            if let nombreInsertar = readLine() {
                print("Introduce el número de teléfono:")
                if let telefonoInsertar = readLine() {
                    if telefonoInsertar.count <= 11 && Int(telefonoInsertar) != nil {
                        agendaContactos[nombreInsertar] = telefonoInsertar
                        print("Contacto insertado correctamente.")
                    } else {
                        print("Número no válido. Debe ser numérico y máximo 11 dígitos.")
                    }
                }
            }

        case "3":
            print("Introduce el nombre del contacto a actualizar:")
            if let nombreActualizar = readLine() {
                if agendaContactos[nombreActualizar] != nil {
                    print("Introduce el nuevo número de teléfono:")
                    if let telefonoActualizar = readLine() {
                        if telefonoActualizar.count <= 11 && Int(telefonoActualizar) != nil {
                            agendaContactos[nombreActualizar] = telefonoActualizar
                            print("Contacto actualizado correctamente.")
                        } else {
                            print("Número no válido. Debe ser numérico y máximo 11 dígitos.")
                        }
                    }
                } else {
                    print("Contacto no encontrado.")
                }
            }

        case "4":
            print("Introduce el nombre del contacto a eliminar:")
            if let nombreEliminar = readLine() {
                if agendaContactos[nombreEliminar] != nil {
                    agendaContactos.removeValue(forKey: nombreEliminar)
                    print("Contacto eliminado correctamente.")
                } else {
                    print("Contacto no encontrado.")
                }
            }

        case "5":
            continuar = false
            print("Programa finalizado.")

        default:
            print("Opción no válida. Selecciona del 1 al 5.")
        }
    }
}