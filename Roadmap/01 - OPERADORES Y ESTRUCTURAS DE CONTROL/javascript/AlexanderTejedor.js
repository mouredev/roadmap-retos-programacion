// Operadores de asignación 

/**Asignación */
var x = 5; // x = y;
var y = 10;
console.log(x);
/**Asignación de adición */
x += y; // x = x + y;
console.log(x);
/**Asignación de resta */
x -= y; // x = x - y;
console.log(x);
/**Asignación de multiplicación */
x *= y; // x = x * y;
console.log(x);
/**Asignación de división */
x /= y; // x = x / y;
console.log(x);
/**Asignación de residuo */
x %= y; // x = x % y;
console.log(x);
/**Asignación de exponenciación */
x **= y; // x = x ** y;
console.log(x);
/**Asignación de desplazamiento a la izquierda */
x <<= y; // x = x << y;
console.log(x);
/**Asignación de desplazamiento a la derecha */
x >>= y; // x = x >> y;
console.log(x);
/**Asignación de desplazamiento a la derecha sin signo*/
x >>>= y; //x = x >>> y
console.log(x);
/**Asignación AND bit a bit*/
x &= y; // x = x & y;
console.log(x);
/**Asignación XOR bit a bit*/
x ^= y; // x = x ^ y;
console.log(x);
/**Asignación OR bit a bit*/
x |= y; // x = x | y;
console.log(x);
/**Asignación AND lógico*/
x &&= y; // x && (x = y);
console.log(x);
/**Asignación OR lógico*/
x ||= y; // x || (x = y);
console.log(x);
/**Asignación de anulación lógica */
x ??= y; // x ?? (x = y)
console.log(x);

// Operadores de comparación 
var x = 10;
var y = 15;
var var1 = true;
var var2 = false;

/**Igualdad */
var z = var1 == var2;
console.log(z);
/**No es igual */
var z = var1 != var2;
console.log(z);
/**Estrictamente igual */
var z = x === y;
console.log(z);
var a = var1 === var2;
console.log(a);
/**Desigualdad estricta */
var z = var1 !== var2;
console.log(z);
/**Mayor que */
var z = x > y;
console.log(z);
/**Mayor o igual que */
var z = x >= y;
console.log(z);
/**Menor que */
var z = x < y;
console.log(z);
/**Menor o igual que */
var z = x <= y;
console.log(z)

//Operadores aritméticos
var x = 12;
var y = 5;

/**Residuo */
var z = x % y;
console.log(z);
/**Incremento */
var z = x++;
console.log(z);
var b = ++x;
console.log(b);
/**Decremento */
var z = x--;
console.log(z);
var b = --x;
console.log(b);
/**Negación Unitaria */
var z = -x;
console.log(z);
/**Positivo Unitario */
var z = +"3";
console.log(z, typeof(z));
/**Operador de exponenciación */
var z = x ** y;
console.log(z);

//Operadores bit a bit
var a = 1;
var b = 0;

/**AND a nivel de bits */
var z = a & b;
console.log(z);
/**OR a nivel de bits */
var z = a | b;
console.log(z);
/**XOR a nivel de bits */
var z = a ^ b;
console.log(z);
/**NOT a nivel de bits */
var z = ~ a;
console.log(z);
/**Desplazamiento a la izquierda */
var z = a << b;
console.log(z);
/**Desplazamiento a la derecha de propagación de signo */
var z = a >> b;
console.log(z);
/**Desplazamiento a la derecha de relleno cero */
var z = a >>> b;
console.log(z);

//Operador de desplazamiento de bits
var a = 9;
var b = 2;

/**Desplazamiento a la izquierda */
console.log(a << b);
/**Desplazamiento a la derecha de propagación de signo */
console.log(a >> b);
/**Desplazamiento a la derecha de relleno cero */
console.log(a >>> b);

//Operadores Lógicos
let expr1 = true;
let expr2 = false;

