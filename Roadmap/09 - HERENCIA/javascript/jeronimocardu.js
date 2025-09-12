class Animal {
  constructor(animal) {
    this.animal = animal
  }
  sonido() {
    return `${this.animal} hace un sonido`
  }
}

class Perro extends Animal {
  constructor(animal, ruido) {
    super(animal)
    this.ruido = ruido
  }
  ladra() {
    return this.sonido() + ' ' + this.ruido
  }
}

const gato = new Animal('gato')
const perro = new Perro('Perro', 'Guau')

// console.log(gato.sonido())
// console.log(perro.ladra())








class Developer {
  constructor(ident, fullname, language) {
    this.ident = ident
    this.fullname = fullname
    this.language = language
  }
  presentation() {
    return `Hi, my name is ${this.fullname} and my ID is ${this.ident}. I use ${this.language}`
  }
}
class GerenteProyecto extends Developer {
  constructor(ident, fullname, language, employees) {
    super(ident, fullname, language)
    this.employees = employees
  }
  add(employerID) {
    this.employees.push(employerID)
  }
  sendOf(employerID) {
    this.employees = this.employees.filter((emp) => emp.ident != employerID)
  }
  showEmployees() {
    return this.employees
  }
}
class Gerente extends GerenteProyecto {
  constructor(ident, fullname, language, employees) {
    super(ident, fullname, language, employees)
  }
  sendOfAll(exit) {
    if (exit) this.employees = []
  }
}







const jeronimo = new Developer(1, 'Jeronimo Cardu', 'javascript')
const tobias = new Developer(2, 'Tobias Acuña', 'python')
const leo = new Developer(3, 'Leonardo Skoliber', 'c')

// console.log(jeronimo.presentation())
// console.log(tobias.presentation())
// console.log(leo.presentation())

const agustin = new GerenteProyecto(4, 'Agustin Botella', 'React Native', [
  jeronimo,
  tobias,
  leo,
])

const lara = new Developer(12, 'Lara', 'Kotlin')

// console.log(agustin.presentation())
// console.log(agustin.showEmployees())
// agustin.add(lara)
// agustin.sendOf(2)
// console.log(agustin.showEmployees())

const jorge = new Gerente(100, 'Jorge Cardu', 'none', [
  jeronimo,
  tobias,
  leo,
  lara,
  agustin,
])

// console.log(jorge.presentation())
// console.log(jorge.showEmployees())
// jorge.sendOf(12)
// console.log(jorge.showEmployees())
// jorge.sendOfAll(true)
// console.log(jorge.showEmployees())
