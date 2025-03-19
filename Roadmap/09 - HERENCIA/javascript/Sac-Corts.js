// Exercise
class Animal {
    constructor(name) {
        this.name = name;
    }

    sound() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    constructor(name) {
        super(name);
    }

    sound() {
        console.log('gua gua gua!');
    }
}

class Cat extends Animal {
    constructor(name) {
        super(name);
    }

    sound() {
        console.log('miau miau miau!')
    }
}

function makeASound(animal) {
    animal.sound();
}

const myDog = new Dog('Junior');
const myCat = new Cat ('Luna');

makeASound(myDog);
makeASound(myCat);

// Extra Exercise //
class Employee {
    constructor(name, id) {
        this.name = name;
        this.id = id;
        this.employeesInCharge = [];
    }

    addEmployee(employee) {
        this.employeesInCharge.push(employee);
    }

    showInformation() {
        console.log(`ID: ${this.id}`);
        console.log(`Name: ${this.name}`);
        if (this.employeesInCharge.length > 0) {
            console.log("Employees in charge:");
            this.employeesInCharge.forEach((employee) => {
                employee.showInformation();
            });
        } 
    }
}

class Manager extends Employee { 
    constructor(name, id, deparment) {
        super(name, id);
        this.deparment = deparment;
    }

    assignEmployee(employee) {
        this.addEmployee(employee);
    }

    showInformation() {
        super.showInformation();
        console.log(`Deparment: ${this.deparment}`);
    }
}

class ProjectManager extends Manager {
    constructor(name, id, deparment, currentProject) {
        super(name, id, deparment);
        this.currentProject = currentProject; 
    }
    
    assignProject(project) {
        this.currentProject = project;
    }

    showInformation() {
        super.showInformation();
        console.log(`Current Project: ${this.currentProject}`);
    } 
}

class Developer extends Employee {
    constructor(name, id, languages, level) {
        super(name, id);
        this.languages = languages;
        this.level = level;
    }

    writeCode() {
        console.log(`${this.name} is writing code in ${this.languages.join(", ")}`);
    }

    showInformation() {
        super.showInformation()
        console.log(`Programming languages: ${this.languages.join(", ")}`);
        console.log(`Level: ${this.level}`);
    }
}

const developer1 = new Developer('Angelo', '3', ['Python, JavaScript, Java, C'], 'Senior');
const developer2 = new Developer('Isaac', '4', ['Python, JavaScript'], 'Junior');
const projectManager = new ProjectManager('Luisa', '2', 'Web Development', 'Project IG');
const manager = new Manager('Luis', '1', 'IT');

manager.assignEmployee(developer1);
projectManager.assignEmployee(developer2);
manager.assignEmployee(projectManager);
manager.showInformation();
developer2.writeCode();
projectManager.assignProject('Project X');
manager.showInformation();