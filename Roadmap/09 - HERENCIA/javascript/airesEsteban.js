/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// EJERCICIO

class Animal {
    constructor(nombre) {
        this.nombre = nombre
    }

    sonido(){
        return `${this.nombre} hace un sonido`
    }
}

class Perro extends Animal {
    constructor(nombre){
    super(nombre)
    }

    sonido(){
        return `${this.nombre} ladra: Guau Guaau!`
    }
}

class Gato extends Animal {
    constructor(nombre){
        super(nombre)
    }

    sonido(){
        return `${this.nombre} maúlla: Miau Miaau!`
    }
}

function imprimirSonido(animal){
    return animal.sonido()
}

const miPerro = new Perro("Dino")
const miGato = new Gato("Démocles")

console.log(imprimirSonido(miPerro))
console.log(imprimirSonido(miGato))


// DIFICULTAD EXTRA

class Empleado {
    constructor(id, nombre){
        this.id = id
        this.nombre = nombre
    }

    mostrarInfo(){
        return `ID: ${this.id} , Nombre: ${this.nombre}`
    }
}

class Gerente extends Empleado{
    constructor(id, nombre){
        super(id, nombre)
        this.empleadosCargo = []
    }

    agregarEmpleadoACargo(empleado){
        this.empleadosCargo.push(empleado)
    }

    mostrarEmpleadosACargo(){
        if (this.empleadosCargo.length === 0){
            retunr `${this.nombre} no tiene empleados a cargo`
        }
        const listaEmpleados = this.empleadosCargo.map(emp => emp.mostrarInfo()).join("\n")
        return `Empleados a cargo de ${this.nombre}:\n${listaEmpleados}`
    }
}

class GerenteProyecto extends Empleado{
    constructor(id, nombre, proyecto){
        super(id,nombre)
        this.proyecto = proyecto
    }

    supervisarProyecto(){
        return `${this.nombre} esta supervisando el proyecto ${this.proyecto}`
    }
}

class Programador extends Empleado{
    constructor(id, nombre, lenguaje){
        super(id,nombre)
        this.lenguaje = lenguaje
    }

    programar(){
        return `${this.nombre} esta programando en ${this.lenguaje}`
    }
}

const gerente = new Gerente(1,"juan Peretz")
const gerenteProyecto = new GerenteProyecto(2, "Raul Lopex", "Sistemas de control")
const programador1 = new Programador(3, "Alvaro Navas", "Java")
const programador2 = new Programador(4, "Julian Lopez", "Javascript")
const programador3 = new Programador(5, "Agustina Romanucci", "Python")

gerente.agregarEmpleadoACargo(gerenteProyecto)
gerente.agregarEmpleadoACargo(programador1)

console.log(gerente.mostrarInfo())
console.log(gerente.mostrarEmpleadosACargo())
console.log(gerenteProyecto.supervisarProyecto())
console.log(programador1.programar())
console.log(programador2.programar())
console.log(programador3.programar())

