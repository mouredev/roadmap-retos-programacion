
//* Operadores aritméticos
let adition = 1 + 1
let subtraction = 2 - 1
let multiplication = 2 * 2
let division = 10 / 2
let module = 4 % 2 // <- retorna el resto de la division
let exponentiation = 2 ** 2 // <- eleva 2 a la potencia de dos

//* Operadores de asignación
let a = 2
a += 2 // a = a + 2
a -= 2 // a = a - 2
a *= 2 // a = a * 2
a /= 2 // a = a / 2
a %= 2 // a = a % 2 <- se le asigna el resto de la division entre los dos
a **= 2 // a = a ** 2 <- a elevado a la potencia de 2

//* Operadores de comparación
let y = 3;
let z = 2;
let w = 1;
console.log(y == '4'); // igualdad de valores sin verificar el tipo
console.log(y != 3); // diferencia de valores sin verificar el tipo
console.log(y === 4); // igualdad de valores verificando el tipo
console.log(y !== 3); // difierencia de valores verificando el tipo
console.log(z > y); // comprueba si z es mayor que y
console.log(z >= y); // comprueba si z es mayor o igual que y
console.log(w < y); // comprueba si w es menor que y
console.log(w <= y); // comprueba si w es mejor o igual que y

//* Operadores lógicos
let age = 24;
age > 18 ? console.log('Soy mayor de edad, una cerveza, por favor') : console.log('No soy mayor de edad'); // Operador condicional o ternario

// AND (&&)
console.log(true && true); // && devuelve verdadero si ambos operandos son verdaderos; de lo contrario, devuelve falso

// OR (||) -> devuelve verdadero si almenos uno de los operandos es verdadero
console.log(false || false); // devuelve false
console.log(true || false); // devuelve true
console.log(false || true); // devuelve true
console.log(true || true); // devuelve true

// Operador NOT (!) -> utilzado para el invertir (negar) valor de una variable. Si una variable vale true, al negarla valdrá false
console.log(!true); // devuelve false
console.log(!false); // devuelve true

//* Condicionales y bucles (entructuras de control)

//Condicionales 
let edad = 18;

if (edad >= 18) {
  console.log("Puedes beber cerveza");
} else {
  console.log("No puedes beber cerveza... aun");
}

// Iterativas
for (let i = 1; i <= 5; i++) {
  console.log("Iteración:", i);
}

let arrayIterativo = [1, 2, 3, 4, 5];
for (let elemento of arrayIterativo) {
  console.log("Elemento:", elemento);
}

// Excepciones
try {
  let result = 10 / 0;
  console.log("Resultado:", result);
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("Bloque finally ejecutado siempre.");
}

// Switch
let diaDeLaSemana = "Viernes";
switch (diaDeLaSemana) {
  case "Lunes":
    console.log("Es el primer día de la semana. Hay que laburar lpm");
    break;
  case "Martes":
  case "Miércoles":
  case "Jueves":
    console.log("Estamos a mitad de semana.");
    break;
  case "Viernes":
    console.log("Fin de la semana laboral. Cerveza");
    break;
  case "Sábado":
  case "Domingo":
    console.log("Proyectos propios, pelis y más cerveza");
    break;
  default:
    console.log("El dia no es valido.");
}


//* Dificultad opcional
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log("Número", i);
  }
}