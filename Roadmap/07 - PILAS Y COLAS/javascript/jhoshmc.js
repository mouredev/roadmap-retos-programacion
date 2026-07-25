// todo ---------------------------------------------------- pilas -----------------------------------
//* mostarndo pila con un array
//* por defecto con array ya vienen push,pop,size,print, solo faltaria agregar peek,
//* que seria el tamaño del apila -1
//* clase pila
class Stack {
  //?atributos: son las propiedades que definen al ogjeto
  constructor() {
    this.stack = [];
  }
  //? metodos: son la acciones que puede realizar el objeto(funciones)
  //* poner un elemento al tope de la pila
  push(elemento) {
    this.stack.push(elemento);
    return this.stack;
  }
  //* eliminar el último elemento y retornar ese elemento
  pop() {
    return this.stack.pop();
  }
  //* Retorna el último valor de la pila sin sacarla de ella
  peek() {
    return this.stack[this.stack.length - 1];
  }
  //* retorna el número de elementos que hay en la pila
  size() {
    return this.stack.length;
  }
  //* muestra el contenido de la pila
  print() {
    console.log(this.stack);
  }
}
function ejecutandoStack() {
  const stack = new Stack();
  console.log(`tamaño de la pila: ${stack.size()}`);
  console.log("agregando elementos a la pila");
  stack.push(1);
  stack.push(2);
  stack.push(3);
  console.log("mostarndo pila");
  stack.print();
  console.log("eliminando elemenos de la pila ");
  let el = stack.pop();
  console.log(`retorno del valor y eliminado: ${el}`);
  stack.print();
  console.log(`retornando el ulimo valor sin eliminarlo: ${stack.peek()}`);
  console.log(`tamalo de la pila: ${stack.size()}`);
}

// ejecutandoStack();

//* pila usando un objeto
class ObjectStack {
  //* atributos
  constructor() {
    this.stack = {};
    this.count = 0; //* se agrega count, como referencia de la posicion actual y saber cuantos elementos hay agregados
  }
  //* metodos
  push(element) {
    /**
     ** para agregar un elemento al objeto,con count se hace referencia a la posicion actual y se hace una
     ** asignacion directa, se incrementa el contador(numero de elementos) y se retorna el objeto
     */
    this.stack[this.count] = element;
    this.count++;
    return this.stack;
  }
  pop() {
    /**
     ** para eliminar el elemento superior en la pila y retornal el valor:
     ** primero se decrementa el contador, para ver el valor del elemento, el tamaño tal-1 para ver el valor de esa posicion
     ** luego se guarda ese valor en una variable
     ** despues se elimina ese valor de la pila
     ** y por último se retorna el valor de esa posicion previamente extraida
     */
    this.count--;
    const elemento = this.stack[this.count];
    delete this.stack[this.count];
    return elemento;
  }
  peek() {
    //* retornamos el último valor de la pila, sin eliminarlo
    return this.stack[this.count - 1];
  }
  size() {
    //* se retorna el tamaño de la pila
    return this.count;
  }
  print() {
    //* se muestra los elementos que están en la pila
    console.log(this.stack);
  }
}
function ejecutandoObjectStack() {
  const oStack = new ObjectStack();
  console.log(`el tamaño actual de la pila es: ${oStack.size()}`);
  console.log("agregando elementos a la pila ");
  oStack.push("uno");
  oStack.push("dos");
  oStack.push("tres");
  console.log(`el tamaño actual de la pila es: ${oStack.size()}`);
  console.log("mostrando la pila");
  oStack.print();
  console.log(`sacando un elemento de la pila: ${oStack.pop()}`);
  console.log(`mostrando el ultimo elemento de la pila: ${oStack.peek()}`);
  console.log("mostrando la pila");
  oStack.print();
}
// ejecutandoObjectStack();

//todo -------------------------------------- colas ------------------------------------------

class Queque {
  //* atributos
  constructor() {
    this.queue = [];
  }
  //* metodos
  add(elemento) {
    //* se va a usar push(), que agrega un nuevo elemento al final del array, retorna la longitud
    this.queue.push(elemento);
    return this.queue;
  }
  //* retornar el primer valor de la cola, sin removerlo
  front() {
    return this.queue[0];
  }
  //* retornar el ultimo valor de la cola, sin removerlo
  back() {
    return this.queue[this.queue.length - 1];
  }
  //* mostrar cola
  print() {
    console.log(this.queue);
  }
  //* eliminar el primer elemento de la cola Y retornar su valor
  pop() {
    return this.queue.shift();
  }
  //* retornar el tamaño de la cola
  size() {
    return this.queue.length;
  }
}

