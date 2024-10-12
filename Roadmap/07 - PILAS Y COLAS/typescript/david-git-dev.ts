/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).*/
//pilas (stacks - LIFO)
class Stack {
  private stack: string[] = [];
  constructor() {}
  agregar(value: string) {
    this.stack.push(value);
  }
  eliminar() {
    this.stack.pop();
  }
  get getStack() {
    return this.stack;
  }
}
//las colas (queue - FIFO)
class Queque {
  private queque: string[] = [];
  constructor() {}
  agregar(value: string) {
    this.queque.unshift(value);
  }
  eliminar() {
    this.queque.pop();
  }
  get getQueque() {
    return this.queque;
  }
}
const cola = new Queque();
const pila = new Stack();
cola.agregar("cliente1");
cola.agregar("cliente2");
cola.agregar("cliente3");
cola.eliminar();
cola.eliminar();
pila.agregar("cliente4");
pila.agregar("cliente5");
pila.agregar("cliente6");
pila.eliminar();
pila.eliminar();
console.log(cola.getQueque, pila.getStack);

 /*
  DIFICULTAD EXTRA (opcional):
  - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    el nombre de una nueva web.*/
class WebBrowser{
  private searchBar:string[]=[]
  constructor(){

  }
   search(url:string){
this.searchBar.push(url);
   }
   /*adelante(){
    /* const history = this.searchBar.length
    if(history>1){
      const url = this.searchBar.shift()
      this.searchBar.push(url as string)
    console.log(url);
    }else{
    console.log('ya estas en la pagina mas actual');

    } */
   atras(url:string){
    const history = this.searchBar.length
    if(history>1){
      const url = this.searchBar.pop()
    }else{
      console.log('blank tab...');
    }
  }
}
  /*
  - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    impresora compartida que recibe documentos y los imprime cuando así se le indica.
    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    interpretan como nombres de documentos.
 */
    class Printer {
      private queque: string[] = [];
      constructor() {}
      set add(doc: string) {
        this.queque.unshift(doc);
      }
      print() {
        return this.queque.length > 0 ? this.queque.pop() : 'No hay nada para imprimir...';
      }
      get getQueque() {
        return this.queque;
      }
    }
    function startPrinter() {
      const printer = new Printer();
      console.log("//Iniciando interfaz....");
      let data: string | null;
      do {
        data = prompt(
          "Dame el nombre del documento o escribe imprimir para comenzar a trabajar..."
        );

        if (data && data.toLocaleLowerCase() !== "imprimir") {
          printer.add = data.toLowerCase();
          alert(`agregado ->${data}`);
        } else if (data && data.toLowerCase() === "imprimir") {
          alert(`Imprimiendo->${printer.print()}`);
        }
            if(data) alert(printer.getQueque.toString())

      } while (data && printer.getQueque.length>0);
    }
    startPrinter();
