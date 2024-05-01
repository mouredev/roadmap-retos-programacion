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

// Aritméticos


let suma= 10 + 5;
console.log(suma)

const resta = 10 - 5
console.log(resta)

const multi = 10 * 5
console.log(multi)

const divi =  3 / 6
console.log(divi)

const modulo = (3 % 6)
console.log(modulo)

const numero1 = 10
const numero2 = 3
console.log( numero1 % numero2)
console.log(numero1 ** numero2)
console.log(numero1 / numero2 )

// Operadores ded comparacion 


console.log( "igualdad",numero1 == numero2 )
console.log ("desigualdad",numero1 != numero2)
console.log("mayor que", numero1 > numero2)
console.log("menor que", numero1 < numero2)
console.log("mayor igual que", numero1 >= numero2)
console.log("menor igual que", numero1 <= numero2 )
 

// operadores logicos
// AND &&: que se cumplan las dos condiciones.
const condicion = 10 + 3 == 13 && 5 - 1 == 4
console.log("and &&", 10 + 3 == 13 && "accion 2", 5 - 1 == 4)

if (condicion) {
    console.log("paso")
} else {
    console.log("no paso")
}

// OR || debe cumplir por lo menos una de la condiciones agregada 
const or = 10 + 10 <= 20 || 10 * 2 == 10
console.log(or)

if (or) {
    console.log("paso")
} else {
    console.log("no paso")
}

// NOT != een el caso que la operacion no se cumpliera se pasara hacer true referiendo a
//  que todo resultado que no sea el correcto lo manda como true

const not = 10 + 2 != 1
console.log(not)
if(not){
    console.log("true")
}else{
    console.log("false")
}

// Operadores de asignacion
let numero = 10;
numero += 1;
console.log(numero)
numero -= 2;
console.log(numero)
numero *= 5;
console.log(numero)
numero /= 2;
console.log(numero)
numero %= 10;
console.log(numero)
numero **= 2;
console.log(numero)


// Operadores de identidad

const my_number = 2
const my_new_numero= 2


// identidad: compara los que es tipo y valor si son iguales
console.log("mi numero es ",  my_number === my_new_numero)

if (my_number === my_new_numero) {
        console.log("paso")
}else{
    console.log("no paso")
}

// operador desigualdad estricta: compara que el tipo y valor no sea identico 
if ( 2 !== "2") {
    console.log("true")
}else{
    console.log("false")
}

// Operador de pertenecia
// IN SI UN OBJETO CONTIENE PROPIEDADES ESPECIFICAS EN LA CUAL BUSCAMOS CON UNA PALABRA CLAVE
const persona = {
    nombre: "Daniel",
    edad: 28,
    habla: true,
    numero: 2,
    
}
if ( 'edad'in persona ) {
        console.log("true")
}else{
    console.log("false")
}
//  NOT IN  !IN: SI UN OBJETO NO CONTIENE LA PROIEDAD ESPECIFICA CON OPERADOR LOGICO DEE NEGACION 
if (!(2 in persona)) {
    console.log("true")
}else{
    console.log("false")
}

// ESTRUCTURA DE CONTROL

// CONDICIONELES 
const num = "juan";


if ( num === "juan") {
    console.log("true");
    // Si numero es "daniel", imprimirá "true"
} else{
    console.log(false)
}

// INTERATIVAS
// for para ejecutar un bloque de codigo varias veces 
 let nume = 2

for (let i = 1; i <= nume; i++) {
    console.log(i);
}

 let  i  = 0
while ( i <= 10) {
    i++;
    console.log(i)
}

// * DIFICULTAD EXTRA (opcional):
// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
    // incremeto de 10 hasta el 55
  console.log(i)
//   condicion donde voy a mostrar los numero pares donde i se divide para 2 y si el reciduo es 0 muestre en consola
// y que no muestre el 16 para que muestre el 16 usamos el != contrario a 16
// tambien los multiplos de 3 se divide i para 3 donde el reciduo tiene que se contrario a 0
    if( i % 2 == 0  &&  i != 16 &&  i % 3 != 0){
console.log(i)
    }else{
        console.log(i)
    }
}