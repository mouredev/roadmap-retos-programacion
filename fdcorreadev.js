/**
 * Realizo el ejercicio leyendo todo sobre los operadores en javascript para con ellos poder interpretar y programarlos
 * fuente: https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_operators#Asignación
 */

let x = 8;
let y = 9;
//Asignación
x = y
console.log(`Asignación ${x}`)
// Asignación de adicion y abreviación
x = 8
y = 9
console.log(`valores de entrada para las operaciones ${x}, ${y}`)
x = x + y
console.log(`Asignación de adicion ${x}`)
// abreviación
x += y
// Asignación de resta y abreviación
x = 8
y = 9

x = x - y
console.log(`Asignación de resta ${x}`)
x -= y

// Asignación de multiplicación y abreviación
x = 8
y = 9

x = x * y
console.log(`Asignación de multiplicación ${x}`)
x *= y
// Asignación de división y abreviación
x = 8
y = 9

x = x / y
console.log(`Asignación de división  ${x}`)
x /= y
// Asignación de residuo y abreviacion
x = 8
y = 9

x = x % y
console.log(`Asignación de residuo  ${x}`)
x %= y

// Asignación de exponenciación y abreviacion
x = 8
y = 9

x = x ** y
console.log(`Asignación de exponenciación  ${x}`)
x **= y
// Asignación de desplazamiento a la izquierda y abreviacion
/* 
REALIZO ESTA ACLARACIÓN PORQUE NO SABIA QUE SIGNIFICABAN

En JavaScript, los operadores << y <<= son operadores de desplazamiento de bits (bitwise shift).
- ejemplo:
El valor de x es 8 (en binario: 00000000000000000000000000001000).
El valor de y es 9.
x << y significa que los bits de x (que es 8) se desplazan 9 posiciones a la izquierda.
8 en binario es 00000000000000000000000000001000.
Después de desplazarlo 9 posiciones a la izquierda: 00000000000000000001000000000000 (que en decimal es 4096).
Ahora, x toma el valor de 4096. 
*/
x = 8
y = 9

x = x << y
console.log(`Asignación de desplazamiento a la izquierda ${x}`)
x <<= y

// Asignación de desplazamiento a la derecha y abreviacion
x = 8
y = 9

x = x >> y
console.log(`Asignación de desplazamiento a la derecha ${x}`)
x >>= y

// Asignación de desplazamiento a la derecha sin signo y abreviación
x = 8
y = 9

x = x >>> y
console.log(`Asignación de desplazamiento a la derecha sin signo ${x}`)
x >>>= y

// Asignación AND bit a bit y abreviación
x = 8
y = 9

x = x & y
console.log(`Asignación AND bit a bit ${x}`)
x &= y

// Asignación XOR bit a bit y abreviación
x = 8
y = 9

x = x ^ y
console.log(`Asignación XOR bit a bit ${x}`)
x ^= y
// Asignación OR bit a bit y abreviación
x = 8
y = 9

x = x | y
console.log(`Asignación OR bit a bit ${x}`)
x |= y
// Asignación AND logico y abreviación
x = 8
y = 9

x && (x = y)
console.log(`Asignación AND logico ${x}`)
x &&= y

// Asignación OR logico y abreviación
x = 8
y = 9

x || (x = y)
console.log(`Asignación OR logico  ${x}`)
x ||= y
// Asignación de anulación lógica y abreviación
x = 8
y = 9

x ?? (x = y)
console.log(`Asignación de anulación lógica ${x}`)
x ??= y

//ESTRUCTURA DE CONTROL PARA JAVASCRIPT

// condicional IF permite elvaluar si cumple una codicion
let mayorEdad = 24

if (mayorEdad >= 18) {
    console.log(`es mayor de edad ${mayorEdad}`)
} else if (mayorEdad > 18 & mayorEdad <= 25) {
    console.log(`es adulto joven ${mayorEdad}`)
} else {
    console.log(`es manor de edad ${mayorEdad}`)
}

// bluce for se ejecuta hasta que la codicion de se cumpla

const pasos = 5

for (let paso = 0; paso <= pasos; paso++) {
    console.log(`estoy dando el paso: ${paso}`)
}


// while ejecuta la sentencia mientras la codicion que se esta evaluando sea verdadera
let contador = 0
while (contador < 4) {
    contador++;
    console.log(`el contador va en ${contador}`)
}
console.log("Contador es igual a ", contador)

// la sentencia "hacer mientras" esto se va ejecutar hasta la condicion del while se cumpla
let result = '';
let cont = 0;
do {
    cont++;
    result = result + cont;
    console.log(`sigo haciendo esto ${result}`)
} while (cont < 5);

console.log(`finalice cumpli la condicion ${result}`);

// switch permite evaluar una expresion item a item o valor de entrada para decidir en que proceso debe correr segun el case
let fruitType = 'naranja'

switch (fruitType) {
    case "manzana":
        console.log(`la Manzana vale 10`)
        break;
    case "naranja":
        console.log(`la naranja vale 5`)
        break;
    case "pera":
        console.log(`la pera vale 8`)
        break;

    default:
        break;
}

try {
    let operation  =  10 / 0;
    if(!isFinite(operation)){
        throw new Error("Resultado es Infinity, operacion no valida");
    }
} catch (error) {
    console.log(`Esta operacion no es valida ${error.message}`)
}

// este es un ejemplo  donde combinamos un blucle y un array con datos para ver como funciona de mejor manera.
let fruta = [{ fruit: "manzana", value: 10 }, { fruit: "naranja", value: 5 }, { fruit: "pera", value: 8 }]

fruta.forEach((fruitType) => {
    switch (fruitType.fruit) {
        case "manzana":
            console.log(`la Manzana vale ${fruitType.value}`)
            break;
        case "naranja":
            console.log(`la naranja vale ${fruitType.value}`)
            break;
        case "pera":
            console.log(`la pera vale ${fruitType.value}`)
            break;

        default:
            break;
    }
})


//ejercicio para practicar lo visto 
/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. 
 */

console.log(`-----------------------------------------Ejercicio practico-----------------------------------------------------------------`)


for(let num = 10; num <= 55; num++){
    if(num % 2 === 0 && num !== 16 && num % 3 !== 0) console.log(num)
}
