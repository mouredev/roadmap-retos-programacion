/**
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

let a =1;
let b =2;
//**aritmeticos */
console.log(a + b); // suma 
console.log(a - b); // resta
console.log(a * b); // multiplicacion
console.log(a / b); // division
console.log(a % b); //modulo
console.log(a ** b); //potencia
//**comparacion */
console.log(a == b); // igual 
console.log(a >= b); // mayor o igual
console.log(a <= b); // menor o igual
console.log(a =! b); // diferente
//*asignacion/**
a = 5;
a = a + 5;

a += 5; 
a -= 5;
a *= 5;
a /= 5;
a &= 5;
a **= 5;
console.log(a);
//*bits/*
/**
 * 0 es 00000000
 * 1 es 00000001
 * 2 es 00000010
 * 3 es 00000011
 * 4 es 00000100
 * 5 es 00000101
 * 6 es 00000110
 * 7 es 00000111
 * 8 es 00001000
 * 9 es 00001001
 */
/**or */

console.log(1 | 7); //*00000111 seria 7
console.log(2 | 6); //*00000110 seria 6
console.log(3 | 5); //*00000111 seria 7
/** and */
console.log(1 & 7); //*00000001 seria 1
console.log(2 & 6); //*00000010 seria 2
console.log(3 & 5); //*00000001 seria 1
//*** estructuras de control 
//* condicionales

let numero = 3;
if (numero < 10) {
        console.log('el numero es menor a 10');        
    } else {
        console.log('No es un numero menor a 10');
    }

//* iterativas
let user = {
    id : 1,
    nombre : 'Miguel',
    edad : 39,
};
for (let datos in user) {
    console.log(datos, user[datos]);
}

let numero1 = 1;
    while (numero1 < 10) {
    console.log('el numero es menor a 10');
    numero1++;
    
}

