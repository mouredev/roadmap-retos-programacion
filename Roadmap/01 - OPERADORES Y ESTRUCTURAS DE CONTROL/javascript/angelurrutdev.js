// Operadores de concatenación  Backsticks se hacen utilizando ALT + 96

let saludo = "¡Hola, ";
let nombre = "Juan!";

let saludoCompleto = saludo + nombre;
console.log(`Saludo completo: ${saludoCompleto}`);

// Operadores aritméticos 

let numero1 = 10;
let numero2 = 5;

// Suma
let suma = numero1 + numero2;
console.log(`Suma: ${numero1} + ${numero2} = ${suma}`);

// Resta
let resta = numero1 - numero2;
console.log(`Resta: ${numero1} - ${numero2} = ${resta}`);

// Multiplicación
let multiplicacion = numero1 * numero2;
console.log(`Multiplicación: ${numero1} * ${numero2} = ${multiplicacion}`);

// División
let division = numero1 / numero2;
console.log(`División: ${numero1} / ${numero2} = ${division}`);

// Módulo (resto de la división)
let modulo = numero1 % numero2;
console.log(`Módulo: ${numero1} % ${numero2} = ${modulo}`);

// Exponenciación
let exponenciacion = numero1 ** numero2;
console.log(`Exponenciación: ${numero1} ** ${numero2} = ${exponenciacion}`);

// División entera (descarta la parte decimal)
let divisionEntera = Math.floor(numero1 / numero2);
console.log(`División entera: ${numero1} // ${numero2} = ${divisionEntera}`);

// Operadores de asignación en 

let resultado = 0;

// Asignación simple
resultado = 10;
console.log(`Resultado después de asignación simple: ${resultado}`);

// Asignación con suma
resultado += 5; // Equivalente a: resultado = resultado + 5;
console.log(`Resultado después de asignación con suma: ${resultado}`);

// Asignación con resta
resultado -= 3; // Equivalente a: resultado = resultado - 3;
console.log(`Resultado después de asignación con resta: ${resultado}`);

// Asignación con multiplicación
resultado *= 2; // Equivalente a: resultado = resultado * 2;
console.log(`Resultado después de asignación con multiplicación: ${resultado}`);

// Asignación con división
resultado /= 4; // Equivalente a: resultado = resultado / 4;
console.log(`Resultado después de asignación con división: ${resultado}`);

// Asignación con módulo
resultado %= 3; // Equivalente a: resultado = resultado % 3;
console.log(`Resultado después de asignación con módulo: ${resultado}`);

// Asignación con exponenciación
resultado **= 2; // Equivalente a: resultado = resultado ** 2;
console.log(`Resultado después de asignación con exponenciación: ${resultado}`);



// Operadores Logicos

console.log(5 > 4) // True
console.log(5 < 4) // False


let edad = 25;
let tieneLicencia = true;
let esEstudiante = false;
let tieneTrabajo = true;

// Operador AND (&&)
console.log("Puede conducir legalmente:", edad >= 18 && tieneLicencia); // Puede conducir legalmente:, true

// Operador OR (||)
console.log("Cumple con alguna condición para algo:", esEstudiante || tieneTrabajo); // Cumple con alguna condición para algo: true

// Combinación de operadores
console.log("Cumple con alguna de las condiciones combinadas:", (edad >= 18 && tieneLicencia) || esEstudiante); //  Cumple con alguna de las condiciones combinadas: true


// Operadores unarios en JavaScript

// Definimos algunas variables para ejemplificar
edad = 25;
tieneLicencia = true;
esEstudiante = false;
tieneTrabajo = true;

// Operador de negación (!)
let esFalso = !esEstudiante;
console.log("¿Es falso?", esFalso); // Devuelve true

// Operador de incremento (++)
let contador = 5;
contador++;
console.log("Contador después del incremento:", contador); // Devuelve 6

// Operador de decremento (--)
let otroContador = 8;
--otroContador;
console.log("Contador después del decremento:", otroContador); // Devuelve 7

// Operador de tipo (typeof)
let miNombre = "Juan";
console.log("Tipo de dato de miNombre:", typeof miNombre); // Devuelve "string"

// Operador de negación binaria (~)
let numeroBinario = 5; // Representación binaria: 00000101
let resultadoNegacionBinaria = ~numeroBinario; // Representación binaria: 11111010
console.log("Resultado de la negación binaria:", resultadoNegacionBinaria); // Devuelve -6

/** 
 *  El operador ! invierte el valor de verdad de una expresión.
 *  El operador ++ incrementa una variable en 1. 
 * El operador -- decrementa una variable en 1.
 * El operador typeof devuelve el tipo de dato de una expresión.
 * El operador ~ realiza la negación binaria de un número.
 */

// Operadores ternarios ? Verdadero. : Falso.

edad = 20;
tieneLicencia = true;

// Operador ternario para asignar un valor
esMayorDeEdad = edad >= 18 ? "Sí" : "No";
console.log("¿Es mayor de edad?", esMayorDeEdad); // Devuelve "Sí"


// EXTRA

for (let numero = 10;
    numero <= 55; numero += 2) {
    if (numero !== 16 && numero % 3 !== 0) {
        console.log(numero);
    }
}



