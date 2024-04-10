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
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */



/* Soluciones */


// Estructuras


class Pila {
  constructor() {
    this.pila = [];
  }

  apilar(elemento) {
    this.pila.push(elemento);
  }

  desapilar() {
    return this.pila.pop();
  }

  estaVacia() {
    return this.pila.length === 0;
  }
}


// Ejemplo de uso

const miPila = new Pila();

miPila.apilar("Hola");
miPila.apilar("Mundo");
miPila.apilar("!");

console.log(`Primer elemento: ${miPila.desapilar()}`); // Salida: !
console.log(`Segundo elemento: ${miPila.desapilar()}`); // Salida: Mundo
console.log(`¿Pila vacía?: ${miPila.estaVacia()}`); // Salida: false
console.log(`Último elemento: ${miPila.desapilar()}`); // Salida: Hola
console.log(`¿Pila vacía?: ${miPila.estaVacia()}`); // Salida: true


class Cola {
  constructor() {
    this.cola = [];
  }

  encolar(elemento) {
    this.cola.push(elemento);
  }

  desencolar() {
    return this.cola.shift();
  }

  estaVacia() {
    return this.cola.length === 0;
  }
}


// Ejemplo de uso

const miCola = new Cola();

miCola.encolar("Primero");
miCola.encolar("Segundo");
miCola.encolar("Tercero");

console.log(`Primer elemento: ${miCola.desencolar()}`); // Salida: Primero
console.log(`Segundo elemento: ${miCola.desencolar()}`); // Salida: Segundo
console.log(`¿Cola vacía?: ${miCola.estaVacia()}`); // Salida: false
console.log(`Último elemento: ${miCola.desencolar()}`); // Salida: Tercero
console.log(`¿Cola vacía?: ${miCola.estaVacia()}`); // Salida: true



/* Extra - Opcional */



// Navegador Web


class NavegadorWeb {
  constructor() {
    this.historial = new Pila();
    this.paginaActual = null;
  }

  navegar(url) {
    if (this.paginaActual) {
      this.historial.apilar(this.paginaActual);
    }
    this.paginaActual = url;
  }

  adelante() {
    if (!this.historial.estaVacia()) {
      this.paginaActual = this.historial.desapilar();
    }
  }

  atras() {
    if (!this.historial.estaVacia()) {
      const aux = this.historial.desapilar();
      this.paginaActual = this.historial.desapilar();
      this.historial.apilar(aux);
    }
  }

  mostrarPaginaActual() {
    console.log(`Página actual: ${this.paginaActual}`);
  }
}

const navegador = new NavegadorWeb();

navegador.navegar("www.google.com");
navegador.navegar("www.youtube.com");
navegador.navegar("www.facebook.com");

navegador.mostrarPaginaActual(); // Salida: Página actual: www.facebook.com

navegador.atras();

navegador.mostrarPaginaActual(); // Salida: Página actual: www.youtube.com

navegador.adelante();

navegador.mostrarPaginaActual(); // Salida: Página actual: www.facebook.com



// Impresora Compartida


class Impresora {
  constructor() {
    this.colaImpresion = new Cola();
  }

  imprimir() {
    if (!this.colaImpresion.estaVacia()) {
      console.log(`Imprimiendo documento: ${this.colaImpresion.desencolar()}`);
    }
  }

  agregarDocumento(nombreDocumento) {
    this.colaImpresion.encolar(nombreDocumento);
  }
}

const impresora = new Impresora();

impresora.agregarDocumento("documento1.pdf");
impresora.agregarDocumento("documento2.docx");
impresora.agregarDocumento("documento3.jpg");


// Ejemplo de uso

while (true) {
  const comando = prompt("Introduzca comando (imprimir, nombre_documento): ");

  if (comando === "imprimir") {
    impresora.imprimir();
  } else {
    impresora.agregarDocumento(comando);
  }
}

