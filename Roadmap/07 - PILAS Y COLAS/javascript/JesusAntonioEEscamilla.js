/** #07 - JavaScript ->Jesus Antonio Escamilla */
/**
 * En JavaScript, las pilas y colas son estructuras de datos comúnmente utilizadas para organizar y gestionar elementos.
 * El LIFO (Last In, First Out) es conocido como Pila, se van apilando y sale el ultimo
 * El FIFO (First In, First Out) es conocida como Cola, el primero en entrar a la cola es primero en salir
 */

//-----PILAS(STACKS - LIFO)-----

const stack = [];

// Introducir elemento en la pila
function pushPila(elemento) {
   stack.push(elemento);
}

// Elimina el ultimo elemento de la pila
function pop() {
   if (stack.length === 0) {
      return "La pila está vacía";
   }
   return stack.pop();
}

// Obtiene el ultimo elemento de la pila no eliminado
function peek() {
   return stack[stack.length - 1];
}

// Obtener el tamaño de la pila
function sizePila() {
   return stack.length;
}

// Ejemplo de uso de la Pila
pushPila(1);
pushPila(2);
pushPila(3);
pushPila(4);

console.log(pop()); // Imprime el 4 que es el elemento eliminado
console.log(peek()); // Imprime el 3 porque es el ultimo elemento de la pila
console.log(sizePila()); // Imprime el tamaño de la pila que es de 3



//-----COLAS(QUEUES - FIFO)-----

const enqueue = [];

// Introducir elemento en la cola
function enqueueCola(elemento) {
   enqueue.push(elemento);
}

// Elimina el primero elemento de la pila
function dequeue() {
   if (enqueue.length === 0) {
      return "La cola está vacía";
   }
   return enqueue.shift();
}

// Obtener el primer elemento de la cola sin eliminarlo
function front() {
   return enqueue[0];
}

// Obtener el tamaño de la cola
function sizeCola() {
   return enqueue.length;
}

// Ejemplo de uso de la Cola
enqueueCola(1);
enqueueCola(2);
enqueueCola(3);
enqueueCola(4);

console.log(dequeue()); // Imprime el 1 que es el elemento eliminado
console.log(front()); // Imprime el 2 porque es el ultimo elemento de la cola
console.log(sizeCola()); // Imprime el tamaño de la cola que es de 3




/**-----DIFICULTAD EXTRA-----*/

/** PILA */
const navegadorWeb = {
   pilaPaginas: [],
   paginaActual: "Inicio",

   ir_A: function(pagina) {
      this.pilaPaginas.push(this.paginaActual);
      this.paginaActual = pagina;
      console.log(`Navegando a: ${this.paginaActual}`);
   },

   adelante: function() {
      if (this.pilaPaginas.length > 0) {
         this.paginaActual = this.pilaPaginas.pop();
         console.log(`Página siguiente: ${this.paginaActual}`);
      } else {
         console.log("No hay páginas siguientes");
      }
   },

   atrás: function() {
      if (this.paginaActual !== "Inicio") {
         this.pilaPaginas.push(this.paginaActual);
         this.paginaActual = "Inicio";
         console.log(`Página anterior: ${this.paginaActual}`);
      } else {
         console.log("No hay páginas anteriores");
      }
   }
};

 // Ejemplo para ejecutar el programa
navegadorWeb.ir_A("Google");
navegadorWeb.ir_A("OpenAI");
navegadorWeb.ir_A("moureDev");
navegadorWeb.adelante();
navegadorWeb.atrás();



/** COLA */
const impresoraCompartida = {
   colaDocumentos: [],

   recibirDocumento: function(documento) {
      this.colaDocumentos.push(documento);
      console.log(`Documento recibido: ${documento}`);
   },

   imprimir: function() {
      if (this.colaDocumentos.length > 0) {
         const documento = this.colaDocumentos.shift();
         console.log(`Imprimiendo documento: ${documento}`);
      } else {
         console.log("No hay documentos en la cola para imprimir");
      }
   }
};

 // Ejemplo de uso de la impresoraCompartida
impresoraCompartida.recibirDocumento("Contrato.pdf");
impresoraCompartida.recibirDocumento("Informe.docx");
impresoraCompartida.recibirDocumento("Factura.pdf");
impresoraCompartida.imprimir();
impresoraCompartida.imprimir();

/**-----DIFICULTAD EXTRA-----*/