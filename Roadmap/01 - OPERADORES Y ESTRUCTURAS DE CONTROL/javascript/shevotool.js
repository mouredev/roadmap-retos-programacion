// Operadores de asignación
let a = 25;
let b = 25;
console.log((a += b));
console.log((a -= b));
console.log((a *= b));
console.log((a /= b));
console.log((a %= b));
console.log((a &= b));
console.log((a ^= b));
console.log((a |= b));
console.log((a &&= b));
console.log((a ||= b));
console.log((a ??= b));

// Operadores de comparación
console.log(a == b);
console.log(a != b);
console.log(a === b);
console.log(a !== b);
console.log(a > b);
console.log(a >= b);
console.log(a < b);
console.log(a <= b);

//Operadores aritméticos
console.log(a % b);
console.log(a++);
console.log(a--);
console.log(--a);
console.log(++a);

// Operadores lógicos
console.log((a = true && true));
console.log((a = true || false));
console.log((a = !false));

// Operador ternario
let resultado = a > b ? "Mayor" : "Menor";
console.log(resultado);

// Operadores de cadena
let nombreCompleto = "Andrey" + " " + "Martinez";
console.log(nombreCompleto);

// Operador de propagación
let arr = [1, 2, 3];
let arr2 = [...arr, 4, 5];
console.log(arr2);

// Operadores de nullish (??)
let valor = null;
console.log(valor ?? "valor por defecto");
