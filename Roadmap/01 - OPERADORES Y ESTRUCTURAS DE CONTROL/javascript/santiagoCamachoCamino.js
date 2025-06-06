// 00 - OPERADORES Y ESTRUCTURAS DE CONTROL
// Santiago Camacho Camino
// 2025-04-22

// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
// Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
// (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

/**
 * Operadores Aritméticos
 */

let a=5;
let b=10;
//Incrementación
console.log(++a); //6
//Muestra el valor de 'a' luego incrementa
console.log(a++); //6
//Resta
console.log(a-b); //-5
//Multiplicación
console.log(a*b); //50
//División
console.log(b/a); //2
//Modulo
console.log(b % a); //0

/**
 * Operadores de Asignación
 */

a += b; //15
a -=b ; //-5
a *= b; //50
a /= b; //0.5
a %= b; //5
a **= b; //9765625


/**
 * Operadores de Comparación
 */

//Operadores racionales
console.log(a > b); // false
console.log(a < b); // true
console.log(a <= b); // true
console.log(a >= b); // false

//Operadores de igualdad
console.log(a == b); //false
console.log(a != b); //true
// compara si son iguales en valor 
// y en tipo de dato
console.log(a !== b); //false 
console.log(a === b); //false 


/**
 * Operadores Lógicos
 */
let verdadero=true;
let falso=false;

//AND -> &&
/*
las dos expresiones tienen que ser verdaderas, para que devuelva 'true', 
si una es falsa devuelve 'false'
*/
console.log(verdadero && falso); //falso
console.log(verdadero && verdadero); //verdadero
console.log(falso && falso); //falso


//OR -> ||
/*
una de las dos expresiones tiene que ser verdadera, para que ddevuelva 'true',
si las dos son falsas devuelve 'false'
*/
console.log(verdadero || falso); //verdader
console.log(verdadero || verdadero); //verdadero
console.log(falso || falso); //falso

//NOT -> !

console.log(!verdadero); //false
console.log(!falso); //verdadero

/**
 * Operadores Bitwise
 */

console.log(a & b); //0
console.log(a | b); //282475259
console.log(a ^ b); //282475259
console.log(~a); //-282475250
console.log(a << b); //1491846144
console.log(a >> b); //275854

/**
 * Operador ternario
 */

let edadOperador=18;
let acceso = edadOperador >=17 ?'Es mayor de edad' : 'Es menor de edad '; //Es mayor de edad

/**
 *  Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 *  Debes hacer print por consola del resultado de todos los ejemplos.
 */

/**
 * Condicionales
 */

let edad=13;

if(edad < 13 ){
    console.log("Eres un niño/a");
}else if(edad >=13 && edad < 18){
    console.log("Eres un adolescente");
}else{
    console.log("Eres un adulto");
}

/**
 * Switch
 */

let numDia=7;

switch (numDia){
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miércoles");
        break;
    case 4:
        console.log("Jueves");
        break;
    case 5:
        console.log("Viernes");
        break;
    case 6:
        console.log("Sábado");
        break;
    default:
            console.log("Domingo");
}

/**
 * For
 */

for(let i = 1; i <=10; i++){
    console.log(i, "y su cuadrado es", Math.pow(i, 2))
}

/**
 * While
 */
let num=5;
while(num >=1){
    console.log(num);
    num--;
}

/**
 * Do...While 
 */
let num2=4;
do{
    console.log(`Número ingresado: ${num2}`);
    num2++;
}while(num2 < 10);


/**
 * For...in
 */

let persona={
    edad: 15,
    nombre: "Pepito",
    apellido: "Peréz",
}

for(let propiedades in persona){
    console.log(`${propiedades}: ${persona[propiedades]}`);
}

/**
 * For...of
 */
let frutas = ["sandia", "banana", "pera", "uva"];

for(let fruta of frutas){
    console.log(fruta);
}

/**
 * break/ continue
 */
for(let i=1; i<=10;i++){
    if(i == 5){
        continue;
    }else if(i == 8){
        break;
    }
    console.log(i);

}

/**
 * Extra
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */
for(let i=10; i<=55; i++){
    if(i % 2 == 1 || i % 3 == 0 || i == 16 ){
        continue;
    }
    console.log(i);
}