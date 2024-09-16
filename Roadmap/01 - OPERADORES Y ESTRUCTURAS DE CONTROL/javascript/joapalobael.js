// Operadores aritmeticos
const suma = (2 + 5);
const resta = (suma - 10);
const multiplicación = (suma * (-resta));
const divison = multiplicación / suma;
let sobrante = 12 % 5;
const exponente = 3 ** 9;

let x = 5;
let y = 5;
x++; // aumentador
y--; // disminuidor




//Estructuras de control
// If
if (suma === 7) {
    console.log(`La suma de 2+5 es igual a ${suma}`);
}

// If else
if (suma === 5) {
    console.log(`La suma de 2+5 es igual a ${suma}`)
} else {
    console.log(`5 es el resultado de sumar 2+3`);
}

// For
for (let index = 0; index < sobrante; index++) {
    console.log(`Voy a contar del 0 al 1. ${index}/1`);
}

//while

while (sobrante < suma) {
    sobrante++;
    console.log("Me encuentro dentro de un while", sobrante);
}

//switch

const TipoDeFruta = "anana";
switch (TipoDeFruta) {
    case "naranja":
        console.log("Las naranjas cuestan $1200 por kg")
        break;
    case "pera":
        console.log("Las peras cuestan $2200 por kg")
        break;
    case "manzana":
        console.log("Las manzanas cuestan $2800 por kg")
        break;
    default:
        console.log(`Disculpa, no tenemos stock de ${TipoDeFruta} en este momento`)
        break;
}



/*ABASTRACCIÓN DEL EJERCICIO*/
/* inicio
        Para los numeros entre 10 y 55 {
            Si (el resto al dividir por 2 es 0 Y el numero es diferente a 16 Y el numero al dividirlo por 3 es diferente a 0){
                mostrar por pantalla el número
            }
        }
fin */

//Resolución ejercicio extra
console.log("#Resolución ejercicio extra");
for (let index = 10; index <= 55; index++) {
    if (index % 2 === 0 && index !== 16 && index % 3 !== 0)
        console.log(`Numero: ${index}`);
}

