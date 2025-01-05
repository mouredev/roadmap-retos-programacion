/*OPERADORES*/
// Operadores aritmeticos
console.log(`Suma: 10 + 3 = ${10 + 3}`);
console.log(`Resta: 10 - 3 = ${10 - 3}`);
console.log(`Producto: 10 * 3 = ${10 * 3}`);
console.log(`Cociente: 10 / 3 = ${10 / 3}`);
console.log(`Residuo: 10 % 3 = ${10 % 3}`);
console.log(`Exponenciacion: 10 ^ 3 = ${10 ** 3}`);
let num = 10;
num++;
console.log(`Incremento: 10 ++ 3 = ${num}`);
num--;
console.log(`Decremento: 10 -- 3 = ${num}`);

//Operadores de asignación

let nombre = "Julian Figueroa";
let x = 20; // Asignacion simple
let y = 10;
console.log((x += y)); // Asignacion con suma
console.log((x -= y)); // Asignacion con resta
console.log((x *= y)); // Asignacion con multiplicacion
console.log((x /= y)); // Asignacion con division
console.log((x %= y)); // Asignacion con modulo

//Operadores de comparación

console.log(x == y); // Igualdad
console.log("Hola" === 25); // estricta
console.log(x != y); // diferente
console.log("Hola" !== 25); // diferente estricta
console.log(x > y); // mayor que
console.log(x < y); // menor que
console.log(x >= y); // mayor o igual que
console.log(x <= y); // menor o igual que

//Operadores de logicos

console.log("Cat" && "Dog");
console.log("Cats" && "Cat");

// Operadores de tipo

console.log(typeof 2.5);

// Operador ternario

par = 4;
impar = 5;
esPar = impar % 2 == 0 ? "Par" : "Impar";
console.log(esPar);

// ESTRUCTURAS DE CONTROL EN JAVASCRIPT
// Condicionales

value = true;
if (value) {
  console.log("Es verdadero");
} else if (null) {
  console.log("Es nulo");
} else {
  console.log("Es falso");
}

// Switch
generoPersona = "masculino";
switch (generoPersona) {
  case "masculino":
    console.log("El genero es masculino");
    break;
  case "femenino":
    console.log("El genero es masculino");
    break;
  default:
    console.log("El genero no está especificado");
    break;
}

// Bucles
//for
suma = 0;
for (let i = 0; i <= 10; i++) {
  // Suma de los numeros hasta el 10
  suma += i;
}
console.log("For: ", suma);

// while
suma = 0;
i = 0;
while (i <= 10) {
  suma += i;
  i++;
}
console.log("While: ", suma);

//do-while

suma = 0;
i = 0;
do {
  suma += i;
  i++;
} while (i <= 10);
console.log("Do while: ", suma);

// Condicionales sobre colecciones
//for ... of

const frutas = ["Manzana", "Pera", "Mango", "Fresa"];

for (const fruta of frutas) {
  console.log(`Fruta: ${fruta}`);
}

//for ... in

const persona = {
  nombre: "Juan",
  edad: 30,
  ciudad: "Bogotá",
};

for (const clave in persona) {
  console.log(`${clave}: ${persona[clave]}`);
}

// try - catch

try {
  dividendo = 10;
  divisor = 1;

  if (divisor === 0) {
    throw new Error("No es posible dividir entre cero.");
  }
  console.log(dividendo / divisor);
} catch (error) {
  console.error("Error: ", error.message);
} finally {
  ("Operacion finalizada");
}
