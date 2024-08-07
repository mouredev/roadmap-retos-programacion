// #01 OPERADORES Y ESTRUCTURAS DE CONTROL
// Ejercicio de la ruta de programacion 2024 / by MoureDev

//          *** Operador de asignación (=) ***

let x = 34;                   //asigna el valor de una variable
let y = 20;
console.log(" asignando un valor x = 34");



//           *** Operadores aritmétricos (operaciones matemáticas) ***

x + y                         // Adición (+)
x - y                         // Resta (-)
x * y                         // Multiplicación (*)
x ** y                        // Exponenciación (**)  --- a partir de ES6 ---
x / y                         // División (/)
x % y                         // Módulo (%) (resto de la división)
x ++                          // Incremento (++)
y --                          // Decremento (--)

console.log(`-------------operaciones aritmeticas--------------`);
console.log(`x + y = ${x+y}`);
console.log(`x - y = ${x-y}`);
console.log(`x * y = ${x*y}`);
console.log(`x ** y = ${x**y}`);
console.log(`x / y = ${x/y}`);
console.log(`x % y = ${x%y}`);
console.log(`x ++ = ${x++}`);
console.log(`x -- = ${x--}`);



//           *** Operadores de asignación de adición ***

x += y;                         // equivale a: x = x + y
x -= y;                         // equivale a: x = x - y
x *= y;                         // equivale a: x = x * y
x /= y;                         // equivale a: x = x / y
x **= y;                        // equivale a: x = x ** y 
x %= y;                         // equivale a: x = x % y 

console.log(`-------------operaciones de asignacion--------------`);
console.log(`x += y = ${x+=y}`);
console.log(`x -= y = ${x-=y}`);
console.log(`x *= y = ${x*=y}`);
console.log(`x **= y = ${x**=y}`);
console.log(`x /= y = ${x/=y}`);
console.log(`x %= y = ${x%=y}`);


//           *** Operadores de comparación ***

x == y;                         // son iguales
x === y;                        // igual valor e igual tipo
x != y;                         // NO son iguales
x !== y;                        // No son iguales o No son del mismo tipo
x > y;                          // mayor que
x < y;                          // menor que
x >= y;                          // mayor o igual
x <= y;                          // menor o igual

console.log(`-------------operaciones de comparación--------------`);
console.log(`Es x igual a y?: ${x==y}`);
console.log(`Es x de igual valor e igual tipo a y?: ${x===y}`);
console.log(`Es x diferente a y?: ${x!=y}`);
console.log(`Es x diferente valor y tipo a y?: ${x!==y}`);
console.log(`Es x mayor que y?: ${x > y}`);
console.log(`Es x menor que y?: ${x < y}`);
console.log(`Es x mayor o igual que y?: ${x >= y}`);
console.log(`Es x menor o igual que y?: ${x <= y}`);






//          *** Operador ternario ***

// ?        tiene tres operandos 
// Con frecuencia se utiliza como atajo para la expresion IF

//          *** Operadores lógicos ***

x > y && y < 10;                 // AND, se usan para concatenar condiciones, todas se deben cumplir
x > y || y < 10;                 // OR, o se cumple una o se cumple la otra
!(x > y)                         // NOT, lo contrario a lo que se expone

console.log(`-------------operaciones lógicos--------------`);

if (x < 100 && x > y) {
    console.log(`${x} es mayor que ${y} pero menor que 100`);
}

if (x > 100 || x > y) {
    console.log(`${x} es mayor que ${y} o es mayor que 100`);
}
if (!(x = y)) {
    console.log(`${x} es diferente de ${y}`);
}


//          *** Operadores de tipo ***

typeof(x)                       // Devuelve el tipo del parámetro

function variable(leng) {       // Creando un objeto
    this.leng = leng;
}
const z = new variable('v');

z instanceof variable           // Devuelve true si un objeto es una instancia de un tipo de objeto

