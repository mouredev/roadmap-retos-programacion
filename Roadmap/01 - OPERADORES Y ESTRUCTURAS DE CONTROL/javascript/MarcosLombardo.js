// Operadores

/* Operadores artméticos */

let num1 = 5 + 5; // Suma
let num2 = 5 - 2; // Resta
let num3 = 5 * 2; // Multiplicación
let num4 = 10 / 2; // División
let num5 = 12 % 2; // Módulo (Resto de la división)

console.log(num1, num2, num3, num4, num5);

/* Operadores de asignación */

let num6 = 8;
num6 += 5; // Asignación de suma
let num7 = 10;
num7 -= 5; // Asignación de resta
let num8 = 2;
num8 *= 2; // Asignación de multiplicación
let num9 = 10;
num9 /= 2; // Asignación de división
let num10 = 9;
num10 %= 3; // Asignación de módulo

console.log(num6, num7, num8, num9, num10);

/* Operadores de comparación */

let comp1 = 5 == "5"; // Igualdad
let comp2 = 5 === "5"; // Igualdad estricta
let comp3 = 8 != "8"; // Desigualdad
let comp4 = 6 !== "6"; // Desigualdad estricta
let comp5 = 10 > 5; // Mayor que
let comp6 = 10 >= 10; // Mayor o igual que
let comp7 = 8 < 12; // Menor que
let comp8 = 8 <= 7 // menor o igual que

console.log(comp1, comp2, comp3, comp4, comp5, comp6, comp7, comp8);

/* Operadores lógicos */

let logi1 = true && true; // AND
let logi2 = true || false; // OR
let logi3 = !true; // NOT

console.log(logi1, logi2, logi3);



// Estructuras de control

let num11 = 5

/* Condicional If */

if (num11 > 3) {
    console.log("Es mayor");
}

/* Condicional If...Else */

if (num11 < 3) {
    console.log("Es mayor");
} else {
    console.log("No es mayor");
}

/* Condicional If...Else If */

if (num11 > 5) {
    console.log("Es mayor");
} else if (5 < 5) {
    console.log("No es mayor");
} else {
    console.log("Es igual")
}

/* Operador ternario */

console.log((num11 > 5) ? "Es mayor" : "No es mayor");

/* Estructura Switch */

let mes = "febrero"

switch (mes) {
    case "febrero":
        console.log("Estamos en verano")
        break;
    case "mayo":
        console.log("Estamos en otoño")
        break;
    case "agosto":
        console.log("Estamos en invierno")
        break;
    case "octubre":
        console.log("Estamos en primavera")
        break;
    default:
        break;
}

/* Bucle For */

let array1 = [];

for (let i = 0; i < 5; i++) {
    array1.push(i);
}

console.log(array1);

/* Bucle While */

let numero = 0;
let array2 = [];

while (numero < 2) {
    array2.push(numero);
    numero++;
}

console.log(array2);

/* Bucle Do...while */

let numero2 = 2;
let array3 = [];

do {
    array3.push(numero2);
    numero2++;
} while (numero2 < 2);

console.log(array3);

/* Bucle For...of */

let colores1 =["Rojo", "Verde", "Azul"];
let array4 = [];

for (let color of colores1) {
    array4.push(color);
}

console.log(array4);

/* Bucle For...in */

let colores2 =["Rojo", "Verde", "Azul"];
let array5 = [];

for (let color2 in colores2) {
    array5.push(color2);
}

console.log(array5);



// Manejo de excepciones

/* Estructura Try...catch */

try {
    let resultado = 10 / 0;
    console.log(resultado);
} catch (error) {
    console.log("Ha ocurrido un error:", error.message);
}



// Dificultad extra

for (let n = 10; n <= 55; n++) {
    if (n % 2 === 0 && n !== 16 && n % 3 !== 0) {
        console.log(n);
    }    
}