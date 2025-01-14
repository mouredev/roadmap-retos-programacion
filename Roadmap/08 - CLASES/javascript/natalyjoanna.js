
// Declaracion 

class Rectangulo {
  constructor(ancho, altura) {
    this.altura = altura;
    this.ancho = ancho;
  }
  
  printRectangulo() {
    console.log(`La altura del rectangulo es de ${this.altura} y su ancho de ${this.ancho}`)
  }
}


// Expresion: la clase es anonima pero esta asignada a una variable
// const Rectangulo = class {
//   constructor(ancho, altura) {
//     this.ancho = ancho;
//     this.altura = altura;
//   }
// }

// // Expresion: la clase tiene su propio nombre diferente al de la variable que se le asigna
// const Rectangulo = class Rectangulo2 {
//   constructor(ancho, altura) {
//     this.ancho = ancho;
//     this.altura = altura;
//   }
// }

let rec = new Rectangulo(23, 50)
rec.printRectangulo()
// Modificar parametros
rec.altura = 33
rec.printRectangulo()

// DIFICULTAD EXRA
class Pila {
  constructor() {
    this.pila = [];
  }

  // Agregar nuevo eleento a la pila
  agregar(elemento) {
    this.pila.push(elemento)
  }

  // Elimina el ultimo elemento de la pila
  eliminar() {
    if (this.size() === 0) return null;
    return this.pila.pop()
  }

  // Imprime toda la pila
  printPila() {
    console.log(this.pila)
  }

  // Devuelve el numero de elementos que contiene la pila
  size() {
    return this.pila.length
  }

}

let pila = new Pila()

// Agregamos valores a la pila
pila.agregar('Manuel')
pila.agregar('Maria')
pila.agregar('Federico')
pila.printPila()
// Eliminamos el ultimo elemento de la pila
pila.eliminar()
pila.printPila()
// Mostrar numero de elementos actual de la pila
console.log(pila.size())

class Cola {
  constructor() {
    this.cola = [];
  }

  // Agregar un elemento a la cola
  agregar(elemento) {
    this.cola.push(elemento)
  }

  // Eliminar el primer elemento de la cola
  eliminar() {
    if(this.size() === 0) return null;
      return this.cola.shift();
    
  }

  // Imprime toda la cola
  printCola() {
    if(this.cola.length === 0) {
      console.log('La cola esta vacia');
    } else {
    console.log(this.cola);
    }
  }

  // Devuelve el numero de elementos que contiene la cola
  size() {
    return this.cola.length
  }

}

let cola = new Cola()


// Agregamos elementos a la cola
cola.agregar(50);
cola.agregar(15);
cola.agregar(515);
cola.agregar(13);
cola.printCola() 
// Eliminamos el primer elemento de la cola
cola.eliminar();
cola.printCola();
// Mostrar el numero de elementos que contiene la cola
console.log(cola.size());