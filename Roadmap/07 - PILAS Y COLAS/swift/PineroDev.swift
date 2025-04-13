/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */


import Foundation


// Struct con comportamiento de una pilas (stacks - LIFO)

struct Stack<T> { // Utilizamos <T> para que se le pueda pasar cualquier tipo de valor
    
    private var elementos: [T] = []
    
    // Usamos mutating para decirle a Swift que no cree una copia y
    // modifique el valor de la estructura ya que la struct es de tipo
    // valor y de modo original hace una copia de la struct al modificarse
    mutating func push(elemento: T){
        elementos.append(elemento) //Agrega el valor al final
    }
    
    mutating func pop() -> T? {
        return elementos.popLast() //Quitamos el ultimo
    }
    
    func peek() -> T? {
        return elementos.last // Leemos el ultimo valor
    }
    
    func isEmpty() -> Bool {
        return elementos.isEmpty // Comprobamnos si la pila esta vacia
    }
    
    func size() -> Int {
        return elementos.count // contamos los elementos de la pila
    }
}

// Struct con comportamiento de una colas (queue - FIFO)

struct Queue<T> {
    
    private var elementos: [T] = []
    
    mutating func enqueue(elemento: T){ //Agrega el valor al final
        elementos.append(elemento)
    }
    
    mutating func dequeue() -> T? { //Quitamos el primero
        return elementos.removeFirst()
    }
    
    func peek() -> T? {
        return elementos.first // Leemos el primer valor
    }
    
    func isEmpty() -> Bool {
        return elementos.isEmpty // Comprobamnos si la pila esta vacia
    }
    
    func size() -> Int {
        return elementos.count // contamos los elementos de la pila
    }
        
}


func webNavigation() {
    
    var posicion: Int = -1
    var cadena:[String] = []
    print("Introduce una url o atras, adelante o salir")
    while true {
        if let urlString = readLine() {
            
            if urlString == "atras"{
                if cadena.isEmpty {
                    print("No hay ninguna web de momento")
                }else if cadena.count == 1 || posicion == 0{
                    print("Estas en la primera pagina")
                }else{
                    posicion -= 1
                    print(cadena[posicion])
                }
                
            }else if urlString == "adelante"{
                if cadena.isEmpty {
                    print("No hay ninguna web de momento")
                }else if posicion == cadena.indices.last{
                    print("Estas en la ultima pagina")
                }else{
                    posicion += 1
                    print(cadena[posicion])
                }
                
            }else if urlString == "salir"{
                print(cadena)
                break
                
            }else{
                cadena.append(urlString)
                posicion += 1
            }
        }
    }
}

//webNavigation()

//----------------------------------------------------------


func impresora() {
    //var posicion: Int = -1
    var documentos:[String] = []
    print("    Introduce el nombre del documento         ")
    print(" o imprimir para imprimir el primer documento ")
    print("            salir para salir                  ")
        
    while true {
        if let inText = readLine(){
            
            if inText == "imprimir"{
                guard let name = documentos.first else {
                        print("Sin documentos en la cola")
                        return
                    }

                    print("Imprimiendo documento \(name) ...")
                    sleep(5)
                    print("Documento \(name) impreso")

                    documentos.removeFirst()
            }else if inText == "salir"{
                break
            }else{
                documentos.append(inText)
            }
        }
    }
}

impresora()
