/*
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.

DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
*/
// 🔥 Superclase Animal
class Animal {
    constructor(nombre) { this.nombre = nombre }

    // Método genérico para emitir sonido
    emitirSonido() {
        return "Este animal no tiene un sonido definido."
    }
}

// 🔥 Subclase Perro
class Perro extends Animal {
    constructor(nombre) {
        super(nombre); // Llama al constructor de la superclase
    }

    // Sobrescribe el método emitirSonido
    emitirSonido() {
        return "Guau guau!";
    }
}

// 🔥 Subclase Gato
class Gato extends Animal {
    constructor(nombre) {
        super(nombre); // Llama al constructor de la superclase
    }

    // Sobrescribe el método emitirSonido
    emitirSonido() {
        return "Miau miau!";
    }
}

// 🔥 Función para imprimir el sonido de un animal
function imprimirSonido(animal) {
    console.log(`${animal.nombre} dice: ${animal.emitirSonido()}`);
}


const miPerro = new Perro("Camilo");
const miGato = new Gato("Reina");

imprimirSonido(miPerro); // Camilo dice: Guau guau!
imprimirSonido(miGato);  // Reina dice: Miau miau!


// 🔥 Extra

// Clase base Empleado
class Empleado {
    constructor(id, nombre) {
        this.id = id;
        this.nombre = nombre;
    }

    mostrarInfo() {
        return `ID: ${this.id}, Nombre: ${this.nombre}`;
    }
}

// Subclase Gerente
class Gerente extends Empleado {
    constructor(id, nombre) {
        super(id, nombre);
        this.empleadosACargo = [];
    }

    // Añadir empleado a su cargo
    agregarEmpleado(empleado) {
        this.empleadosACargo.push(empleado);
    }

    // Mostrar empleados a su cargo
    mostrarEmpleadosACargo() {
        if (this.empleadosACargo.length === 0) {
            return `${this.nombre} no tiene empleados a su cargo.`;
        }
        const listaEmpleados = this.empleadosACargo.map(emp => emp.mostrarInfo()).join("\n");
        return `Empleados a cargo de ${this.nombre}:\n${listaEmpleados}`;
    }
}

// Subclase Gerente de Proyectos
class GerenteProyecto extends Empleado {
    constructor(id, nombre, proyecto) {
        super(id, nombre);
        this.proyecto = proyecto;
    }

    // Supervisar proyectos
    supervisarProyecto() {
        return `${this.nombre} está supervisando el proyecto "${this.proyecto}".`;
    }
}

// Subclase Programador
class Programador extends Empleado {
    constructor(id, nombre, lenguaje) {
        super(id, nombre);
        this.lenguaje = lenguaje;
    }

    // Programar
    programar() {
        return `${this.nombre} está programando en ${this.lenguaje}.`;
    }
}


const gerente = new Gerente(1, "Juan Pérez");
const gerenteProyecto = new GerenteProyecto(2, "Ana López", "Sistema de Gestión");
const programador1 = new Programador(3, "Carlos Ramírez", "JavaScript");
const programador2 = new Programador(4, "María González", "Python");

gerente.agregarEmpleado(gerenteProyecto);
gerente.agregarEmpleado(programador1);
gerente.agregarEmpleado(programador2);

console.log(gerente.mostrarInfo());
console.log(gerente.mostrarEmpleadosACargo());
console.log(gerenteProyecto.supervisarProyecto());
console.log(programador1.programar());
console.log(programador2.programar());