/*
* EJERCICIO:
* 1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
*   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
*   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
* 2- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
*   que representen todos los tipos de estructuras de control que existan
*   en tu lenguaje:
*   Condicionales, iterativas, excepciones...
* 3- Debes hacer print por consola del resultado de todos los ejemplos.
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

/* Soluciones */

/* 1 - 3 */

/* Aritméticos */

let a = 5;
let b = 2;

console.log("Suma:", a + b);       // Suma: 7
console.log("Resta:", a - b);      // Resta: 3
console.log("Multiplicación:", a * b); // Multiplicación: 10
console.log("División:", a / b);   // División: 2.5
console.log("Módulo:", a % b);     // Módulo: 1
console.log("Incremento:", ++a);   // Incremento: 6
console.log("Decremento:", --b);   // Decremento: 1

/* Lógicos */

let x = true;
let y = false;

console.log("AND:", x && y);   // AND: false
console.log("OR:", x || y);    // OR: true
console.log("NOT:", !x);       // NOT: false

/* Comparación */

let num1 = 10;
let num2 = "10";

console.log("Igualdad:", num1 == num2);      // Igualdad: true
console.log("Igualdad estricta:", num1 === num2); // Igualdad estricta: false
console.log("Desigualdad:", num1 != num2);    // Desigualdad: false
console.log("Desigualdad estricta:", num1 !== num2); // Desigualdad estricta: true
console.log("Mayor que:", num1 > num2);       // Mayor que: false
console.log("Menor que:", num1 < num2);       // Menor que: false

/* Asignación */

let variable = 10;

variable += 5;
console.log("Suma y asignación:", variable); // Suma y asignación: 15

variable *= 2;
console.log("Multiplicación y asignación:", variable); // Multiplicación y asignación: 30

/* Identidad */

let obj1 = { name: "John" };
let obj2 = { name: "John" };

console.log("Igualdad de identidad:", obj1 === obj2); // Igualdad de identidad: false

/* Pertenencia */

let array = [1, 2, 3, 4, 5];

console.log("Pertenece al array:", 3 in array); // Pertenece al array: true

/* Bits */

let num3 = 5; // Representación binaria: 101
let num4 = 3; // Representación binaria: 011

console.log("AND a nivel de bits:", num3 & num4); // AND a nivel de bits: 1
console.log("OR a nivel de bits:", num3 | num4);  // OR a nivel de bits: 7

/* 2 - 3 */

/* Estructuras de Control */

/* Condicionales */

let edad = 18;

if (edad >= 18) {
    console.log("Puedes beber alcohol xD.");
} else {
    console.log("No puedes beber alcohol :'(.");
}

/* Iterativas */

for (let i = 1; i <= 5; i++) {
    console.log("Iteración:", i);
}

let arrayIterativo = [10, 20, 30, 40, 50];
for (let elemento of arrayIterativo) {
    console.log("Elemento:", elemento);
}

/* Excepciones */

try {
    // Código que puede generar una excepción
    let resultado = 10 / 0;
    console.log("Resultado:", resultado);
} catch (error) {
    console.error("Error:", error.message);
} finally {
    console.log("Bloque finally ejecutado siempre.");
}

/* Extra - Switch */

let diaDeLaSemana = "Lunes";

switch (diaDeLaSemana) {
    case "Lunes":
        console.log("Es el primer día de la semana.");
        break;
    case "Martes":
    case "Miércoles":
    case "Jueves":
        console.log("Estamos a mitad de semana.");
        break;
    case "Viernes":
        console.log("¡Viernes! Fin de la semana laboral.");
        break;
    case "Sábado":
    case "Domingo":
        console.log("Fin de semana, tiempo para descansar.");
        break;
    default:
        console.log("Día no reconocido.");
}


/* Opcional */

for (let i = 10; i <= 55; i++) {
    if (
        i % 2 === 0 && i !== 16 && i % 3 !== 0
    ) {
        console.log("Número", i );
    }
}