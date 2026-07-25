// https://www.typescriptlang.org/

// Herencia básica
class Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  makeSound(): void {
    console.log(`${this.name} hace un sonido`);
  }
}

class Dog extends Animal {
  makeSound(): void {
    console.log(`${this.name} dice: guau`);
  }
}

class Cat extends Animal {
  makeSound(): void {
    console.log(`${this.name} dice: miau`);
  }
}

function printSound(animal: Animal): void {
  animal.makeSound();
}

printSound(new Dog("Rex"));
printSound(new Cat("Whiskers"));
printSound(new Animal("Animal genérico"));

// Dificultad extra: jerarquía de empresa

class Employee {
  id: number;
  name: string;
  subordinates: Employee[] = [];

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  addSubordinate(employee: Employee): void {
    this.subordinates.push(employee);
  }

  display(): void {
    console.log(`[${this.id}] ${this.name}`);
  }
}

class Manager extends Employee {
  department: string;

  constructor(id: number, name: string, department: string) {
    super(id, name);
    this.department = department;
  }

  display(): void {
    console.log(`[${this.id}] Manager: ${this.name} (Dpto: ${this.department})`);
  }
}

class ProjectManager extends Employee {
  project: string;

  constructor(id: number, name: string, project: string) {
    super(id, name);
    this.project = project;
  }

  display(): void {
    console.log(`[${this.id}] Project Manager: ${this.name} (Proyecto: ${this.project})`);
  }
}

class Programmer extends Employee {
  language: string;

  constructor(id: number, name: string, language: string) {
    super(id, name);
    this.language = language;
  }

  display(): void {
    console.log(`[${this.id}] Programmer: ${this.name} (${this.language})`);
  }
}

const cto = new Manager(1, "Sara", "Engineering");
const pm = new ProjectManager(2, "Luis", "Plataforma v2");
const dev1 = new Programmer(3, "Ana", "TypeScript");
const dev2 = new Programmer(4, "Marcos", "Python");

pm.addSubordinate(dev1);
pm.addSubordinate(dev2);
cto.addSubordinate(pm);

cto.display();
for (const sub of cto.subordinates) {
  sub.display();
  for (const inner of sub.subordinates) {
    inner.display();
  }
}
