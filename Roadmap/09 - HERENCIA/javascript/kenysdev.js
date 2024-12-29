/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#9 HERENCIA Y POLIMORFISMO
---------------------------------------
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

// ________________________________________________________
// Clase base Animal
class Animal {
    constructor(name, sound) {
        this.name = name;
        this.sound = sound;
    }

    makeSound() {
        console.log(`${this.name} hace: ${this.sound}`);
    }
}

// Subclases
class Dog extends Animal {
    constructor(name) {
        super(name, "Woof");
    }
}

class Cat extends Animal {
    constructor(name) {
        super(name, "Meow");
    }
}

// Crear instancias y llamar a sus métodos
const dog = new Dog("Max");
const cat = new Cat("Milo");
dog.makeSound();
cat.makeSound();

// ________________________________________________________
// DIFICULTAD EXTRA

// Jerarquía de empleados
class Employee {
    static employees = [];

    constructor(identifier, tasks, staff = new Set()) {
        this.identifier = identifier;
        this.tasks = tasks;
        this.staff = staff;
    }

    add(names) {
        names.forEach(name => Employee.employees.push({ identifier: this.identifier, name }));
    }

    println() {
        Employee.employees
            .filter(employee => employee.identifier === this.identifier)
            .forEach(employee => console.log(`${employee.name} -> ${this.identifier}`));
    }

    functions() {
        console.log(`\nFunciones de ${this.identifier}`);
        this.tasks.forEach(task => console.log(task));
        console.log("--------------------");
    }

    subordinates() {
        console.log(`\nSubordinados de un ${this.identifier}`);
        Employee.employees
            .filter(employee => this.staff.has(employee.identifier))
            .forEach(employee => console.log(`${employee.name} -> ${employee.identifier}`));
        console.log("--------------------");
    }
}

class Manager extends Employee {
    constructor() {
        super("Gerente", ["- Supervisión", "- Toma de decisiones"], new Set(["Gerente de Proyecto", "Programador"]));
    }
}

class ProjectManager extends Employee {
    constructor() {
        super("Gerente de Proyecto", ["- Planificación", "- Coordinación de proyectos"], new Set(["Programador"]));
    }
}

class Programmer extends Employee {
    constructor() {
        super("Programador", ["- Desarrollo", "- Mantenimiento de código"], new Set());
    }
}

// __________________________
const manager = new Manager();
const projectManager = new ProjectManager();
const programmer = new Programmer();

manager.add(["Ben", "Dan"]);
projectManager.add(["Ray", "Joe"]);
programmer.add(["Leo", "Sam", "Zoe", "Ana"]);

manager.functions();
projectManager.functions();
programmer.functions();

manager.subordinates();
projectManager.subordinates();

manager.println();
projectManager.println();
