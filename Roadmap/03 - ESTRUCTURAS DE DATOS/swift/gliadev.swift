import Foundation

// Creación de un array
var numeros = [1, 2, 3, 4, 5]

// Inserción
numeros.append(6) // Añade al final
numeros.insert(0, at: 0) // Inserta al inicio

// Borrado
numeros.remove(at: 0) // Elimina el primer elemento

// Actualización
numeros[0] = 10 // Camia el primer elemento

// Ordenación
numeros.sort() // Ordena el array

// Creación de un set
var conjunto = Set(["manzana", "naranja", "plátano"])

// Inserción
conjunto.insert("uva")

// Borrado
conjunto.remove("naranja")



// Creación de un diccionario
var edades = ["Juan": 25, "Ana": 30, "Pedro": 22]

// Inserción
edades["Luis"] = 28

// Borrado
edades.removeValue(forKey: "Ana")

// Actualización
edades["Juan"] = 26

// Ordenación por clave
let clavesOrdenadas = edades.keys.sorted()

// Creación de una tupla
var persona = (nombre: "Carlos", edad: 35)

// Actualización
persona.edad = 36


import Foundation

var contactos = [String: String]() // Diccionario para almacenar contactos

func agregarContacto(nombre: String, telefono: String) {
    let esNumerico = Int(telefono) != nil
    let longitudValida = telefono.count <= 11

    if esNumerico && longitudValida {
        contactos[nombre] = telefono
        print("Contacto agregado.")
    } else {
        print("Número de teléfono inválido.")
    }
}

func eliminarContacto(nombre: String) {
    if contactos.removeValue(forKey: nombre) != nil {
        print("Contacto eliminado.")
    } else {
        print("Contacto no encontrado.")
    }
}

func actualizarContacto(nombre: String, telefono: String) {
    if contactos[nombre] != nil {
        contactos[nombre] = telefono
        print("Contacto actualizado.")
    } else {
        print("Contacto no encontrado.")
    }
}

func buscarContacto(nombre: String) {
    if let telefono = contactos[nombre] {
        print("Número de \(nombre): \(telefono)")
    } else {
        print("Contacto no encontrado.")
    }
}

// Ejemplo de uso
agregarContacto(nombre: "Alice", telefono: "1234567890")
buscarContacto(nombre: "Alice")
actualizarContacto(nombre: "Alice", telefono: "0987654321")
eliminarContacto(nombre: "Alice")


