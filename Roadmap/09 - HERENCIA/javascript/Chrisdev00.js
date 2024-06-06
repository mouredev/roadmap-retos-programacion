//  * EJERCICIO:
//  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
//  * implemente una superclase Animal y un par de subclases Perro y Gato,
//  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
//  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
//  * Cada empleado tiene un identificador y un nombre.
//  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
//  * actividad, y almacenan los empleados a su cargo.


class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }
    sonido() {
        throw new Error("El método sonido debe ser implementado por las clases hijas.");
    }
}

class Perro extends Animal {
    constructor(nombre) {
        super(nombre);
    }

    sonido() {
        return "Guauu";
    }
}

class Gato extends Animal {
    constructor(nombre) {
        super(nombre);
    }

    sonido() {
        return "Miauu";
    }
}


const mi_perro = new Perro("Rufo");
const mi_gato = new Gato("Bigotes");

console.log(mi_perro.nombre);  
console.log(mi_perro.sonido()); 

console.log(mi_gato.nombre);    
console.log(mi_gato.sonido());

//  -----------------------------  EXTRA  -----------------------------------

class Empleado {
    constructor(identificador, nombre) {
        this.identificador = identificador;
        this.nombre = nombre;
    }

    toString() {
        return `ID: ${this.identificador}, Nombre: ${this.nombre}`;
    }
}

class Gerente extends Empleado {
    constructor(identificador, nombre, departamento) {
        super(identificador, nombre);
        this.departamento = departamento;
    }

    toString() {
        return `ID: ${this.identificador}, Nombre: ${this.nombre}, Departamento: ${this.departamento}`;
    }
}

class GerenteProyecto extends Gerente {
    constructor(identificador, nombre, departamento, proyectos) {
        super(identificador, nombre, departamento);
        this.proyectos = proyectos;
    }

    toString() {
        return `ID: ${this.identificador}, Nombre: ${this.nombre}, Departamento: ${this.departamento}, Proyectos: ${this.proyectos}`;
    }
}

class Programador extends Empleado {
    constructor(identificador, nombre, lenguaje) {
        super(identificador, nombre);
        this.lenguaje = lenguaje;
    }

    toString() {
        return `ID: ${this.identificador}, Nombre: ${this.nombre}, Lenguaje: ${this.lenguaje}`;
    }
}

const gerente_proyecto = new GerenteProyecto(1, "Juan", "Desarrollo", ["Proyecto A", "Proyecto B"]);
const programador = new Programador(2, "Pedro", "JavaScript");

console.log(gerente_proyecto.toString());
console.log(programador.toString());


