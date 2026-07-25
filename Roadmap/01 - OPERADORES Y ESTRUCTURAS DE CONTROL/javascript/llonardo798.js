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

// Tipos de operadores en JavaScript

// 1. Operadores Aritméticos
console.log("1. Operadores Aritméticos");

let suma = 5 + 5;                                   // Operador de suma (+)
console.log("Suma: " + suma);                       // 10

let resta = suma - 5;                               // Operador de resta (-)
console.log("Resta:" + resta);                      // 5

let multiplicacion = suma * 5;                      // Operador de multiplicación (*)
console.log("Multiplicación: " + multiplicacion);   // 50

let division = suma / 5                             // Operador de división (/)
console.log("División: " + division);               // 2

let modulo = suma % 3;                              // Operador de módulo (%) - Módulo (resto o sobrante de la división) 10 % 3 = 1 se puede considerar como 10/3 = 3 y sobra 1
console.log("Modulo: " + modulo);                   // 1

let incremento = suma++;                            // Operador de incremento (++)
console.log("Incremento: " + incremento);           // 6

let decremento = suma--;                            // Operador de decremento (--)
console.log("Decremento: " + decremento);           // 5

let exponenciacion = 2 ** 3;                        // Operador de exponenciación (**)
console.log("Exponenciación" + exponenciacion);     // 8

// Ejemplo de uso de operadores aritméticos 
let numero1 = 5;
let numero2 = 3;
let resultado = (((numero1 + numero2) * (numero1 - numero2)) / numero2) % numero2 + numero1++ - --numero2 + numero1 ** numero2
console.log("Uso de todos los operadores aritmeticos: " + resultado);         // 41.333....



// 2. Operadores Bit a Bit
console.log("2. Operadores Bit a Bit");

let operadorA = 60;  // 60 = 0011 1100
let operadorB = 13;  // 13 = 0000 1101
let operadorC = -10; // -10 = 1111 1111 1111 1111 1111 1111 1111 0110

let operadorAnd = operadorA & operadorB; // Operador de AND bit a bit (&)
console.log("AND: " + operadorAnd);       // 12
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ & (AND)
// 0000 1100 -> 12

let operadorOr = operadorA | operadorB;   // Operador de OR bit a bit (|)
console.log("OR: " + operadorOr);         // 61
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ | (OR)
// 0011 1101 -> 61

let operadorXor = operadorA ^ operadorB;  // Operador de XOR bit a bit (^)
console.log("XOR: " + operadorXor);       // 49
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ ^ (XOR)
// 0011 0001 -> 49

let operadorNot = ~operadorA;             // Operador de NOT bit a bit (~)
console.log("NOT: " + operadorNot);       // -61
// Explicación con binarios:
// 0011 1100 -> 60
// ------------ ~ (NOT)
// 1100 0011 -> -61

let operadorDesplazamientoIzquierda = operadorA << 2; // Operador de desplazamiento a la izquierda (<<)
console.log("Desplazamiento a la izquierda: " + operadorDesplazamientoIzquierda); // 240
// Explicación con binarios:
// 0011 1100 -> 60
// --------- << (Desplazamiento a la izquierda de 2 bits)
// 1111 0000 -> 240

let operadorDesplazamientoDerecha = operadorA >> 2; // Operador de desplazamiento a la derecha (>>)
console.log("Desplazamiento a la derecha: " + operadorDesplazamientoDerecha); // 15
// Explicación con binarios:
// 0011 1100 -> 60
// --------- >> (Desplazamiento a la derecha de 2 bits)
// 0000 1111 -> 15

let operadorDesplazamientoDerechaSinSigno = operadorC >>> 2; // Operador de desplazamiento a la derecha sin signo (>>>)
console.log("Desplazamiento a la derecha sin signo: " + operadorDesplazamientoDerechaSinSigno); // 1073741821
// Explicación con binarios:
// 1111 1111 1111 1111 1111 1111 1111 0110 -> -10
// --------- >>> (Desplazamiento a la derecha sin signo de 2 bits)
// 0011 1111 1111 1111 1111 1111 1111 1101 -> 1073741821



