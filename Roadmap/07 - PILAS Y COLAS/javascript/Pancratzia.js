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

/************************ PARTE 1 ************************/

/***** PILAS *****/
/*
Una PILA es una estructura de datos que almacena datos en una secuencia. Solo hay una forma para alegrar elementos y estos se incorportanen un orden determinado. Operan bajo la modalidad llamada LIFO, es decir, siempre el último elemento agregado va a ser el primero que saquemos. 
Un ejemplo de pila es el historial del navegador, donde podemos ver que cada página que visitamos se monta encima de la anterior. Esto genera una pila de registros, y podemos volver a ella dando click al botón de "Volver" del navegador.
*/
/****************/

class Pila {
  constructor() {
    this.pila = [];
  }

  push(elemento) {
    this.pila.push(elemento);
  }

  pop() {
    this.pila.pop();
  }

  peek() {
    return this.pila[this.pila.length - 1];
  }

  size() {
    return this.pila.length;
  }

  print() {
    return this.pila;
  }
}

const ejemploPila = new Pila();

console.log(
  `Al inicio, la pila está vacía por lo que el size() devolverá 0: ${ejemploPila.size()}`
);

for (let i = 0; i < 5; i++) {
  ejemploPila.push(i);
}

console.log(
  `Luego del push, la pila tiene ${ejemploPila.size()} elementos, que son: ${ejemploPila.print()}`
);
console.log(
  `El peek o primer elemento de la pila es: ${ejemploPila.peek()}. Recuerda que este es el último elemento agregado a la pila.`
);

ejemploPila.pop();

console.log(
  `Luego del pop, la pila tiene ${ejemploPila.size()} elementos, que son: ${ejemploPila.print()}. Su peek ahora es ${ejemploPila.peek()}`
);

/***** COLAS *****/
/*
Una COLA es una estructura de datos que almacena datos en una secuencia. La operacion de inserción de un elemento en la COLA se llama encolar y la operación de extracción de un elemento se llama desencolar. Operan bajo la modalidad llamada FIFO, es decir, siempre el primer elemento agregado va a ser el primero que se extraiga.
Un ejemplo de cola es la cola de un banco, donde podemos ver que los clientes en la cola son los primeros en ser atendidos. 
*/
/****************/

class Cola {
  constructor() {
    this.cola = [];
  }

  encolar(elemento) {
    this.cola.push(elemento);
  }

  desencolar() {
    this.cola.shift();
  }

  peek() {
    return this.cola[0];
  }

  size() {
    return this.cola.length;
  }

  print() {
    return this.cola;
  }
}

const ejemploCola = new Cola();
console.log(
  `Al inicio, la cola está vacia por lo que el size() devolverá 0: ${ejemploCola.size()}`
);

for (let i = 0; i < 5; i++) {
  ejemploCola.encolar(i);
}

console.log(
  `Luego del encolar, la cola tiene ${ejemploCola.size()} elementos, que son: ${ejemploCola.print()}`
);
console.log(
  `El peek o primer elemento de la cola es: ${ejemploCola.peek()}. Recuerda que este es el primero en ser encolado y el primero que será desencolado.`
);
ejemploCola.desencolar();

console.log(
  `Luego del desencolar, la cola tiene ${ejemploCola.size()} elementos, que son: ${ejemploCola.print()}. Su peek ahora es ${ejemploCola.peek()}`
);

/************************ PARTE 2 ************************/

class NavegadorWeb {
  constructor() {
    this.historial = new Pila();
    this.paginaActual = "";
    this.indexPaginaActual = 0;
  }

  navegar(pagina) {
    this.historial.push(pagina);
    this.paginaActual = pagina;
    this.indexPaginaActual = this.historial.size() - 1;
  }

  adelante() {
    if (this.historial.size() > 0) {
      this.indexPaginaActual++;
      this.paginaActual = this.historial.pila[this.indexPaginaActual]
    } else {
      console.log("No hay historial en este navegador");
    }
  }

  atras() {
    if (this.historial.size() > 0) {
        this.indexPaginaActual--;
        this.paginaActual = this.historial.pila[this.indexPaginaActual]
    } else {
      console.log("No hay historial en este navegador");
    }
  }

  mostrarPaginaActual(){
    return this.paginaActual;
  }
}

const navegador = new NavegadorWeb();

navegador.atras()
navegador.adelante() //No hay historial actualmente

navegador.navegar("https://www.google.com")
navegador.navegar("https://www.facebook.com")
navegador.navegar("https://www.twitter.com")
navegador.navegar("https://www.youtube.com")
navegador.navegar("https://www.linkedin.com")

console.log(`Tu historial actual es: ${navegador.historial.print()}. Y te encuentras en al página ${navegador.mostrarPaginaActual()}`);

navegador.atras()
navegador.atras()
navegador.atras()
navegador.atras()

console.log(`Ahora te encuentras en la página: ${navegador.mostrarPaginaActual()}`);

