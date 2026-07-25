//operadores y estructuras de control

//operadores de aritmeticos

let a: number = 10;
let b: number = 3;

console.log(a + b); //13
console.log(a * b); 
console.log(a / b); 
console.log(a - b); 
console.log(a % b); 
console.log(a ** b); 

//operadores de turno
let i: number = 4;
let t: number = 2;
console.log("i << j = " + (i  << t));
console.log("i >> j = " + (i  >> t));
console.log("i >>> j = " + (i >>>t));
//operadores relacionales
let k: number = 4;
let j: number = 2;
console.log("k < j = " + (k < j));
console.log("k > j = " + (k > j));

//operadores de asignacion
let x: number = 10;
let y: number = 5;

x += y; // x = x + y
console.log("x += y: " + x);

x -= y; // x = x - y
console.log("x -= y: " + x);

x *= y; // x = x * y
console.log("x *= y: " + x);

x /= y; // x = x / y
console.log("x /= y: " + x);

x %= y; // x = x % y
console.log("x %= y: " + x);

x **= y; // x = x ** y
console.log("x **= y: " + x);
//operadores logicos
let p: boolean = true;
let q: boolean = false;

console.log("p && q = " + (p && q)); // false
console.log("p || q = " + (p || q)); // true
console.log("!p = " + (!p)); // false
console.log("!q = " + (!q)); // true

//operadores de comparacion
let m: number = 10;
let n: number = 20;

console.log("m == n = " + (m == n)); // false
console.log("m != n = " + (m != n)); // true
console.log("m > n = " + (m > n)); // false
console.log("m < n = " + (m < n)); // true
console.log("m >= n = " + (m >= n)); // false
console.log("m <= n = " + (m <= n)); // true
console.log("m === n = " + (m === n)); // false
// Estructuras de control

// if-else
let age: number = 18;
if (age >= 18) {
    console.log("Eres un adulto");
} else {
    console.log("Eres menor de edad");
}

// switch
let day: number = 3;
switch (day) {
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
        console.log("Día inválido");
}

// for loop
for (let i = 0; i < 5; i++) {
    console.log("i = " + i);
}

// while loop
let count: number = 0;
while (count < 5) {
    console.log("count = " + count);
    count++;
}

// do-while loop
let num: number = 0;
do {
    console.log("num = " + num);
    num++;
} while (num < 5);



for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}