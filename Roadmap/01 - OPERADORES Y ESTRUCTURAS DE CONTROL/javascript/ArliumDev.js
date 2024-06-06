// Operadores aritméticos

let suma = 1 + 1;
let resta = 2 - 1;
let division = 6 / 2;
let multiplicacion = 5 * 9;
let resto = 15 % 3;


// Operadores de asignación

let z = 1;
z += 5; // Adición
z -= 1; // Sustracción
z *= 5; // Multiplicación
z /= 2; // División
z %= 2; // Resto


// Incremento y decremento

let sumRes = 2;
sumRes++;
sumRes--;


// Operadores de comparación

let num1 = 6;
let num2 = 8;
let comp1 = num1 > num2;
let comp2 = num1 < num2;
let comp3 = num1 >= num2;
let comp4 = num1 <= num2;
let comp5 = num1 === num2;
let comp6 = num1 !== num2;


// Operadores lógicos

let and = true && true;
let or = true || false;


// Operadores de negación

let truthy = true;
let falsy = false;
console.log(!truthy);
console.log(!falsy);
console.log(!!truthy);


// Operadores de igualdad o identidad

let same1 = 5 === 5;
let same2 = 5 === "5";
let same3 = 5 !== 5;


// typeof

let typeNumber = 7;
let typeString = "I'm a string";
let typeBoolean = true;
let typeUndef = undefined;
let typeNull = null;
console.log(typeof typeNumber);
console.log(typeof typeString);
console.log(typeof typeBoolean);
console.log(typeof typeUndef);
console.log(typeof typeNull);


// Operador de concatenación

let start = "Hola, ";
let end = "Javascript";
console.log(start + end);


/* Estructuras de control */

// if...else

let language = "Javascript";
if (language !== "Javascript") {
  console.log("Te equivocas de carpeta, amigo");
} else {
  console.log("Estás en la carpeta correcta");
}


// Switch

let monthNum = 7;
switch (monthNum) {
  case 1:
    console.log("January");
    break;
  case 2:
    console.log("February");
    break;
  case 3:
    console.log("March");
    break;
  case 4:
    console.log("April");
    break;
  case 5:
    console.log("May");
    break;
  case 6:
    console.log("June");
    break;
  case 7:
    console.log("July");
    break;
  case 8:
    console.log("August");
    break;
  case 9:
    console.log("September");
    break;
  case 10:
    console.log("October");
    break;
  case 11:
    console.log("November");
    break;
  case 12:
    console.log("December");
    break;
  default:
    console.log("The number doesn't match any month");
}


// For 

for (let i = 0; i < 3; i++) {
    console.log(i);
}


// While 

let counter = 10;
while (counter > 0) {
    console.log(counter);
    counter--;
}


// Do While
let countUp = 0;
do {
    console.log(countUp);
    countUp++;
} while (countUp <= 5);


// forEach

let numbers  = [1,2,3,4,5,6,7,8];
numbers.forEach((number) => {
    number++;
    console.log(number);
});