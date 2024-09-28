class Animal {
    constructor(public name: string) {}

    sound(): string {
        return 'The animal make a sound';
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name);
    }

    sound(): string {
        return 'Woof'; 
    }
}

class Cat extends Animal {
    constructor(name: string) {
        super(name);
    }

    sound(): string{
        return 'Meow';
    }
}

function printSound(animal: Animal): void {
    console.log(`${animal.name} say: ${animal.sound()}`);
}

const myDog = new Dog("Junior");
const myCat = new Cat("Mauricio");

printSound(myDog);
printSound(myCat);

// ** Extra Exercise ** //
class Employee {
    constructor (
        public id: number,
        public name: string
    ) {}

    showDetails(): void {
        console.log(`Employee ID: ${this.id}, Name: ${this.name}`);
    }
}

class Manager extends Employee {
    employeesInCharge: Employee[] = [];

    constructor(id: number, name: string) {
        super(id, name);
    }

    addEmployeeInCharge(employee: Employee): void {
        this.employeesInCharge.push(employee);
    }

    showDetails(): void {
        super.showDetails();
        console.log('Manager in charge of:');
        this.employeesInCharge.forEach(emp => emp.showDetails());
    }
}

class ProjectManager extends Manager {
    projects: string[] = [];

    constructor(id: number, name: string) {
        super(id, name);
    }

    assignProject(project: string): void {
        this.projects.push(project);
    }

    showDetails(): void {
        super.showDetails();
        console.log(`Assigned projects: ${this.projects.join(', ')}`);
    }
}

class Programmer extends Employee {
    languages: string[] = [];

    constructor(id: number, name: string, languages: string[]) {
        super(id, name);
        this.languages = languages;
    }

    showDetails(): void {
        super.showDetails();
        console.log(`Languages: ${this.languages.join(', ')}`);
    }
}

const programmer1 = new Programmer(1, 'Isaac', ["JavaScript", "Python", "TypeScript"]);
const programmer2 = new Programmer(2, 'Mancheco', ["JavaScript", "Python", "TypeScript", "C++"]);

const projectManager = new ProjectManager(3, "Carlos");

projectManager.addEmployeeInCharge(programmer1);
projectManager.addEmployeeInCharge(programmer2);
projectManager.assignProject("Project X");
projectManager.showDetails();