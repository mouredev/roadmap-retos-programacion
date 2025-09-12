//Tipo de estructura de datos JS

//ARRAYS

//Array con elementos
const myArray = ["Hola", "Mundo", "JavaScript", "Retos de programación", 11];
console.log(myArray);

//Inserción, push inserta un nuevo elemento al final de un array
const myArrayInsercion = [
  "Hola",
  "Mundo",
  "JavaScript",
  "Retos de programación",
  11,
];
myArrayInsercion.push(12);
console.log(myArrayInsercion);

//Borrado, shift elimina el primer elemento de un array
const myArrayBorrar = [
  "Hola",
  "Mundo",
  "JavaScript",
  "Retos de programación",
  11,
];
myArrayBorrar.shift();
console.log(myArrayBorrar);

//Actualizacion, al seleccionar una posicion del array podemos actualizar su valor
const myArrayActualizado = [
  "Hola",
  "Mundo",
  "JavaScript",
  "Retos de programación",
  11,
];
myArrayActualizado[1] = "World";
console.log(myArrayActualizado);

//Ordenación, con sort ordenamos los elementos, primero numeral y luego alfabeticamente en string
const myArrayOrdenado = [
  "Hola",
  "Mundo",
  "JavaScript",
  "Retos de programación",
  11,
];
myArrayOrdenado.sort();
console.log(myArrayOrdenado);

//OBJETOS
//Los objetos están compuestos por 2 clasificaciones clave y valor

//Objeto
const miObjeto = {
  pais: "Chile",
};

//Insersión de clave : valor a un objeto
miObjeto["nombre"] = "Andy";
console.log(miObjeto);

//Actualización de valor de una clave dentro de un objeto
miObjeto.nombre = "Lucy";
console.log(miObjeto);

//Borrado de clave - valor
delete miObjeto.pais;
console.log(miObjeto);

//PILAS
//Se caracteriza por seguir la secuencia LIFO
//Inicializacion de pila o stack
class Pila {
  constructor() {
    this.items = [];
  }
  //Metodo para validar pila vacía
  isEmpty() {
    return this.items.length === 0;
  }
  //Metodo para retornar el valor que está por sobre el último elemento
  last() {
    if (this.isEmpty() === 0) {
      return "La pila está vacía";
    }
    return this.items[this.items.length - 1];
  }
  //Metodo de inserción de valor a la pila
  push(item) {
    this.items[this.items.length] = item;
  }

  //Metodo para borrar el último valor de la pila
  pop() {
    if (this.isEmpty()) {
      return "la pila está vacia";
    }
    const lastElement = this.items[this.items.length - 1];
    this.items.length -= 1;
    return lastElement;
  }
}

const miPila = new Pila();
//Inserción a la pila de valor
miPila.push("hola");
miPila.push("mundo");
miPila.push("Javascript");
console.log(miPila);

//Comprobación de último elemento en la pila
console.log(miPila.last());

//Borrado de último elemento de la pila
console.log(miPila.pop());
//Pila con nuevos valores al borrar el ultimo que se ingresó
console.log(miPila);

//Actualizar pila
miPila.items[0] = "bye";
console.log(miPila);

//COLAS
//Se caracteriza por seguir la secuencia FIFO
//Inicializacion de cola
class Cola {
  constructor() {
    this.items = [];
    this.initialIndex = 0;
  }
  //validacion de cola vacía
  isEmpty() {
    return this.initialIndex >= this.items.length;
  }

  top() {
    if (this.isEmpty()) {
      return "La cola está vacía";
    }
    return this.items[this.initialIndex];
  }

  //Metodo para agregar elemento a la cola
  enqueue(element) {
    this.items[this.items.length] = element;
  }

  //Metodo para borrar elemento de la cola
  dequeue() {
    if (this.isEmpty()) {
      return "La cola está vacía";
    }
    const firstElement = this.items[this.initialIndex];
    delete this.items[this.initialIndex];
    this.initialIndex++;
    return firstElement;
  }
}

const miCola = new Cola();

//Insercion de elementos a la cola
miCola.enqueue("Hola");
miCola.enqueue("Mundo");
miCola.enqueue("Javascript");
//cola con elementos
console.log(miCola);

//Ver el primer elemento ingresado y primer elemento en salir
console.log(miCola.top());

//Actualizar cola
miCola.items[0] = "bye";
console.log(miCola);

//Borrado de primer elemento ingresado
console.log(miCola.dequeue());

//Ejercicio extra pendiente...
