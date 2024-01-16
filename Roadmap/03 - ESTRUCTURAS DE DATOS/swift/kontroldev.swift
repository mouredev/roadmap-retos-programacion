import Foundation

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */


// Crear un array de enteros
var numeros = [1, 2, 3, 4, 5]

// Insertar un elemento al final del array
numeros.append(6)

// Borrar el primer elemento del array
numeros.removeFirst()

// Actualizar el valor del tercer elemento del array
numeros[2] = 7

// Ordenar el array de forma ascendente
numeros.sort()

// Crear un set de cadenas
var colores = Set(["rojo", "verde", "azul"])

// Insertar un elemento al set
colores.insert("amarillo")

// Borrar un elemento del set
colores.remove("rojo")

// Comprobar si el set contiene un elemento
colores.contains("verde")

// Crear un diccionario que asocia nombres con edades
var personas = ["Ana": 25, "Luis": 30, "Pedro": 28]

// Insertar un par clave-valor al diccionario
personas["Marta"] = 27

// Borrar un par clave-valor del diccionario
personas["Luis"] = nil

// Actualizar el valor de una clave del diccionario
personas["Pedro"] = 29

// Ordenar el diccionario por clave
let ordenado = personas.sorted(by: {$0.key < $1.key})

// Crear una tupla con dos elementos
var coordenada = (x: 10, y: 20)

// Acceder al primer elemento de la tupla
coordenada.x

// Actualizar el valor del segundo elemento de la tupla
coordenada.y = 15

// Crear un enum con casos asociados a valores
enum Estacion: String {
    case primavera = "Marzo"
    case verano = "Junio"
    case otono = "Septiembre"
    case invierno = "Diciembre"
}

// Crear una variable de tipo enum
var estacionActual = Estacion.primavera

// Acceder al valor asociado al caso del enum
estacionActual.rawValue

// Crear un struct con propiedades y métodos
struct Rectangulo {
    var ancho: Double
    var alto: Double
    
    // Método para calcular el área
    func area() -> Double {
        return ancho * alto
    }
    
    // Método para comparar si dos rectángulos son iguales
    func igualA(otro: Rectangulo) -> Bool {
        return self.ancho == otro.ancho && self.alto == otro.alto
    }
}

// Crear una instancia de struct
var rect1 = Rectangulo(ancho: 5, alto: 10)

// Acceder a una propiedad del struct
rect1.ancho

// Llamar a un método del struct
rect1.area()

// Crear otra instancia de struct
var rect2 = Rectangulo(ancho: 10, alto: 5)

// Comparar dos instancias de struct
rect1.igualA(otro: rect2)

// Crear una clase con propiedades, métodos e inicializador
class Circulo {
    var radio: Double
    var color: String
    
    // Inicializador de la clase
    init(radio: Double, color: String) {
        self.radio = radio
        self.color = color
    }
    
    // Método para calcular el perímetro
    func perimetro() -> Double {
        return 2 * 3.14 * radio
    }
    
    // Método para cambiar el color
    func cambiarColor(nuevoColor: String) {
        self.color = nuevoColor
    }
}

// Crear una instancia de clase
var circ1 = Circulo(radio: 3, color: "rojo")

// Acceder a una propiedad de la clase
circ1.radio

// Llamar a un método de la clase
circ1.perimetro()

// Cambiar el valor de una propiedad de la clase
circ1.cambiarColor(nuevoColor: "azul")



// DIFICULTAD EXTRA (opcional):
// Crear un diccionario vacío para almacenar los contactos
var agenda: [String: String] = [:]

// Crear una variable para controlar el bucle
var continuar = true

// Mostrar un mensaje de bienvenida
print("Bienvenido a la agenda de contactos")

// Iniciar el bucle
while continuar {
    // Mostrar las opciones disponibles
    print("Seleccione una opción:")
    print("1. Buscar un contacto")
    print("2. Insertar un contacto")
    print("3. Actualizar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")
    
    // Leer la opción del usuario
    let opcion = readLine() ?? ""
    
    // Ejecutar la opción elegida
    switch opcion {
    case "1":
        // Buscar un contacto
        print("Introduzca el nombre del contacto que desea buscar:")
        let nombre = readLine() ?? ""
        if let numero = agenda[nombre] {
            print("El número de teléfono de \(nombre) es \(numero)")
        } else {
            print("No se ha encontrado ningún contacto con ese nombre")
        }
    case "2":
        // Insertar un contacto
        print("Introduzca el nombre del contacto que desea insertar:")
        let nombre = readLine() ?? ""
        print("Introduzca el número de teléfono del contacto que desea insertar:")
        let numero = readLine() ?? ""
        // Validar que el número sea numérico y tenga menos de 11 dígitos
        if let _ = Int(numero), numero.count < 11 {
            agenda[nombre] = numero
            print("Se ha insertado el contacto \(nombre) con el número \(numero)")
        } else {
            print("El número de teléfono no es válido")
        }
    case "3":
        // Actualizar un contacto
        print("Introduzca el nombre del contacto que desea actualizar:")
        let nombre = readLine() ?? ""
        if agenda[nombre] != nil {
            print("Introduzca el nuevo número de teléfono del contacto:")
            let numero = readLine() ?? ""
            // Validar que el número sea numérico y tenga menos de 11 dígitos
            if let _ = Int(numero), numero.count < 11 {
                agenda[nombre] = numero
                print("Se ha actualizado el contacto \(nombre) con el número \(numero)")
            } else {
                print("El número de teléfono no es válido")
            }
        } else {
            print("No se ha encontrado ningún contacto con ese nombre")
        }
    case "4":
        // Eliminar un contacto
        print("Introduzca el nombre del contacto que desea eliminar:")
        let nombre = readLine() ?? ""
        if agenda[nombre] != nil {
            agenda[nombre] = nil
            print("Se ha eliminado el contacto \(nombre)")
        } else {
            print("No se ha encontrado ningún contacto con ese nombre")
        }
    case "5":
        // Salir
        print("Gracias por usar la agenda de contactos")
        continuar = false
    default:
        // Opción inválida
        print("La opción introducida no es válida")
    }
}
