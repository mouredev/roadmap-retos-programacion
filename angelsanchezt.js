/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

/*
Operadores
*/

// Operadores aritméticos
console.log(`Suma: 10 + 3 = ${10 + 3}`);
console.log(`Resta: 10 - 3 = ${10 - 3}`);
console.log(`Multiplicación: 10 * 3 = ${10 * 3}`);
console.log(`División: 10 / 3 = ${10 / 3}`);
console.log(`Módulo: 10 % 3 = ${10 % 3}`);
console.log(`Exponente: 10 ** 3 = ${10 ** 3}`);

// Operadores de comparación
console.log(`Igualdad: 10 == 3 es ${10 == 3}`);
console.log(`Desigualdad: 10 != 3 es ${10 != 3}`);
console.log(`Mayor que: 10 > 3 es ${10 > 3}`);
console.log(`Menor que: 10 < 3 es ${10 < 3}`);
console.log(`Mayor o igual que: 10 >= 10 es ${10 >= 10}`);
console.log(`Menor o igual que: 10 <= 3 es ${10 <= 3}`);

// Operadores lógicos
console.log(`AND &&: 10 + 3 == 13 and 5 - 1 == 4 es ${10 + 3 == 13 && 5 - 1 == 4}`);
console.log(`OR ||: 10 + 3 == 13 or 5 - 1 == 4 es ${10 + 3 == 14 || 5 - 1 == 4}`);
console.log(`NOT !: not 10 + 3 == 14 es ${!(10 + 3 == 14)}`);

// Operadores de asignación
let my_number = 11;  // asignación
console.log(my_number);
my_number += 1;  // suma y asignación
console.log(my_number);
my_number -= 1;  // resta y asignación
console.log(my_number);
my_number *= 2;  // multiplicación y asignación
console.log(my_number);
my_number /= 2;  // división y asignación
console.log(my_number);
my_number %= 2;  // módulo y asignación
console.log(my_number);
my_number **= 1;  // exponente y asignación
console.log(my_number);
my_number //= 1;  // división entera y asignación
console.log(my_number);

// Operadores de identidad
let my_new_number = my_number;
console.log(`my_number is my_new_number es ${my_number === my_new_number}`);
console.log(`my_number is not my_new_number es ${my_number !== my_new_number}`);


// Operadores de bits
let a = 10;  // 1010
let b = 3;   // 0011
console.log(`AND: 10 & 3 = ${a & b}`);   // 0010
console.log(`OR: 10 | 3 = ${a | b}`);    // 1011
console.log(`XOR: 10 ^ 3 = ${a ^ b}`);   // 1001
console.log(`NOT: ~10 = ${~a}`);
console.log(`Desplazamiento a la derecha: 10 >> 2 = ${a >> 2}`);   // 0010
console.log(`Desplazamiento a la izquierda: 10 << 2 = ${a << 2}`);  // 101000

/*
Estructuras de control
*/

// Condicionales
let my_string = "Brais";

if (my_string === "MoureDev") {
    console.log("my_string es 'MoureDev'");
} else if (my_string === "Brais") {
    console.log("my_string es 'Brais'");
} else {
    console.log("my_string no es 'MoureDev' ni 'Brais'");
}

// Iterativas
for (let i = 0; i <= 10; i++) {
    console.log(i);
}

let j = 0;
while (j <= 10) {
    console.log(j);
    j++;
}

// Manejo de excepciones
try {
    console.log(variable_no_definida);
} catch (error) {
    console.log("Se ha producido un error");
} finally {
    console.log("Ha finalizado el manejo de excepciones");
}

/*
Extra
*/

for (let number = 10; number <= 55; number++) {
    if (number % 2 === 0 && number !== 16 && number % 3 !== 0) {
        console.log(number);
    }
}
