// Implementación de una pila (stack) utilizando un array
function crearPila() {
  const items = [];

  function push(element) {
    items.push(element);
  }

  function pop() {
    if (isEmpty()) {
      return "La pila está vacía";
    }
    return items.pop();
  }

  function isEmpty() {
    return items.length === 0;
  }

  function peek() {
    if (isEmpty()) {
      return "La pila está vacía";
    }
    return items[items.length - 1];
  }

  function size() {
    return items.length;
  }

  return { push, pop, isEmpty, peek, size };
}

// Implementación de una cola (queue) utilizando un array
function crearCola() {
  const items = [];

  function enqueue(element) {
    items.push(element);
  }

  function dequeue() {
    if (isEmpty()) {
      return "La cola está vacía";
    }
    return items.shift();
  }

  function isEmpty() {
    return items.length === 0;
  }

  function front() {
    if (isEmpty()) {
      return "La cola está vacía";
    }
    return items[0];
  }

  function size() {
    return items.length;
  }

  return { enqueue, dequeue, isEmpty, front, size };
}

// Ejemplo de la pila
const pila = crearPila();
pila.push(1);
pila.push(2);
pila.push(3);

console.log("Elemento superior de la pila:", pila.peek());
console.log("Desapilando:", pila.pop());
console.log("Elemento superior de la pila después de desapilar:", pila.peek());

// Ejemplo de la cola
const cola = crearCola();
cola.enqueue("A");
cola.enqueue("B");
cola.enqueue("C");

console.log("Primer elemento de la cola:", cola.front());
console.log("Desencolando:", cola.dequeue());
console.log("Primer elemento de la cola después de desencolar:", cola.front());

// Ejercicio extra
// Pila
function simularNavegador() {
  const historial = crearPila();

  function navegarA(pagina) {
    historial.push(pagina);
    console.log("Navegando a:", pagina);
  }

  function adelante() {
    const paginaSiguiente = historial.pop();
    if (paginaSiguiente) {
      console.log("Avanzando a:", paginaSiguiente);
    } else {
      console.log("No hay páginas siguientes en el historial");
    }
  }

  function atras() {
    const paginaAnterior = historial.pop();
    if (paginaAnterior) {
      console.log("Retrocediendo a:", paginaAnterior);
    } else {
      console.log("No hay páginas anteriores en el historial");
    }
  }

  return { navegarA, adelante, atras };
}

// Uso
const navegador = simularNavegador();

navegador.navegarA("Google");
navegador.navegarA("Facebook");
navegador.navegarA("Twitter");

navegador.atras();
navegador.adelante();
navegador.atras();
navegador.atras();
navegador.adelante();
navegador.atras();

// Cola
function simularImpresora() {
  const colaImpresion = crearCola();

  function recibirDocumento(documento) {
    colaImpresion.enqueue(documento);
    console.log("Documento recibido:", documento);
  }

  function imprimir() {
    const documentoAImprimir = colaImpresion.dequeue();
    if (documentoAImprimir) {
      console.log("Imprimiendo documento:", documentoAImprimir);
    } else {
      console.log("No hay documentos en la cola de impresión");
    }
  }

  return { recibirDocumento, imprimir };
}

// Ejemplo de uso
const impresora = simularImpresora();

impresora.recibirDocumento("Documento1.txt");
impresora.recibirDocumento("Documento2.pdf");
impresora.recibirDocumento("Documento3.doc");

impresora.imprimir();
impresora.imprimir();
impresora.imprimir();
impresora.imprimir();
