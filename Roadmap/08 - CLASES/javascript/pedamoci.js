class Pokemon {
  name  //  <--- atributo
  primerTipo  //  <--- atributo
  segundoTipo  //  <--- atributo

  constructor(name, primerTipo, segundoTipo) {  //  <--- inicializador
    this.name = name
    this.primerTipo = primerTipo
    this.segundoTipo = segundoTipo
  }

  imprimirAtributos() {  //  <--- función que imprime los atributos
    console.log(`${this.name} es de tipo ${this.primerTipo} y ${this.segundoTipo}`)
  }

  /*imprimirAtributos(name) {  //  <--- función que imprime los atributos
    Object.entries(name).forEach(([key, value]) => {
      console.log(`${key}: ${value}`)
    })
    //console.log(`${this.name} es de tipo ${this.primerTipo} y ${this.segundoTipo}`)
  }*/
}

const dartix = new Pokemon('Dartix', 'Planta', 'Volador')  // <--- crandola y estableciendo sus parametros
dartix.imprimirAtributos()

/*dartix.imprimirAtributos(dartix)*/

dartix.name = 'Decidueye'  // <--- modificando sus parametros
dartix.segundoTipo = 'Fantasma'  // <--- modificando sus parametros
dartix.imprimirAtributos()  // <--- imprimiendo los parametros con la función dentro de la clase

/*dartix.imprimirAtributos(dartix)*/

// ----------------------------------------- DIFICULTAD EXTRA -----------------------------------------
  // CLASE REPRESENTANDO ESTRUCTURA DE PILA
    class Pila {
      constructor(name) {
        this.namePila = name
        this.pila = []
      }
    
      add(name) {
        this.pila.push(name)
        console.log(`Se ha añadido a la pila el elemento '${name}'`)
      }
    
      delete(name) {
        if (this.pila.length === 0) {
          console.log('La pila esta vacia')
        } else if (name === undefined) {
          this.pila.pop()
          console.log('Ultimo elemento de la pila eliminado')
        } else if (this.pila.includes(name)) {
          let index = this.pila.lastIndexOf(name)  // <--- obtiene en el array la posición del elemento que se quiere eleminar
          let lastElementPila = this.pila.slice(index + 1) // <--- guarda los elementos que hay despues del que se desea eliminar
          this.pila = this.pila.slice(0, index).concat(lastElementPila) // <--- corta el array original hasta el elemento que se quiere eliminar (no incluido) y se le añade el   array   con los elemntos guardados
          console.log(`se ha eliminado ${name} de la pila`)
        } else {
          console.log(`No hay elementos con el nombre: '${name}' en la pila`)
        }
      }
    
      numberElements() {
        console.log(`Hay ${this.pila.length} elementos en la pila`)
      }
    
      printAll() {
        while (this.pila.length !== 0) {
          console.log(`Se a impreso el elemento ${this.pila[this.pila.length - 1]}`)
          this.pila.pop()
        }
        console.log('La pila esta vacia')
      }
    }

    const nuevaPila = new Pila('primera pila')
    console.log(nuevaPila)

    // añade elementos
    nuevaPila.add('pepe'); nuevaPila.add('jaime'); nuevaPila.add('juan'); nuevaPila.add('pedro'); nuevaPila.add('luffy'); nuevaPila.add('deadpool'); nuevaPila.add('red');  nuevaPila. add('aang'); nuevaPila.add('homero'); nuevaPila.add('spiderman'); nuevaPila.numberElements()

    nuevaPila.delete('zoro') // <--- intento de borrar elemento no existente
    nuevaPila.delete('red') // <--- borrar elemento existente por nombre
    nuevaPila.delete() // <--- borrar último elemento

    nuevaPila.numberElements()
    nuevaPila.printAll()

  // CLASE REPRESENTANDO ESTRUCTURA DE COLA
  class Cola {
    constructor(name) {
      this.nameCola = name
      this.cola = []
    }
  
    add(name) {
      this.cola.push(name)
      console.log(`Se ha añadido a la cola el elemento '${name}'`)
    }
  
    delete(name) {
      if (this.cola.length === 0) {
        console.log('La cola esta vacia')
      } else if (name === undefined) {
        this.cola.shift()
        console.log('Primer elemento de la cola eliminado')
      } else if (this.cola.includes(name)) {
        let index = this.cola.lastIndexOf(name)  // <--- obtiene en el array la posición del elemento que se quiere eleminar
        let lastElementCola = this.cola.slice(index + 1) // <--- guarda los elementos que hay despues del que se desea eliminar
        this.cola = this.cola.slice(0, index).concat(lastElementCola) // <--- corta el array original hasta el elemento que se quiere eliminar (no incluido) y se le añade el   array   con los elemntos guardados
        console.log(`se ha eliminado ${name} de la cola`)
      } else {
        console.log(`No hay elementos con el nombre: '${name}' en la cola`)
      }
    }
  
    numberElements() {
      console.log(`Hay ${this.cola.length} elementos en la cola`)
    }
  
    printAll() {
      while (this.cola.length !== 0) {
        console.log(`Se a impreso el elemento ${this.cola[0]}`)
        this.cola.shift()
      }
      console.log('La pila esta vacia')
    }
  }

  const nuevaCola = new Cola('primera cola')
  console.log(nuevaCola)

  // añade elementos
  nuevaCola.add('pepe'); nuevaCola.add('jaime'); nuevaCola.add('juan'); nuevaCola.add('pedro'); nuevaCola.add('luffy'); nuevaCola.add('deadpool'); nuevaCola.add('red');  nuevaCola. add('aang'); nuevaCola.add('homero'); nuevaCola.add('spiderman'); nuevaCola.numberElements()

  nuevaCola.delete('zoro') // <--- intento de borrar elemento no existente
  nuevaCola.delete('red') // <--- borrar elemento existente por nombre
  nuevaCola.delete() // <--- borrar último elemento

  nuevaCola.numberElements()
  nuevaCola.printAll()