/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
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