function ejecutandoQueque() {
  const queque = new Queque();
  console.log(`tamaño de la cola: ${queque.size()}`);
  console.log(`agregando elementos a la cola .....`);
  queque.add("primero");
  queque.add("segundo");
  queque.add("tercero");
  console.log(`tamaño de la cola: ${queque.size()}`);
  console.log(" mostrando cola: ");
  queque.print();
  console.log(`quitando elementod e la cola: ${queque.pop()}`);
  queque.print();
  console.log(`mostrando primer elemento de la cola: ${queque.front()}`);
  console.log(`mostrando ultimo elemento de la cola: ${queque.back()}`);
}

// ejecutandoQueque();

class ObjectQueque {
  //* atributos
  constructor() {
    this.queque = {};
    this.count = 0;
  }
  //* metodos
  add(element) {
    this.queque[this.count] = element;
    this.count++;
    return this.queque;
  }
  pop() {
    this.count--;
    const val = this.queque[0];
    const length = Object.keys(this.queque).length;
    for (let i = 0; i < length - 1; i++) {
      this.queque[i] = this.queque[i + 1];
    }
    delete this.queque[length - 1];
    return val;
  }
  front() {
    return this.queque[0];
  }
  back() {
    return this.queque[this.count - 1];
  }
  print() {
    console.log(this.queque);
  }
  size() {
    return this.count;
  }
}
function ejecutandoObjectQueque() {
  const oQueque = new ObjectQueque();
  console.log(`tamaño de la cola: ${oQueque.size()}`);
  console.log("agregando elementos a la cola: ");
  oQueque.add("primero");
  oQueque.add("segundo");
  oQueque.add("tercero");
  console.log(`tamaño de la cola: ${oQueque.size()}`);
  console.log(`primer elemento de la cola: ${oQueque.front()}`);
  console.log(`ultimo elemento en la cola: ${oQueque.back()}`);
  console.log("mostrando cola: ");
  oQueque.print();
  console.log(`eliminando elemento de la cola: ${oQueque.pop()}`);
  oQueque.print();
  console.log(`eliminando elemento de la cola: ${oQueque.pop()}`);
  oQueque.print();
  console.log(`eliminando elemento de la cola: ${oQueque.pop()}`);
  oQueque.print();
  console.log(`tamaño de la cola: ${oQueque.size()}`);
}

// ejecutandoObjectQueque();

//! ejercicios extra
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const preguntar = (texto) => {
  return new Promise((resolve) => rl.question(texto, resolve));
};

async function historialWeb() {
  const historialAtras = new Stack();
  const historialSiquiente = new Stack();
  let paginaActual = "inicio";
  let option;
  console.log("\t historial web: \n");
  console.log("vienvenido al historial web, hay 4 opciones: ");
  const data = [
    { option: "visitar citio", accion: "ingresar el nombre de la pagina" },
    { option: "retroceder", accion: "ingresar b" },
    { option: "siguiente", accion: "ingresar n" },
    { option: "salir", accion: "ingresar s" },
  ];
  console.table(data);
  while (true) {
    console.log(`\npagina actual: ${paginaActual}`);
    option = await preguntar("ingrese option: ");
    let copia = option.toLowerCase();
    if (copia == "b" || copia == "n" || copia == "s") {
      if (historialAtras.size() > 0) {
        if (copia == "b") {
          historialSiquiente.push(paginaActual);
          paginaActual = historialAtras.pop();
        }
      } else {
        console.log("\n previamente no hay paginas registradas\n");
      }
      if (historialSiquiente.size() > 0) {
        if (copia == "n") {
          historialAtras.push(paginaActual);
          paginaActual = historialSiquiente.pop();
        }
      } else {
        console.log("\naun no hay paginas registradas\n");
      }

      if (copia == "s") {
        console.log("\nsaliendo del historial.......\n");
        break;
      }
    } else {
      historialAtras.push(paginaActual);
      paginaActual = option;
    }
  }
  rl.close();
}

// historialWeb();

async function impresora() {
  const cola = new Queque();
  let option;
  let copia;
  console.log("\n\timpresora compartida\n");
  console.log(
    "bienvenido a la impresora compartida, estas son las siguientes opciones"
  );
  const data = [
    {
      option: "ingresar documento",
      accion: "ingresar el nombre del documento",
    },
    { option: "imprimir", accion: "escribir i" },
    { option: "salir", accion: "escribir s" },
  ];
  console.table(data);
  while (true) {
    if (cola.size() > 0) {
      console.log(
        `\ndocumentos en cola:${cola.size()}, documento: ${cola.front()}`
      );
      option = await preguntar("ingrese opcion: ");
      copia = option.toLowerCase();
      if (copia == "i" || copia == "s") {
        if (copia == "i") {
          console.log(`\nimprimendo: ${cola.pop()}`);
        }
        if (copia == "s") {
          console.log("\nsaliendo de la impresora......\n");
          break;
        }
      } else {
        cola.add(option);
      }
    } else {
      console.log("\nno hay documentos en cola\n");
      option = await preguntar("ingrese documento: ");
      cola.add(option);
    }
  }
  rl.close();
}

impresora();
