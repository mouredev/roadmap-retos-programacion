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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

import Foundation

// Arrays - El orden de los elementos es importante
// pero no es importante que se repitan

//Ejemplos de creación
var arraryString = ["Pepe", "Juan", "Luis"]
var arraOfString = Array(arrayLiteral: "Pepe", "Juan", "Luis")

//Contador
var arrayString2 = ["Pepe", "Juan", "Luis"]
print("The arrayString2 contain \(arrayString2.count) elements")
print(arrayString2 [0])

//Agregador e inserción
arrayString2.append("Maria")
arrayString2 += ["Ana", "Susana"]
print(arrayString2)
arrayString2.insert("Juanito", at: 0)
print(arrayString2)

//Ordenanción
arrayString2.sort()
print(arrayString2)

//Actualizacion
arrayString2[6] = "Mercedes"
print(arrayString2)

//Borrado
arrayString2.remove(at: 0)
arrayString2.removeFirst()
print(arrayString2)

arrayString2.removeAll()
if arrayString2.isEmpty{
    print("El arrayString2 esta vacio")
}else{
    print("El arrayString2  contiene elementos")
}


// Set - El orden de los elementos no es importante
// pero si que no se repitan

// Ejemplo de creación
var setString = Set(["Pepe", "Juan", "Luis"])
var setOfString = Set(arrayLiteral: "Pepe", "Juan", "Luis")

print("The setString contain \(setString.count) elements")
print(setString)

// Inserción
setString.insert("Maria")
print(setString)

// Comprobación
print(setString.contains("Pepe"))

// Borrado
setString.remove("Juan")
print(setString)
if setString.isEmpty{
    print("El setString esta vacio")
}else{
    print("El setString contiene elementos")
}


// Diccionarios - Cada valor tiene asociado una clave
// tampoco estan ordenados

// Ejemplos de creación
var dictionary: [String: String] = [:]

var dictionaryWithValues: [String: String] = ["Nombre": "Pedro",
                                              "Apellido": "Garcia",
                                              "Ciudad": "Murcia"]
print(dictionaryWithValues)
print("The dictionaryWithValues contain \(dictionaryWithValues.count) elements")

// Agregación
dictionaryWithValues["Edad"] = "25"
print(dictionaryWithValues)

// Comprobación
print(dictionaryWithValues.keys.contains("Nombre"))

// Actualizacion
dictionaryWithValues.updateValue( "30", forKey: "Edad")
print(dictionaryWithValues)

// Borrado
dictionaryWithValues.removeValue(forKey: "Ciudad")
dictionaryWithValues["Edad"] = nil
print(dictionaryWithValues)
dictionaryWithValues.removeAll()
if dictionaryWithValues.isEmpty{
    print("El dictionaryWithValues esta vacio")
}else{
    print("El dictionaryWithValues contiene elementos")
}

//----------------------------------------------
//----------------------------------------------
//----------------------------------------------
// Ejercicio DIFICULTAD EXTRA

func agenda(){
    print("---------------------------")
    print("|  Bienvenido a la agenda |")
    print("|                         |")
    print("|      By PineroDev       |")
    print("---------------------------")
    print("Elige una opción:")
    print("1 - Buscar")
    print("2 - Crear")
    print("3 - Actualizar")
    print("4 - Borrar")
    print("5 - Mostrar listado")
    print("6 - Salir")
    let opcion = readLine()
        
        switch opcion {
        case "1":
            buscarContacto()
        case "2":
            agregarContacto()
        case "3":
            actualizarContacto()
        case "4":
            borrarContacto()
        case "5":
            mostrarListado()
        case "6":
            print("Gracias por usar la agenda")
            sleep(5)
            break
        default:
            print("Opcion incorrecta")
            sleep(5)
            agenda()
        }
    }

var diccionarioAgenda: [String: Int] = [:]

func buscarContacto() {
    var nombre: String = ""
    print("Introduzca el nombre del contacto a buscar:")
    if let nombreIngresado = readLine(){
        nombre = nombreIngresado
    }
    if diccionarioAgenda.isEmpty{
        print("Agregue un contacto primero")
    }else if let datos = diccionarioAgenda[nombre]{
        print("Nombre: \(nombre) - Telefono:\(datos)" )
    }else {
        print("El contacto \(nombre) no se encuentra en la agenda")
    }
    sleep(5)
    agenda()
}

func agregarContacto() {
    var nombre: String = ""
    var numero: Int = 0
    
    print("Agregar Contacto")
    print("Ingrese nombre:")
    
    if let nombreIngresado = readLine(){
        nombre = nombreIngresado
    }
    
    print("Ingrese telefono:")
    if let numeroIngresado = readLine(){
        if let numeroIngresado = Int(numeroIngresado){
            if numeroIngresado < 99999999999 && numeroIngresado > 1 {
                numero = numeroIngresado
            }else {
                print("El numero de telefono debe ser de menos de 12 digitos")
                agenda()
            }
        }else {
            print( "Debe ingresar un numero valido")
            agenda()
            }
    }
    diccionarioAgenda[nombre] = numero
    print("Contacto agragado exitosamente")
    sleep(3)
    agenda( )
}

func actualizarContacto() {
    var nombre: String = ""
    var nombreActual: String = ""
    var numero: Int = 0
    
    print("Introduzca el nombre del contacto a actualizar:")
    if let nombreIngresado = readLine(){
        nombreActual = nombreIngresado
    }
    if diccionarioAgenda.keys.contains(nombreActual){
        print( "Ingrese el nuevo nombre:")
        if let nombreActualizado = readLine(){
            nombre = nombreActualizado
            print("Ingrese telefono:")
            if let numeroIngresado = readLine(){
                if let numeroIngresado = Int(numeroIngresado){
                    if numeroIngresado < 99999999999 && numeroIngresado > 1 {
                        numero = numeroIngresado
                    }else {
                        print("El numero de telefono debe ser de menos de 12 digitos")
                    }
                }else {
                    print( "Debe ingresar un numero valido")
                }
            }
        }
    }else{
        print("El contacto \(nombreActual) no existe")
    }
    diccionarioAgenda[nombreActual] = nil
    diccionarioAgenda[nombre] = numero
    //diccionarioAgenda.updateValue( numero, forKey: nombreActual )
    print("Contacto actualizado con exito")
    sleep(5)
    agenda()
}

func borrarContacto() {
    var nombre: String = ""
    print("Introduzca el nombre del contacto a borrar:")
    if let nombreIngresado = readLine(){
            nombre = nombreIngresado
    }
    if diccionarioAgenda.keys.contains(nombre) {
        diccionarioAgenda[nombre] = nil
        print( "El Contacto \(nombre) ha sido borrado con exito")
    }else {
        print("El contacto \(nombre) no existe")
    }
    sleep(5)
    agenda()
}
    
func mostrarListado() {
    print(diccionarioAgenda)
    sleep(10)
    agenda()
    }


agenda( )
        







