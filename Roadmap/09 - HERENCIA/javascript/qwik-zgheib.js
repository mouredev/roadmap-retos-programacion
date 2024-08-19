/* -- exercise */
class Animal {
  constructor(name) {
    this.name = name;
  }

  makeSound() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name);
  }

  makeSound() {
    console.log(`${this.name} says: Woof! Woof!`);
  }
}

class Cat extends Animal {
  constructor(name) {
    super(name);
  }

  makeSound() {
    console.log(`${this.name} says: Meow! Meow!`);
  }
}

function printAnimalSound(animal) {
  animal.makeSound();
}

let dog = new Dog("Firulais");
let cat = new Cat("Silvester");

printAnimalSound(dog);
printAnimalSound(cat);

/* -- extra chanllenge */
class Employee {
  constructor(id, name) {
    this.id = id;
    this.name = name;
  }

  printDetails() {
    console.log(`ID: ${this.id}, Name: ${this.name}`);
  }
}

class Manager extends Employee {
  constructor(id, name) {
    super(id, name);
    this.employeesInCharge = [];
  }

  addEmpleado(employee) {
    this.employeesInCharge.push(employee);
  }

  printDetails() {
    super.printDetails();
    console.log("Employees under this manager:");
    this.employeesInCharge.forEach((emp) => emp.printDetails());
  }
}

class ProjectManager extends Manager {
  constructor(id, name, project) {
    super(id, name);
    this.project = project;
  }

  printDetails() {
    super.printDetails();
    console.log(`Project: ${this.project}`);
  }
}

class Programmer extends Employee {
  constructor(id, name, language) {
    super(id, name);
    this.language = language;
  }

  printDetails() {
    super.printDetails();
    console.log(`Programming Language: ${this.language}`);
  }
}

let manager = new Manager(1, "Alice");
let projectManager = new ProjectManager(2, "Bob", "Project X");
let programmer1 = new Programmer(3, "Charlie", "JavaScript");
let programmer2 = new Programmer(4, "David", "Python");

manager.addEmpleado(programmer1);
projectManager.addEmpleado(programmer2);
manager.printDetails();
projectManager.printDetails();