// 3. Operadores de Asignación.
console.log("3. Operadores de Asignación");

let asignacion = 5;                                         // Operador de asignación (=)
console.log("Asignación: " + asignacion);                   // 5

asignacion += 5;                                            // Operador de suma y asignación (+=)
console.log("Suma y asignación: " + asignacion);            // 10

asignacion -= 5;                                            // Operador de resta y asignación (-=)
console.log("Resta y asignación: " + asignacion);           // 5

asignacion *= 5;                                            // Operador de multiplicación y asignación (*=)
console.log("Multiplicación y asignación: " + asignacion);  // 25

asignacion /= 5;                                            // Operador de división y asignación (/=)
console.log("División y asignación" + asignacion);          // 5

asignacion %= 3;                                            // Operador de módulo y asignación (%=)
console.log("Modulo y asignación: " + asignacion);          // 2

asignacion **= 3;                                           // Operador de exponenciación y asignación (**=)
console.log("Exponenciación y asignación: " + asignacion);  // 8

asignacion <<= 5;                                           // Operador de desplazamiento a la izquierda y asignación (<<=)
console.log("Desplazamiento a izquierda: " + asignacion);   // 256
// Explicación con binarios:
// 0000 0000 1000 -> 8
// --------- <<= (Desplazamiento a la izquierda de 5 bits)
// 0001 0000 0000 -> 256

// let desplazamient = suma >> resta;

asignacion >>= 2;                                           // Operador de desplazamiento a la derecha y asignación (>>=)
console.log("Desplazamiento a derecha: " + asignacion);      // 64
// Explicación con binarios:
// 0001 0000 0000 -> 256
// --------- >>= (Desplazamiento a la derecha de 2 bits)
// 0000 0100 0000 -> 64

// Operador de desplazamiento a la derecha sin signo y asignación (>>>=) desplaza los bits a la derecha 
// sin importar si el numero es positivo o negativo para lo cual agrerga 0 a la izquierda
let a = -10;
a >>>= 2;                                                   // Operador de desplazamiento a la derecha sin signo y asignación (>>>=)
console.log("Despolazamient a derecha sin signo: " + a);    // 1073741821
// Explicación con binarios:
// 1111 1111 1111 1111 1111 1111 1111 0110 -> -10
// --------- >>>= (Desplazamiento a la derecha sin signo de 2 bits)
// 0011 1111 1111 1111 1111 1111 1111 1101 -> 1073741821

let num1 = 60;
num1 &= 13;                                                         // Operador de AND bit a bit y asignación (&=)
console.log("Operador de AND bit a bit y asignación: " + num1);     // 12
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ & (AND)
// 0000 1100 -> 12

num1 = 60;
num1 |= 13;                                                         // Operador de OR bit a bit y asignación (|=)
console.log("Operador de OR bit a bit y asignación: " + num1);      // 61
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ | (OR)
// 0011 1101 -> 61

num1 = 60;
num1 ^= 13;                                                         // Operador de XOR bit a bit y asignación (^=)
console.log("Operador de XOR bit a bit y asignación" + num1);       // 49
// Explicación con binarios:
// 0011 1100 -> 60
// 0000 1101 -> 13
// ------------ ^ (XOR)
// 0011 0001 -> 49



// 4. Operadores de Comparación
console.log("4. Operadores de Comparación");

let comparacionIgual = 5 == 5;                                          // Operador de igualdad (==)
console.log("Igualdad: " + comparacionIgual);                           // true

let comparacionEstrictamenteIgual = 5 === 5;                            // Operador de igualdad estricta (===), no solo compara el valor sino también el tipo de dato
console.log("Igualdad estricta: " + comparacionEstrictamenteIgual);     // true

