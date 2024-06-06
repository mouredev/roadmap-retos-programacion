import Foundation

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */



// Reemplaza 'kontroldev' con tu nombre de usuario real de GitHub si es necesario
let fileName = "kontroldev.txt"
let fileURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0].appendingPathComponent(fileName)

let content = """
Tu nombre
Edad
Lenguaje de programación favorito
"""

do {
    // Crear el archivo y escribir el contenido
    try content.write(to: fileURL, atomically: true, encoding: .utf8)
    
    // Leer e imprimir el contenido del archivo
    let fileContent = try String(contentsOf: fileURL, encoding: .utf8)
    print(fileContent)
    
    // Borrar el archivo
    try FileManager.default.removeItem(at: fileURL)
    print("El archivo \(fileName) ha sido borrado.")
} catch {
    print("Ha ocurrido un error: \(error)")
}


//MARK: - Extra

struct Product {
    let name: String
    var quantity: Int
    let price: Double
    
    func display() {
        print("Producto: \(name), Cantidad vendida: \(quantity), Precio: \(price)")
    }
}

// Función para leer productos del archivo
func readProductsFromFile() -> [Product] {
    var products = [Product]()
    let fileName = "ventas.txt"
    let fileURL = URL(fileURLWithPath: fileName)
    
    do {
        let content = try String(contentsOf: fileURL)
        let lines = content.components(separatedBy: .newlines)
        
        for line in lines {
            let components = line.components(separatedBy: ", ")
            if components.count == 3 {
                let name = components[0]
                let quantity = Int(components[1]) ?? 0
                let price = Double(components[2]) ?? 0.0
                let product = Product(name: name, quantity: quantity, price: price)
                products.append(product)
            }
        }
    } catch {
        print("Error al leer el archivo:", error.localizedDescription)
    }
    
    return products
}

// Función para escribir productos en el archivo
func writeProductsToFile(products: [Product]) {
    let fileName = "ventas.txt"
    let fileURL = URL(fileURLWithPath: fileName)
    var lines = [String]()
    
    for product in products {
        let line = "\(product.name), \(product.quantity), \(product.price)"
        lines.append(line)
    }
    
    let content = lines.joined(separator: "\n")
    
    do {
        try content.write(to: fileURL, atomically: true, encoding: .utf8)
    } catch {
        print("Error al escribir en el archivo:", error.localizedDescription)
    }
}

// Función para añadir un producto
func addProduct() -> Product {
    print("Ingrese el nombre del producto:")
    let name = readLine() ?? ""
    
    print("Ingrese la cantidad vendida:")
    let quantity = Int(readLine() ?? "0") ?? 0
    
    print("Ingrese el precio:")
    let price = Double(readLine() ?? "0.0") ?? 0.0
    
    return Product(name: name, quantity: quantity, price: price)
}

// Función para consultar todos los productos
func displayAllProducts(products: [Product]) {
    for product in products {
        product.display()
    }
}

// Función para calcular la venta total
func totalSale(products: [Product]) -> Double {
    var total: Double = 0.0
    for product in products {
        total += Double(product.quantity) * product.price
    }
    return total
}

// Función principal
func main() {
    var products = readProductsFromFile()
    
    var choice: Int = 0
    repeat {
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Consultar todos los productos")
        print("3. Calcular venta total")
        print("4. Salir")
        print("Ingrese su opción:")
        
        if let input = readLine(), let option = Int(input) {
            choice = option
            
            switch choice {
            case 1:
                let newProduct = addProduct()
                products.append(newProduct)
                writeProductsToFile(products: products)
                print("Producto añadido exitosamente.")
            case 2:
                displayAllProducts(products: products)
            case 3:
                let total = totalSale(products: products)
                print("Venta total: \(total)")
            case 4:
                // Borrar el archivo antes de salir
                let fileName = "ventas.txt"
                let fileURL = URL(fileURLWithPath: fileName)
                do {
                    try FileManager.default.removeItem(at: fileURL)
                    print("El archivo se ha borrado exitosamente.")
                } catch {
                    print("Error al borrar el archivo:", error.localizedDescription)
                }
            default:
                print("Opción no válida.")
            }
        } else {
            print("Entrada no válida. Inténtelo de nuevo.")
        }
    } while choice != 4
}

// Ejecutar el programa
main()
