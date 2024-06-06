/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 1. Pila (LIFO)
class Pila {
    constructor() {
      this.pila = [];
    }
  
    // Agregar un elemento a la pila
    push(elemento) {
      this.pila.push(elemento);
    }
  
    // Sacar un elemento de la pila
    pop() {
      return this.pila.pop();
    }
  
    // Ver el último elemento de la pila sin sacarlo
    peek() {
      return this.pila[this.pila.length - 1];
    }
  
    // Ver si la pila está vacía
    estaVacia() {
      return this.pila.length === 0;
    }
  }
  
  // Ejemplo de uso
  const pila = new Pila();
  pila.push("Elemento 1");
  pila.push("Elemento 2");
  pila.push("Elemento 3");
  
  // Imprime ["Elemento 3", "Elemento 2", "Elemento 1"]
  console.log("Pila:", pila); 
  
  // Imprime "Elemento 3"
  const elementoSacado = pila.pop();
  console.log("Elemento sacado:", elementoSacado); 
  
  // Imprime ["Elemento 2", "Elemento 1"]
  console.log("Pila:", pila); 
  
  // Imprime false
  console.log("¿La pila está vacía?:", pila.estaVacia()); 

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  // 2. Cola (FIFO)
class Cola {
  constructor() {
    this.cola = [];
  }

  // Agregar un elemento a la cola
  enqueue(elemento) {
    this.cola.push(elemento);
  }

  // Sacar un elemento de la cola
  dequeue() {
    return this.cola.shift();
  }

  // Ver el primer elemento de la cola sin sacarlo
  peek() {
    return this.cola[0];
  }

  // Ver si la cola está vacía
  estaVacia() {
    return this.cola.length === 0;
  }
}

// Ejemplo de uso
const cola = new Cola();
cola.enqueue("Elemento 1");
cola.enqueue("Elemento 2");
cola.enqueue("Elemento 3");

// Imprime ["Elemento 1", "Elemento 2", "Elemento 3"]
console.log("Cola:", cola); 

// Imprime "Elemento 1"
const elementoSacado = cola.dequeue();
console.log("Elemento sacado:", elementoSacado); 

// Imprime ["Elemento 2", "Elemento 3"]
console.log("Cola:", cola); 

// Imprime false
console.log("¿La cola está vacía?:", cola.estaVacia()); 

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Simulación de Navegación Web con Pila y Cadenas de Texto

// Implementación de Pila
class Pila {
    constructor() {
      this.pila = [];
    }
  
    // Agregar un elemento a la pila
    push(elemento) {
      this.pila.push(elemento);
    }
  
    // Sacar un elemento de la pila
    pop() {
      return this.pila.pop();
    }
  
    // Ver el último elemento de la pila sin sacarlo
    peek() {
      return this.pila[this.pila.length - 1];
    }
  
    // Ver si la pila está vacía
    estaVacia() {
      return this.pila.length === 0;
    }
  }

 // Simulación de Navegación
 const pilaPaginas = new Pila(); // Pila para almacenar las páginas visitadas
let paginaActual = ""; // Página actual

// Función para navegar a una nueva página
function navegar(nuevaPagina) {
  if (paginaActual !== "") {
    pilaPaginas.push(paginaActual); // Guarda la página actual en el historial
  }
  paginaActual = nuevaPagina;
  console.log(`Navegando a: ${paginaActual}`);
}

// Función para ir hacia atrás
function irAtras() {
  if (!pilaPaginas.estaVacia()) {
    paginaActual = pilaPaginas.pop();
    console.log(`Moviendo hacia atrás a: ${paginaActual}`);
  } else {
    console.log("No hay páginas en el historial");
  }
}

// Función para ir hacia adelante
function irAdelante() {
  if (!pilaPaginas.estaVacia()) {
    paginaActual = pilaPaginas.pop();
    console.log(`Moviendo hacia adelante a: ${paginaActual}`);
  } else {
    console.log("No hay páginas por delante");
  }
}

// Ejemplo de uso
navegar("Google");
navegar("Facebook");
navegar("YouTube");

irAtras(); // YouTube -> Facebook
irAtras(); // Facebook -> Google

irAdelante(); // Facebook
irAdelante(); // YouTube

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Simulación de Impresora Compartida con Cola y Cadenas de Texto

// Implementación de Cola
class Cola {
    constructor() {
      this.cola = [];
    }
  
    // Agregar un elemento a la cola
    enqueue(elemento) {
      this.cola.push(elemento);
    }
  
    // Sacar un elemento de la cola
    dequeue() {
      return this.cola.shift();
    }
  
    // Ver el primer elemento de la cola sin sacarlo
    peek() {
      return this.cola[0];
    }
  
    // Ver si la cola está vacía
    estaVacia() {
      return this.cola.length === 0;
    }
  }

  //  Simulación de Impresora
  const colaImpresion = new Cola(); // Cola para almacenar los documentos a imprimir

// Función para imprimir un documento
function imprimir() {
  if (!colaImpresion.estaVacia()) {
    const documento = colaImpresion.dequeue();
    console.log(`Imprimiendo documento: ${documento}`);
  } else {
    console.log("No hay documentos para imprimir");
  }
}

// Función para añadir un documento a la cola de impresión
function agregarDocumento(documento) {
  colaImpresion.enqueue(documento);
  console.log(`Documento "${documento}" añadido a la cola de impresión`);
}

// Ejemplo de uso
agregarDocumento("Documento 1");
agregarDocumento("Documento 2");
agregarDocumento("Documento 3");

imprimir(); // Imprimiendo documento: Documento 1
imprimir(); // Imprimiendo documento: Documento 2

agregarDocumento("Documento 4");

imprimir(); // Imprimiendo documento: Documento 3
imprimir(); // Imprimiendo documento: Documento 4