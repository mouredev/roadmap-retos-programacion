/*
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
    > #### Dificultad: Fácil | Publicación: 02 /01 / 24 | Corrección: 08 /01 / 24

## Ejercicio

    ```
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


let dev = 'Gracias'


// Operadores Aritmeticos: retornan el resultado de esas operaciones aritm.

let suma = 5 + 2
let resta = 11 - 10
let multiplicacion = 5 * 5
let division = 10 / 2
let resto = 10 % 2
let exponenciacion = 5 ** 5
let incremento = 5; incremento++
let decremento = 5; decremento--
let negativo = -1
let conversion_de_string_a_numero = +'1'


// Operadores de Asignacion:

x = 10      /* Asignacion simple */
x += 10     /* Suma y Asigna */
x -= 10     /* Resta y Asigna */
x *= 10     /* Multiplica y Asigna */
x /= 10     /* Divide y Asigna */
x %= 10     /* Saca el resto y Asigna */
x **= 10    /* Potencia y Asigna */


// OPERADORES DE COMPARACION: retornan boleanos true o false

10 == '10'      // Igualdad "compara valor" */
10 != '10'     // Desigualdad "compara valor" */
10 === '10'     // Igualdad estricta "compara valor y tipo"
10 !== '10'     // Desigualdad estricta "compara valor y tipo"
10 > 10     // Mayor que
10 < '10'     // Menor que
10 >= '10'     // Mayor o igual que
10 <= '10'     // Menor o igual que

// Operadores Logicos:  para loops/condiciones

true && false  // AND logico
true || false  // AND logico
!true          // NOT logico
true ?? false; // null o undefined para condicionales

// Operador Ternario:

dev ? true : false      // Condicional


// Comprobacion en consola de todos los EJEMPLOS:
console.log(`
    Operadores Aritmeticos:

    suma: ${suma}
    resta: ${resta}
    multiplicacion: ${multiplicacion}
    division: ${division}
    resto: ${resto}
    exponenciacion: ${exponenciacion}
    incremento: ${incremento}
    decremento: ${decremento}
    negativo: ${negativo}

    Operadores de Aisgnacion:
   ${x = 10}      <-- Asignacion simple
   ${x += 10}     <-- Suma y Asigna
   ${x -= 10}     <-- Resta y Asigna
   ${x *= 10}     <-- Multiplica y Asigna
   ${x /= 10}     <-- Divide y Asigna
   ${x %= 10}     <-- Saca el resto y Asigna
   ${x **= 10}    <-- Potencia y Asigna

    Operadores de Comparacion:

    ${10 == '10'}      <-- Igualdad "compara valor" */
    ${10 != '10'}     <-- Desigualdad "compara valor" */
    ${10 === '10'}     <-- Igualdad estricta "compara valor y tipo"
    ${10 !== '10'}     <-- Desigualdad estricta "compara valor y tipo"
    ${10 > 10}        <-- Mayor que
    ${10 < '10'}     <-- Menor que
    ${10 >= '10'}     <-- Mayor o igual que
    ${10 <= '10'}     <-- Menor o igual que

    Operadores Logicos:

    ${true && false}  <-- AND logico
    ${true || false}  <-- AND logico
    ${!true}          <-- NOT logico
    ${dev ?? false}   <-- null o undefined para condicionales

    Operador Ternario:
    ${dev ? true : false}    < --Condicional
    `)


//DIFICULTAD EXTRA(opcional):
/*Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

for (let i = 10; i <= 55; i++) {
    if (i == 16 || i % 3 == 0 || i % 2 !== 0) {
        continue;
    }
    console.log(i)
}










