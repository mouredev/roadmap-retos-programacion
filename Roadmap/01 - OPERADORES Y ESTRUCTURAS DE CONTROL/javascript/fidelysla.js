
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * 
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

//? TIPOS DE OPERADORES

// **Operadores Aritmeticos**
let num1 = 3
num1 + num1
num1 - 1
num1++
num1++
num1--
++num1
--num1
++num1
// console.log(num1);

num1 * num1
num1 ** num1
num1 / num1
12 % 5

// **Operador de asignacion**
let num2 = 20
num2 += 1
num2 -= 1
num2 *= 1
num2 /= 2
num2 **= 2

// **Operadores de comparacion**
3 == "3" //true
3 === "3" //false
4 != "4" //false
4 !== "4" //true
3 > 2 //true
4 < 5 //true
6 >= 5 //true

// **Operadores Logicos**
let isString = true;
let isNum = false;

console.log(isString && isNum);
console.log(isString || isNum);
console.log(!isNum);

// **Operadores Bit a Bit**
let a = 5;  // Representación binaria: 0101
let b = 3;  // Representación binaria: 0011

console.log(a & b);  // 1 (AND a nivel de bits)
console.log(a | b);  // 7 (OR a nivel de bits)



// ? Ejemplos de tipos de estructuras de control

// **Condicionales**

// If-else
if (isString && isNum) {
    console.log("Son tipos de datos verdaderos");
} else if (isString || isNum) {
    console.log("Por lo menos uno es tipo de dato verdadero");
}

if ( 15 > 16 ) {
    console.log("Consola 1");
} else if (15 < 16) {
    console.log("Consola 2");
}

// Switch
let day = new Date().getDay()
switch (day) {
    case 0:
        console.log("Hoy es Domingo");
        break;
    case 1:
        console.log("Hoy es Lunes");
        break;
    case 2:
        console.log("Hoy es Martes");
        break;
    case 3:
        console.log("Hoy es Miercoles");
        break;
    case 4:
        console.log("Hoy es Jueves");
        break;
    case 5:
        console.log("Hoy es Viernes");
        break;
    default:
        console.log("Hoy es Sabado");
        break;
};

// **Ciclos**

// For
for (let index = 0; index <= 10; index++) {
    (index % 2 === 0)
        ? console.log(index)
        : "";
};

// for in
let abc = { a: 1, b: 2, c: 3 };
for (const key in abc) {
    if (Object.hasOwnProperty.call(abc, key)) {
        const element = abc[key];
        console.log(element);
    }
};

// for of
let arr1 = ["a","b","c","d","e"]
for (const iterator of arr1) {
    console.log(iterator);
};

// forEach
arr1.forEach( (v, i) => {
    console.log(`Index: ${i}, Value: ${v}`);
});

// While
// Numeros entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
let num3 = 10
while (num3 <= 55) {
    if (num3 === 10) {
        console.log(num3);
    } else if (num3 % 3 === 0 || num3 === 16) {

    } else {
        console.log(num3);
    }
    num3++
    num3++
};

// do-while
do {
    console.log(num3);
    num3++
} while (num3 <= 20);


// **Manejo de Errores**

try {
    noExiste;
    console.log("*")
} catch (error) {
    console.log(error)
} finally {
    console.log("*")
};
