//Operadores de asignación
console.log(`Operadores de asignación`)
let a = 5;
let b = 10;

console.log(`Operador =: a = 5`);
console.log(`Operador =: b = 10`);
console.log(`Operador +=: a += b = ${a += b}`)
console.log(`Operador -=: a -= b = ${a -= b}`)
console.log(`Operador *=: a *= b = ${a *= b}`)
console.log(`Operador /=: a /= b = ${a /= b}`)
console.log(`Operador %=: a %= b = ${a %= b}`)
console.log(`Operador **=: a **= b = ${a **= b}`)
console.log(`Operador >>=: a >>= b = ${a >>= b}`)
console.log(`Operador <<=: a <<= b = ${a <<= b}`)
console.log(`Operador >>>=: a >>>= b = ${a >>>= b}`)
console.log(`Operador &=: a &= b = ${a &= b}`)
console.log(`Operador ^=: a ^= b = ${a ^= b}`)
console.log(`Operador |=: a |= b = ${a |= b}`)
console.log(`Operador &&=: a &&= b = ${a &&= b}`)
console.log(`Operador ||=: a ||= b = ${a ||= b}`)
console.log(`Operador ??=: a ??= b = ${a ??= b}`)
console.log(`.........................................`)

//Operadores aritméticos
console.log(`Operadores aritméticos`);
let num1 = 18;
let num2 = 2;
let num3 = "5"

console.log(`Suma: ${num1} + ${num2} = ${num1 + num2}`);
console.log(`Resta: ${num1} - ${num2} = ${num1 - num2}`);
console.log(`Multiplicación: ${num1} * ${num2} = ${num1 * num2}`);
console.log(`División: ${num1} / ${num2} = ${num1 / num2}`);
console.log(`Modulo: ${num1} % ${num2} = ${num1 % num2}`);
console.log(`Exponente: ${num1} ** ${num2} = ${num1 ** num2}`);
console.log(`Incrementa en 1 y devuelve  el operando: ++num1 = ${++num1}`);
console.log(`Devuelve  el operando e incrementa en 1: num1++ = ${num1++}`);
console.log(`Decrementa en 1 y devuelve  el operando: ++num1 = ${--num1}`);
console.log(`Devuelve  el operando y decrementa en 1: num1++ = ${num1--}`);
console.log(`Invierte el valor del operando: -num1 = ${-num1}`);
console.log(`Convierte el operando en un número: +num3 = ${typeof (+num3)}`);
console.log(`.........................................`);

//Operadores lógicos
console.log(`Operadores lógicos`);
console.log(`&&: false && false = ${false && false}`);
console.log(`||: true || false = ${true || false}`);
console.log(`!: !num2 = ${!num2}`);
console.log(`.........................................`);

//Operadores de comparación
console.log(`Operadores de comparación`);
console.log(`Operador ==: num1 == num2 = ${num1 == num2}`);
console.log(`Operador ===: num1 === num2 = ${num1 === num2}`);
console.log(`Operador !=: num1 != num2 = ${num1 != num2}`);
console.log(`Operador !==: num1 !== num2 = ${num1 !== num2}`);
console.log(`Operador >: num1 > num2 = ${num1 > num2}`);
console.log(`Operador >=: num1 >= num2 = ${num1 >= num2}`);
console.log(`Operador <: num1 < num2 = ${num1 < num2}`);
console.log(`Operador <=: num1 <= num2 = ${num1 <= num2}`);
console.log(`.........................................`);

//Operadores de bit
console.log(`Operadores de bit`);
let x = 9;
let y = 12
console.log(`Operador &: x & y = ${x & y}`);
console.log(`Operador |: x | y = ${x | y}`);
console.log(`Operador ^: x & y = ${x ^ y}`);
console.log(`Operador ~: ~x = ${~x}`);
console.log(`Operador <<: x << y = ${x << y}`);
console.log(`Operador >>: x >> y = ${x >> y}`);
console.log(`Operador >>>: x >>> y = ${x >>> y}`);
console.log(`.........................................`);

//Estructuras de control
console.log(`Estructuras de control`);

console.log(`Condicional if`);
if (num1 < num2) {
    console.log(`${num1} es menor que ${num2}`);
} else if (num1 > num2) {
    console.log(`${num1} es mayor que ${num2}`);
} else {
    console.log(`${num1} es igual que ${num2}`);
}

console.log(`.........................................`);

console.log(`Declaración switch`);
let nota = 3;

switch(nota) {
    case 5:
        console.log(`Enhorabuena has obtenido un sobresaliente`);
        break;
    case 4:
        console.log(`Buen trabajo pero podrías haberlo echo mejor`);
        break;
    case 3:
        console.log(`Has obtenido un suficiente`);
        break;
    case 2:
        console.log(`No has aprobado por poco`);
        break;
    case 1:
        console.log(`No has estudiado nada, trabaja un poquito más para la próxima`);
        break;
    default:
        console.log(`Error, introduce una nota entre 1 y el 5`);
}

console.log(`.........................................`);

//Bucle for
console.log(`Bucle for`);
for (let i = 0; i < 10; i++) {
    console.log(i);
}

console.log(`.........................................`);

//Estructura for...of
let lista = [1, 4, 6, 2, 3, 7, 10, 12];
console.log(`Estructura for...of`);
for (let valor of lista) {
    console.log(valor);
}

console.log(`.........................................`);

//Estructura forEach
console.log(`Estructura forEach`);
lista.forEach(valor => {
    console.log(valor);
});

console.log(`.........................................`);

//Estructura for...in
let persona = {
    nombre: "Mario",
    apellido: "Velasco",
    edad: 34,
    idDeveloper: true
};

console.log(`Estructura for...in`);
for(let propiedad in persona) {
    console.log(`Muestra la clave del objeto -> ${propiedad}`);
    console.log(`Muestra el valor de cada propiedad del objeto ${persona[propiedad]}`);
};

console.log(`.........................................`);

//Bucle while
let i = 0;
let max = 10;

console.log(`Bucle while`);

while (i < max) {
    console.log(`El valor de i es: ${i}`);
    i++;
}

console.log(`.........................................`);

//Do...while
console.log(`Bucle Do...while`);
let j = 0
do {
    console.log(`El valor de j es: ${j}`);
    j++
}while (j < max);

console.log(`.........................................`);

//Excepciones
console.log(`Excepciones`);
const miConstante = 30;

try {
    miConstante = 20;   
}catch (error){
    console.error(`Ha habido una excepción ${error}`);
}

console.log(`.........................................`);

//EXTRA
console.log(`DIFICULTAD EXTRA`);
for(let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0){
        console.log(i);
        
        if (i == 52) {
            i+=3;
            console.log(i);
        }
    }
}