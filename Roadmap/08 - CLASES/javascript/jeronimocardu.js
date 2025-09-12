class Phone {
  constructor(marca, color) {
    ;(this.marca = marca), (this.color = color)
  }
  imprimirDatos() {
    console.log(`Tengo un celular ${this.marca} de color ${this.color}`)
  }
}

const myPhone = new Phone('samsung', 'rojo')
// myPhone.imprimirDatos()

myPhone.marca = 'Apple'
myPhone.color = 'gris'
// myPhone.imprimirDatos()

/** EJERCICIO */

class Pila {
  constructor(pilaArray) {
    this.pila = pilaArray
  }
  add(element) {
    this.pila.push(element)
  }
  delete() {
    this.pila.pop()
  }
  length() {
    console.log(this.pila.length)
  }
  print() {
    console.log(this.pila)
  }
}

class Cola {
  constructor(colaArray) {
    this.cola = colaArray
  }

  add(element) {
    this.cola.push(element)
  }
  delete() {
    this.cola.shift()
  }
  length() {
    console.log(this.cola.length)
  }
  print() {
    console.log(this.cola)
  }
}

const arrayOfThePila = new Pila([1, 2, 3, 4, 5, 6])
const arrayOfTheCola = new Cola([1, 2, 3, 4, 5, 6])

console.log('/////// PILA ///////')
arrayOfThePila.print()
arrayOfThePila.length()
arrayOfThePila.add(7)
arrayOfThePila.print()
arrayOfThePila.length()
arrayOfThePila.delete()
arrayOfThePila.print()

console.log('/////// COLA ///////')
arrayOfTheCola.print()
arrayOfTheCola.length()
arrayOfTheCola.add(7)
arrayOfTheCola.print()
arrayOfTheCola.length()
arrayOfTheCola.delete()
arrayOfTheCola.print()
