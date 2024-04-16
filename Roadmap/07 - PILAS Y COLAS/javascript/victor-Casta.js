/*
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

//Pilas (stacks - Last In First Out)
class Pila {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  getLastElement() {
    if (this.items === 0) {
      return "La pila está vacía";
    }
    const lastItem = this.items.splice(this.items.length - 1, 1)[0];
    return lastItem;
  }
}

const pila = new Pila();
pila.push(1);
pila.push(2);
pila.push(3);
console.log(pila.getLastElement());
console.log(pila.items);

//colas (queue - First In First Out)
class Cola {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  getFirstItem() {
    const element = this.items.shift();
    return element;
  }
}

const colas = new Cola();
colas.push(1);
colas.push(2);
colas.push(3);
console.log(colas.getFirstItem());
console.log(colas.items);

/*
 *Extra 1
 */
class Web {
  constructor() {
    this.navigation = [];
  }

  action(action, url) {
    if (action === "adelante") {
      this.next(url);
    } else if (action === "atras") {
      return this.back();
    }
  }

  next(url) {
    this.navigation.push(url);
  }

  back() {
    if (this.navigation.length === 0) {
      return "No hay páginas para retroceder";
    }
    return this.navigation.pop();
  }
}

const Chrome = new Web();
Chrome.action("adelante", "https://chrome.google.com");
Chrome.action("adelante", "https://google.com");
console.log(Chrome.navigation);
Chrome.back();
console.log(Chrome.navigation);

/*
  *Extra 2
*/

class Print {
  constructor() {
    this.printSpooler = [];
  }

  action(action, document) {
    if (action === 'insertar') {
      this.insertDocument(document);
    } else if (action === 'imprimir') {
      return this.print();
    } else {
      console.log('Acción desconocida');
    }
  }

  insertDocument(document) {
    this.printSpooler.push(document);
  }

  print() {
    if (this.printSpooler.length <= 0) {
      console.log('No hay documentos pendientes');
      return null;
    } else {
      return this.printSpooler.shift();
    }
  }
}

let myPrint = new Print();
myPrint.action('insertar', 'Hoja de trabajo 1');
myPrint.action('insertar', 'Hoja de trabajo 2');
myPrint.action('insertar', 'Hoja de trabajo 3');
console.log(myPrint.printSpooler);
myPrint.action('imprimir');
console.log(myPrint.printSpooler);
