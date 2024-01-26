import Foundation

 //* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 // * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

 //ARRAY
 var holasoyunarray: [Int] = []

//añadir
 holasoyunarray.append(3)
 holasoyunarray += [12]
  print("\(holasoyunarray)")
//modificar
holasoyunarray[0] = 15
holasoyunarray.insert(33, at: 1)
 print("\(holasoyunarray)")
 //eliminar
 let valoreliminado = holasoyunarray.remove(at: 1)
  print("\(holasoyunarray) se elimino el valor: \(valoreliminado)")


//SETS
var soyunset = Set<Character>()
soyunset.insert("z") //Se añade z
soyunset.insert("a") //Se añade a
print(soyunset)
soyunset.remove("z")
print(soyunset)
if soyunset.contains("a"){
 print("Cotiene a")
}
//soyunset = []
//los sets se pueden usar para actualizar informacion y juntar.
var setpar: Set = [2,4,6,8]
var setimpart: Set = [1,3,5,7,9]
var setrandom: Set = [2,8,5]
var nuevoset = setpar.union(setimpart).sorted()
print(nuevoset)
nuevoset = []
nuevoset = setpar.intersection(setimpart).sorted()
print(nuevoset)
nuevoset = setpar.subtracting(setrandom).sorted()
print(nuevoset)
nuevoset = []
nuevoset = setpar.symmetricDifference(setrandom).sorted()
print(nuevoset)

//diccionarios

var soyundiccionario: [Int : String] = [:]
soyundiccionario[16] = "David"
//añadir
soyundiccionario[1] = "Adrian"
//modificar
soyundiccionario[16] = "Daniela"
print(soyundiccionario)
//remover
soyundiccionario[16] = nil
print(soyundiccionario)
soyundiccionario[2] = "Carlos"
var valorremovido = soyundiccionario.removeValue(forKey: 1)
soyundiccionario[3] = "Pam"
soyundiccionario[5] = "Daniel"
//iterando
for (id, nombre) in soyundiccionario{ //tambien sirve dic.keys y dic.values
    print("\(id) : \(nombre)")
}

//ENUM

enum estadosdelagua : CaseIterable {
    case solido
    case liquido
    case gaseoso
}

for estados in estadosdelagua.allCases{
    print(estados)
}

enum amigos{
    case manolito(String,String,String)
    case adrian(String,String,String)
}

var amigosdemanolito = amigos.manolito("David", "Daniela", "Zoey")
amigosdemanolito = .adrian("Jose", "Salome", "Susan")

switch amigosdemanolito {
    case .manolito(let a, let b, let c):
    print("Amigos de manolito: \(a), \(b), \(c)")
    case .adrian(let d, let e, let f):
    print("Amigos de adrian: \(d), \(e), \(f)")
}

//Structures

struct soyunaestructura{
    var altura: Int = 0
    var Ancho: Int = 0
}


//class

class soyunaclase{
    var valores = soyunaestructura()
    var nombre: String 

    init(nombre: String){
        self.nombre = nombre
    }

    func obtenerarea(){
        let valorfinal = valores.Ancho * valores.altura
        print(valorfinal)
    }

}

let estructura = soyunaestructura()


let clase = soyunaclase(nombre:"Rectangulo")

clase.valores.altura = 15
clase.valores.Ancho = 30
clase.obtenerarea()


 /* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda(DONE), inserción(Agregar), actualización(MOStrar) y eliminación de contactos. (DONE)
 * - Cada contacto debe tener un nombre y un número de teléfono.(DONE)
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación(DONE)
 *   los datos necesarios para llevarla a cabo.(DONE)
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.(DONE)
 */

 class Contactos{
    var numero : Int
    var nombre : String

    init(numero: Int, nombre: String){
        self.numero = numero
        self.nombre = nombre
    }

    func mostrar(){
        print(nombre)
        print(numero)
    }


    

 }

 class AgendaContacto{

    var listaContacto = [Contactos]()

    func agregar(){

        var validacion  = false
        print("Ingrese nombre: ")
        var nombren = String(readLine()!)
        print("Ingrese numero: ")

        while(validacion == false){
        if let numeron = Int(readLine()!){
        
        if(numeron < 100000000 ){
            validacion = true
              var nuevoContacto = Contactos(numero: numeron, nombre: nombren)
                listaContacto.append(nuevoContacto)
        }
        else{ print("otro numero porfa")}
        } else {
            print("Entrada invalida")
        }
         }
        
      
    }

    func mostrars(){
        for contacto in listaContacto{
            contacto.mostrar()
            print("-------")
        }
    }

    func borrar(){
        print("Ingrese un nombre a eliminar")
        let nombre = String(readLine()!)
        var i: Int = 0
        
        for contacto in listaContacto{
            if(nombre == contacto.nombre){
                listaContacto.remove(at: i)
            }
            i += 1
        }
    }

    func buscar(){
        print("Ingrese un nombre a buscar")
        let nombre = String(readLine()!)
        var i: Int = 0
        
        for contacto in listaContacto{
            if(nombre == contacto.nombre){
                contacto.mostrar()
            }
            i += 1
        }
    }
 }

 let nuevocontacto = AgendaContacto()

 func menu(){

    var validacion: Bool = false
    while(validacion == false){
    print("AGENDA DE CONTACTOS:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto" )
    print("4. Mostrar Contactos")
    print("5. SAlir")
    var opcion = Int(readLine()!)!
    switch (opcion) {
        case 1:
        nuevocontacto.agregar()
        case 2:
        nuevocontacto.buscar()
        case 3:
        nuevocontacto.borrar()
        case 4:
        nuevocontacto.mostrars()
        case 5:
        validacion = true
        default:
        print("Ingrese otro valor :)")
    }
    }
 }


menu()