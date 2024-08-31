// herencia y polimorfismo

class Animal {
    constructor(name, age, gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
    sonido() {
        console.log(`${this.name} hace sonido`);
    }
};

// herencia
class Dog extends Animal {
    constructor(name, age, gender, raza) {
        super(name, age, gender);
        this.raza = raza;
    }
    getRaza() {
        console.log(`${this.name} es un perro de raza ${this.raza}`);
    }
    sonido() {
        console.log(`${this.raza} es un perro que ladra`);
    }
};

class Cat extends Animal {
    constructor(name, age, gender, raza) {
        super(name, age, gender);
        this.raza = raza;
    }
    getRaza() {
        console.log(`${this.name} es un gato de raza ${this.raza}`);
    }
    sonido() {
        console.log(`${this.raza} es un gata que maulla`);
    }
};

// polimorfismo
/**
 * El polimorfismo permite que los metodos se comporten de diferentes maneras
 * segun el contexto en el que ses llamen.
 */
class Ave extends Animal{
    sonido() {
        console.log("El ave canta");
    }
}

const animales = [
    new Animal("Pedro", 5, "masculino"),
    new Dog("Pedro", 3, "masculino", "Labrador"),
    new Cat("Gatito", 6, "masculino", "Siamese"),
    new Ave()
];

animales.forEach(animal => {
    animal.sonido();
});

/*
* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

class Empleados{
    constructor(id, nombre){
        this.id = id;
        this.nombre = nombre;
    }
    getNombre() {
        return this.nombre;
    }
};

class Gerente extends Empleados{
    constructor(id, nombre, proyectos){
        super(id, nombre);
        this.proyectos = proyectos;
    }
    getProyectos() {
        return this.proyectos;
    }
};

class GerenteDeProyecto extends Gerente{
    agregarProyecto(proyecto){
        this.proyectos.push(proyecto);
    }
};

class Programador extends Empleados{
    constructor(id, nombre, lenguajes){
        super(id, nombre);
        this.lenguajes = lenguajes;
    }
    getLenguajes() {
        return this.lenguajes;
    }
};

const gerentes = [
    new Gerente(1, "Pedro", ["Proyecto 1", "Proyecto 2"]),
    new GerenteDeProyecto(2, "Juan", ["Proyecto 3", "Proyecto 4"]),
    new Programador(3, "Carlos", ["Java", "Python", "C++"])
];

gerentes.forEach(gerente => {
    console.log(gerente.getNombre());
});

gerentes.forEach(gerente => {
    console.log(gerente.getProyectos());
});

gerentes.forEach(gerente => {
    gerente.agregarProyecto("Proyecto 5");
    console.log(gerente.getProyectos());
});
