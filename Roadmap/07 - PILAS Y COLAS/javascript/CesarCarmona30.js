/**
 * EJERCICIO
 */

// PILA
let stack = [];

// Push
stack.push('Cucumber');
stack.push('Radish');
stack.push('Tomato');
stack.push('Orange');
stack.push('Apple');

console.table(stack);

// Pop
stack.pop()
console.table(stack);
stack.pop()
console.table(stack);

// COLA
let queue = [];

// Enqueue
queue.push('Banana');
queue.push('Melon');
queue.push('Strawberry');
queue.push('Onion');
queue.push('Garlic');
console.table(queue);

// Dequeue
queue.shift();
console.table(queue);
queue.shift();
console.table(queue);

//PILA - Navegador
//COLA - Impresora

class WebBrowser {
  constructor() {
    this.pages = [];
    this.index = null
    this.currentPage = null;
  }

  addPage(page) {
    this.pages.push(page);
    this.index = this.pages.length - 1;
    this.currentPage = this.pages[this.index];
  }

  goForward() {
    this.currentPage = this.pages[this.index++];
    if (this.currentPage != undefined) {
      return this.currentPage;
    }
    this.index--;
    console.error('Sin referencia de página adelante');
    return '-';
  }

  goBackward() {
    try {
      this.currentPage = this.pages[this.index--];
      return this.currentPage;
    } catch (error) {
      this.index++;
      console.error('Sin páginas en el historial');
      return '-';
    }
  }
}

function browserHistory(browser, input) {
    let page;
    console.log(`>_${input}`);
    switch (input) {
      case 'adelante':
        page = browser.goForward();
        console.log(`Página actual: ${page}`);
        break;
      case 'atras':
        page = browser.goBackward();
        console.log(`Página actual: ${page}`);
        break;
      case 'salir':
        break;
      default:
        let new_page = input;
        browser.addPage(new_page);
        console.log(`Nueva página: ${new_page}`);
        break;
  }
}

const edge = new WebBrowser();
browserHistory(edge, 'Wikipedia');
browserHistory(edge, 'YouTube');
browserHistory(edge, 'Amazon');
browserHistory(edge, 'atras');
browserHistory(edge, 'atras');
browserHistory(edge, 'adelante');