/*
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   que representen todos los tipos de estructuras de control que existan
   en tu lenguaje:
   Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Operators (Operadores)

// Arithmetic Operators

// Addition Operator (+) 
let ageOne = 15;
let ageTwo = 20;
let ageAddition = ageOne + ageTwo;
console.log(`The age addition is ${ageAddition}`);

// Subtraction Operator (-)
let fathersAge = 42;
let daughtersAge = 8;
let ageDifference = fathersAge - daughtersAge;
console.log(`The age difference is ${ageDifference}`);

// Multiplication Operator (*)
let applesPerBox = 3;
let numberOfBoxes = 43;
let totalApples = applesPerBox * numberOfBoxes;
console.log(`The total amount of apples is ${totalApples}`);

// Exponentiation Operator (**)
let myBase = 2;
let myExponent = 3;
let myExponentiationResult = myBase ** myExponent;
console.log(`The result of the exponentiation is ${myExponentiationResult}`);

// Division Operator (/)
let myDividend = 540;
let myDivisor = 9;
let divisionResult = myDividend / myDivisor;
console.log(`The result of the dividion is ${divisionResult}`);

// Modulus Operator (%)
let myModulusDividend = 369;
let myModulusDivisor = 6;
let myModulusResult = myDividend % myDivisor;
console.log(`The modulus of this division is ${myModulusResult}`);

// Increment Operator (++)
let incrementalVariable = 0;
let incrementResult = ++incrementalVariable;
console.log(`The increment of this variable is ${incrementResult}`);

// Decrement Operator (--)
let decrementalVariable = 12;
let decrementResult = --decrementalVariable;
console.log(`The decrement of the variable is ${decrementResult}`)

// Assignment Operators
// (=) assigns a  value to a variable
let myShoes = "a pair of shoes";
let mySize = 42;
console.log(`I have ${myShoes} size ${mySize}`);
console.log(`Addition assignment operator (+=) size: ${mySize += 1}`);
console.log(`Subtraction assignment operator (-=) size: ${mySize -= 2}`);
console.log(`Multiplication assignment operator (*=) size: ${mySize *= 3}`);
console.log(`Division assignment operator (/=) size: ${mySize /= 3}`);
console.log(`Modulus assignment operator (%=) size: ${mySize %= 6}`);
console.log(`Exponentiation assignment operator (**=) size: ${mySize **= 2}`);

// Comparison Operators
let coordinateX = 2;
let errorMessage = "2"
let coordinateY = 7;
console.log(`Comparison Equal to (==). Is coordinateX equal to errorMessage: ${coordinateX == errorMessage}`); //allows type coercion (it converts operands to a common type before comparing)
console.log(`Comparison Equal value and equal type (===) ${coordinateX === coordinateY}`); //requires both the value and type to be the same.
console.log(`Comparison Not Equal (!=) ${coordinateX != coordinateY}`);
console.log(`Comparison Not equal value or not equal type (!==) ${coordinateX !== coordinateY}`);
console.log(`Comparison Greater than (>) ${coordinateX > coordinateY}`);
console.log(`Comparison Less than (<) ${coordinateX < coordinateY}`);
console.log(`Comparison Greater than or equal to (>=) ${coordinateX >= coordinateY}`);
console.log(`Comparison less than or equal to (<=) ${coordinateX <= coordinateY}`);
console.log(`Comparison ternary operator (?) Is it less? ${coordinateX < coordinateY ? "Yes it is" : "No it is not"}`);

// Logical Operators
const x = 3;
const y = 6;
const z = 9;
console.log(`Logical AND - This expresion is: ${(x < y) && (y < z)}`);
console.log(`Logical OR - This expresion is: ${(x < y) || (y > z)}`);
console.log(`Logical Not - This expresion is ${! (x > y)}`);

//Type Operators
console.log(typeof (x >= y));

class Vehicle{}
class Honda extends Vehicle{}
const myHonda = new Honda();

console.log(myHonda instanceof Honda);
console.log(myHonda instanceof Vehicle);
console.log(myHonda instanceof Object);

// Bitwise Operators
let myNumberX = 10;
let myNumberY = 3;
console.log(`Bitwise AND (&) ${myNumberX & myNumberY}`);
console.log(`Bitwise OR (|) ${myNumberX | myNumberY}`);
console.log(`Bitwise NOT (~) ${~ myNumberX}`);
console.log(`Bitwise XOR (^) ${myNumberX ^ myNumberY}`);
console.log(`Left shift (<<) ${myNumberX << myNumberY}`);
console.log(`Right shift (>>) ${myNumberX >> myNumberY}`);
console.log(`Unsigned right shift (>>>) ${myNumberX >>> myNumberY}`);

/* Control statements */

// if statements
let cupOfCoffee = "empty";
let coffeMakerStatus = "off";

if(cupOfCoffee === "full"){
   console.log("You can drink some coffee");
} else if (coffeMakerStatus === "off"){
   console.log("Turn on the coffee maker, right now!");
} else {
   console.log("Don't worry Everything is ok");
}

// Switch Statement
let carStatus = "iddle";
switch(carStatus) {
   case "moving":
     console.log("You will get home");
     break;
   case "stopped":
     console.log("You are not moving");
     break;
   default:
     console.log("Try to start your car");
 } 

 // for loop
 let cars = ["Honda", "Chevrolet", "Mercedes Benz", "Renault"];
 for (let i = 0; i < cars.length; i ++){
   console.log(cars[i]);
 }

 // while loop
 let i = 0;
 while(i < cars.length){
   console.log(cars[i]);
   i++;
 }

 // do while loop
 let j = 0;
 do {
   console.log(cars[j]);
   j++;
 } while(j < cars.length);

// try catch statement
try {
   let i = 0;
   while(i < cars.length){
     console.log(cars[i]);
     i++;
   }
 } catch (error) {
   console.log(error.message);
 } finally {
   console.log("The loop has finished");
 }

/* Extra 
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/
for (i = 10; i <= 55;   i++){
  if (i % 2 === 0){
    if (i !== 16 && i % 3 !== 0){
      console.log(i);
    }
  }
  }