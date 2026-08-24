// https://www.typescriptlang.org/

// Pila (LIFO) con array
const stack: number[] = [];
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.pop()); // 3
console.log(stack);       // [1, 2]

// Cola (FIFO) con array
const queue: number[] = [];
queue.push(10);
queue.push(20);
queue.push(30);
console.log(queue.shift()); // 10
console.log(queue);         // [20, 30]

// Dificultad extra

// Navegador con pila
class Browser {
  private back: string[] = [];
  private forward: string[] = [];
  private current: string = "";

  visit(page: string): void {
    if (this.current) this.back.push(this.current);
    this.current = page;
    this.forward = [];
    console.log(`Página actual: ${this.current}`);
  }

  goBack(): void {
    if (this.back.length === 0) {
      console.log("No hay páginas anteriores");
      return;
    }
    this.forward.push(this.current);
    this.current = this.back.pop()!;
    console.log(`Página actual: ${this.current}`);
  }

  goForward(): void {
    if (this.forward.length === 0) {
      console.log("No hay páginas siguientes");
      return;
    }
    this.back.push(this.current);
    this.current = this.forward.pop()!;
    console.log(`Página actual: ${this.current}`);
  }
}

const browser = new Browser();
browser.visit("google.com");
browser.visit("github.com");
browser.visit("typescriptlang.org");
browser.goBack();
browser.goBack();
browser.goForward();

// Impresora con cola
class Printer {
  private queue: string[] = [];

  addDocument(name: string): void {
    this.queue.push(name);
    console.log(`Documento "${name}" añadido a la cola`);
  }

  print(): void {
    if (this.queue.length === 0) {
      console.log("No hay documentos en cola");
      return;
    }
    const doc = this.queue.shift()!;
    console.log(`Imprimiendo: ${doc}`);
  }
}

const printer = new Printer();
printer.addDocument("informe.pdf");
printer.addDocument("factura.pdf");
printer.addDocument("contrato.docx");
printer.print();
printer.print();
printer.print();
printer.print();
