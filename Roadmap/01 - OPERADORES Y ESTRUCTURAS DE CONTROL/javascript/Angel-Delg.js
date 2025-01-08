// Operador de asignación " = " para asignar cada fruta
const Pineapple = '🍍'
const Apple = '🍎'
const Grapes = '🍇'

// podemos usar " + " para concatenar strings
const Apples = Apple + '🍎'
const Pineapples = Pineapple + '🍍'

console.log(Apples) // output: '🍎🍎'
console.log(Pineapples) // output: '🍍🍍'
console.log(Grapes) // output: '🍇'

// Podemos realizar operaciones matemáticas usando + , -, / and  *

const amountApples = 2
let amountPeoples = 1

// Podemos usar " - " para restar elementos de tipos numbers
console.log(amountApples - amountPeoples);  // output: 1

// Tambien podemos multiplicar el numero de manzanas por el numero de personas
console.log(amountApples * amountPeoples); // output: 2

// Y dividir el numero de manzanas por la cantidad de personas que hay.
console.log(amountApples / amountPeoples); // output: 2

// podemos usar operador de modulo para saber el reciduo de una divisió " % "
let ram = Math.ceil(Math.random() * 10);
(ram % 2 === 0) ? console.log("Par") : console.log("Impar");

/* 
   ====================================================================
      Operadores logicos : and, or, not
   ====================================================================
*/

let and = true && false // output: false
let or = false || true // output: true
let negacion = !false // output: true
!!negacion // true
!![]; // true
![]; // false
// Tambien podemos realizar condiciónes rapidas

const response = '🍉'
response === '🍏' && true // output: false 
response === '🍉' || false // output: false

/* 
   ====================================================================
      podemos realizar estructuras de control selectiva o condicional.
   ====================================================================
*/

const seasons = {
   Summer: '🍉',
   Spring: '🍓',
   Winter: '🥝',
   Autumn: '🍑'
}

// podemos realizar una operación selectiva para saber que comer dependiendo de la estación del año
const currentSeason = "Summer"

if(seasons[currentSeason]){
   console.log(`Hora de comer ${seasons[currentSeason]}`);
}

/* 
   ====================================================================
      Tambien puede existir un caso else
   ====================================================================
*/

const FruitBox = {
   Pineapple: 10,
   Apples: 5,
   Tangerine: 14,
   Kiwi: 20
}

// podemos verificar si hay frutas para todos en la playa

const Peoples = 9

if(FruitBox["Pineapple"] >= Peoples){
   console.log("Hay piñas para todos");
}
else {
   console.log("Ohh no alguien no alcanzo a comer piña")
}

/* 
   ====================================================================
      Tambien podemos realizar multiples casos usando switch, case
   ====================================================================
*/

const day = new Date().getDay();

switch(day){
   case 0:{
      console.log("Sunday")
      break;
   }
   case 1:{
      console.log("Monday");
      break;
   }
   case 2:{
      console.log("Tuesday");
      break;
   }
   case 3:{
      console.log("Wednesday");
      break
   }
   case 4:{
      console.log("Thursday")
      break
   }
   case 5:{
      console.log("Friday");
      break
   }
   case 6:{
      console.log("Saturday");
      break;
   }
   default:{
      console.log("This day is incorrect!");
   }
}
// como puedes observar tiene varios caso en dependencia del dia de la semana que te encuentres

/* 
   ====================================================================
      Estructura de control repetitiva o ciclica: for, do while, while, for of, for in
   ====================================================================
*/

// la estructura del for(variable inicializada; condición ; proceso de incremento)
for(let i = 0; i < Math.ceil(Math.random() * 40); i++){
   console.log(i);
}
/*
   Math.ceil(Math.random() * 40) => numero aleatorio 0 - 40
   por lo que puede terminar en cualquier número que se encuentre en ese rango
*/

let counter = 0;

do{
   // realizar proceso
   console.log(counter);
   counter++;
}while(counter != 10);


// tambien podemos usar while
counter = 0

// en este caso primero evalua la condición para ver si entra en el ciclo, por lo tanto en un 
// do while primero realiza un proceso y luego evalua la condición
while(counter != 10){
   console.log(counter)
   counter++;
}

/*
   Algunas abreviaciones.

   "counter++" = "counter += 1" = "counter = counter + 1"
   "counter--" = "counter -= 1" = "counter = counter - 1"

   "counter *= 2" = "counter = counter * 2"
   "counter /= 2" = "counter = counter / 2"
*/

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

for(let i = 10; i <= 55; i+=1){
   if(i % 2 === 0 && i !== 16 && i % 3 !== 0){
      console.log(i);
   }
}
