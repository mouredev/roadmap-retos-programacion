import Foundation


// PROGRAMA QUE CREA UN JSON Y UN XML
print("\nPROGRAMA QUE CREA UN JSON Y UN XML.")



// Diccionario donde estaran los datos solicitados al usuario contenidos.
var dictionary: [String:Any] = [:]
var lenguagesArray: [String] = []
var jsonPath: String = ""
var xmlPath: String = ""
var jsonURL: URL = URL(filePath: "")
var xmlURL: URL = URL(filePath: "")


// Pide el nombre al usuario.
print("\nIntroduce tu nombre:")
if let name = readLine() {
    dictionary["name"] = name
}

// Pide la edad al usuario.
print("\nIntroduce tu edad:")
if let age: String = readLine(), let ageInt: Int = Int(age) {
    dictionary["age"] = ageInt
}

// Pide la fecha de nacimiento al usuario.
print("\nIntroduce tu fecha de nacimiento, (dd/mm/yyyy):")
if let birthdate: String = readLine() {
    dictionary["birthdate"] = birthdate
}

// Pide los lenguajes de programación al usuario.
print("\nIntroduce tus lenguajes de programación:")
// El usuario puede ingresar lenguajes hasta que ponga la palabre exit.
while true {
    // Comprueba que el usuario pone exit para salir del bucle y guardar el array en el campo "lenguages"
    if let lenguage = readLine() {
        if lenguage == "exit" {
        dictionary["lenguages"] = lenguagesArray
        break
        }
        lenguagesArray.append(lenguage)
    }
    print("Para terminar introduce \"exit\"")
}

// Pide al usuario el nombre y ruta del fichero JSON.
print("\nIntroduce la ruta y el nombre del fichero JSON.")
if let fileName = readLine() {

    jsonPath = fileName
    jsonURL = URL(filePath: fileName)

    if FileManager.default.fileExists(atPath: fileName) {
        print("El fichero ya existe.")
    
    } else {

        do {
            let jsonData = try JSONSerialization.data(withJSONObject: dictionary, options: .prettyPrinted)
    
            // Escribir el JSON en el fichero.
            try jsonData.write(to: jsonURL)
    
            print("Archivo JSON creado en: \(jsonURL)")
        } catch {
            print("Error al crear el archivo JSON: \(error.localizedDescription)")
        }
    }  
}




// Crea un string con la cabecera del xml.
var xmlString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
xmlString.append("<data>\n")

// Itera en las claves y valores del diccionario.
for (key, value) in dictionary {
    // Pone como etiqueta xml la clave del dicionario.
    xmlString.append("\t<\(key)>")

    // Detecta si alguno de los valores del diccionario es un array de string.
    if let arrayValue = value as? [String] {
        // Si algun valor es un array itera en el.
        for item in arrayValue {
            // Crea el tag item añadiendo cada valor del array.
            xmlString.append("\n\t\t<item>\(item)</item>")
        }
    } else {
        // Si no hay un array añade la clave como tag xml.
        xmlString.append("\(value)")
    }
    // Pone como valor de la tag el valor de cada clave del dicionario.
    xmlString.append("</\(key)>\n")
}
// Cierra la cabecera del xml.
xmlString.append("</data>")

// Pide al usuario la ruta y el nombre del xml.
print("\nIntroduce la ruta y el nombre del fichero XML:")
if let fileName = readLine() {

    xmlPath = fileName
    xmlURL = URL(filePath: fileName)

    if FileManager.default.fileExists(atPath: fileName) {
        print("El fichero ya existe.")
    
    } else {
        do {
            // Escribe el xml en un fichero.
            try xmlString.write(to: xmlURL, atomically: true, encoding: .utf8)
        
            print("Archivo XML creado en: \(xmlURL)")
        } catch {
            print("Error al crear el archivo XML: \(error.localizedDescription)")
        }
    }
}

sleep(4)




// Muestra por consola el fichero JSON.
print("\nFichero JSON.")
var processToShowJsonFile = Process()
processToShowJsonFile.launchPath = "/bin/cat"
processToShowJsonFile.arguments = [jsonPath]
processToShowJsonFile.launch()
processToShowJsonFile.waitUntilExit()




