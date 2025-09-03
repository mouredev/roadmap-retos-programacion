/*
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.
*/

class Person {
    constructor(name, age){
        this.name = name
        this.age = age
    }

    imprimirDatos(){
        console.log(`Nombre: ${this.name}, Edad: ${this.age}`)
    }
}
// Instancia
const person = new Person ("Esteban", 38)
person.imprimirDatos()

// Modificar los atributos

person.name = "Carlos"
person.age = 22
person.imprimirDatos()

//  EXTRA - Pila y Cola

// Clase Pila (Stack - LIFO)

class Pila {
    constructor(data){
        this.data = data
    }

    addElementAction(element){
        return this.data.unshift(element)
    }

    deleteElementAction(){
        return this.data.shift()
    }

    numberElementAction(){
        return this.data.length
    }

    get addElement(){
        return this.addElementAction
    }

    get deleteElement(){
        return this.deleteElementAction
    }

    get numberElement(){
        return this.numberElementAction
    }
}

const nuevaPila = new Pila([])

console.log("Pila vacia", nuevaPila)
nuevaPila.addElement(1)
nuevaPila.addElement(2)
nuevaPila.addElement(3)
console.log('Nuevos elementos agregados', nuevaPila)
console.log('Cantidad de elementos', nuevaPila.numberElement())
nuevaPila.deleteElement()
console.log('Eliminado ultimo elemento', nuevaPila)

class Cola {
    constructor(data){
        this.data = data
    }

     addElementAction(element){
        return this.data.push(element)
    }

    deleteElementAction(){
        return this.data.shift()
    }

    numberElementAction(){
        return this.data.length
    }

    get addElement(){
        return this.addElementAction
    }

    get deleteElement(){
        return this.deleteElementAction
    }

    get numberElement(){
        return this.numberElementAction
    }

}

const nuevaCola = new Cola([])

console.log("Pila vacia", nuevaCola)
nuevaCola.addElement(1)
nuevaCola.addElement(2)
nuevaCola.addElement(3)
console.log('Nuevos elementos agregados', nuevaCola)
console.log('Cantidad de elementos', nuevaCola.numberElement())
nuevaCola.deleteElement()
console.log('Eliminado ultimo elemento', nuevaCola)
