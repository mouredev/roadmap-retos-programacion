//: [Previous](@previous)

/*
 * 18miguelgalarza.swift Release #03 - swift
 * EJERCICIO: #03 ESTRUCTURAS DE DATOS
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


import Foundation
import SwiftUI
import PlaygroundSupport


var greeting = "Hello, playground"

//Estructuras soportadas por swift

struct structPersona {
/*
 Struct: cuando haces set en una variable o constante se asigna el valor original y no una referencia
 struct: Las estructuras no admiten la herencia en Swift. No puedes heredar propiedades o métodos de otra estructura ni de una clase.
 */
    var nombre: String
    var apellido: String
    var edad: Int
    var sexo:Character
}

class automovil {
/* Las clases pueden compartirse en todo el código
 */
    var color = "neutro"
    var precio = 0
    var numeroLlantas = 4

    init(color: String, precio: Int) {
        self.color = color
        self.precio = precio
    }
    
    init (){}
    
    func encender() -> Bool{return true}
    func apagar() -> Bool{return true}
    func acelerar() -> Bool{return true}
}

var objetoKia = automovil()

objetoKia.encender()

enum DiaDeLaSemana {
    case lunes
    case martes
    case miercoles
    case jueves
    case viernes
    case sabado
    case domingo
}

protocol ConductaCanina {
    func ladrar()
    func correr()
}


extension String {
    func hacerMayusculas() -> String {
        return self.uppercased()
    }
}


func intercambiar<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

//Tuplas
let coordenadas = (3.0, 4.0)

//Closures
let miCierre = { (nombre: String) -> String in
    return "Hola, \(nombre)!"
}

let saludo = miCierre("Mundo") // saludo = "Hola, Mundo!"

//Optionals
var nombre: String? = "Juan"


//guards Statements: Usado para salir temprano de una función si ciertas condiciones no se cumplen
let patinetas = ["skateboard", "longboards","penny"]

enum MiError: Error {
    case ErrorConocido
}

guard let patin = patinetas.last else {
    print("No existe patineta")
    throw MiError.ErrorConocido
}

//print("\u{2713} Ejemplo de guard para buscar : \(patin)")


/*
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

class Contacto {
    
    var nombre:String = ""
    var numeroContacto:String = ""  //trabeje con 6 para ejecutar pruebas más rápidas
    
    init(_ nombre: String, _ numeroContacto: String) {
        self.nombre = nombre
        self.numeroContacto = numeroContacto
    }
    
    init() {
    }

}

var listaDeContacto: [Contacto] = []  //variable global que hará la función de una Base de datos


func agenda(_ operacion:Character, _ contacto:Contacto ){
    
    // Crear un array de objetos Persona
    //CRUD
    switch operacion {
    case "C": //opción create
        listaDeContacto.append(contacto)
        print("\nSUCCESS:create, tu lista de contactos ahora tiene  \(listaDeContacto.count) contactos")
        
    case "R":  //opción read
       
        // Buscar en el arreglo de personas por el nombre
        let contactoConNumeroBuscado = listaDeContacto.filter { $0.numeroContacto == contacto.numeroContacto }

        if contactoConNumeroBuscado.isEmpty {
            print("\nERROR(CRUD): No se encontró ningún contacto con el número '\(contacto.numeroContacto )'.")
        } else {
            for contacto in contactoConNumeroBuscado {
                print("\nSUCCESS:read Se encontró a \(contacto.nombre) con número de contacto \(contacto.numeroContacto) ")
            }
        }
        
    case "U": //opción update
      
        // Buscar el primer contacto que tenga el numero que deseas actualizar
        if let contactoAActualizar = listaDeContacto.first(where: { $0.numeroContacto == contacto.numeroContacto  }) {
           
            // Modificar las propiedades del objeto encontrado, para el ejemplo será un dato en duro
            contactoAActualizar.numeroContacto = "080081"
            
            // Mostrar el objeto actualizado
            print("\nSUCCESS:update - Contacto actualizado: \(contactoAActualizar.nombre) tiene ahora un número de contacto \(contactoAActualizar.numeroContacto)")
        } else {
            print("\nERROR(CRUD): No se encontró ningún contacto con el nombre '\(contacto.numeroContacto)'.")
        }
               
    case "D": //opción delete
     
        //buscamos la posicion del contacto que vamos a eliminar
        if let index = listaDeContacto.firstIndex(where: { $0.numeroContacto == contacto.numeroContacto  }) {
           
            // Modificar las propiedades del objeto encontrado, para el ejemplo será un dato en duro
            listaDeContacto.remove(at: index)
            
            // Mostrar el objeto actualizado
            print("\nSUCCESS: delete - Contacto : \(contacto.nombre) - \(contacto.numeroContacto) eliminado")
        } else {
            print("\nERROR(CRUD): No se encontró ningún contacto con el número '\(contacto.numeroContacto)'.")
        }
  
        
    default: print("\nERROR(CRUD): no existe esta operación ****")
    }
    
    
    imprimirListaContacto()
    
}
func validaSoloNumeros(_ cadena: String) -> Bool {
//Función para validar que la cadena solo contenga números
    return !cadena.isEmpty && cadena.rangeOfCharacter(from: CharacterSet.decimalDigits.inverted) == nil
}

func imprimirListaContacto(){
    
    print("**** Cantidad de contactos actualizados: \(listaDeContacto.count) ****")
    for contacto in listaDeContacto {
        print("Nombre: \(contacto.nombre) - Número: \(contacto.numeroContacto) ")
    }
    
}


struct ContentView: View {
    @State private var nombre: String = ""
    @State private var numerocontacto: String = ""
    @State private var operacion: String = ""
    private var contacto = Contacto()
    
    var body: some View {
                
        VStack {
            Text("Agenda de Contactos")
                .font(.title)
                .fontWeight(.bold)
                .foregroundColor(.blue)
                .padding()
            
            TextField("Nombre", text: $nombre)
                .padding()
            
            TextField("Número de Contacto", text: $numerocontacto)
                .padding()
            
            TextField("operacion(C,R,U,D)", text: $operacion)
                .padding()
            
            Button("Aceptar") {
    
                
                if validaSoloNumeros(numerocontacto) && numerocontacto.count <= 6  && !operacion.isEmpty && !nombre.isEmpty && numerocontacto.count >= 0 {
 
                    //Se permite al parámetro "operacion" que acepte cualquier OTRO caracter con el fin de generar crash en el programa.
                    
                    agenda(Character(operacion),Contacto(nombre,numerocontacto))
        
                    
                }else{
                    
                    //validacionnes en consola
                    print("************* validaciones ***************")
                    print(nombre.isEmpty ? "Agregar nombre":"")
                    print(numerocontacto.count == 0 ? "Agregar número de contacto":"")
                    print(!validaSoloNumeros(numerocontacto) ? "Usar únicamente números en el contacto":"")
                    print(numerocontacto.count > 6  ? "El número de contacto sólo puede tener máximo 6 dígitos":"")
                    print(operacion.isEmpty  ? "Operador no puede ser nulo":"")
      
                    
                    
                }
                
            }// button Aceptar
            .padding()

                      
             Button("Cerrar") {
                          
                PlaygroundPage.current.finishExecution()
                          
            }
            .padding()

                      
        }
        .padding()
    }
}

PlaygroundPage.current.setLiveView(ContentView())