// Muestra por consola el fichero XML.
print("\n\nFichero XML.")
var processToShowXmlFile = Process()
processToShowXmlFile.launchPath = "/bin/cat"
processToShowXmlFile.arguments = [xmlPath]
processToShowXmlFile.launch()
processToShowXmlFile.waitUntilExit()

sleep(4)




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.")




// Clase que almacenara los datos del fichero JSON.
class JsonFile: Decodable {
    var name: String
    var age: Int
    var birthdate: String
    var lenguages: [String]
}

// Obtiene el Path del fichero JSON.
jsonPath = FileManager.default.currentDirectoryPath + "/data.json"

// Si Si el fihero tiene datos los almacena el la variable data.
if let data = FileManager.default.contents(atPath: jsonPath) {
    do {
        // Decodifica los datos del JSON en la clase JsonFile.
        let jsonFile = try JSONDecoder().decode(JsonFile.self, from: data)
        
        print("\n\nDatos del fichero JSON.")
        // Imprime los datos de la clase JsonFile.
        print("Nombre: \(jsonFile.name)")
        print("Edad: \(jsonFile.age)")
        print("Fecha de nacimiento: \(jsonFile.birthdate)")
        print("Lenguajes: \(jsonFile.lenguages)")
    } catch {
        print(error.localizedDescription)
    }
} else {
    print("No se puedo leer el fichero JSON.")
}




// Clase que almacenara los datos del fichero XML.
class XmlFile {
    var name: String = ""
    var age: Int = 0
    var birthdate: String = ""
    var languages: [String] = []
}

// Obtiene el Path del fichero XML.
xmlPath = FileManager.default.currentDirectoryPath + "/data.xml"

// Si el fichero tiene datos los almacene en la bariable data.
if let data = FileManager.default.contents(atPath: xmlPath) {
    // Crea un objeto de la clase XMLParser() y le pasa los datos del fichero.
    let parser = XMLParser(data: data)
    // Objeto de la clase XmlHandler.
    let xmlHandler = XmlHandler()
    // Usa la clase XmlHandler como delegado del objeto parser.
    parser.delegate = xmlHandler

    // Si el parser encuentra datos.
    if parser.parse() {
        // Decodifica los datos del fichero en la en la clase XmlFile().
        let xmlFile = xmlHandler.xmlFile
        
        print("\nDatos del fichero XML.")
        // Imprime los datos de la clase XmlFile.
        print("Nombre: \(xmlFile.name)")
        print("Edad: \(xmlFile.age)")
        print("Fecha de nacimiento: \(xmlFile.birthdate)")
        print("Languajes: \(xmlFile.languages)")
    } else {
        print("Error parsing XML.")
    }
} else {
    print("No se pudo leer el archivo XML.")
}

// Crea la clase que se usara como delegado en el parser.
class XmlHandler: NSObject, XMLParserDelegate {
    var xmlFile = XmlFile()
    var currentElement = ""
    var currentLanguage = ""

    func parser(_ parser: XMLParser, didStartElement elementName: String, namespaceURI: String?, qualifiedName qName: String?, attributes attributeDict: [String : String] = [:]) {
        currentElement = elementName
        if elementName == "lenguages" {
            xmlFile.languages = []
        }
    }

    func parser(_ parser: XMLParser, foundCharacters string: String) {
        let trimmedString = string.trimmingCharacters(in: .whitespacesAndNewlines)
        if !trimmedString.isEmpty {
            switch currentElement {
            case "name":
                xmlFile.name = trimmedString
            case "age":
                if let age = Int(trimmedString) {
                    xmlFile.age = age
                }
            case "birthdate":
                xmlFile.birthdate = trimmedString
            case "item":
                currentLanguage = trimmedString
            default:
                break
            }
        }
    }

    func parser(_ parser: XMLParser, didEndElement elementName: String, namespaceURI: String?, qualifiedName qName: String?) {
        if elementName == "item" {
            xmlFile.languages.append(currentLanguage)
        }
    }
}

sleep(4)




// Elimina el fichero JSON.
do {
    try FileManager.default.removeItem(at: jsonURL)
    print("\n\nFichero JSON borado.")
} catch {
    print(error.localizedDescription)
}




// Elimina el fichero XML.
do {
    try FileManager.default.removeItem(at: xmlURL)
    print("\nFichero XML borrado.")
} catch {
    print(error.localizedDescription)
}
