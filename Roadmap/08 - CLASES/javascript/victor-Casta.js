class Personaje {
  constructor(nombre, poder) {
    this.nombre = nombre;
    this.poder = poder;
  }

  hablar() {
    return `Soy ${this.nombre}`;
  }

  atacar() {
    return this.poder;
  }
}

const batman = new Personaje('Batman', 'Lucha');
console.log(batman.hablar());
console.log(batman.atacar());

/*
  *Extra
*/

class Pila {
  constructor() {
    this.items = [];
  }

  insert(element) {
    this.items.push(element);
  }

  delete() {
    return this.items.pop();
  }

  counter() {
    return this.items.length;
  }

  getContent() {
    this.items.forEach(item => console.log(item));
  }
}

let pila1 = new Pila();
//----------- insertar elementos ----------
pila1.insert(1);
pila1.insert(2);
pila1.insert(3);
console.log('Contenido de la pila:', pila1.items);
console.log('-'.repeat(10));
//----------- Eliminar elemento ----------
pila1.delete();
console.log('Contenido de la pila después de eliminar:', pila1.items);
console.log('-'.repeat(10));
//----------- Cantidad de elementos ----------
console.log('Cantidad de elementos en la pila:', pila1.counter());
console.log('-'.repeat(10));
//----------- Contenido ----------
console.log('Contenido de la pila:');
pila1.getContent();

class Cola {
  constructor() {
    this.items = [];
  }

  insert(element) {
    this.items.push(element);
  }

  delete() {
    return this.items.splice(0, 1)[0];
  }

  counter() {
    return this.items.length;
  }

  getContent() {
    this.items.forEach(item => console.log(item));
  }
}

const cola1 = new Cola();
cola1.insert('a');
cola1.insert('b');
cola1.insert('c');
cola1.delete(); // Se eliminó 'a' de la cola
console.log('Cantidad de elementos en la cola:', cola1.counter());
console.log('Contenido de la cola:');
cola1.getContent();
