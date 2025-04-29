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

//
// HERENCIA 
//

// Superclase Animal
class Animal {
    constructor(nombre){
        this.nombre = nombre
    }

    emitirSonido(){
        console.log(this.nombre + ' hace un sonido')
    }
}

// Subclase Perro 
class Perro extends Animal {
    emitirSonido(){
        console.log(this.nombre + ' dice: guau')
    }
}

// Subclase Gato 
class Gato extends Animal {
    emitirSonido(){
        console.log(this.nombre + ' dice: miau')
    }
}

// Instancio las clases 
const perro = new Perro('Firulais')
const gato = new Gato('Michi')

// LLamo al metodo de la clase y se obversa la herencia del nombre que viene desde el padre Animal 
perro.emitirSonido() 
gato.emitirSonido()  

//
// EXTRA
//

class Empleado {
    constructor(nombre, id) {
        this.nombre = nombre
        this.id = id
        this.empleadosACargo = []
    }

    mostrarDatos() {
        console.log(`- Empleado: ${this.nombre} - ${this.id}`)
    }

    agregarEmpleadosACargo(empleado) {
        this.empleadosACargo.push(empleado)
    }

    listarEmpleadosACargo() {
        this.empleadosACargo.forEach(e => e.mostrarDatos())
    }
}

class Gerente extends Empleado {
    constructor(nombre, id, departamento) {
        super(nombre, id)
        this.departamento = departamento
    }

    mostrarDatos() {
        console.log(`- Gerente: ${this.nombre} - ${this.id} - ${this.departamento}`)
    }
}

class GerenteProyecto extends Empleado {
    constructor(nombre, id, proyecto) {
        super(nombre, id)
        this.proyecto = proyecto
    }

    cambiarProyecto(nuevoProyecto) {
        this.proyecto = nuevoProyecto
    }

    mostrarDatos() {
        console.log(`- Gerente de Proyecto: ${this.nombre} - ${this.id} - ${this.proyecto}`)
    }
}

class Programador extends Empleado {
    constructor(nombre, id) {
        super(nombre, id)
        this.lenguajes = []
    }

    agregarLenguaje(lenguaje) {
        this.lenguajes.push(lenguaje)
    }

    mostrarDatos() {
        console.log(`- Programador: ${this.nombre} - ${this.id} - Lenguajes: ${this.lenguajes.join(', ')}`)
    }
}

// Crear instancias
const gerente = new Gerente('Laura', 1, 'Tecnología')
const gerenteProyecto = new GerenteProyecto('Marcos', 2, 'WebApp 2025')
const programador1 = new Programador('Lucía', 3)
const programador2 = new Programador('Juan', 4)

// Asignar relaciones y propiedades
gerente.agregarEmpleadosACargo(gerenteProyecto)
gerenteProyecto.agregarEmpleadosACargo(programador1)
gerenteProyecto.agregarEmpleadosACargo(programador2)
programador1.agregarLenguaje('JavaScript')
programador1.agregarLenguaje('Python')
programador2.agregarLenguaje('Java')
gerenteProyecto.cambiarProyecto('MobileApp 2026')

// Mostrar datos
console.log('📋 Datos del Gerente:')
gerente.mostrarDatos()
console.log('👥 Empleados a cargo del Gerente:')
gerente.listarEmpleadosACargo()

console.log('📋 Datos del Gerente de Proyecto:')
gerenteProyecto.mostrarDatos()
console.log('👥 Empleados a cargo del Gerente de Proyecto:')
gerenteProyecto.listarEmpleadosACargo()

console.log('📋 Datos de los Programadores:')
programador1.mostrarDatos()
programador2.mostrarDatos()

