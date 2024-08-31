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
let a = 1;
let b = 2;
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let modulo = a % b;
let incremento = a++;
let decremento = a--;

console.log('Suma = '+ suma);
console.log('Resta = '+ resta);
console.log('Multiplicación = '+ multiplicacion);
console.log('División = '+ division);
console.log('Módulo = '+ modulo);
console.log('Incremento = '+ incremento);
console.log('Decremento = '+ decremento);

// Asignacion

a = b;
console.log('a = b = '+ a);
a += 2;
console.log('Suma a = '+ a);
a -= 2;
console.log('Resta a = '+ a);
a *= 2;
console.log('Multiplicación a = '+ a);
a /= 2;
console.log('División a = '+ a);

// Comparación e identidad

console.log('a = '+a+' | b = '+ b);
let c = a > b;
console.log('a mayor que b -> '+c);
c = a < b;
console.log('a menor que b -> '+c);
c = a >= b;
console.log('a mayor o igual que b -> '+c);
c = a <= b;
console.log('a menor o igual que b -> '+c);
c = a == b;
console.log('a igual que b -> '+c);
c = a === b;
console.log('a estrictamente igual que b -> '+c);
c = a != b;
console.log('a diferente que b -> '+c);
c = a !== b;
console.log('a estrictamente diferente que b -> '+c);

// logicos

let combined = true && false;
console.log('AND -> '+ combined);
combined = true || false;
console.log('OR -> '+ combined);
combined = !true;
console.log('NOT -> '+ combined);

// Concatenar

let cadena1 = "Hola ";
let cadena2 = "mundo!";
let concatenada = cadena1 + cadena2;
console.log('Concatenación -> '+ concatenada);

// operadores ternarios

console.log(combined);
let resultado = combined===true? "Si" : "No";
console.log('Operador ternario -> '+ resultado);

// Tipos de datos
console.log(typeof(combined));
console.log(typeof(resultado));


// propagacion 
const numeros = [1, 2, 3, 4, 5];
console.log(...numeros); // Salida: 1 2 3 4 5

const numeros2 = [6, 7, 8];
const numerosCombinados = [...numeros, ...numeros2];
console.log(numerosCombinados); // Salida: [1, 2, 3, 4, 5, 6, 7, 8]


// membresia

    //in
    const persona = { nombre: 'Juan', edad: 30 };

    console.log('nombre' in persona); // true
    console.log('apellido' in persona); // false

    //instanceof
    class Persona {
        constructor(nombre) {
            this.nombre = nombre;
        }
    }
    
    const juan = new Persona('Juan');

    console.log(juan instanceof Persona); // true
    console.log(juan instanceof Array); // false
    
// exponenciacion
let potencia = a ** 4;
console.log(potencia);

// bits 
let x = 5; // Representación binaria: 0101

// Operador &= (AND a nivel de bits y asignación)
x &= 3; // Equivalente a: x = x & 3
// 0101 & 0011 = 0001 (resultado: 1)
console.log(x); // Salida: 1

// Operador |= (OR a nivel de bits y asignación)
x |= 8; // Equivalente a: x = x | 8
// 0001 | 1000 = 1001 (resultado: 9)
console.log(x); // Salida: 9

// Operador ^= (XOR a nivel de bits y asignación)
x ^= 12; // Equivalente a: x = x ^ 12
// 1001 ^ 1100 = 0101 (resultado: 5)
console.log(x); // Salida: 5

// Operador <<= (desplazamiento a la izquierda y asignación)
x <<= 2; // Equivalente a: x = x << 2
// 0101 << 2 = 010100 (resultado: 20)
console.log(x); // Salida: 20

// Operador >>= (desplazamiento a la derecha y asignación)
x >>= 1; // Equivalente a: x = x >> 1
// 010100 >> 1 = 001010 (resultado: 10)
console.log(x); // Salida: 10

// Operador >>>= (desplazamiento a la derecha sin signo y asignación)
x >>>= 1; // Equivalente a: x = x >>> 1
// 001010 >>> 1 = 000101 (resultado: 5)
console.log(x); // Salida: 5

// Estructuras de control

//if
let z = 26, y = 28;
if(z < y) {
    console.log('z es menor que y');
} else {
    console.log('No es menor que el');
}

// for

const animals = ['dog', 'cat', 'bird', 'horse']
for (let mascotas of animals) {
    //console.log(mascotas);
}

for (let i = 0; i <= animals.length; i++) {
    //console.log(animals[i]);
}

for (let name in animals) {
    //console.log('Indice '+name);
}

// while
let i = 0;
while(i < animals.length) {
    //console.log(animals[i]);
    i++;
}

// do while
let q = 0;
const nums = [29.8748, 30.1234, 30.1234, 3, 4, 5, 6, 7, 8, 9, 10]
do {
    //console.log(nums[q]);
    q++;
} while (q < nums.length);

// switch
let verdader = true;
let falso = false;
let input = undefined;

switch (input) {
    case verdader:
        console.log('Verdadero');
        break;
    case falso:
        console.log('Falso');
        break;
    default:
        console.log('No aplica');
        break;
}

// try/catch

try {
    let result = 10 / 0;
    console.log(result);
} catch (error) {
    console.log(error.message); // Mostrará "Division by zero"
} finally {
    console.log('Final');
}

// DIFICULTAD EXTRA (opcional):
// Crea un programa que imprima por consola todos los números comprendidos
// entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
console.log('\nSTART PROGRAM\n');
const output = [];
const programa = (i) => (i !== 16 && i % 3 !== 0 && i % 2 === 0) ? output.push(i) : null;

for (let i = 10; i <= 55; i++) programa(i);

console.log(output);
console.log('\nEND PROGRAM\n');
