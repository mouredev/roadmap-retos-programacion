import Foundation
print("PILA")
// Pila
var stackItems: [Any] = []

// Metodo push: añade nuevos elementos al final de la pila.
stackItems.append("Pepe")
stackItems.append("Alicia")
stackItems.append("Raul")
stackItems.append("Marta")

print("Metodo peak")
// Metodo peak: devuelve el ultimo elemento de la pila.
if let firstOut = stackItems.last {
    print(firstOut)
}

print("Metodo pop")
// Metodo pop: devuelve el ultimo elemento de la pila y lo elimina.
if let stackLastIn = stackItems.popLast() {
    print(stackLastIn)

}


print("\nCOLA")
// Cola
var queueItems: [Any] = []

// Metodo enqueue: añade nuevo elemento al final de la cola.
queueItems.append("Cupertino")
queueItems.append("Madrid")
queueItems.append("Bogota")
queueItems.append("Tokio")

print("Metodo from")
// Metodo from: devuelve el primer elemento de la cola.
if let firstOut = queueItems.first {
    print(firstOut)
}

print("Metodo dequeue")
// Metodo dequeue: devuelve el primer elementos de la cola y lo elimina.
let queueFirstIn = queueItems.removeFirst()
print(queueFirstIn)




// Dificultad extra.
print("\n\nDIFICULTAD EXTRA")

// Simulador de navegación de paginas web.
print("\nSimulador de Navegación de Paginas Web")

// Array donde se almacenas las paginas web.
var webSites: [String] = []
// variable que evalua si termina el programa.
var stackProgramContinue = true
// Variable para contar el indice del array.
var stepper: Int = 1

// Nuestra el menu de las opciones que se pueden realizar
showStackExerciseMenu()

// Loop que se ejecuta hasta que stackProgramContinue es false (cuando introduces "exit").
while stackProgramContinue {

    // Crea la variable input con el texto que introducca el usuario.
    if let input = readLine() {

        // Evalua la variable input y ejecuta el codigo dependiendo de lo que introducca el usuario.
        switch input {

            // Si se introduce una pagina web sw imprime la wev introducida.
            case inputWebSite(web: input):
                webSites.append(input)
                if let last = webSites.last {
                    print(last)
                }

            // Se mueve al indice anterios del array y imprime el valor.  
            case "atras":
                if webSites.isEmpty {
                    print("No hay paginas")
                    continue
                }
                stepper += 1
                if stepper == webSites.count + 1 {
                    stepper = webSites.count
                    print("No Hay Mas Paginas")
                } else {
                    print(webSites[webSites.count - stepper])
                }

            // Se muevo al indice siguiente del array y imprime el calor.
            case "adelante":
                if webSites.isEmpty {
                    print("No Hay Paginas")
                    continue
                }
                stepper -= 1
                if stepper == 0 {
                    stepper = 1
                    print("No Hay Mas Paginas")
                } else {
                    print(webSites[webSites.count - stepper])
                }

            // Salir del programa.
            case "exit":
                stackProgramContinue = false

            // Si la opcion no es valida imprime "Opcion no Valida".
            default:
                print("Opcion no Valida")
        }
    }
}

// funcion que evalua si una pagina es .com y tiene www. para que sea una direccion correcta y devuelva la pagina si es correcto.
func inputWebSite(web name: String) -> String {
    // Variable para almacenar los tres primeros caracteres de la pagina.
    var firstCharacters = ""
    // Variable para almacenar los tres ultimos caracteres de la pagina.
    var lastCharacters: String = ""
    var lastCharactersReversed: String = ""
    // Variable para almacenar los tres ultimos caracteres de la pagina, pero del reves.

    // Loop que almacena los tres primeros caracteres en la variable firstCharacters
    for character in name {
        firstCharacters.append(character)
        if firstCharacters.count == 4 {
            break
        }
    }

    // Loop que almacena los tres ultimos caracteres de la pagina del reves.
    for character: Character in name.reversed() {
        lastCharactersReversed.append(character)
        if lastCharactersReversed.count == 4 {
            break
        }
    }

    // Loop que almacena los tres ultimos caracteres de la pagina en orden no del reves
    for character: Character in lastCharactersReversed.reversed() {
        lastCharacters.append(character)
    }

    // Evalua si la pagina empieza por "www" y termina ".com" para devolver el nombre de la pagina
    if firstCharacters == "www." && lastCharacters == ".com" {
        return name
    }

    // Devuelve "Web no Valida" si la pagina no empieza por "www" y terminal por ".com"
    return "Web no Valida"
}

// Funcion que imprime las opciones del menu.
func showStackExerciseMenu() {
    print("\nIntroduce Una Opción.\n")
    print("[Pagina Web .com] - Navega a Una Nueva Pagina.")
    print("[atras] - Navega a la Pagina Anterior")
    print("[adelante] - Navega a la Siguiente Pagina.")
    print("[exit] - Salir Del Programa.\n")
}



// Simulador de impresora
print("\nSimulador de Impresora")

import Foundation

// Array que almacena todos los ficheros de la cola.
var documents: [String] = []
// Variable que hace salir del programa cuando es false
var queueProgramContinue: Bool = true

showQueueMenu()

// Loop que se ejecuta hasta que queueProgramContinue es false (cuando introduces "exit").
while queueProgramContinue {
    
    // Crea la variable input con el texto que introducca el usuario.
    if let input = readLine() {

        // Evalua la variable input y ejecuta el codigo dependiendo de lo que introducca el usuario.
        switch input {

            // Si se introduce un nuevo fichero se añade a la cola.
            case inputDocument(document: input):
                documents.append(input)

            // Imrime el primer fichero de la cola y lo elimina de la cola.
            case "imprimir":
                if documents.isEmpty {
                    print("No Hay Documentos en la Cola")
                } else {
                    if let first = documents.first {
                    print(first)
                }
                documents.removeFirst()
                }

            // Sale del programa.
            case "exit":
                queueProgramContinue = false

            default:
                print("Opción No Valida")
        }
    }
}

// funcion que evalua si un tenga la extensión .pdf para que sea un fichero valido y devuelva el fichero si es valido.
func inputDocument(document name: String) -> String {
    // Evalua si el fichero tiene estensión .pdf y si lo tiene devuelve el fichro
    if name.contains(".pdf") {
        return name
    }
    
    // Devuelve "Documento no Valido" si no tiene extension .pdf.
    return "Documento no Valido"
}

// Funcion que imprime las opciones del menu.
func showQueueMenu() {
    print("\nIngresa Una Opción\n")
    print("[Fichro .pdf] - Añade un Fichero a la Cola de Impresión")
    print("[imprimir] - Imprime el Primer Fichero de la Cola")
    print("[exit] - Salir del Programa\n")
}