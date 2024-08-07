// ** EJERCICIO

class Animal { // Definición de la superclase Animal
    constructor(nombre, edad) {
        this.nombre = nombre
        this.edad = edad
    }

    emitirSonido() {
        console.log(`${this.nombre} hace un sonido.`);
    }

    imprimirDatos() {
        console.log(`Nombre: ${this.nombre}, Edad: ${this.edad}`);
    }
}

class Perro extends Animal { // Definición de la subclase Perro que extiende de Animal
    constructor(nombre, edad, raza) {
        super(nombre, edad);
        this.raza = raza;
    }

    emitirSonido() {
        console.log(`${this.nombre} dice: ¡Guau! ¡Guau!`);
    }

    imprimirDatos() {
        super.imprimirDatos();
        console.log(`Raza: ${this.raza}`);
    }
}

class Gato extends Animal { // Definición de la subclase Gato que extiende de Animal
    constructor(nombre, edad, color) {
        super(nombre, edad);
        this.color = color;
    }

    emitirSonido() {
        console.log(`${this.nombre} dice: ¡Miau! ¡Miau!`);
    }

    imprimirDatos() {
        super.imprimirDatos();
        console.log(`Color: ${this.color}`);
    }
}

// Creación de instancias de las subclases
let miPerro = new Perro('Rex', 5, 'Labrador');
let miGato = new Gato('Mishi', 3, 'Negro');

// Modificación de atributos
miPerro.nombre = 'Max';
miGato.edad = 4;

// Uso de métodos
miPerro.emitirSonido(); // Max dice: ¡Guau! ¡Guau!
miGato.emitirSonido(); // Mishi dice: ¡Miau! ¡Miau!

// Imprimir datos
miPerro.imprimirDatos();
// Nombre: Max, Edad: 5
// Raza: Labrador

miGato.imprimirDatos();
// Nombre: Mishi, Edad: 4
// Color: Negro


// ** DIFICULTAD EXTRA ** -----------------------------------------------------------------------------------------------------------------------------------------------

class Empleado {
    constructor(id, nombre) {
        this.id = id
        this.nombre = nombre
    }

    printInfo() {
        console.log(`Nombre: ${this.nombre}, ID: ${this.id}`)
    }
}

class Gerente extends Empleado {
    constructor(id, nombre, empleadosACargo) {
        super(id, nombre)
        this.empleadosACargo = empleadosACargo
    }

    planear() {
        console.log(`${this.nombre} está planeando con los empleados: ${this.empleadosACargo}.`);
        console.log(`Plan de tarea número: ${Math.floor(Math.random() * 100)}`);
        // David está planeando con los empleados: Alícia, Pepe. Plan de tarea número: 56.
    }
}

class GerenteDeProyectos extends Empleado {
    constructor(id, nombre, empleadosACargo) {
        super(id, nombre);
        this.empleadosACargo = empleadosACargo;
    }

    gestionaProyectos() {
        console.log(`${this.nombre} está gestionando proyectos con los empleados: ${this.empleadosACargo}.`);
        console.log(`Proyecto número: ${Math.floor(Math.random() * 100)}`);
        // Eva está gestionando proyectos con los empleados: Carlos,Saray. Proyecto número 98.
    }
}

class Programador extends Empleado {
    constructor(id, nombre, empleadosACargo) {
        super(id, nombre);
        this.empleadosACargo = empleadosACargo;
    }

    programa() {
        console.log(`${this.nombre} está programando proyectos con los empleados: ${this.empleadosACargo}.`);
        console.log(`Proyecto número: ${Math.floor(Math.random() * 100)}`);
        // Juan está programando proyectos con los empleados: Quique,Pablo. Proyecto número: 88.
    }
}

// Datos de ejemplo
const empl1 = new Empleado(1, 'Alícia')
const empl2 = new Programador(2, 'Pepe')
const empl3 = new Programador(3, 'Carlos')
const empl4 = new Empleado(4, 'Saray')
const empl5 = new Empleado(5, 'Quique')
const empl6 = new Empleado(6, 'Pablo')

const gerente1 = new Gerente(7, 'David', [empl1.nombre, empl2.nombre]);
const gerenteDeProyectos = new GerenteDeProyectos(8, 'Eva', [empl3.nombre, empl4.nombre]);
const programador = new Programador(9, 'Juan', [empl5.nombre, empl6.nombre]);

// Uso de métodos

gerente1.planear();
gerenteDeProyectos.gestionaProyectos();
programador.programa();

