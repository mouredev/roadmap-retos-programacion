class Animal {

  constructor(nombre) {
    this.nombre = nombre
  }

  sonido() {
    return `${this.nombre} hace un sonido.`
  }
}

class Perro extends Animal {

  constructor(nombre) {
    super(nombre)
  }

  sonido() {
    return `${this.nombre} ladra: ¡Guau guau!`
  }

}

class Gato extends Animal {

  constructor(nombre) {
    super(nombre)
  }

  sonido() {
    return `${this.nombre} maúlla: ¡Miau miau!`
  }

}

function imprimirSonido(animal) {
  return animal.sonido();
}

const miPerro = new Perro("Rex")
const miGato = new Gato("Mimi")

console.log(imprimirSonido(miPerro))
console.log(imprimirSonido(miGato))
