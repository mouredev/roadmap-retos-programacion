class Saludo {
  constructor(lenguaje) {
    this.lenguaje = lenguaje
  }

  getSaludo() {
    return `Hola desde ${this.lenguaje}`
  }
}

let saludo = new Saludo('JavaScript')
console.log(saludo.getSaludo())

// Pila
class Pila {

  constructor(data) {
    this.data = data
  }

  setData(data) {
    return this.data.push(data)
  }

  getRemoveData() {
    return this.data.pop()
  }

  getSize() {
    return this.data.length
  }

  getData() {
    return this.data
  }

  getIsEmpty() {
    return this.getSize() === 0 ? true : false
  }

}

let pila = new Pila([])
console.log(`¿La pila está vacía?: ${pila.getIsEmpty()}`)
pila.setData(5)
pila.setData(10)
pila.setData(6)
pila.setData(2)
pila.setData(8)
console.log(`Elementos en la pila: ${pila.getData()}`)
console.log(`¿La pila está vacía?: ${pila.getIsEmpty()}`)
console.log(`¿Cuál es el tamaño de la pila?: ${pila.getSize()}`)
console.log(`El valor ${pila.getRemoveData()} ha sido removido de la pila`)
console.log(`Elementos en la pila: ${pila.getData()}`)
console.log(`¿Cuál es el tamaño de la pila?: ${pila.getSize()}`)


// Cola
class Cola {

  constructor(data) {
    this.data = data
  }

  setData(data){
    this.data.push(data)
  }

  getRemoveData() {
    return this.data.shift()
  }

  getSize() {
    return this.data.length
  }

  getData() {
    return this.data
  }

  getIsEmpty() {
    return this.getSize() === 0 ? true : false
  }

}

let cola = new Cola([])
console.log(`¿La cola está vacía?: ${cola.getIsEmpty()}`)
cola.setData(5)
cola.setData(10)
cola.setData(6)
cola.setData(2)
cola.setData(8)
console.log(`Elementos en la cola: ${cola.getData()}`)
console.log(`¿La cola está vacía?: ${cola.getIsEmpty()}`)
console.log(`¿Cuál es el tamaño de la cola?: ${cola.getSize()}`)
console.log(`El valor ${cola.getRemoveData()} ha sido removido de la cola`)
console.log(`Elementos en la cola: ${cola.getData()}`)
console.log(`¿Cuál es el tamaño de la cola?: ${cola.getSize()}`)
