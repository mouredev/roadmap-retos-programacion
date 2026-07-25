/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */

//
// Clases
//

// Definición de clase 
class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre
        this.edad = edad
    }

    presentar() {
        console.log(`Nombre: ${this.nombre}`)
        console.log(`Edad: ${this.edad}`)
    }
}

// Instanciar una clase 
const persona1 = new Persona('Gianfranco', 25)

// Mostrar atributos mediante metodo de la clase
persona1.presentar()

// Modificar atributos
persona1.nombre = 'Nataniel'
persona1.edad = 30

// Mostrar atributos modificados
persona1.presentar()

//
// EXTRA
//

class Pila {
    constructor(){
        this.items = []
    }

    push(element){
        this.items.push(element)
    }
    pop(){ 
        if (this.items.length === 0) return undefined
        return this.items.pop()
    }
    peek(){
        if (this.items.length === 0) return undefined
        return this.items.length -1
    }
    size(){
        return this.items.length
    }
    print(){
        if (this.items.length === 0) return undefined
        console.log(this.items)
    }
    clear(){
        this.items = []
    }
}
console.group('| PILAS |')
// Creación de una nueva pila
const miPila = new Pila()
// Agregar elementos
miPila.push('Documento 1')
miPila.push('Documento 2')
miPila.push('Documento 3')
// Ver el contenido de la pila
console.log("Contenido de la pila:")
miPila.print()  
// Ver el último elemento sin eliminarlo
console.log("Último elemento (peek):", miPila.peek())  
// Ver el tamaño de la pila
console.log("Tamaño de la pila:", miPila.size())  
// Eliminar el último elemento
console.log("Elemento eliminado (pop):", miPila.pop())  
// Ver el contenido después de hacer pop
console.log("Contenido de la pila después de pop:")
miPila.print()  
// Ver el tamaño de la pila después de pop
console.log("Tamaño de la pila después de pop:", miPila.size())  
// Vaciar completamente la pila
miPila.clear()
console.log("Contenido de la pila después de clear:")
miPila.print()
console.groupEnd()

class Cola {
    constructor(){
        this.cola = []
    }

    push(element){
        this.cola.push(element)
    }
    shift(){
        if (this.size() > 0){
            return this.cola.shift()
        } else {
            console.log('La cola esta vacia')
            return undefined
        }
    }
    peek(){
        if (this.size() > 0){
            return this.cola[0]
        } else {
            console.log('La cola esta vacia')
            return undefined
        }
    }
    size(){
        return this.cola.length
    }
    print(){
        console.log(this.cola)
    }
}

console.group('| COLAS |')
// Crear una nueva cola
const cola = new Cola()

// Inicializar
console.log("Inicializando cola:")
cola.print()  

// Agregar elementos a la cola
cola.push('Documento 1')
cola.push('Documento 2')
cola.push('Documento 3')

// Imprimir la cola con elementos
console.log("Después de agregar elementos:")
cola.print() 
// Ver el primer elemento sin eliminarlo
console.log("Primer elemento (peek):", cola.peek())  
// Ver el tamaño de la cola
console.log("Tamaño de la cola:", cola.size()) 
// Eliminar un elemento de la cola
console.log("Eliminando primer elemento:", cola.shift()) 
// Ver el primer elemento y tamaño después de la eliminación
console.log("Primer elemento después del shift:", cola.peek()) 
console.log("Tamaño después del shift:", cola.size())  
// Imprimir la cola después de una eliminación
console.log("Cola después de eliminar un elemento:")
cola.print()  
// Intentar eliminar todos los elementos
console.log("Eliminando el resto de los elementos:")
cola.shift()  
cola.shift()  
cola.shift()  
// Ver el tamaño de la cola después de eliminar todos los elementos
console.log("Tamaño final de la cola:", cola.size())  
// Ver el primer elemento cuando la cola está vacía
console.log("Intentando ver el primer elemento cuando la cola está vacía:", cola.peek())  
console.groupEnd()