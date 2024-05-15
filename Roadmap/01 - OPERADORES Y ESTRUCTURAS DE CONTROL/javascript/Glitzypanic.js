// OPERADORES ARITMÉTICOS
var a = 2;
var b = 3;

console.log(a + b); // Suma
console.log(a - b); // Resta
console.log(a * b); // Multiplicación
console.log(a / b); // División
console.log(a % b); // Módulo
console.log(a ** b); // Potencia
console.log(++a); // Incremento
console.log(--a); // Decremento

// OPERADORES DE ASIGNACIÓN
var numero = 5;
console.log(numero); // Asignación

numero += 3;
console.log(numero); // Asignación de suma

numero -= 3;
console.log(numero); // Asignación de resta

numero *= 3;
console.log(numero); // Asignación de multiplicación

numero /= 3;
console.log(numero); // Asignación de división

numero %= 3;
console.log(numero); // Asignación de módulo

numero **= 3;
console.log(numero); // Asignación de potencia

// OPERADORES DE CADENAS DE STRING
var nombreCompleto = "José" + " " + "Daniel" + " " + "Farías" + " " + "Cordoba";
console.log(nombreCompleto); // Concatenación

// OPERADORES DE COMPARACIÓN
console.log(2 == 3); // False
console.log("2" == 2); // True

console.log(2 != 4); // True
console.log(2 != "2"); // False

console.log(2 === 2); // True
console.log(2 === "2"); // False

console.log(1 !== 2); // True
console.log(2 !== "2"); // True

console.log(2 > 3); // False
console.log(5 > 6); // False

console.log(2 >= 3); // False
console.log(2 >= 2); // True

console.log(2 < 3); // True
console.log(2 < 2); // False

console.log(2 <= 3); // True
console.log(2 <= 2); // True

// OPERADORES LÓGICOS
console.log(true && true); // True
console.log(true && false); // False

console.log(true || true); // True
console.log(true || false); // True

console.log(!true); // False
console.log(!false); // True

// OPERADORES BITWISE
var num1 = 5; // 101
var num2 = 3; // 011
console.log(num1 & num2); // 001
console.log(num1 | num2); // 111
console.log(num1 ^ num2); // 110
console.log(~num1); // 010
console.log(num1 << 1); // 1010
console.log(num1 >> 1); // 10

// OPERADORES ESPECIALES
let result = 200 > 100 ? "Es mayor" : "Es menor";
console.log(result); // Es mayor

console.log(typeof 2); // Number
console.log(typeof "2"); // String
console.log(typeof true); // Boolean
console.log(typeof {}); // Object
console.log(typeof []); // Object
console.log(typeof null); // Object
console.log(typeof undefined); // Undefined
console.log(typeof function () {}); // Function

// OPERADOR OBJETO
var persona = {
  nombre: "José",
  apellido: "Farías",
  edad: 25,
};
console.log(persona.edad); // 25
console.log(persona.nombre); // José

// ESTRUCTURAS DE CONTROL
var edad = 25;

if (edad >= 18) {
  console.log("Acceso permitido");
} else if (edad >= 18) {
  console.log("Acceso permitido");
} else {
  console.log("Acceso denegado");
}

var i = 0;

while (i <= 10) {
  console.log(i);
  i++;
}

for (var i = 0; i <= 11; i++) {
  console.log(i);
}

// EJERCICIO
for (var i = 10; i <= 56; i++) {
  if (i % 2 == 0 && i != 16 && i % 3 != 0) {
    console.log(i);
  }
}
