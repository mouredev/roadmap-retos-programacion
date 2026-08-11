/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

// Clase padre
/* class Animal {
    constructor(nombre) {
        this.nombre = nombre
    }

    sonido(){
        console.log(`${this.nombre} hace un sonido. `)
    }
}

// Clase hija
class Perro extends Animal {
    sonido() {
        console.log(`${this.nombre} ladra.`)
    }

}

// Clase hija
class Gato extends Animal {
    sonido() {
        console.log(`${this.nombre} maulla`)
    }
}

function imprimirSonido(animal) {
    animal.sonido()
}

const perro1 = new Perro("Naima")
imprimirSonido(perro1)

const gato1 = new Gato("Thyrion")
imprimirSonido(gato1)

const pato1 = new Animal("Adolfo")
imprimirSonido(pato1) */

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Clase Padre
class Empleado {
    constructor(id, nombre) {
        this.id = id
        this.nombre = nombre
        this.empleados = []
    }

    añadirEmpleado(empleado) {
        this.empleados.push(empleado)
    }

    imprimirEmpleados() {
        this.empleados.forEach(empleado => {
            console.log(`ID: ${empleado.id}, Nombre: ${empleado.nombre}`)
        });
    }
}

// Clase Hija
class Gerente extends Empleado {
    constructor(id, nombre) {
        super(id, nombre)
    }

    imprimirEmpleados() {
        console.log(`${this.nombre}, supervisa a los gerentes de proyectos.`)
        console.log("y tiene bajo su supervisión a los gerentes de proyectos: ")
        super.imprimirEmpleados()
    }
}

// Clase Hija
class GerenteProyecto extends Empleado {
    constructor(id, nombre, proyecto) {
        super(id, nombre)
        this.proyecto = proyecto
    }
    imprimirEmpleados() {
        console.log(`${this.nombre}, supervisa el proyecto: ${this.proyecto};.
Y tiene bajo su supervisión al programador: `)
        super.imprimirEmpleados()
    }

}

// Clase Hija
class Programador extends Empleado {
    constructor(id, nombre, lenguaje) {
        super(id, nombre)
        this.lenguaje = lenguaje
    }
    imprimirEmpleados() {
        console.log(`${this.nombre}, desarrolla el código del proyecto.`)
    }

    code() {
        console.log(`${this.nombre} programa en ${this.lenguaje}`)
    }

    añadirEmpleado(empleado) {
        console.log(`Los programadores no tienen empleados a su cargo, ${empleado.nombre} no se añadirá.`)
    }
}

const gerente1 = new Gerente(1, "Paco")
const gerenteProyecto1 = new GerenteProyecto(2, "Manolo", "Proyecto 1")
const gerenteProyecto2 = new GerenteProyecto(3, "Pedro", "proyecto 2")
const programador1 = new Programador(4, "Antonio", "JavaScript")
const programador2 = new Programador(5, "Edelmiro", "kotlin")
const programador3 = new Programador(6, "Andelino", "Java")
const empleado1 = new Empleado(7,"Eufrasio")

gerente1.añadirEmpleado(gerenteProyecto1)
gerente1.añadirEmpleado(gerenteProyecto2)

gerenteProyecto1.añadirEmpleado(programador1)
gerenteProyecto2.añadirEmpleado(programador2)



gerente1.imprimirEmpleados()
gerenteProyecto1.imprimirEmpleados()
gerenteProyecto2.imprimirEmpleados()
programador1.imprimirEmpleados()
programador2.imprimirEmpleados()
empleado1.imprimirEmpleados()
programador1.code()
programador2.code()

programador1.añadirEmpleado(programador2)