let comparacionDistinto = 5 != 5;                                       // Operador de distinto (!=)
console.log("Distinto: " + comparacionDistinto);                        // false

let comparacionEstrictamenteDistinto = 5 !== 5;                         // Operador de distinto estricto (!==), no solo compara el valor sino también el tipo de dato
console.log("Distinto estricto: " + comparacionEstrictamenteDistinto);  // false

let comparacionMayorQue = 5 > 3;                                        // Operador de mayor que (>)
console.log("Mayor que: " + comparacionMayorQue);                       // true

let comparacionMenorQue = 5 < 3;                                        // Operador de menor que (<)
console.log("Menor que: " + comparacionMenorQue);                       // false

let comparacionMayorIgualQue = 5 >= 5;                                  // Operador de mayor o igual que (>=)
console.log("Mayor o igual que: " + comparacionMayorIgualQue);          // true

let comparacionMenorIgualQue = 5 <= 3;                                  // Operador de menor o igual que (<=)
console.log("Menor o igual que: " + comparacionMenorIgualQue);          // false



// 5. Operadores Lógicos

let logicoAnd = true && false;                  // Operador AND lógico (&&) - Devuelve true si ambos operandos son true
console.log("AND lógico: " + logicoAnd);        // false

let logicoOr = true || false;                   // Operador OR lógico (||) - Devuelve true si al menos uno de los operandos es true
console.log("OR lógico: " + logicoOr);          // true

let logicoNot = !true;                          // Operador NOT lógico (!) - Devuelve true si el operando es false y viceversa
console.log("NOT lógico: " + logicoNot);        // false

// Ejemplo de uso de operadores lógicos

let edad = 16;
let estaAcompanado = false;

let puedeVerPelicula = edad >= 18 || (edad >= 16 && estaAcompanado);
console.log(puedeVerPelicula);
// Cambiamos el valor de la variable estaAcompanado a valor contrario por diversión.
if (!puedeVerPelicula) {
    console.log("Puedes ver la película");
} else {
    console.log("No puedes ver la película");
}



// 6. Operadores de Cadena
console.log("6. Operadores de Cadena");

let cadena1 = "Hola, la suma de: " + suma + " y " + resta + " es " + (suma + resta);       // Concatenación (+)
console.log(cadena1);                                                                       // Hola, la suma de: 5 y 5 es 10


// 7. Operador Condicional (Ternario)
console.log("7. Operador Condicional (Ternario)");

let puedeVerPelicula2 = edad >= 18 ? "Puede ver la película" : "No puede ver la película";  // Operador condicional (Ternario)
console.log(puedeVerPelicula2);                                                             // No puede ver la película

// 8. Otros Operadores
console.log("8. Otros Operadores");

// Se crea el objeto persona
let persona = {
    nombre: "Leonardo",
    edad: 26
};

let operadorTypeof = typeof persona;                                // Operador typeof - Devuelve el tipo de dato de una variable
console.log("Tipo de dato de suma: " + operadorTypeof);             // object

let operadorDelete = delete persona.edad;                           // Operador delete - Elimina una propiedad de un objeto
console.log("Propiedad eliminada: " + operadorDelete);              // true

let operadorIn = "nombre" in persona;                               // Operador in - Devuelve true si una propiedad existe en un objeto
console.log("Propiedad en el objeto: " + operadorIn);               // true

let operadorInstanceOf = persona instanceof Object;                 // Operador instanceof - Devuelve true si un objeto es una instancia de otro
console.log("Es una instancia de Object: " + operadorInstanceOf);   // true

let operadorNew = new Date();                                       // Operador new - Crea una nueva instancia de un objeto
console.log("Nueva instancia de Date: " + operadorNew);             // Fecha actual


// DIFICULTAD EXTRA - Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos)
// pares, y que no son ni el 16 ni múltiplos de 3.

console.log("DIFICULTAD EXTRA");

for (let i = 10; i < 56; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}