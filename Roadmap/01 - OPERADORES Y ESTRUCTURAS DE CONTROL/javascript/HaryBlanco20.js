let x = 10;
let y = 5;

let suma = x + y; // Suma: 15
let resta = x - y; // Resta: 5
let multiplicacion = x * y; // Multiplicación: 50
let division = x / y; // División: 2
let modulo = x % y; // Módulo: 0
let incremento = ++x; // Incremento: 11
let decremento = --y; // Decremento: 4

// Estructura de control: if-else
if (x > y) {
    console.log("x es mayor que y");
} else {
    console.log("x no es mayor que y");
}

// Estructura de control: switch
let day = "Monday";
switch (day) {
    case "Monday":
        console.log("Today is Monday");
        break;
    case "Tuesday":
        console.log("Today is Tuesday");
        break;
    case "Wednesday":
        console.log("Today is Wednesday");
        break;
    default:
        console.log("Today is not Monday, Tuesday, or Wednesday");
}

// Estructura de control: for loop
for (let i = 0; i < 5; i++) {
    console.log("Iteration: " + i);
}

// Estructura de control: while loop
let i = 0;
while (i < 5) {
    console.log("Iteration: " + i);
    i++;
}

// Estructura de control: do-while loop
let j = 0;
do {
    console.log("Iteration: " + j);
    j++;
} while (j < 5);

// Estructura de control: for...in loop
const person = {
    name: "Hary",
    age: 34,
    city: "New York"
};
for (let key in person) {
    console.log(key + ": " + person[key]);
}

// Estructura de control: for...of loop
const fruits = ["manzana", "pera", "naranja"];
for (let fruit of fruits) {
    console.log(fruit);
}

// Estructura de control: try-catch
try {
    // Code that may throw an error
    throw new Error("Tienes un error");
} catch (error) {
    console.log("Error: " + error.message);
}

// Estructura de control: try-catch-finally
try {
    // Code that may throw an error
    throw new Error("Tienes un error");
} catch (error) {
    console.log("Error: " + error.message);
} finally {
    console.log("El bloque de código ha finalizado");
}


//Dificultad extra

for(let i= 10; i<=55;i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0){
        console.log(i)
    }
}

