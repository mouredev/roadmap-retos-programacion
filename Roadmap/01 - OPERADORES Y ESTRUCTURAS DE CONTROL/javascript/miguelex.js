// Ejemplo de operadores aritméticos


let a = 10;
let b = 2;
console.log("La suma es: " + (a+b));
console.log("La resta es: " + (a-b));
console.log("La multiplicación es: " + (a*b));
console.log("La división es: " + (a/b));
console.log("El resto es: " + (a%b));
console.log("El incremento es: " + (++a));
console.log("El decremento es: " + (--b));
console.log("El negativo es: " + (-a));

// Operadores de asignación

console.log("La suma es: " + (a+=b));
console.log("La resta es: " + (a-=b));
console.log("La multiplicación es: " + (a*=b));
console.log("La división es: " + (a/=b));
console.log("El resto es: " + (a%=b));

// Operadores de comparación

console.log("Igual: " + (a==b));
console.log("Identico: " + (a===b));
console.log("Distinto: " + (a!=b));
console.log("No identico: " + (a!==b));
console.log("Menor: " + (a<b)); 
console.log("Mayor: " + (a>b));
console.log("Menor o igual: " + (a<=b));
console.log("Mayor o igual: " + (a>=b));

// Operadores lógicos

console.log("AND: " + (a<b && a>b));
console.log("OR: " + (a<b || a>b));
console.log("NOT: " + !(a<b));

// Operadores nivel bit

console.log("AND: " + (a&b));
console.log("OR: " + (a|b));
console.log(~a);     
console.log(a << 1); 
console.log(a >> 1); 
console.log(b >>> 1)

// Ejemplo bucle For

for (let i = 0; i < 10; i++) {
    console.log(i);
}

// Ejemplo bubcle for in

let cadena = "Hola mundo";
for (let i in cadena) {
    console.log(cadena[i]);
}

// Ejemplo bucle for of

for (let i of cadena) {
    console.log(i);
}

// Ejemplo switch

let dia = 1;

switch (dia) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes");
        break;
    default:
        console.log("Otro día");
        break;
}

// Ejemplo while

let i = 0;

while (i < 10) {
    console.log(i);
    i++;
}

// Ejemplo do while

let j = 0;

do {
    console.log(j);
    j++;
} while (j < 10);

// Manejo de excepciones

try {
    let x = 10;
    let y = 0;
    if (y == 0) {
        throw("División por cero");
    }
    let z = x / y;
    console.log(z);
} catch (error) {
    console.log(error);
} finally {
    console.log("Terminado");
}

// Ejercicio extra

function ejercicioExtra() {
    for (let i = 10; i <= 55; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i);
        }
    }
}

ejercicioExtra();





