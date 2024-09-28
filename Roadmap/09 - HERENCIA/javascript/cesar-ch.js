/*
    #09 HERENCIA Y POLIMORFISMO
*/

class Animal {
    constructor(name) {
        this.name = name
    }

    sound() {
        console.log(`${this.name} makes a sound.`)
    }
}

class Dog extends Animal {
    constructor(name) {
        super(name)
    }
    sound() {
        console.log(`Guau, guau!`)
    }
}

class Cat extends Animal {
    constructor(name) {
        super(name)
    }
    sound() {
        console.log(`Miau, miau!`)
    }
}

const dog = new Dog('Firulais')
console.log(dog.name)
dog.sound()
const cat = new Cat('Garfield')
console.log(cat.name)
cat.sound()

/* 
    DIFICULTAD EXTRA 
*/

class Empleado {
    constructor(id, nombre) {
        this.id = id
        this.nombre = nombre
        this.empleadosACargo = []
    }
    agregarEmpleado(empleado) {
        this.empleadosACargo.push(empleado)
    }

    imprimirEmpleados() {
        console.log(this.empleadosACargo.map(empleado => empleado.nombre));
    }
}

class Gerente extends Empleado {
    constructor(id, nombre) {
        super(id, nombre)
    }
    actividad() {
        console.log('Gerente')
    }
}

class GerenteProyecto extends Empleado {
    constructor(id, nombre) {
        super(id, nombre)
    }
    actividad() {
        console.log('Gerente de Proyecto')
    }
}

class Programador extends Empleado {
    constructor(id, nombre) {
        super(id, nombre)
    }
    actividad() {
        console.log('Programador')
    }
}

const gerente = new Gerente(1, 'Juan')
const gerenteProyecto = new GerenteProyecto(2, 'Pedro')
const gerenteProyecto2 = new GerenteProyecto(3, 'Luis')
const programador = new Programador(4, 'Maria')
const programador2 = new Programador(5, 'Ana')
const programador3 = new Programador(6, 'Jorge')
const programador4 = new Programador(7, 'Carlos')

gerente.agregarEmpleado(gerenteProyecto)
gerente.agregarEmpleado(gerenteProyecto2)

gerenteProyecto.agregarEmpleado(programador)
gerenteProyecto.agregarEmpleado(programador2)
gerenteProyecto2.agregarEmpleado(programador3)
gerenteProyecto2.agregarEmpleado(programador4)

gerente.imprimirEmpleados()
gerenteProyecto.imprimirEmpleados()
gerenteProyecto2.imprimirEmpleados()
programador.imprimirEmpleados()

gerente.actividad()
gerenteProyecto.actividad()
programador.actividad()