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

// Operadores Aritméticos
let suma: number = 5 + 3;
let resta: number = 10 - 2;
let multiplicacion: number = 4 * 2;
let division: number = 20 / 4;
let modulo: number = 10 % 3;
let exponente: number = 2 ** 3;
console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Módulo:", modulo);
console.log("Exponente:", exponente);

// Operadores de Comparación
let esIgual: boolean = (5 == 5); // Igualdad
let esDiferente: boolean = (5 != 3); // Desigualdad
let esMayor: boolean = (10 > 5); // Mayor que
let esMenor : boolean = (3 < 7); // Menor que     
let esMayorIgual: boolean = (5 >= 5); // Mayor o igual que
let esMenorIgual: boolean = (2 <= 3); // Menor o igual que
console.log("Igualdad => 5 == 5:", esIgual);
console.log("Desigualdad => 5 != 3:", esDiferente);
console.log("Mayor que => 10 > 5:", esMayor);
console.log("Menor que => 3 < 7:", esMenor);
console.log("Mayor o igual que => 5 >= 5:", esMayorIgual);
console.log("Menor o igual que => 2 <= 3:", esMenorIgual);

// Operadores Lógicos
let logicoAnd: boolean = true && false; // Lógico AND
let logicoOr: boolean = true || false; // Lógico OR        
console.log("Operador lógico AND => true && false:", logicoAnd);
console.log("Operador lógico OR => true || false:", logicoOr);

// Operadores de Asignación
let asignacion: number = 5; // Asignación
console.log("Asignación:", asignacion);
asignacion %= 2; // Asignación con módulo
console.log("Asignación con módulo y asignacion %= 2:", asignacion);
asignacion += 3; // Asignación con suma
console.log("Asignación con suma y asignacion += 3:", asignacion);
asignacion **= 2; // Asignación con exponente
console.log("Asignación con exponente y asignacion **= 2:", asignacion);

// Operadores de Identidad
let identidad: boolean = 5 === 5; // Identidad
console.log("Identidad => 5 === 5:", identidad);
let pertenencia: boolean = [1, 2, 3].includes(2); // Pertenencia
console.log("Pertenencia => [1, 2, 3].includes(2):", pertenencia);

// Estructuras de control
let condicion: number = 10;
if (condicion >= 5) {
    console.log(`Condición cumplida: el número ${condicion} es mayor o igual que 5`);
}   else {
    console.log(`Condición no cumplida: el número ${condicion} no es mayor que 5`);
}

// Estructuras de control iterativas
let i: number = 5;
console.log(`Iterando con FOR del 0 al ${i}:`);
for (i = 0; i <= 5; i++) {
    console.log("Iteración:", i);
}

console.log(`Iterando con WHILE mientras i sea mayor que 0:`);
while (i > 0) {
    console.log("Mientras i sea mayor que 0, i:", i);  
    i--;
}

// Manejo de excepciones
try {
    let divisor = 0;
    if (divisor === 0) {
        throw new Error("División por cero no permitida");
    }
    let resultado: number = 10 / divisor;
    console.log(resultado);
} catch (error) {
    console.error("Error:", error);
}

// DIFICULTAD EXTRA
console.log("Números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:");
for (let i = 10; i <= 55; i++) {
    if(i%2==0 && i%3 != 0){
        if(i!=16)
            console.log(i);        
    }
}
