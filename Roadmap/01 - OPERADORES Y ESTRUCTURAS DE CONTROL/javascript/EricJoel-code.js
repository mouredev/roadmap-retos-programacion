// Tipos de operadores en JavaScript

//Operadores Aritméticos

let number = 10;
let number2 = 5;

console.log("Suma: " + (number + number2));
console.log("Resta: " + (5 - 3));
console.log("Multiplicación: " + (6 * 7));
console.log("División: " + (20 / 4));
console.log("Módulo: " + (10 % 3));
console.log("Incremento: " + (++number));
console.log("Decremento: " + (--number2));
console.log("Potenciación: " + (2 ** 3));

//Operadores de Comparación

console.log("Igualdad: " + (2 == 2));
console.log("Desigualdad: " + (3 != 3))
console.log("Mayor que: " + (5 > 8));
console.log("Menor que: " + (8 < 10));
console.log("Mayor o igual que: " + (7 >= 7));
console.log("Menor o igual que: " + (4 <= 6));

// Operadores Lógicos

console.log("AND lógico: " + (10 > 3 && 5 < 2));
console.log("OR lógico: " + (10 > 3 || 5 < 2));
console.log("NOT lógico: " + (!10 < 3));

// Operadores de asignación

let x = 15;

x += 5;
console.log("Asignación con suma: " + x);

x -= 3;
console.log("Asignación con resta: " + x);

x *= 2;
console.log("Asignación con multiplicación: " + x);

x /= 4;
console.log("Asignación con división: " + x);

x %= 6;
console.log("Asignación con módulo: " + x);

console.log("Asignación con potenciación: " + (x **= 2));

// Operadores de cadena

let saludo = "Hola, ";
let nombre = "Mundo!";
let mensajeCompleto = saludo + nombre;
console.log("Concatenación de cadenas: " + mensajeCompleto);

// Operadores ternarios

let edad = 20;
let esAdulto = (edad >= 18) ? "Sí, es adulto." : "No, es menor de edad.";
console.log("Operador ternario: " + esAdulto);

// Operadores de tipo de dato

console.log("Tipo de dato de '13': " + (typeof 13));
console.log("Tipo de dato de 'mensajeCompleto': " + (typeof mensajeCompleto));
console.log("Tipo de dato de 'true': " + (typeof true));

// Operadores de incremento y decremento

let contador = 0;
console.log("Contador inicial: " + contador);
contador++;
console.log("Contador después de incrementar: " + contador);
contador--;
console.log("Contador después de decrementar: " + contador);

// Operadores de identidad

let a = 5;
let b = '5';
let identidad = a === b;
console.log("¿a es idéntico a b?: " + identidad);

// Operadores de pertenencia

let arreglo = [1, 2, 3, 4, 5];
console.log("¿El arreglo contiene el número 3?: " + arreglo.includes(3));
console.log("¿El arreglo contiene el número 6?: " + arreglo.includes(6));

// Operadores bit a bit

let bitA = 5;  // En binario: 0101
let bitB = 3;  // En binario: 0011
console.log("AND bit a bit: " + (bitA & bitB)); // Resultado: 0001 (1 en decimal)
console.log("OR bit a bit: " + (bitA | bitB)); // Resultado: 0111 (7 en decimal)
console.log("XOR bit a bit: " + (bitA ^ bitB)); // Resultado: 0110 (6 en decimal)  

// Desplazamiento a la izquierda
console.log("Desplazamiento a la izquierda: " + (bitA << 1)); // Resultado: 1010 (10 en decimal)
// Desplazamiento a la derecha
console.log("Desplazamiento a la derecha: " + (bitA >> 1)); // Resultado: 0010 (2 en decimal)
// Desplazamiento a la derecha sin signo
console.log("Desplazamiento a la derecha sin signo: " + (bitA >>> 1)); // Resultado: 0010 (2 en decimal)    
// Operador NOT bit a bit
console.log("NOT bit a bit: " + (~bitA)); // Resultado: 1010 (en complemento a dos, -6 en decimal)
// Operador de negación bit a bit
console.log("Negación bit a bit: " + (~bitB)); // Resultado: 1100 (en complemento a dos, -4 en decimal)


// Estructuras de control

// Condicionales

let num = 7;

if (num > 0) {
    console.log(num + " es un número positivo.");
} else if (num < 0) {
    console.log(num + " es un número negativo.");
} else {
    console.log("El número es cero.");
}

// Condicional switch

let dia = 3;

switch (dia) {
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
    case 7:
        console.log("Domingo");
        break;
    default:
        break;
}

// Bucles

// Bucle for

for (let i = 1; i <= 5; i++) {
    console.log("Iteración número: " + i);
}

// Bucle while

let count = 1;
while (count <= 5) {
    console.log("Cuenta: " + count);
    count++;
}

// Bucle do...while

let conteo = 1;
do {
    console.log("Conteo: " + conteo);
    conteo++;
} while (conteo <= 3);

// Bucle for...of

let frutas = ["Manzana", "Platano", "Mango"];
for (let fruta of frutas) {
    console.log("Fruta: " + fruta);
}

// Bucle for...in

let persona = { nombre: "Joel", edad: 23, ciudad: "San Francisco" };
for (let clave in persona) {
    console.log(clave + ": " + persona[clave])
}

// Manejo de Excepciones
try {
    let resultado = 10 / 0;
    if (!isFinite(resultado)) {
        throw new Error("División por cero no permitida.");
    }
    console.log("Resultado: " + resultado);
} catch (error) {
    console.error("Error: " + error.message);
}

/* 
Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos) pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0)
        console.log(i);
}