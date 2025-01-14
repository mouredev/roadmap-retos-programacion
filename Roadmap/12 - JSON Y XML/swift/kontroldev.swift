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


// Definición de la clase personalizada
class Persona: Codable {
    var nombre: String
    var edad: Int
    var fechaNacimiento: Date
    var lenguajesProgramacion: [String]

    init(nombre: String, edad: Int, fechaNacimiento: Date, lenguajesProgramacion: [String]) {
        self.nombre = nombre
        self.edad = edad
        self.fechaNacimiento = fechaNacimiento
        self.lenguajesProgramacion = lenguajesProgramacion
    }
}

// Creación de una instancia de la clase Persona
let persona = Persona(nombre: "Juan", edad: 30, fechaNacimiento: Date(), lenguajesProgramacion: ["Swift", "Python", "JavaScript"])

// Creación del archivo JSON
if let url = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.json"),
   let data = try? JSONEncoder().encode(persona) {
    try? data.write(to: url)
    print(String(data: data, encoding: .utf8) ?? "Error al convertir a String")
}

// Creación del archivo XML
if let url = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.xml"),
   let data = try? PropertyListEncoder().encode(persona) {
    try? data.write(to: url)
    print(String(data: data, encoding: .utf8) ?? "Error al convertir a String")
}

// Lectura y transformación de los datos almacenados en el XML y el JSON
if let urlJSON = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.json"),
   let urlXML = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.xml"),
   let dataJSON = try? Data(contentsOf: urlJSON),
   let dataXML = try? Data(contentsOf: urlXML),
   let personaDesdeJSON = try? JSONDecoder().decode(Persona.self, from: dataJSON),
   let personaDesdeXML = try? PropertyListDecoder().decode(Persona.self, from: dataXML) {
    print(personaDesdeJSON)
    print(personaDesdeXML)
}

// Borrado de los archivos
do {
    let urlJSON = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.json")
    let urlXML = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first?.appendingPathComponent("persona.xml")
    try FileManager.default.removeItem(at: urlJSON!)
    try FileManager.default.removeItem(at: urlXML!)
} catch {
    print("Error al borrar los archivos")
}


/// **Ejercicios Extra

import Foundation

class Person: Codable {
    var name: String
    var age: Int
    var email: String

    // Inicialización a partir de JSON
    init(fromJSON data: Data) throws {
        let decoder = JSONDecoder()
        let person = try decoder.decode(Person.self, from: data)
        self.name = person.name
        self.age = person.age
        self.email = person.email
    }

    // Inicialización a partir de XML
    init(fromXML data: Data) throws {
        let parser = XMLParser(data: data)
        let delegate = PersonXMLParserDelegate()
        parser.delegate = delegate
        parser.parse()

        guard let person = delegate.person else {
            throw NSError(domain: "XMLParsingError", code: 0, userInfo: nil)
        }
        self.name = person.name
        self.age = person.age
        self.email = person.email
    }
}

// Clase auxiliar para parsear XML
class PersonXMLParserDelegate: NSObject, XMLParserDelegate {
    var person: Person?
    var currentElement = ""
    var currentName = ""
    var currentAge = 0
    var currentEmail = ""

    func parser(_ parser: XMLParser, didStartElement elementName: String, namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [String : String] = [:]) {
        currentElement = elementName
    }

    func parser(_ parser: XMLParser, foundCharacters string: String) {
        let trimmedString = string.trimmingCharacters(in: .whitespacesAndNewlines)
        if !trimmedString.isEmpty {
            switch currentElement {
            case "name":
                currentName += trimmedString
            case "age":
                if let age = Int(trimmedString) {
                    currentAge = age
                }
            case "email":
                currentEmail += trimmedString
            default:
                break
            }
        }
    }

    func parser(_ parser: XMLParser, didEndElement elementName: String, namespaceURI: String?, qualifiedName qName: String?) {
        if elementName == "person" {
            person = Person(name: currentName, age: currentAge, email: currentEmail)
        }
    }
}

/// *Paso 2: Leer y transformar los datos

func readData(fromFile path: String) throws -> Data {
    return try Data(contentsOf: URL(fileURLWithPath: path))
}

func createPerson(fromFile path: String) throws -> Person {
    let data = try readData(fromFile: path)
    if path.hasSuffix(".json") {
        return try Person(fromJSON: data)
    } else if path.hasSuffix(".xml") {
        return try Person(fromXML: data)
    } else {
        throw NSError(domain: "UnsupportedFileType", code: 0, userInfo: nil)
    }
}

/// *Paso 3: Borrar los archivos después de procesarlos

func deleteFile(atPath path: String) throws {
    try FileManager.default.removeItem(atPath: path)
}

func processAndDeleteFile(atPath path: String) {
    do {
        let person = try createPerson(fromFile: path)
        print("Person created: \(person)")
        try deleteFile(atPath: path)
        print("File deleted: \(path)")
    } catch {
        print("Error processing file: \(error)")
    }
}

let jsonFilePath = "path/to/your/file.json"
let xmlFilePath = "path/to/your/file.xml"

processAndDeleteFile(atPath: jsonFilePath)
processAndDeleteFile(atPath: xmlFilePath)
