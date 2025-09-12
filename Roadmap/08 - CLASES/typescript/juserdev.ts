// # #08 CLASES
// > #### Dificultad: Fácil | Publicación: 19/02/24 | Corrección: 26/02/24

// ## Ejercicio


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


//Estructura basica de Clases

namespace clase8 {
    class Persona { // Porpiedad
        nombre: string;

        constructor(nombre: string){
            this.nombre = nombre //Inicializacion
        }

        saludar(): string{ //metodo - esto es como una funcion
            return `¡Hola! soy ${this.nombre}` 
        }
    }

    //crear una instancia
    const Persona1 = new Persona("Sebastian")
    console.log(Persona1.saludar()) //¡Hola! soy Sebastian


    //Modificadores de acceso

    class Banco {
        public nombreBanco: string
        private balanceBanco: number

        constructor(Nombre: string, balance: number){
            this.nombreBanco = Nombre
            this.balanceBanco = balance
        }

        public consultarBalance(): string{
            return `el balance es $${this.balanceBanco}`
        }

        private actualizarBalance(cantidad: number): void {
            this.balanceBanco += cantidad
        }
    }

    const banco1 = new Banco("Banco Central", 1000)
    console.log(banco1.consultarBalance())
    
    //banco1.actualizarBalance(500) //la propidad actualizarBalance es privada

    //Metodos y propieaddes estaticas

    class Matematicas {
        static PI: number = 3.1416

        static calcularCircunferencia(radio: number): number{
            return 2 * this.PI * radio
        }
    }

    console.log(Matematicas.PI)
    console.log(Matematicas.calcularCircunferencia(5))

    // Herencia

    class Animal {
        nombre: string

        constructor(nombre: string) {
            this.nombre = nombre
        }

        emitirSonido(): string {
            return `Hace un sonido generico`
        }
    }

    class Perro extends Animal {
        emitirSonido(): string {
            return `¡Guau!`
        }
    }

    class Pollito extends Animal{
        emitirSonido(): string {
            return `Pio pio pio!!`
        }
    }

    const gato = new Animal("Michi")
    console.log(gato.nombre)
    console.log(gato.emitirSonido())

    const perro = new Perro("Firulais")
    console.log(perro.nombre)
    console.log(perro.emitirSonido())

    const pollito = new Pollito("Theo")
    console.log(pollito.nombre)
    console.log(pollito.emitirSonido())

    // Clases abstractas

    abstract class Figura {
        abstract calcularArea(): number

        description(): string {
            return `Soy una figura geometria`
        }
    }

    class Cuadrado extends Figura {
        lado: number

        constructor(lado: number){
            super()
            this.lado = lado
        }

        calcularArea(): number {
            return this.lado ** 2
        }
    }


    const cuadrado = new Cuadrado(4)
    console.log(cuadrado.description())
    console.log(cuadrado.calcularArea())


    // Interface vs Calses

    interface Vehiculo {
        marca: string
        modelo: string
        conducir(): void
    }

    class Coche implements Vehiculo {
        marca: string
        modelo: string

        constructor(marca: string, modelo: string){
            this.marca = marca
            this.modelo = modelo
        }

        conducir(): void {
            console.log(`Conduiendo un ${this.marca} modelo ${this.modelo}`)
            return
        }
    }

    const coche = new Coche("toyota", "corola")
    coche.conducir()

    // Ejemplo practico mas largo

    class Personas {
        nombre: string
        edad: number
        ocupacion: string

        constructor(nombre: string, edad: number, ocupacion: string) {
            this.nombre = nombre
            this.edad = edad
            this.ocupacion = ocupacion
        }

        saludar(): string{
            return `¡Hola! soy ${this.nombre}`
        }

        presentarse(): string {
            return `Me llamo ${this.nombre}, tengo ${this.edad} y soy ${this.ocupacion}.`
        }

        cumplirAnios(): void {
            this.edad++
        }
    }

    const personas1 = new Personas("Ana", 25, "desarrolladora Web")
    const personas2 = new Personas("Sebastian", 33, "desarrollador web")


    console.log(personas1.saludar())
    console.log(personas1.presentarse())

    console.log(personas2.nombre)
    console.log(personas2.edad)
    console.log(personas2.ocupacion)
    console.log(personas2.presentarse())

    personas2.cumplirAnios()
    console.log(personas2.presentarse())



    //! SOLUCION DEL PROBLEMA

    class Programer {
        name: string
        sername?: string
        age: number
        lenguajes: string[]

        constructor(name: string, age: number, lenguajes: string[], sername?: string){
            this.name = name
            this.sername = sername
            this.age = age
            this.lenguajes = lenguajes
        }

        print(): string{
            return `nombre: ${this.name}${this.sername ? ", Apellido: " + this.sername : ""}, edad: ${this.age}, lenguajes: ${this.lenguajes}`
        }

    }

    const sebastian = new Programer("Sebastian", 30, ["JavaScipt", "TypeScript"])
    const juan = new Programer("juan", 33, ["JavaScipt", "TypeScript"], "rocha")

    console.log(sebastian.print())
    console.log(juan.print())

    sebastian.age = 33 //modifique la edad

    console.log(sebastian.print()) //edad modificada

    //! DIFICULTAD EXTRA

    class Stack {
        stack: any[]

        constructor(){
            this.stack = []
        }

        push(item){
            this.stack.push(item)
            return this.stack
        }

        pop(){
            if (this.count() === 0) {
                return "no hay nada que borrar"
            }
            return this.stack.pop()
        }

        count(){
            return this.stack.length
        }

        print(){
            if (this.count() > 0) {
                return this.stack.slice().reverse()
            }
            return "El Stack esta vacio"
        }
    }

    const stack = new Stack()
    
    stack.push("A")
    stack.push("B")
    stack.push("C")
    console.log(stack.count())
    console.log(stack.print())
    console.log(stack.pop())
    console.log(stack.count())
    console.log(stack.print())
    console.log(stack.pop())
    console.log(stack.count())
    console.log(stack.print())
    console.log(stack.pop())
    console.log(stack.count())
    console.log(stack.print())


    class Queue {
        queue: any[]

        constructor(){
            this.queue = []
        }

        push(item){
            this.queue.push(item)
            return this.queue
        }

        shift(){
            if (this.count() === 0) {
                return "no hay nada que borrar"
            }
            return this.queue.shift()
        }

        count(){
            return this.queue.length
        }

        print(){
            if (this.count() > 0) {
                return this.queue.slice()
            }
            return "El queue esta vacio"
        }
    }

    const myQueue = new Queue()
    
    myQueue.push("A")
    myQueue.push("B")
    myQueue.push("C")
    console.log(myQueue.count())
    console.log(myQueue.print())
    console.log(myQueue.shift())
    console.log(myQueue.count())
    console.log(myQueue.print())
    console.log(myQueue.shift())
    console.log(myQueue.count())
    console.log(myQueue.print())
    console.log(myQueue.shift())
    console.log(myQueue.count())
    console.log(myQueue.print())
    console.log(myQueue.shift())
    console.log(myQueue.count())
    console.log(myQueue.print())

}