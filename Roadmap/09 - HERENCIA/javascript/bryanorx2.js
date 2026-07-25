/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
    constructor(name){
        this.name = name
    }

    sound(){
        console.log("Sonido genérico")
    }
}

class Perro extends Animal{
    sound() {
        console.log(`${this.name} hace Guau`)
    }
}

class Gato extends Animal {
    sound() {
        console.log(`${this.name} hace Miau`)
    }
}

let newPerro = new Perro("Doki")
let newGato = new Gato("Felix")

newPerro.sound()
newGato.sound()

/* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Empleados {
    constructor (name, ID, listEmpleados = []){
        this.name = name
        this.ID = ID
        this.listEmpleados = listEmpleados
    }

    mostrarInfo() {
        console.log("Empleado")
    }

    empleadosACargo(){
        console.log(this.listEmpleados.map(e => e.name).join(", "))
    }
}

class Gerentes extends Empleados {
    constructor(name, ID, departamento, listEmpleados) {
        super(name, ID, listEmpleados)
        this.departamento = departamento
    }

    mostrarInfo() {
        console.log(`--Empleado: ${this.name} | ${this.ID}`)
        console.log(`Departamento: ${this.departamento}`)
    }

    empleadosACargo() {
        console.log(`${this.name} tiene a su cargo :${this.listEmpleados.map(e => e.name).join(", ")}`)
    }
}

class GerentesDeProyectos extends Empleados {
    constructor(name, ID, proyecto, listEmpleados) {
        super(name, ID, listEmpleados)
        this.proyecto = proyecto
    }

    mostrarInfo() {
        console.log(`--Empleado: ${this.name} | ${this.ID}`)
        console.log(`Proyecto actual: ${this.proyecto}`)
    }

    empleadosACargo() {
        console.log(`${this.name} tiene a su cargo :${this.listEmpleados.map(e => e.name).join(", ")}`)
    }
}

class Programadores extends Empleados {
    constructor (name, ID, lenguaje) {
        super(name, ID)
        this.lenguaje = lenguaje
    }

    mostrarInfo() {
        console.log(`--Empleado: ${this.name} | ${this.ID}`)
        console.log(`Lenguaje principal ${this.lenguaje}`)
    }
}

let newProgramadores1 = new Programadores("Luis", "3", "JavaScript")
let newProgramadores2 = new Programadores("María", "4", "Python")
let newGerenteProyecto = new GerentesDeProyectos("Carlos", "2", "App Mobile", [newProgramadores1, newProgramadores2])
let newGerente = new Gerentes("Ana", "1", "Tecnología", [newGerenteProyecto, newProgramadores1, newProgramadores2])


newGerente.mostrarInfo()
newGerenteProyecto.mostrarInfo()
newProgramadores1.mostrarInfo()
newProgramadores2.mostrarInfo()

newGerente.empleadosACargo()
newGerenteProyecto.empleadosACargo()