if (z instanceof variable) {
    console.log("z es una instancia del objeto 'variable'");
    
}
//          *** Operadores bit a bit ***

x & y                           // Realiza una operación AND binaria. Devuelve 1 en las posiciones de bit dónde las posiciones de los dos operadores tienen un 1.
x | y                           // Realiza una operación OR binaria. Devuelve un cero en las posiciones de bit dónde las posiciones de los dos operadores tienen un 0.
x ^ y                           // Realiza una operación XOR binaria. Devuelve un cero en las posiciones dónde el bit es el mismo y un 1 dónde las posiciones son diferentes.
~x                              // Realiza una operación NOT binaria.
x << y                          // Realiza un desplazamiento de bits a la izquierda.
x >> y                          // Realiza un desplazamiento de bits a la derecha.
x >>> y                         // Realiza un desplazamiento de bits a la derecha rellenando con ceros.

//          *** Estructuras de Control ***

// Condicional IF ELSE

if (x > y) {                                    // Las declaraciones condicionales se utilizan para 
    console.log(`${x} es mayor que ${y}`);      // realizar diferentes acciones en función de 
                                                // diferentes condiciones.
} else if(x < y) {
    console.log(`${x} es menor que ${y}`);
    
} else{
    console.log('Son iguales');
    
}

// Condicional Switch

switch (typeof(x)) {                                            // La declaración de switch se utiliza para 
    case 'number':                                              // realizar diferentes acciones según 
        console.log(`${x} es de tipo numerico`);                // diferentes condiciones.
        
        break;
    case 'string':
        console.log(`${x} es de tipo cadena de texto`);
        
        break;   
    case 'boolean':
        console.log(`${x} es de tipo booleano`);
        
        break;  

    default:
        console.log(`${x} es de un tipo diferente, mas adelante seguiremos averiguando`);

        break;
}

//              *** Bucles (Loops) ***
// Los bucles pueden ejecutar un bloque de código varias veces.
// Bucle FOR

for (let i = 0; i < 5; i++) {               
    console.log("El numero es " + i );
}

// Bucle FOR IN
// La instrucción for in recorre las propiedades de un objeto, o tambien de un Array

const someone: object = { name: 'Camilo', age: 34 };
for (const p in someone) {
    console.log(`${p} -> ${someone[p]}`);
}

// Bucle FOR OF
// Recorre los valores de un objeto iterable. Le permite recorrer estructuras de datos iterables como arrays, strings, maps, NodeLists y más:

const myArray: number[] = [1, 2, 5, 2, 7, 9];
for (const myNumber of myArray) {
    console.log(`# => ${myNumber}`);
}

// Bucle While
// Recorre un bloque de código siempre que una condición especificada sea verdadera.

let mySecondNumber: number = 0;
while (mySecondNumber < 5) {
    console.log(`Iteración: ${mySecondNumber}`);
    mySecondNumber++;
}

// Bucle Do While
// El bucle do while es una variante del bucle while. Este bucle ejecutará el bloque de código una vez,
// antes de verificar si la condición es verdadera, luego repetirá el bucle mientras la condición sea verdadera.

mySecondNumber = 0;
do {
    console.log(`Iteración: ${mySecondNumber}`);
    mySecondNumber++;
} while (mySecondNumber < 5);

//          ***Manejo de errores (try catch)***

// El mecanismo try...catch en TypeScript detecta excepciones durante la ejecución del código dentro del bloque try. 
// Cuando se produce un error, el control se pasa al bloque catch, lo que le permite manejar el error con elegancia.

try {
    throw Error('codigo que de error');
} catch (e: any) {
    console.log('error');
    console.log(e.message);
} finally {
    console.log('codigo que si se ejecutará');
}


// **********************************************************************************************************
//          *** Dificultad extra***

/*Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
console.log("Ejercicio extra");

for (let i = 10; i <= 55; i++) {
    if ((i % 2 === 0) && (i !== 16) && (i % 3 !== 0)) {
        console.log(i);
    }
}