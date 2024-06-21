import Foundation

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

class Perfil: Codable {
    let nombre: String
    let edad: Int
    let nacimiento: String
    let lenguajes: [String]
    
    init(nombre: String, edad: Int, nacimiento: String, lenguajes: [String]) {
        self.nombre = nombre
        self.edad = edad
        self.nacimiento = nacimiento
        self.lenguajes = lenguajes
    }
}

func json() {
    let person = Perfil(nombre: "James", edad: 35, nacimiento: "20/03/1998", lenguajes: ["Swift", "Kotlin", "Java"])
    let encoder = JSONEncoder()
    
    if let url = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("person.json"),
       let data = try? encoder.encode(person) {
        try? data.write(to: url)
        print(String(data: data, encoding: .utf8) ?? "Error al convertir el json a String")
    }
    
    let personContent = """
        nombre: James
        edad: 35
        nacimiento: 20/03/1989
        lenguajes: Swift, Kotlin, Java
    """
    print(personContent)
    
    do {
        try FileManager.default.removeItem(atPath: "person.json")
    } catch {
        print("Error el intantar borrar el archivo json \(error.localizedDescription)")
    }
}

func xml() {
    let person = Perfil(nombre: "James", edad: 35, nacimiento: "20/03/1989", lenguajes: ["Swift", "Java", "Kotlin"])
    let encoder = JSONEncoder()
    
    if let url = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("person.xml"),
       let data = try? encoder.encode(person) {
        try? data.write(to: url)
        print(String(data: data, encoding: .utf8) ?? "Error al convertir el archivo a XML")
    }
    
    let personContent = """
        nombre: James
        edad: 35
        nacimiento: 20/03/1989
        lenguajes: Swift, Java, Kotlin
    """
    print(personContent)
    
    do {
        try FileManager.default.removeItem(atPath: "person.xml")
    } catch {
        print("Error al intentar eliminar el archivo xml \(error.localizedDescription)")
    }
}












