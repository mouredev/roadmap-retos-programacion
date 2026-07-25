class Animal {

    constructor(name, color) {
        this.name = name
        this.color = color
    }

    makeNoise() {
        console.log('Some nice noise')
    }
 
}

class Cat extends Animal {

    makeNoise() {
        console.log('miau')
    }

}

class Dog extends Animal {

    makeNoise() {
        console.log('guau')
    }

}

// let newAnimal = new Animal()
// newAnimal.makeNoise()
// let newCat = new Cat()
// newCat.makeNoise()
// let newDog = new Dog()
// newDog.makeNoise()


 class CompanyWorkers {

    constructor(name, id) {
        this.name = name
        this.id = id
    }
 }

 class Manager extends CompanyWorkers {
    constructor(name, id, department) {
        super(name, id)
        this.department = department
        this.workersList = []
    }

    addWorker(worker) {
        this.workersList.push(worker)
    }
 }

 class ProjectManager extends CompanyWorkers {

    constructor(name, id, projectName) {
        super(name, id)
        this.projectName = projectName
        this.workersList = []
    }

    addWorker(worker) {
        this.workersList.push(worker)
    }
 }

 class Developer extends CompanyWorkers {

    constructor(name, id, programmingLanguage) {
        super(name, id)
        this.programmingLanguage = programmingLanguage
    }
 }

 // Manager
let company = new CompanyWorkers("Company", 1)
let newManager = new Manager('Lucia', 2, 'Marketing')
let newProjectManager = new ProjectManager('Fernanda', 3, 'Marketing')
newManager.addWorker(newProjectManager)
console.log(newManager.workersList)

// ProjectManager
let newDeveloper = new Developer('Juan', 4, 'Python')
newProjectManager.addWorker(newDeveloper)
console.log(newProjectManager.workersList)