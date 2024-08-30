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

//------------------------------- aritmeticos --------------------------------------
///////////////////////////////////////////////////////////
//suma
console.log("la suma de 15 + 10 es :"+(15 + 10));

//resta 
console.log("la resta de 15 - 10 es :"+(15 - 10));

//multiplicacion 
console.log("la multiplicacion de 15 * 10 es :"+(15 * 10));

//division
console.log("la division de 15 / 10 es :"+(15 / 10));

//modulo o residuo de la division
console.log("el modulo de 15 % 10 es :"+(15 % 10));

//Exponenciacion 
console.log("la Exponenciacion de 15 ** 10 es :"+(2 ** 4));

//incremento 

for (let i = 0 ; i < 4 ; i++ ){
    console.log(i)
};

//decremento 

for (let i = 5 ; i > 0  ; i-- ){
    console.log(i)
};

//------------------------------operadores de compracion---------------------------------

//igual 

let igual = 10 

if (igual == 10){
console.log("el numero dado es igual a :" + igual)
};

//estrictamente igual

let estrictamenteIgual = 10 

if (estrictamenteIgual === 10){
console.log("el numero dado es igual a :" + estrictamenteIgual)
};

//No es igual 

let noEsIgual = 5;

if (noEsIgual != 10){
console.log("el numero dado no es igual " );
};

//estrictamenteNoEsIgual

let estrictamenteNoEsIgual = 5;

if (estrictamenteNoEsIgual !== 10){
console.log("el numero dado no es igual " );
};

//mayor que 

let a = 20;
let b = 70;

console.log(a > b);

//menor que 

console.log(a < b);

//mayor o igual 
console.log(a >= b);

//menor o igual 
console.log(a <= b);

//--------------------------operadores logicos----------------------------------------- 

//and 