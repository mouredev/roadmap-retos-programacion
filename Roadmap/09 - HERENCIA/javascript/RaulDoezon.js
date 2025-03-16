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

console.log("+++++++++ EJERCICIO +++++++++");
class Animal {
  constructor(animalName, animalSound) {
    this.animalName = animalName;
    this.animalSound = animalSound;
  }

  showAnimal() {
    console.log(`Soy un ${this.animalName}.`);
  }
}

class Perro extends Animal {
  constructor(animalName, animalSound) {
    super(animalName, animalSound);
  }

  showSound() {
    console.log(`El sonido que emito es un ${this.animalSound}.`);
  }
}

class Gato extends Animal {
  constructor(animalName, animalSound) {
    super(animalName, animalSound);
  }

  showSound() {
    console.log(`El sonido que emito es un ${this.animalSound}.`);
  }
}

let perro = new Perro("perro", "ladrido");
perro.showAnimal();
perro.showSound();
let gato = new Gato("gato", "maullido");
gato.showAnimal();
gato.showSound();

console.log("\n+++++++++ DIFICULTAD EXTRA +++++++++");
class Employees {
  constructor(employeeId, employeeName) {
    this.employeeId = employeeId;
    this.employeeName = employeeName;
    this.employeesInCharge = [];
  }

  add(employee) {
    this.employeesInCharge.push(employee);
  }

  showEmployees() {
    for (let index = 0; index < this.employeesInCharge.length; index++) {
      const theEmployee = this.employeesInCharge[index];
      console.log(theEmployee.employeeName);
    }
  }
}

class Manager extends Employees {
  constructor(employeeId, employeeName) {
    super(employeeId, employeeName);
  }

  manageGeneral() {
    console.log(`ID: ${this.employeeId}. ${this.employeeName} está a cargo de todos los proyectos activos.`);
  }
}

class ProjectManager extends Employees {
  constructor(employeeId, employeeName, areaName) {
    super(employeeId, employeeName);
    this.areaName = areaName;
  }

  manageArea() {
    console.log(`ID: ${this.employeeId}. ${this.employeeName} está manejando el área de ${this.areaName}.`);
  }
}

class Programmer extends Employees {
  constructor(employeeId, employeeName, projectName) {
    super(employeeId, employeeName, projectName);
    this.projectName = projectName;
  }

  project() {
    console.log(`ID: ${this.employeeId}. ${this.employeeName}  está desarrollando el proyecto de ${this.projectName}.`);
  }
}

let manager = new Manager("05", "Fabián");
let projectManager1 = new ProjectManager("33", "Juan", "Diseño de niveles");
let projectManager2 = new ProjectManager("19" ,"Ana", "Programación");
let programmer1 = new Programmer("03", "Raúl", "Metroid 6");
let programmer2 = new Programmer("20", "Luis", "Resident Evil: Code Veronica - Remake");

manager.manageGeneral();
manager.add(projectManager1);
manager.add(projectManager2);

projectManager1.manageArea();
projectManager1.add(programmer1);

projectManager2.manageArea();
projectManager2.add(programmer2);

programmer1.project();
programmer2.project();

console.log("\nEmpleados a cargo del Gerente:");
manager.showEmployees();
console.log("\nEmpleados a cargo del Gerente de Proyectos:");
projectManager1.showEmployees();
projectManager2.showEmployees();
