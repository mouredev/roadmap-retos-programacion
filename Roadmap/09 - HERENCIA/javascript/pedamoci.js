class Animal {
  constructor(name) {
    this.name = name
  }
  hablar(modo){
    console.log(modo)
  }
}

class Perro extends Animal {
  constructor(name){
    super(name)
  }
  ladrar() {
    this.hablar('guau')
  }
}

class Gato extends Animal {
  constructor(name){
    super(name)
  }
  maullar() {
    this.hablar('miau')
  }
}

const perro = new Perro('Teo')
const gato = new Gato('Cleopatra')

perro.ladrar()
gato.maullar()

// ------------------------------------ DIFICULTAD EXTRA ------------------------------------
class Empleado {
  constructor(id, name) {
    this.id = id
    this.name = name
    this.subordinados = []
  }

  agregarSubordinado(empleado) {
    this.subordinados.push(empleado)
  }
}
class Gerente extends Empleado {
  constructor(id, name) {
    super(id, name)
  }

  asingProycet(manager, proyect) {
    console.log(`${this.name} le ha asignado a ${manager.name} el proyecto ${proyect}`)
  }
}

class ProjectManager extends Empleado {
  constructor(id, name, gerente) {
    super(id, name)
    gerente.agregarSubordinado(this)
  }

  asignTaskProgramador(programador, tarea) {
    console.log(`${this.name} le ha asignado a ${programador.name} programar ${tarea}`)
    programador.programar(tarea)
  }
}

class Programador extends Empleado {
  constructor(id, name, manager) {
    super(id, name)
    manager.agregarSubordinado(this)
  }

  programar(tarea) {
    console.log(`Empezando a programar ${tarea}`)
    console.log(`${this.name} ha teminado de programar ${tarea}`)
  }
}

const gerente1 = new Gerente(1, "Gerardo")
const gerente2 = new Gerente(2, "Alfredo")
const gerente3 = new Gerente(3, "Jaime")

const pm1 = new ProjectManager(10, "Laura", gerente1)
const pm2 = new ProjectManager(20, "Roberto", gerente1)
const pm3 = new ProjectManager(30, "Walter", gerente2)
const pm4 = new ProjectManager(40, "Sofía", gerente2)
const pm5 = new ProjectManager(50, "Carmela", gerente3)
const pm6 = new ProjectManager(60, "Bautista", gerente3)


const programador1 = new Programador(100, 'Juan', pm1)
const programador2 = new Programador(200, 'Mauricio', pm1)
const programador3 = new Programador(300, 'Federico', pm2)
const programador4 = new Programador(400, 'Baltazar', pm2)
const programador5 = new Programador(500, 'Sergio', pm3)
const programador6 = new Programador(600, 'Dario', pm3)
const programador7 = new Programador(700, 'Manuel', pm4)
const programador8 = new Programador(800, 'Raul', pm4)
const programador9 = new Programador(900, 'Horacio', pm5)
const programador10 = new Programador(1000, 'Tomas', pm5)
const programador11 = new Programador(1100, 'Carlos', pm6)
const programador12 = new Programador(1200, 'Francisco', pm6)

// Proyect manger le asigna una tarea a un programador y este la realiza
pm1.asignTaskProgramador(programador1, 'Página web')

// Gerente le asigna un proyecto a un proyect manager
gerente2.asingProycet(pm4, 'silksong')


// Programador programa 
programador12.programar('ToDo')

console.log(`El gerente ${gerente1.name} tiene de subordinados a ${gerente1.subordinados[0].name} y a ${gerente1.subordinados[1].name}, ${gerente1.subordinados[0].name} tiene como subordinados a ${gerente1.subordinados[0].subordinados[0].name} y a ${gerente1.subordinados[0].subordinados[1].name} y ${gerente1.subordinados[1].name} tiene como subordinados a ${gerente1.subordinados[1].subordinados[0].name} y a ${gerente1.subordinados[1].subordinados[1].name}`)

console.log(`El gerente ${gerente2.name} tiene de subordinados a ${gerente2.subordinados[0].name} y a ${gerente2.subordinados[1].name}, ${gerente2.subordinados[0].name} tiene como subordinados a ${gerente2.subordinados[0].subordinados[0].name} y a ${gerente2.subordinados[0].subordinados[1].name} y ${gerente2.subordinados[1].name} tiene como subordinados a ${gerente2.subordinados[1].subordinados[0].name} y a ${gerente2.subordinados[1].subordinados[1].name}`)

console.log(`El gerente ${gerente3.name} tiene de subordinados a ${gerente3.subordinados[0].name} y a ${gerente3.subordinados[1].name}, ${gerente3.subordinados[0].name} tiene como subordinados a ${gerente3.subordinados[0].subordinados[0].name} y a ${gerente3.subordinados[0].subordinados[1].name} y ${gerente3.subordinados[1].name} tiene como subordinados a ${gerente3.subordinados[1].subordinados[0].name} y a ${gerente3.subordinados[1].subordinados[1].name}`)