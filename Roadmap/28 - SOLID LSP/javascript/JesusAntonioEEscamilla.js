/** #28 - JavaScript -> Jesus Antonio Escamilla */

/**
 * Principio de Segregación de Interfaces: Una clase no debe estar obligada a implementar interfaces que no usa.
 * En lugar de tener una interfaz grande y general, se deben tener varias interfaces específicas y pequeñas.
 * Este principio establece que los objetos de una clase derivada deben poder ser sustituidos por objetos de la
   clase base sin alterar el funcionamiento del programa.
 */

//---EJERCIÓ---
//INCORRECTO
class Bird_{
   fly(){
      throw new Error("This method should be overridden");
   }
}

class Eagle_ extends Bird_{
   fly(){
      return "Eagle flying high!";
   }
}

class Penguin_ extends Bird_{
   fly(){
      return"Penguin can't flying!";
   }
}

const eagle_ = new Eagle_();
const penguin_ = new Penguin_();

console.log(eagle_.fly());
console.log(penguin_.fly());


//CORRECTO
class Bird{
   move(){
      throw new Error("This method should be overridden");
   }
}

class Eagle extends Bird{
   move(){
      console.log("Eagle is Walking!!");
   }
}

class Penguin extends Bird{
   move(){
      console.log("Penguin is Walking!!");
   }
}

function makeBirdMove(bird) {
   bird.move();
}

const eagle = new Eagle();
const penguin = new Penguin();

makeBirdMove(eagle);
makeBirdMove(penguin);



/**-----DIFICULTAD EXTRA-----*/

// Creando la clase
class Vehículos{
   constructor(){
      this.speed = 0;
   }

   acelerar(){
      throw new Error("Método 'acelerar' debe ser implementado");
   }

   frenar(){
      throw new Error("Método 'frenar' debe ser implementado");
   }

   getSpeed(){
      return this.speed;
   }
}

// Sub-clases la clase principal
class Coche extends Vehículos{
   acelerar(speed){
      console.log(`El coche esta acelerando, con ${speed} km/h`);
   }

   frenar(speed){
      console.log(`El coche esta frenando, con ${speed} km/h`);
   }
}

class Trailer extends Vehículos{
   acelerar(speed){
      console.log(`El tailer esta acelerando, con ${speed} km/h`);
   }

   frenar(speed){
      console.log(`El trailer esta frenando, con ${speed} km/h`);
   }
}

class Moto extends Vehículos{
   acelerar(speed){
      console.log(`El moto esta acelerando, con ${speed} km/h`);
   }

   frenar(speed){
      console.log(`El moto esta frenando, con ${speed} km/h`);
   }
}

// Comprobación del LSP
function pruebaLSP(vehículo) {
   vehículo.acelerar(2);
   vehículo.frenar(1);
}

// Ejemplo LSP
const coche = new Coche();
const trailer = new Trailer();
const moto = new Moto();

// console.log("Prueba con Coche:");
pruebaLSP(coche);

// console.log("Prueba con Trailer:");
pruebaLSP(trailer);

// console.log("Prueba con Moto:");
pruebaLSP(moto);

/**-----DIFICULTAD EXTRA-----*/