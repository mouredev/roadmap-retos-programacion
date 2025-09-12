/* -- exercise */
class Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  makeSound(): void {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  constructor(name: string) {
    super(name);
  }

  makeSound(): void {
    console.log(`${this.name} says: Woof! Woof!`);
  }
}

class Cat extends Animal {
  constructor(name: string) {
    super(name);
  }

  makeSound(): void {
    console.log(`${this.name} says: Meow! Meow!`);
  }
}

function printAnimalSound(animal: Animal): void {
  animal.makeSound();
}

let dog = new Dog("Firulais");
let cat = new Cat("Silvester");

printAnimalSound(dog);
printAnimalSound(cat);

/* -- extra challenge */
class Employee {
  id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  printDetails(): void {
    console.log(`ID: ${this.id}, Name: ${this.name}`);
  }
}

class Manager extends Employee {
  employeesInCharge: Employee[];

  constructor(id: number, name: string) {
    super(id, name);
    this.employeesInCharge = [];
  }

  addEmployee(employee: Employee): void {
    this.employeesInCharge.push(employee);
  }

  printDetails(): void {
    super.printDetails();
    console.log("Employees under this manager:");
    this.employeesInCharge.forEach((emp) => emp.printDetails());
  }
}

class ProjectManager extends Manager {
  project: string;

  constructor(id: number, name: string, project: string) {
    super(id, name);
    this.project = project;
  }

  printDetails(): void {
    super.printDetails();
    console.log(`Project: ${this.project}`);
  }
}

class Programmer extends Employee {
  language: string;

  constructor(id: number, name: string, language: string) {
    super(id, name);
    this.language = language;
  }

  printDetails(): void {
    super.printDetails();
    console.log(`Programming Language: ${this.language}`);
  }
}

let manager = new Manager(1, "Alice");
let projectManager = new ProjectManager(2, "Bob", "Project X");
let programmer1 = new Programmer(3, "Charlie", "JavaScript");
let programmer2 = new Programmer(4, "David", "Python");

manager.addEmployee(programmer1);
projectManager.addEmployee(programmer2);
manager.printDetails();
projectManager.printDetails();
