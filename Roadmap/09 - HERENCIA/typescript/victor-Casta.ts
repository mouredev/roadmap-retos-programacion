/*
  * EJERCICIO:
  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
  * implemente una superclase Animal y un par de subclases Perro y Gato,
  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
*/

abstract class Animal {
  protected readonly name: string
  protected readonly age: number
  protected readonly color: string

  constructor(name: string, age: number, color: string) {
    this.name = name
    this.age = age
    this.color = color
  }

  abstract sound(): void
}

class Cat extends Animal {
  sound(): void {
    console.log(`${this.name} el gato hace "Miau!"`)
  }
}

class Dog extends Animal {
  sound(): void {
    console.log(`${this.name} el perro hace "Guau!"`)
  }
}

const dog1: Dog = new Dog('Max', 2, 'café')
dog1.sound()

const cat1: Cat = new Cat('Michi', 1, 'negro')
cat1.sound()

/*
  * DIFICULTAD EXTRA (opcional):
  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
  * Cada empleado tiene un identificador y un nombre.
  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
  * actividad, y almacenan los empleados a su cargo.
*/

class Employee {
  protected readonly id: number
  protected name: string

  constructor(id: number, name: string) {
    this.id = id
    this.name = name
  }

  displayInfo(): void {
    console.log(`ID: ${this.id}, Name: ${this.name}`)
  }
}

class Manager extends Employee {
  private employees: string[] = []

  constructor(id: number, name: string, employees: string[] = []) {
    super(id, name)
    this.employees = employees
  }

  addEmployee(employee: string): void {
    this.employees.push(employee)
  }

  getEmployees(): string[] {
    return this.employees
  }

  displayInfo(): void {
    super.displayInfo()
    console.log(`Managed Employees: ${this.employees.join(', ') || 'No employees'}`)
  }
}

class ProjectManager extends Employee {
  private projects: string[] = []

  constructor(id: number, name: string, projects: string[] = []) {
    super(id, name)
    this.projects = projects
  }

  addProject(projectName: string): void {
    this.projects.push(projectName)
  }

  getProjects(): string[] {
    return this.projects
  }

  displayInfo(): void {
    super.displayInfo()
    console.log(`Projects: ${this.projects.join(', ') || 'No projects'}`)
  }
}

class Developer extends Employee {
  private skills: string[] = []

  constructor(id: number, name: string, skills: string[] = []) {
    super(id, name)
    this.skills = skills
  }

  addSkill(skill: string): void {
    if (!this.skills.includes(skill)) {
      this.skills.push(skill)
    } else {
      console.log(`${this.name} already has skill: ${skill}`)
    }
  }

  getSkills(): string[] {
    return this.skills
  }

  displayInfo(): void {
    super.displayInfo()
    console.log(`Skills: ${this.skills.join(', ') || 'No skills'}`)
  }
}


const manager = new Manager(1, "Alice", ["Bob", "Charlie"])
manager.addEmployee("Dave")
manager.displayInfo()

const projectManager = new ProjectManager(2, "Eve", ["Project A", "Project B"])
projectManager.addProject("Project C")
projectManager.displayInfo()

const developer = new Developer(3, "Tom", ["JavaScript", "TypeScript"])
developer.addSkill("React")
developer.addSkill("JavaScript")
developer.displayInfo()
