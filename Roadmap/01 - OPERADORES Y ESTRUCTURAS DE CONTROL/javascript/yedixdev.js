//Asigno variables para realizar las operaciones
let a = 8;
let b = 5;
let c = "5"; // c es un numero en cadena de texto tipo string
let d = 10;

//Operadores arismeticos
console.log(a + b); //Suma = 13
console.log(a - b); //Resta = 3
console.log(a * b); //Multiplicacion = 40
console.log(a / b); //Division = 1.6
console.log(a % b); //Modulo 3 (El residuo de la división de 8 entre 5)

//Operaciones de comparacion
console.log(a > b); // 8 mayor que 5 = true
console.log(b >= c); // 5 mayor o igual que "5" = true (debido a la conversión de tipos)
console.log(a < b); // 8 menor que 5 = false
console.log(a <= c); // 8 menor o igual que "5" = false
console.log(a == b); // 8 igual a 5 = false
console.log(a == c); // 8 igual a "5" = true (debido a la conversión de tipos)
console.log(a === c); // 8 estrictamente igual a "5" = false (no son del mismo tipo)
console.log(a !== c); // 8 no es estrictamente igual a "5" = true (no son del mismo tipo)

//Operaciones  indiferentes
console.log(a != b); // 8 diferente a 5 = true (son numeros diferentes)
console.log(a != c); // 8 diferente a "5" = false (debido a la conversión de tipos)
console.log(a !== b); // 8 estrictamente diferente a 5 = true
console.log(a !== d); // 8 estrictamente diferente a 10 = true

//Operaciones   logicos
console.log(a > b && b < d); // true (true AND true)
console.log(a < b || b < d); // true (false OR true)
console.log(!(a === c)); // true (NOT false)
console.log(a < b && b >= c); // false (false AND true)
console.log(a > b || c === d); // true (true OR false)
console.log(a !== b && a > d); // false (true AND false)
