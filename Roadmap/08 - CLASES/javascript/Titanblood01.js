//Clases en JavaScript

//Sirven como una especie de plantilla para instanciar objetos, en base a lo que se
//defina dentro de estas, se usa para representar entidades del mundo real con distintos
//comportamientos, en javascript se los crea de la siguiente manera:

class Perro {
    #name;  //Atributo o propiedad privada
    constructor(name, color, race){ //Atributos que vaya a tener la clase
        this.#name = name;
        this.color = color;
        this.race = race;
    } //el metodo constructor o inicializador permite instanciar el objeto con estas caracteristicas

    get name() { //get para obtener el nombre privado
        return this.#name
    }

    set name(name) { //set para asignar un nuevo nombre privado
        this.#name = name
    }


    description(){ //metodos de la clase
        console.log('His color is:', this.color);
        console.log('His race is:', this.race);
    }

    bark() {
        console.log('wauf wauf!!')
    }
}


let dogy = new Perro('Doggy', 'Cafe', 'Golden')
console.log('Its name is:', dogy.name)
dogy.name = 'Moro'
console.log('Its new name is:', dogy.name)
dogy.description()
console.log('Moro Habla!!')
dogy.bark()


class Gun { //Existen metodos estaticos que permiten usarlos sin necesidad de instanciar una clase
    static shoot(){
        console.log('bam bam bam bam')
    }
}

Gun.shoot() // se llama a la clase y al metodo sin necesidad de instanciar un objeto


/* 
    DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
*/

//Pila
class stackClass {
    constructor() {
        this.elements = []
    }

    push(element){
        this.elements.push(element)
        console.log('Elemento añadido a la pila')
    }

    pop(){
        return this.elements.pop()
    }

    length(){
        return this.elements.length
    }

    get display(){
        console.log('Estos son los elementos de la pila')
        return this.elements
    }
}

let pila = new stackClass()

pila.push(4)
pila.push(5)
pila.push('Hola')
pila.push(4)
let longitud = pila.length()
console.log(`Esta es la longitud de la pila: ${longitud}`)
console.log(pila.display)
let removeElement = pila.pop()
console.log(`Sacando ${removeElement} de la pila`)
pila.length()
longitud = pila.length()
console.log(`Esta es la longitud de la pila: ${longitud}`)
console.log(pila.display)



//Cola
console.log('////////////////')
class queueClass {
    constructor() {
        this.queueElements = []
    }
    
    enqueue(element){
        this.queueElements.push(element)
        console.log('Elemento añadido a la cola')
    }
    
    dequeue(){
        return this.queueElements.shift()
    }
    
    length(){
        return this.queueElements.length
    }
    
    get display(){
        console.log('Estos son los elementos de la cola')
        return this.queueElements
    }
}
let cola = new queueClass()

cola.enqueue('A')
cola.enqueue('B')
cola.enqueue('Hola')
cola.enqueue('C')
let longitudCola = cola.length()
console.log(`Esta es la longitud de la cola: ${longitudCola}`)
console.log(cola.display)
let removeQueueElement = cola.dequeue()
console.log(`Sacando ${removeQueueElement} de la cola`)
cola.length()
longitudCola = cola.length()
console.log(`Esta es la longitud de la cola: ${longitudCola}`)
console.log(cola.display)