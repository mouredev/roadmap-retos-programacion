import Foundation


var path: String = ""
var name: String = ""
var age: String = ""
var programmingLenguage = ""
var productName = ""
var soldProduct = ""
var productPrice: Int = 0
var deleteFile: String = ""
var filePath: URL = URL(filePath: "")



print("Introduce la ruta y el nombre del fichero.")
if let fileName = readLine() {
    
    filePath = URL(filePath: fileName)
    path = fileName

    if FileManager.default.fileExists(atPath: path) {
        print("El fichero ya existe.")
    }

    do {
        try fileName.write(to: filePath, atomically: true, encoding: .utf8)
        print("Fichero creado.")
    } catch {
        print("Error al crear fichero: \(error)")
    }
}

print("\nIntroduce el nombre:")
if let nameInput = readLine() {
    
    name = nameInput

        if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe.")
    }
    if let file = FileHandle(forWritingAtPath: path) {
        do {
            try file.seekToEnd()
        }
        do {
            try file.write(contentsOf: "\(name)".data(using: .utf8)!)
            print("Nombre Introducido.")
        } catch {
            print("ERROR -> \(error.localizedDescription)")
        }
        do {
            try file.close()
        }
    }
}

print("\nIntroduce la edad:")
if let ageInput = readLine() {
    
    age = ageInput
    
    if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe.")
    }
    if let file = FileHandle(forWritingAtPath: path) {
        do {
            try file.seekToEnd()
        }
        do {
            try file.write(contentsOf: "\n\(age)".data(using: .utf8)!)
            print("Edad introducida.")
        } catch {
            print("ERROR -> \(error.localizedDescription)")
        }
        do {
            try file.close()
        }
    }
}

print("\nIntroduce el lenguaje de programación:")
if let lenguageInput = readLine() {
    
    programmingLenguage = lenguageInput

    if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe.")
    }
    if let file = FileHandle(forWritingAtPath: path) {
        do {
            try file.seekToEnd()
        }
        do {
            try file.write(contentsOf: "\n\(programmingLenguage)\n".data(using: .utf8)!)
            print("Lenguaje introducido.")
        } catch {
            print("ERROR -> \(error.localizedDescription)")
        }
        do {
            try file.close()
        }
    }
}

print("\nIntroduce el nombre fichero 1ue quieres mostras.")
if let showFile = readLine() {

    if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe.")
    }

    let process = Process()
    process.launchPath = "/bin/cat"
    process.arguments = [showFile]
    process.launch()
    process.waitUntilExit()
}

print("\nIntroduce el nombre del fichero que quieres borrar")
if let deleteFileInput = readLine() {
    
    deleteFile = deleteFileInput

    if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe")
}
    do {
    try FileManager.default.removeItem(atPath: deleteFile)
    print("Archivo eliminado exitosamente")
} catch {
    print("Error al eliminar el archivo: \(error)")
}
}




// DIFICULTAD EXTRA
print("\nDIFICULTAS EXTRA")

print("\nIntroduce la ruta y el nombre del fichero.")
createFile()

while true {
    
    showMenuOptions()

    if let input = readLine() {

        switch input {
            case "1":
                addProduct()
            case "2":
                showProductInfo()
            case "3":
                print("Actualizar producto.")
            case "4":
                print("Eliminar producto.")
            case "exit":
                print("Saliendo del programa.")
                exitProgram()
            default:
                print("Opción no valida")
        }
    }
    sleep(2)
}




func showMenuOptions() {

    print("\nElige una opción.\n")
    print("[1] - Añadir producto.")
    print("[2] - Mostrar procucto.")
    print("[3] - Actualizar producto.")
    print("[4] - Eliminar producto.")
    print("[exit] - Salir del programa")
}



func createFile() {

    if let fileName = readLine() {
    
        filePath = URL(filePath: fileName)
        path = fileName

        if FileManager.default.fileExists(atPath: path) {
            print("El fichero ya existe.")
        }

        do {
            try name.write(to: filePath, atomically: true, encoding: .utf8)
            print("Fichero creado.")
        } catch {
            print("Error al crear fichero: \(error)")
        }
    }
}



func addProduct() {

    print("\nIntroduce el nombre del prosucto.")
    if let productNameInput = readLine() {
    
        productName = productNameInput

        if !FileManager.default.fileExists(atPath: path) {
            print("El fichero no existe.")
        }
        if let file = FileHandle(forWritingAtPath: path) {
            do {
                try file.seekToEnd()
            } catch {
                print(error.localizedDescription)
            }
            do {
                try file.write(contentsOf: "Nobre del producto: \(productNameInput)".data(using: .utf8)!)
                print("Nombre del producnto introducido.")
            } catch {
                print("ERROR -> \(error.localizedDescription)")
            }
            do {
                try file.close()
            } catch {
                print(error.localizedDescription)
            }
        }
    }

    print("\nIntroduce cuantos productos venfidos.")
    if let soldProductInput = readLine() {
        soldProduct = soldProductInput

        if let file = FileHandle(forWritingAtPath: path) {
            do {
                try file.seekToEnd()
            } catch {
                print(error.localizedDescription)
            }
            do {
                try file.write(contentsOf: "\nProductos vendidos: \(soldProductInput)".data(using: .utf8)!)
                print("Cantidad de productos vendidos introducido.")
            } catch {
                print("ERROR -> \(error.localizedDescription)")
            }
            do {
                try file.close()
            } catch {
                print(error.localizedDescription)
            }
        }
        

    }

    print("\nIntroduce el precio de producto")
    if let productPriceInput = readLine(), let intProductPriceInput = Int(productPriceInput) {
        productPrice = intProductPriceInput

        if let file = FileHandle(forWritingAtPath: path) {
            do {
                try file.seekToEnd()
            } catch {
                print(error.localizedDescription)
            }
            do {
                try file.write(contentsOf: "\nPrecio del producto: \(productPrice)\n\n".data(using: .utf8)!)
                print("Precio del producto introducido.")
            } catch {
                print("ERROR -> \(error.localizedDescription)")
            }
            do {
                try file.close()
            } catch {
                print(error.localizedDescription)
            }
        }
    }
}



func showProductInfo() {

    print("\nIntroduce el articulo que quieras mostras.")
    if let showProductInput = readLine() {

        if !FileManager.default.fileExists(atPath: path) {
            print("El fichero no existe.")
        }

        let catProcess = Process()
        catProcess.launchPath = "/bin/cat"
        catProcess.arguments = [path]

        let grepProcess = Process()
        grepProcess.launchPath = "/usr/bin/grep"
        grepProcess.arguments = ["-A", "2", showProductInput]

        let pipe = Pipe()
        catProcess.standardOutput = pipe
        grepProcess.standardInput = pipe

        catProcess.launch()
        grepProcess.launch()
        catProcess.waitUntilExit()
        grepProcess.waitUntilExit()
    }
}



func exitProgram() {
    if !FileManager.default.fileExists(atPath: path) {
        print("El fichero no existe")
    }
    do {
        try FileManager.default.removeItem(atPath: path)
        print("Archivo eliminado exitosamente")
    } catch {
        print("Error al eliminar el archivo: \(error)")
    }
    exit(0)
}



