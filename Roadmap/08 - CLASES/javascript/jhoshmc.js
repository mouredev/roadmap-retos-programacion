class Mamifero {
  //? Atributos
  constructor(especie, nombre, edad) {
    this._especie = especie;
    this._nombre = nombre;
    this._edad = edad;
  }
  //? metodos
  saludar() {
    if (this._especie == "humano") {
      console.log(
        `\nhola mi nombre es ${this._nombre} y tengo ${this._edad}, mucho gusto`
      );
    } else {
      console.log(`\n mi nombre es ${this._nombre} y saludo dandote la pata`);
    }
  }
}

class Pila {
  //? atributos
  constructor() {
    this.stack = [];
  }
  //? metodos
  //*ver si la pila está vacia, true:vacia, false: tiene elementos
  empty() {
    return this.stack.length == 0;
  }
  //* agregar elementos a la pila
  push(elemento) {
    this.stack.push(elemento);
  }
  //* mostrar el último elemento de la pila sin eliminarlo
  end() {
    if (this.stack.length !== 0) {
      return this.stack[this.stack.length - 1];
    }
    console.log("\nno se puede mostrar elemento, la pila esta vacia");
  }
  //* eliminar el último elemento de la pila y retornarlo
  pop() {
    if (this.stack.length !== 0) {
      return this.stack.pop();
    }
    console.log("\nno se puele elimnar cuando la pila esta vacia");
  }
  //*retornar el tamaño de la pila
  size() {
    return this.stack.length;
  }
  //* mostrar la pila
  print() {
    if (this.stack.length !== 0) {
      console.log(this.stack);
    } else {
      console.log("\n la pila esta vacia");
    }
  }
}

class Cola {
  //? atributos
  constructor() {
    this.queque = [];
  }
  //? metodos
  //* metodo para saber si la cola esta vacia, true: esta vacia, false: tiene elementos
  empty() {
    return this.queque.length == 0;
  }
  //*para egregar un elemento al final de la cola
  push(elemento) {
    this.queque.push(elemento);
  }
  //* para eliminar el primer elemento de la cola y retornar su valor
  pop() {
    if (this.queque.length !== 0) {
      return this.queque.shift();
    }
    console.log("\n no hay elemento en la cola");
  }
  //*para mostrar el primer elmento de la cola sin eliminarlo
  front() {
    if (this.queque.length !== 0) {
      return this.queque[0];
    } else {
      console.log("\nno hay elementos en la cola");
    }
  }
  //* para mostrar el tamaño de la cola
  size() {
    return this.queque.length;
  }
  //* mostrar la cola
  print() {
    if (this.queque.length !== 0) {
      console.log(this.queque);
    } else {
      console.log("\nno hay elementos en la cola para mostrar");
    }
  }
}

function ejercicio() {
  const miguel = new Mamifero("humano", "miguel", 20);
  const chester = new Mamifero("canina", "chester", 3);
  const laila = new Mamifero("canina", "laila", 2);
  const lita = new Mamifero("felina", "lita", 1);
  miguel.saludar();
  chester.saludar();
  laila.saludar();
  lita.saludar();
}
//todo ejercicios extras
function extraPila() {
  const pila = new Pila();
  console.log(`la pila esta vacia?: ${pila.empty()}`);
  console.log("agregando elementos a la pila: ");
  pila.push(1);
  pila.push(2);
  pila.push(3);
  console.log(`el tamaño de la pila es: ${pila.size()}`);
  console.log("mostrando elementos de la pila: ");
  pila.print();
  console.log(`la pila esta vacia?: ${pila.empty()}`);
  console.log(`mostrado ultimo elemento de la pila: ${pila.end()}`);
  console.log(`eliminando el ultimo elmento de la pila: ${pila.pop()}`);
  pila.print();
  console.log(`eliminando el ultimo elmento de la pila: ${pila.pop()}`);
  pila.print();
  console.log(`eliminando el ultimo elmento de la pila: ${pila.pop()}`);
  pila.print();
}
function extraCola() {
  const cola = new Cola();
  console.log(`la cola esta vacia?: ${cola.empty()}`);
  console.log("agregando elementos a la pila");
  cola.push(1);
  cola.push(2);
  cola.push(3);
  console.log(`tamaño de la cola: ${cola.size()}`);
  console.log(`primer elemento de la cola: ${cola.front()}`);
  console.log("mostrando cola: ");
  cola.print();
  console.log(`eliminando el primer elemento de la cola: ${cola.pop()}`);
  cola.print();
  console.log(`eliminando el primer elemento de la cola: ${cola.pop()}`);
  cola.print();
  console.log(`eliminando el primer elemento de la cola: ${cola.pop()}`);
  cola.print();
}
//todo ejecutando programas
ejercicio();
extraPila();
extraCola();
