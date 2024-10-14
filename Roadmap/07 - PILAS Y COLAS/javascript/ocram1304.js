// Pila
class Pila {
    constructor() {
      this.stack = []
      this.top = 0
    }
  
    // Añade un elemento al final de la pila
    push(newValue) {
      this.stack.push(newValue)
      this.top += 1
    }
  
    // Regresa y remiueve el último elemento de la  pila
    pop() {
      if (this.top !== 0) {
        this.top -= 1
        return this.stack.pop()
      }
      throw new Error('Stack Underflow')
    }
  
    // Regresa el número de elementos de la pila
    get length() {
      return this.top
    }
  
    // Regresa si la pila estta vacia
    get isEmpty() {
      return this.top === 0
    }
  
    // Regresa  el último elemento sin removerlo "peak"
    get last() {
      if (this.top !== 0) {
        return this.stack[this.stack.length - 1]
      }
      return null
    }
  
    // Checa si un objeto es instancia de la clase pila
    static isStack(el) {
      return el instanceof Stack
    }
  }
  //Cola
  class Cola{
    //Constructor de la cola
    constructor(){
      this.queue  = [];

    }
    //Añadir un nuevo valor a la cola (encolar)
    push( value){
        this.queue .push(value);
    }
    //Eliminar el primer elemento de la cola (des-encolar)
    pop(){
      if(this.queue.length !==  0){
        return this.queue.shift();
      }
     throw new  Error("Cola vacia");
    }
    //Obtener el frente de la cola
    get FrenteCola(){
      if(this.queue.length !==  0){
        return this.queue[0];
      }
      throw new  Error("Cola vacia");
    }
    //Obtener el final de la cola
   get FinalCola(){
    if(this.queue.length !==  0){
      return this.queue[this.queue.length-1];
    }
    throw new  Error("Cola vacia");
    }
    //Verificar si la cola está vacia
    isEmpty(){
      return this.queue.length === 0;
    }

  }

  //Dificultad extra
  //Pagina atras/adelante
  class Pagina {
    constructor(actual) {
      this.anterior = new Pila();
      this.actual = actual; 
      this.siguiente = new Pila(); 
    }
  
    get paginaActual() { 
      return this.actual;
    }
  
    avanzarSiguiente() { 
      if (!this.siguiente.isEmpty()) { 
        this.anterior.push(this.actual);
        this.actual = this.siguiente.pop();
      }
      return this.actual;
    }
  
    avanzarAnterior() { 
      if (!this.anterior.isEmpty()) {
        this.siguiente.push(this.actual);
        this.actual = this.anterior.pop();
      }
      return this.actual;
    }
  }

  class Impresora {
    constructor(documento) {
      this.documento = documento;
      this.flujo = new Cola();
      this.documentoImpreso;
    }
  
    encolarDocumento() {
      if(this.documento.trim() !== ""){
        this.flujo.push(this.documento.slice(0, 1)); 
      }
      else{
        throw new Error("No hay documentos para imprimir");
      }
      
    }
  
    imprimirDocumento() {
      if (!this.flujo.isEmpty()) {
        this.documentoImpreso = this.flujo.pop(); // Asigna el documento impreso a la propiedad
        return this.documentoImpreso;
      }
      throw new Error("No hay documentos para imprimir"); // Lanza un error si no hay documentos
    }
  }
  

