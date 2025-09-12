// Operadores de asignación
let x = 10; // asignación
x += 5; // suma y asignación
x -= 2; // resta y asignación
x *= 3; // multiplicación y asignación
x /= 2; // división y asignación
x %= 3; // módulo y asignación

// Operadores aritméticos
let y = x + 5; // suma
let z = x - y; // resta
let a = x * y; // multiplicación
let b = x / y; // división
let c = x % y; // módulo
let d = x++; // incremento
let e = y--; // decremento

// Operadores de comparación
let isEqual = x == y; // igual a
let isNotEqual = x != y; // no igual a
let isStrictEqual = x === y; // estrictamente igual a
let isStrictNotEqual = x !== y; // estrictamente no igual a
let isGreaterThan = x > y; // mayor que
let isLessThan = x < y; // menor que
let isGreaterThanOrEqual = x >= y; // mayor o igual que
let isLessThanOrEqual = x <= y; // menor o igual que

// Operadores lógicos
let and = x > 5 && y < 10; // y lógico
let or = x > 5 || y < 10; // o lógico
let not = !(x == y); // no lógico

// Operador ternario
let result = x > y ? "x es mayor que y" : "x no es mayor que y";

// Operador typeof
let type = typeof x; // devuelve el tipo de una variable


// Estructuras de control
// Declaraciones condicionales
let xx = 10;
if (xx > 5) {
    console.log("xx es mayor que 5");
} else if (xx < 5) {
    console.log("xx es menor que 5");
} else {
    console.log("xx es igual a 5");
}

// Declaración switch
switch (x) {
    case 5:
        console.log("x es 5");
        break;
    case 10:
        console.log("x es 10");
        break;
    default:
        console.log("x no es ni 5 ni 10");
        break;
}

// Bucle for
for (let i = 0; i < 5; i++) {
    console.log("El valor de i es: " + i);
}

// Bucle while
let i = 0;
while (i < 5) {
    console.log("El valor de i es: " + i);
    i++;
}

// Bucle do while
i = 0;
do {
    console.log("El valor de i es: " + i);
    i++;
} while (i < 5);

// Manejo de excepciones
try {
    let y = x * z; // z no está definido, por lo que se lanzará una excepción
} catch (error) {
    console.log("Ha ocurrido un error: " + error.message);
} finally {
    console.log("Este bloque se ejecuta independientemente de si se produjo una excepción o no");
}

// Dificultad Extra

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}
