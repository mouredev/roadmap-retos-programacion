/*---Clase---*/
class miclase{
    constructor(nombre, pais){
        this.nombre = nombre;
        this.pais = pais;
    }
    saludar(){
        console.log("Bienvenido a " + this.pais +" "+ this.nombre);
    }
}

let bienvenido = new miclase("Julio","Guatemala");
bienvenido.saludar(); //Bienvenido a Guatemala Julio

bienvenido.pais = "Peten";
bienvenido.saludar(); //Bienvenido a Peten Julio

/*---Dificultad extra---*/
//--Pila
class Pila {
   constructor(pila) {
           this.pila =[]
   }
   push(elemento){
       return this.pila.push(elemento)
   }
   pop(){
       if(this.size()===0){
           return "Cola vacia";
       }
       return this.pila.pop();
   }
   size(){
       return this.pila.length;
   }
   print(){
       this.pila.forEach((element) => {
           console.log(element);         
       });
   }  
}


let mipila = new Pila();
mipila.push(1);
mipila.push(2);
mipila.push(3);
mipila.pop(); // 3
mipila.pop(); // 2
mipila.print();//1
//mipila.size();


//---Cola
class Cola {
   constructor(cola) {
           this.cola =[];
   }
   enqueue(elemento){
       return this.cola.push(elemento);
   }
   dequeue(){
       if(this.size()===0){
           return "Cola vacia";
       }
       return this.cola.shift();
   }
   size(){
       return this.cola.length;
   }
   print(){
       this.cola.forEach((element) => {
           console.log(element);         
       });
   }  
}

let micola = new Cola();
micola.enqueue(1);
micola.enqueue(2);
micola.enqueue(3);
micola.dequeue(); // 1
micola.dequeue(); // 2
micola.print();//3
//micola.size();

