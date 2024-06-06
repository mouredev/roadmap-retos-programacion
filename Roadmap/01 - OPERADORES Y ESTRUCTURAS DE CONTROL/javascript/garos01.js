// operadores aritmeticos
let a = 5;
let b = 3;
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let modulo = a % b;
let potencia = a ** b;

console.log(suma, resta, multiplicacion, division, modulo, potencia);

// Operadores de comparación
let igual = a == b;
let diferente = a != b;
let mayor_que = a > b;
let menor_que = a < b;

// Operadores lógicos
let and_logico = a > b && a < 20;
let or_logico = a < b || b > 0;
let not_logico = !(a == b);

console.log(
  igual,
  diferente,
  mayor_que,
  menor_que,
  and_logico,
  or_logico,
  not_logico
);

// Operadores de asignacion
let c = 5;
c += 3;
console.log(c);

let array1 = [1, 2, 3];
let array2 = [1, 2, 3];

// Operadores de identidad
let identidad = array1 === array2;
let no_identidad = array1 !== array2;

// Operadores de pertenencia
let pertenece = 1 in array1;
let no_pertenece = !(4 in array1);

console.log(identidad, no_identidad, pertenece, no_pertenece);

// Operadores a nivel de bits
let bitwise_and = a & b;
let bitwise_or = a | b;
let bitwise_xor = a ^ b;
let bitwise_not_a = ~a;
let left_shift = a << 1;
let right_shift = a >> 1;

console.log(
  bitwise_and,
  bitwise_or,
  bitwise_xor,
  bitwise_not_a,
  left_shift,
  right_shift
);

// Estructuras de control
// Condicional
let edad = 18;

if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// Iterativas
for (let i = 0; i < 5; i++) {
  console.log(i);
}

while (edad < 21) {
  console.log("Eres menor de 21 años");
  edad++;
}

// Excepciones
try {
  let resultado = 10 / 0;
} catch (error) {
  console.log("Error: División por cero");
} finally {
  console.log("Este bloque se ejecuta siempre");
}
