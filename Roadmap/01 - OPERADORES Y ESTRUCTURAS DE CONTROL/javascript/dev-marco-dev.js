//OPERADORES ARITMETICOS
let suma = 5 + 5;
let resta = 15 - 10;
let multiplicacion = 5 * 5;
let division = 20 / 4;
let exponente = 2 ** 2;
let modulo = 4 % 4;
let x = 5;
x++; // console.log(x) da como resultado 6
x--; // console.log(x) vuelve a dar como resultado 5

//Acortadores
/*Estos acortadores hacen dos cosas a la vez primero hacen la operacion 
y a la vez asigna a la variable*/

//Ejemplos
// x += y ---> x = x + y
// x -= y ---> x = x - y
// x *= y ---> x = x * y
// x /= y ---> x = x / y
// x %= y ---> x = x % y
// x **= y ---> x = x ** y

//OPERADORES LOGICOS

// && and para que devuelva true ambos tiene que ser true
// || or  devuelve true si al menos uno de los operandos es true devuelve false si ambos son false
// ! not niega el operando si es false ahora sera true y visceversa
// ?? devuelve el valor del operando de la izquierda siempre y cuando no sea ni null ni undefined

// OPERADORES DE COMPARACION
//igualdad de valor
10 == 10;

// igualdad de valor

10 === 10;

// diferente de

3 != 3;

// diferencia estricta

3 !==
  // mayor que

  30 > 15;

// menor que

15 < 30;

// mayor o igual que

30 >= 30;

// menor o igual que

15 <= 15;

/* operadores de pertenencia
operador in verifica si una propiedad o clave existe dentro de un objeto

*/

let animal = {
  nombre: "negra",
  edad: 4,
};

console.log("nombre" in animal); //true

//tambien se puede para un arreglo

let array = [1, 2, 4, 5, 6];

console.log(4 in array); //true

/* el metodo inludes tambien se utiliza para verificar si algun elemento esta dentro
de un array*/

let array1 = [2, 4, 5, 6, 7];
console.log(array1.includes(9)); //false

//Ejercicio
/*Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.*/

for (let i = 10; i <= 55; i++) {
  if (i % 2 == 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
