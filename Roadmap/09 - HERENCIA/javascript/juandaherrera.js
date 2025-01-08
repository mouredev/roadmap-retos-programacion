/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */

class Animal {
    constructor(name) {
        this.name = name;
    }

    makeSound() {
        throw new Error(
            "Método makeSound() debe ser implementado por subclases"
        );
    }
}

class Perro extends Animal {
    makeSound() {
        console.log("Guauuu");
    }
}

class Gato extends Animal {
    makeSound() {
        console.log("Miauu");
    }
}

const firulais = new Perro("Firulais");
const mishi = new Gato("Mishi");

firulais.makeSound(); // Guauuu
mishi.makeSound(); // Miauu

/*
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Simulación simple de generación de UUID en JavaScript
function generateUUID() {
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(
        /[xy]/g,
        function (c) {
            var r = (Math.random() * 16) | 0,
                v = c === "x" ? r : (r & 0x3) | 0x8;
            return v.toString(16);
        }
    );
}

class Employee {
    constructor(name, salary, leader = null) {
        this.id = generateUUID();
        this.name = name;
        this.salary = salary;
        this.leader = leader;
        this.directReports = [];

        if (leader) {
            leader.addDirectReport(this);
        }
    }

    addDirectReport(employee) {
        this.directReports.push(employee);
    }

    execute() {
        throw new Error("Método execute() debe ser implementado por subclases");
    }
}

class Manager extends Employee {
    execute() {
        return "Definiendo estrategía para que la compañía crezca...";
    }
}

class ProjectManager extends Employee {
    constructor(name, salary, project, leader = null) {
        super(name, salary, leader);
        this.project = project;
    }

    execute() {
        return `Liderando y supervisando el proyecto: ${this.project}`;
    }
}

class Developer extends Employee {
    constructor(name, salary, leader = null) {
        super(name, salary, leader);
        this.project = leader ? leader.project : "sin proyecto";
    }

    execute() {
        return `Desarrollando en el proyecto: ${this.project}`;
    }
}

const manager = new Manager("Juan David", 35000000);
const projectManager1 = new ProjectManager(
    "Esteban",
    13000000,
    "Incentivos",
    manager
);
const projectManager2 = new ProjectManager(
    "Santiago",
    12500000,
    "Algoritmo",
    manager
);

const developer1 = new Developer("Daniel", 8000000, projectManager1);
const developer2 = new Developer("Julian", 8500000, projectManager1);
const developer3 = new Developer("Felipe", 8000000, projectManager1);
const developer4 = new Developer("Duván", 9000000, projectManager2);
const developer5 = new Developer("Brais", 11000000, projectManager2);

// Función para imprimir la información de un empleado
function printEmployeeInfo(employee) {
    console.log(`ID: ${employee.id}`);
    console.log(`Nombre: ${employee.name}`);
    console.log(`Salario: ${employee.salary}`);
    console.log(`Líder: ${employee.leader ? employee.leader.name : "N/A"}`);
    console.log(
        "Reportes Directos: ",
        employee.directReports.map((e) => e.name).join(", ")
    );
    console.log(`Ejecutando: ${employee.execute()}`);
    console.log("----------------------");
}

printEmployeeInfo(manager);
printEmployeeInfo(projectManager1);
printEmployeeInfo(developer5);
