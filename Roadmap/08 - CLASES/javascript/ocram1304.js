//Clases
class Persona{
    #nombre;
    #edad;
    #sexo;
    #carrera;
    constructor(nombre,edad, sexo,carrera){
        this.#nombre=  nombre;
        this.#sexo = sexo;
        this.#edad = edad;
        this.#carrera = carrera;

    }
    saludos(){
        console.log(`Hola soy ${this.#nombre}, tengo ${this.#edad} y soy ${this.#carrera}`);

    }
    actualizar(nuevaEdad,nuevaCarrera){
        this.#edad = nuevaEdad;
        this.#carrera = nuevaCarrera;
    }

}
const  Gerardo  = new Persona("Gerardo",23,"masculino","Sistemas");
Gerardo.saludos();
Gerardo.actualizar(24,"Barbero");
Gerardo.saludos();

//Difucultad  extra
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

    showItems(){
        if(!this.isEmpty()){
            for(let i= 0; i< top;i++){
            console.log(this.stack[i]);
             }
        }
        else{
            throw new Error ("Pila  vacia"); 
        }
        
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

  const monedas = new Pila();
  monedas.push("1");
  monedas.push("5");
  monedas.push("10");
  monedas.push("20");
  monedas.showItems();

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
    showItems(){
        if(!this.isEmpty()){
            for(let i  = this.queue.length-1;i>=0;i--){
                console.log(this.queue[i]);
            }
        }
        else{
            throw new Error ("Cola vacia");
        }
        
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

  const filaTortillas = new Cola();
  filaTortillas.push(1);
  filaTortillas.push(2);
  filaTortillas.push(3);
  filaTortillas.push(4);
  filaTortillas.showItems();
