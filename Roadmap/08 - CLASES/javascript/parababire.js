//Clases: funciones especiales. La sintaxis puede ser de dos formas.

/*Declaración de clases*/

class Vehiculo {//Utilizamos la palabra reservada class y por convención el nombre en mayuscula.
  constructor(fabricante, modelo) {//Solo puede ser llamado un constructor o inicializador por clase.
    this.fabricante = fabricante;
    this.modelo = modelo;
  }
  get fabricante() {
    return this._fabricante;
  }
  set fabricante(fabricante) {
    this._fabricante = fabricante;
  }
  get modelo() {
    return this._modelo;
  }
  set modelo(modelo) {
    this._modelo = modelo;
  }
  caracteristicas() {
    console.log(`Vehiculo marca ${this.fabricante} modelo ${this.modelo}`);
  }
}
let carro = new Vehiculo("Toyota", "Corrolla");
console.log(`Compre un ${carro.fabricante} ${carro.modelo}.`);
carro.caracteristicas();
carro.modelo = "Prius";
carro.caracteristicas();

/*Expresión de clases*/

//Anónima
let Perro = class {
  constructor(patas, cola, raza) {
    this.patas = patas;
    this.cola = cola;
    this.raza = raza;
  }
}

//Nombrada
let Rectangulo = class Rectangulo1 {
  constructor(alto, ancho) {
    this.alto = alto;
    this.ancho = ancho;
  }
}

//Extra

class Pila {
  constructor() {
    this.pila = [];
  }
  push(element) {
    this.pila.push(element);
    return this.pila;
  }
  pop() {
    return this.pila.pop();
  }
  size() {
    return this.pila.length;
  }
  print() {
    console.log(this.pila);
  }
}

let pila = new Pila();
pila.push("María");
pila.push("Luis");
pila.push("Pedro");
pila.push("Yolanda");
pila.print();
console.log(pila.pop());
console.log(pila.size());
pila.print();

class Queue {
  constructor() {
    this.queue = [];
  }
  enqueue(element) {
    this.queue.push(element);
  }
  dequeue() {
    return this.queue.shift();
  }
  size() {
    return this.queue.length;
  }
  print() {
    console.log(this.queue);
  }
}

let queue = new Queue();
queue.enqueue("María");
queue.enqueue("Luis");
queue.enqueue("Pedro");
queue.enqueue("Yolanda");
queue.print();
console.log(queue.dequeue());
console.log(queue.size());
queue.print();