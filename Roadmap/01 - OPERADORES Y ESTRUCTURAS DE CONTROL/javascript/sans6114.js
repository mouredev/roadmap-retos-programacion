/*
// Operadores Aritméticos
let num1 = 10;
let num2 = 5;

console.log("Operadores Aritméticos:");
console.log(`Suma: ${num1} + ${num2} = ${num1 + num2}`); // Suma
console.log(`Resta: ${num1} - ${num2} = ${num1 - num2}`); // Resta
console.log(`Multiplicación: ${num1} * ${num2} = ${num1 * num2}`); // Multiplicación
console.log(`División: ${num1} / ${num2} = ${num1 / num2}`); // División
console.log(`Módulo: ${num1} % ${num2} = ${num1 % num2}`); // Módulo

// Operadores de Asignación
console.log("\nOperadores de Asignación:");
let result = 0;
result += num1; // Suma y asigna
console.log(`Asignación de suma: result += ${num1} -> result = ${result}`);
result -= num2; // Resta y asigna
console.log(`Asignación de resta: result -= ${num2} -> result = ${result}`);
result *= num2; // Multiplica y asigna
console.log(`Asignación de multiplicación: result *= ${num2} -> result = ${result}`);
result /= num2; // Divide y asigna
console.log(`Asignación de división: result /= ${num2} -> result = ${result}`);

// Operadores de Comparación
console.log("\nOperadores de Comparación:");
console.log(`Es igual: ${num1} == ${num2} -> ${num1 == num2}`); // Igual
console.log(`Es idéntico: ${num1} === ${num2} -> ${num1 === num2}`); // Idéntico, osea estrictamente igual a
console.log(`Es diferente: ${num1} != ${num2} -> ${num1 != num2}`); // Diferente
console.log(`Es diferente (estricto): ${num1} !== ${num2} -> ${num1 !== num2}`); // Diferente estricto
console.log(`Es mayor: ${num1} > ${num2} -> ${num1 > num2}`); // Mayor
console.log(`Es menor: ${num1} < ${num2} -> ${num1 < num2}`); // Menor
console.log(`Es mayor o igual: ${num1} >= ${num2} -> ${num1 >= num2}`); // Mayor o igual
console.log(`Es menor o igual: ${num1} <= ${num2} -> ${num1 <= num2}`); // Menor o igual

// Operadores Lógicos
console.log("\nOperadores Lógicos:");
let a = true;
let b = false;
console.log(`Y (AND): ${a} && ${b} -> ${a && b}`); // AND
console.log(`O (OR): ${a} || ${b} -> ${a || b}`); // OR
console.log(`NO (NOT): !${a} -> ${!a}`); // NOT, es la negación

// Operadores de Identidad
console.log("\nOperadores de Identidad:");
console.log(`Identidad: ${num1} === ${num1} -> ${num1 === num1}`); // Identidad
console.log(`No identidad: ${num1} !== ${num2} -> ${num1 !== num2}`); // No identidad

// Operadores de Pertenencia
console.log("\nOperadores de Pertenencia:");
let array = [1, 2, 3, 4, 5];
console.log(`¿1 pertenece al array? ${array.includes(1)}`); // Pertenencia
console.log(`¿6 pertenece al array? ${array.includes(6)}`); // Pertenencia

// Operadores de Bits (no los entendi mucho)
console.log("\nOperadores de Bits:");
let bit1 = 5;  // 0101 en binario
let bit2 = 3;  // 0011 en binario
console.log(`AND Bit a Bit: ${bit1} & ${bit2} = ${bit1 & bit2}`); // AND
console.log(`OR Bit a Bit: ${bit1} | ${bit2} = ${bit1 | bit2}`); // OR
console.log(`XOR Bit a Bit: ${bit1} ^ ${bit2} = ${bit1 ^ bit2}`); // XOR
console.log(`Negación Bit a Bit: ~${bit1} = ${~bit1}`); // NOT
console.log(`Desplazamiento Izquierda: ${bit1} << 1 = ${bit1 << 1}`); // Desplazamiento a la izquierda
console.log(`Desplazamiento Derecha: ${bit1} >> 1 = ${bit1 >> 1}`); // Desplazamiento a la derecha


//CONDICIONALES
//IF ELSE
const numero = 15
if (numero >= 10) {
    if (numero == 10) {
        console.log('el numero es 10')
    } else {
        console.log('numero no es 10, es mayor')
    }
} else {
    console.log('el numero es menor a 10')
}
const nombres = [
    'santiago',
    'juan',
    'martin',
    'natalia',
    'pablo',
]
//SWITCH
for (let i = 0; i < nombres.length; i++) {
    switch (nombres[i]) {
        case 'santiago':
            console.log(`hola ${nombres[i]}, en esta iteración estoy saludando a santi.`)
            break;
        case 'juan':
            console.log(`hola ${nombres[i]}, en esta iteración estoy saludando a juan.`)
            break;
        case 'martin':
            console.log(`hola ${nombres[i]}, en esta iteración estoy saludando a martin.`)
            break;
        default:
            console.log('esta case va a imprimirse 2 veces')
            break;
    }
}

//CICLOS
//WHILE
let miNombre = 'santi'
while (miNombre.length <= 10) {
    if (miNombre.length == 10) {
        console.log('tu variable logro tener 10 caracteres')
        break
    }
    console.log(miNombre)
    miNombre += 'i'
}
//DO WHILE
let miNumero = 10
while (miNumero > 20) {
    console.log('se ejecuto el while')
}

do {
    console.log('se ejecuto el do while')
} while (miNumero > 20)

//FOR
const misNumeros = [
    1,
    2,
    3,
    4,
    5,
    6,
]
for (let i = 0; i < misNumeros.length; i++) {
        (misNumeros[i] % 2 === 0) ? console.log(`${misNumeros[i]}, es par`) : console.log(`no es par,`)
}
/*
/* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

//forma 1
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0) {
        if (i === 16 || i % 3 == 0) {
            continue //continue pasara a la siguiente iteracion, si pusiera break el programa al encontrar con 16 dejaria de ejecutarse.
        }
        console.log(i)
    }
}
console.log('forma 2:')
//forma 2
for (let i = 10; i <= 55; i++) {
if(i % 2 === 0 && i !== 16 && i % 3 !== 0){
    console.log(i) 
}
}