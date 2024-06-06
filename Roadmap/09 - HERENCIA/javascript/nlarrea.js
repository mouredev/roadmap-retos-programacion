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


class Animal {
    constructor(name) {
        this.name = name;
    }

    sound() {
        console.log(null);
    }
}


class Dog extends Animal {
    sound() {
        console.log('Guau!');
    }
}


class Cat extends Animal {
    sound() {
        console.log('Miau!');
    }
}


const myDog = new Dog('Lagun');
myDog.sound();  // Guau

const myCat = new Cat('Kira');
myCat.sound();  // Miau


/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */


class Employee {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.employees = [];
    }

    add(employee) {
        this.employees.push(employee);
    }

    printEmployees() {
        console.log(`\n${this.name}'s employees:`);
        for (let employee of this.employees) {
            console.log(` - ${employee.name}`);
        }
    }
}


class Manager extends Employee {
    coordinate() {
        console.log(`\n${this.name} is coordinating all of the company's projects`);
    }
}


class ProjectManager extends Employee {
    constructor(id, name, project) {
        super(id, name);
        this.project = project;
    }

    coordinate() {
        console.log(`\n${this.name} is coordinating: ${this.project}`);
    }
}


class Programmer extends Employee {
    constructor(id, name, language) {
        super(id, name);
        this.language = language;
    }

    code() {
        console.log(`\n${this.name} is programming using ${this.language} language`);
    }

    add(employee) {
        console.log(`\nA programmer has no employees.\n${employee.name} won't be added.`);
    }
}


// Initializing employees
const myManager = new Manager(1, 'ManagerName');
const myPm1 = new ProjectManager(2, 'PM1', 'Project 1');
const myPm2 = new ProjectManager(3, 'PM2', 'Project 2');
const myProgrammer1 = new Programmer(4, 'P1', 'Python');
const myProgrammer2 = new Programmer(5, 'P2', 'React');
const myProgrammer3 = new Programmer(6, 'P3', 'JavaScript');
const myProgrammer4 = new Programmer(7, 'P4', 'SQL');

// Adding employees
myManager.add(myPm1);
myManager.add(myPm2);

myPm1.add(myProgrammer1);
myPm1.add(myProgrammer2);

myPm2.add(myProgrammer3);
myPm2.add(myProgrammer4);

myProgrammer1.add(myProgrammer4);  // won't work
/* prints:
A programmer has no employees.
P4 won't be added.
*/

// Tasks
myManager.coordinate();
// ManagerName is coordinating all of the company's projects
myPm1.coordinate();
// PM1 is coordinating: Project 1
myProgrammer1.code();
// P1 is programming using Python language
myProgrammer2.code();
// P2 is programming using React language
myPm1.printEmployees();
/* prints:
PM1's employees:
 - P1
 - P2
*/
myManager.printEmployees();
/* prints:
ManagerName's employees:
 - PM1
 - PM2
*/