class Animal{
  constructor(name: string, size: string, isDomestic: Boolean){
    this.name = name
    this.size = size
    this.isDomestic = isDomestic
  }
}

class Dog extends Animal{
  get makeDogSound(){
    return this.dogSound()
  }
  
  dogSound() {
    return 'bark' + ' ' + this.name
  }
}

class Cat extends Animal{
  get makeCatSound(){
    return this.catSound()
  }
  
  catSound() {
    return 'meow' + ' ' + this.name
  }
}

const myDog = new Dog('Dolly', 'small', true)
console.log(myDog.makeDogSound)

const myCat = new Cat('Snowball', 'small', true)
console.log(myCat.makeCatSound)




/* DIFICULTAD EXTRA */

class Empleado{
  constructor(id: string, employeeName: string){
    this.id = id
    this.employeeName = employeeName
  }

  get makePresentation(){
    return this.presentation()
  }

  presentation(){
    return 'Hola, mi nombre es ' + this.employeeName
  }
}

class Gerente extends Empleado{
  constructor(id: string, employeeName: string, clients: Array<string> = []){
  super(id, employeeName)
    this.clients = clients
  }

  get showClientsList(){
    return this.clientsList()
  }

  clientsList(){
    return this.clients
  }

  addNewClient(companyName: string){
    this.clients.push(companyName)
  }

}

const newGerente = new Gerente('1', 'Andres')
console.log(newGerente.makePresentation)
console.log(newGerente.showClientsList)
newGerente.addNewClient('ITO')
console.log(newGerente.showClientsList)


class GerenteProyecto extends Empleado{
  constructor(id: string, employeeName: string, projects: Array<string> = []){
    super(id, employeeName)
    this.projects = projects
  }

  get showProjectsList(){
    return this.projectsList()
  }

  projectsList(){
    return this.projects
  }

  startProject(projectName: string){
    this.projects.push(projectName)
  }

  finishProject(projectName: string){
    this.projects = this.projects.filter(project => project !== projectName)
  }  
}


const newGerenteProyecto = new GerenteProyecto('2', 'Edith')
console.log(newGerenteProyecto.makePresentation)
console.log(newGerenteProyecto.showProjectsList)
newGerenteProyecto.startProject('Web page')
newGerenteProyecto.startProject('Mobile app')
newGerenteProyecto.startProject('Logo refresh')
console.log(newGerenteProyecto.showProjectsList)
newGerenteProyecto.finishProject('Mobile app')
console.log(newGerenteProyecto.showProjectsList)


class Programador extends Empleado{
  constructor(id: string, employeeName: string, tasks: Array<string> = []){
    super(id, employeeName)
    this.tasks = tasks
  }

  get showTasksList(){
    return this.tasksList()
  }

  tasksList(){
    return this.tasks
  }

  startNewTask(newTask: string){
    this.tasks.push(newTask)
  }

  finishTask(taskName: string){
    this.tasks = this.tasks.filter(task => task !== taskName)
  }
}

const newProgramador = new Programador('3', 'Jesus')
console.log(newProgramador.makePresentation)
console.log(newProgramador.showTasksList)
newProgramador.startNewTask('refactor sign in function')
newProgramador.startNewTask('fix form styles')
newProgramador.startNewTask('create props TS interface')
console.log(newProgramador.showTasksList)
newProgramador.finishTask('fix form styles')
console.log(newProgramador.showTasksList)