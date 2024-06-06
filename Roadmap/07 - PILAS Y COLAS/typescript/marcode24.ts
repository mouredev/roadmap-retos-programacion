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

class Stack<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  push(element: T): void {
    this.items.push(element);
  }

  pop(): T | string {
    if (this.isEmpty()) {
      return 'La pila está vacía';
    }
    return this.items.pop() as T;
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  clear(): void {
    this.items = [];
  }

  size(): number {
    return this.items.length;
  }
}

class Queue<T> {
  private items: T[];

  constructor() {
    this.items = [];
  }

  enqueue(element: T): void {
    this.items.push(element);
  }

  dequeue(): T | string {
    if (this.isEmpty()) {
      return 'La cola está vacía';
    }
    return this.items.shift() as T;
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  size(): number {
    return this.items.length;
  }
}

const pila = new Stack<number>();
pila.push(1);
pila.push(2);
pila.push(3);
console.log(pila.pop()); // 3
console.log(pila.pop()); // 2

const cola = new Queue<string>();
cola.enqueue('a');
cola.enqueue('b');
cola.enqueue('c');
console.log(cola.dequeue()); // a
console.log(cola.dequeue()); // b

class Navegador {
  private history: Stack<string>;
  private future: Stack<string>;
  private currentPage: string | null;

  constructor() {
    this.history = new Stack<string>();
    this.future = new Stack<string>();
    this.currentPage = null;
  }

  // navegar a una nueva página
  goToPage(page: string): void {
    if (this.currentPage !== null) {
      this.history.push(this.currentPage);
    }
    this.currentPage = page;
    this.future.clear();
    console.log('Página actual: ', this.currentPage);
  }

  // retroceder a la página anterior
  goBack(): void {
    if (this.history.isEmpty()) {
      console.log('No hay páginas anteriores');
      return;
    }
    this.future.push(this.currentPage as string);
    this.currentPage = this.history.pop() as string;
    console.log('Página actual: ', this.currentPage);
  }

  // avanzar a la página siguiente
  goForward(): void {
    if (this.future.isEmpty()) {
      console.log('No hay páginas siguientes');
      return;
    }
    this.history.push(this.currentPage as string);
    this.currentPage = this.future.pop() as string;
    console.log('Página actual: ', this.currentPage);
  }
}

const navegador = new Navegador();
navegador.goToPage('google.com');
navegador.goToPage('facebook.com');
navegador.goToPage('twitter.com');
navegador.goBack(); // regresa a facebook.com
navegador.goBack(); // regresa a google.com
navegador.goForward(); // avanza a facebook.com
navegador.goToPage('instagram.com'); // instagram.com
navegador.goBack(); // regresa a facebook.com
navegador.goForward(); // avanza a instagram.com

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
