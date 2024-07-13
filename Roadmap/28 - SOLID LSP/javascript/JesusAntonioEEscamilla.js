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
      console.log("Flying");
   }
}

class Eagle_ extends Bird_{
   fly(){
      console.log("Eagle flying high!");
   }
}

class Penguin_ extends Bird_{
   fly(){
      throw new Error("Penguins can't fly!!");
   }
}

function makeBirdFly_(bird) {
   bird.fly();
}

const eagle_ = new Eagle_();
const penguin_ = new Penguin_();

makeBirdFly_(eagle_);
makeBirdFly_(penguin_);


//CORRECTO
class Bird{
   move(){
      console.log("Moving");
   }
}

class FlyingBird extends Bird{
   fly(){
      console.log("Flying");
   }
}

class Eagle extends FlyingBird{
   fly(){
      console.log("Eagle flying high!!");
   }
}

class Penguin extends Bird{
   move(){
      console.log("Penguin waddling");
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

// Pendiente

/**-----DIFICULTAD EXTRA-----*/