/**AND lógico */
console.log(expr1 && expr2);
/**OR Lógico */
console.log(expr1 || expr2);
/**NOT Lógico */
console.log(!expr1);
console.log(!expr2);

//Operador de Cadena
console.log('Hola ' + 'JavaScript' );

let hello = 'Hola ';
console.log(hello += 'JavaScript');

//Operador condicional (ternario)
let val1 = 20;
let val2 = 15;

let isAdult = val2 >= 18 ? 'Adult' : 'Minor';
console.log(isAdult);

//Operador unarios

/**DELETE */
x = 42;
var o = 43;
var myObj = { h:4, }

console.log(delete x);
console.log(delete o);
console.log(delete Math.PI);
console.log(delete myObj.h);

/**typeof */
let myFun = new Function('5 + 2');
let myName = 'Alexander';
var age = 26;
let fruit = ['apple', 'wathermelon', 'Banana'];

console.log(typeof(myFun));
console.log(typeof(myName));
console.log(typeof(age));
console.log(typeof(fruit));
console.log(typeof(true));

//Estructuras de control en JavaScript

/** Condicionales
 * if - else if
 * Confirmar si una persona es mayor de edad 
 * */
var age = 10;
if (age >= 18 ){
    console.log('Eres mayor de edad, puedes pasar')
} else if (age < 18) {
    console.log('Lo sentimos, pero no puedes pasar')
} else if (age != Number) {
    console.log('Por favor ingresa un dato valido')
}
/**Swith
 * Mensaje dependiendo del día
 */
let day = 'lunes';
switch (day) {
    case 'lunes':
        console.log(`perfecto hoy es ${day}`)
        break;
    case 'martes':
        console.log(`perfecto hoy es ${day}`)
        break;
    case 'miercoles':
        console.log(`perfecto hoy es ${day}`)
        break;
    case 'jueves':
        console.log(`perfecto hoy es ${day}`)
        break;
    case 'viernes':
        console.log(`perfecto hoy es ${day}`)
        break;
    default:
        console.log(`Perfectooo es Fin de Semana`)
}

/**Bucles (Iteraciones)
 * for
 */
for (let i = 0; i < 5; i++ ){
    console.log(i)
}

/**Recorrido de un array */
let food = ['Meat','Beans','Milk','Potatos','Tomatos','Eggs'];

for (let i = 0; i < food.length; i++ ){
    let list = food[i]
    console.log(`The food in your list is ${list}`)
}

/**While */
let suma = 0;
let numero = 1;

while (numero <= 10){
    console.log('Suma ', suma += numero);
    console.log('Numero ', numero++);
}

/**do while */

let result = '';
let i = 0;

do {
    i = i + 1;
    result = result + i;
} while (i < 5);
console.log(result);

/**for in */
const object = {a:1, b:2, c:3}

for (const property in object){
    console.log(`${property}: ${object[property]}`);
}

/**for of */
const array1 = ["a", "b", "c"];

for (const element of array1) {
    console.log(element);
}

let persona = { nombre: "Alexander", edad: 26, ciudad: "Colombia" };

for (let clave in persona) {
    console.log(clave + ": " + persona[clave]);
}

/**Control de excepciones
 * try catch
 */

try {
    let resultado = 10 / 0;
    console.log(resultado);
} catch (error) {
    console.log("Se ha producido un error: " + error.message);
}

/**throw */

function verificarEdad(edad) {
    if (edad < 18) {
        throw new Error("No puedes acceder, eres menor de edad.");
    }
    return "Acceso permitido.";
}

/**finally */

try {
    console.log("Intentando ejecutar código...");
} catch (error) {
    console.log("Error encontrado: " + error.message);
} finally {
    console.log("Este código se ejecuta siempre.");
}

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

for (i = 10; i <= 55; i++){
    let result = i / 3;
    if (i % 2 === 0 && Number.isInteger(result) === false){
        if (i === 16){ continue };
        console.log(i);
    };
};
