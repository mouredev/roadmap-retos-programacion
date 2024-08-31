// Operadores aritméticos
let suma = 5 + 3;
let resta = 6 - 2;
let division = 10 / 2;
let multiplicacion = 7 * 8;
let resto = 15 % 2;

// Operadores de asignacion
let x = 1;
x = x + 4; // adición x=5
x = x - 2; // sustración x=3
x = x * 3; // multiplicacion x=9
x = x / 3; // division x=3
x = x % 2; // resto x=1

// pre incremento
let a = 4;
let b = ++a * 2;
console.log(b); // Imprime 10 y establece a=5
// post incremento
let c = 4;
let d = c++ * 2;
console.log(d); // Imprime 8 y establece c=5
// pre decremento
let e = 5;
let f = --e * 2;
console.log(f); // Imprime 8 y establece e=4
// post decremento
let g = 5;
let h = g-- * 2;
console.log(h); // Imprime 10 y establece g=4

// Operadores de comparacion
let num1 = 5;
let num2 = 2;
let bool1 = num1 > num2; // bool1 = true
let bool2 = num1 < num2; // bool2 = false
let bool3 = num1 <= num2; // bool3 = flase
let bool4 = num1 >= num2; // bool3 = false
let bool5 = num1 === num2; // bool5 = false
let bool6 = num1 !== num2; // bool6 = true

// Operadores logicos
//AND
let and1 = true && true; // log1 = true
let and2 = true && false; // log2 = false
let and3 = false && true; // log3 = false
//OR
let or1 = true || true; // or1 = true
let or2 = true || false; // or2 = true
let or3 = false || true; // or3 = true
let or4 = false || false; // or3 = false

// Operadores de Negacion
let verdadero = true;
let falso = false;
console.log(!verdadero); // Imprime false
console.log(!falso); // Imprime true
console.log(!!verdadero); // Imprime true

// Operadores de identidad o igualdad
let igual1 = 2 === 2; // igual1 = true
let igual2 = 2 === "2"; // igual2 = false
let igual3 = 2 !== 2; // igual3 = false
let igual4 = 2 !== 3; // igual4 = true

// Operador typeof
let type1 = 5;
let type2 = "alejandro";
let type3 = true;
let type4 = undefined;
console.log(typeof type1); // Imprime "number"
console.log(typeof type2); // Imprime "string"
console.log(typeof type3); // Imprime "boolean"
console.log(typeof type4); // Imprime "undefined"

// Operador de concatenacion
let cad1 = "Hola";
let cad2 = "JavaScript";
console.log(cad1 + " " + cad2); // Imprime "Hola JavaScript"

// Estructuras de control

// if...else
let nota = 8;
if (nota >= 6) {
  console.log("materia apobada con " + nota);
} else {
  console.log("desaprobó con un " + nota);
}

// Switch
let numeroMes = 3;
switch (numeroMes) {
  case 1:
    console.log("Enero");
    break;
  case 2:
    console.log("Febrero");
    break;
  case 3:
    console.log("Marzo");
    break;
  case 4:
    console.log("Abril");
    break;
  case 5:
    console.log("Mayo");
    break;
  case 6:
    console.log("Junio");
    break;
  case 7:
    console.log("Julio");
    break;
  case 8:
    console.log("Agosto");
    break;
  case 9:
    console.log("Septiembre");
    break;
  case 10:
    console.log("Octubre");
    break;
  case 11:
    console.log("Noviembre");
    break;
  case 12:
    console.log("Diciembre");
    break;
  default:
    console.log("el numero ingresado no corresponde a un mes");
}

// For
for (let x = 0; x < 5; x++) {
  console.log(x + 1); // 1,2,3,4,5
}

// ForEach
let numeros = [0, 1, 2, 3, 4, 5];
numeros.forEach(function (numero) {
  console.log(numero);
});

// While
let contador = 1;
while (contador <= 5) {
  console.log(contador); // 1,2,3,4,5
  contador++;
}

// Do While
let cuentaRegresiva = 5;
do {
  console.log(cuentaRegresiva); // 5,4,3,2,1
  cuentaRegresiva--;
} while (cuentaRegresiva !== 0);

/*
    DIFICULTAD EXTRA:
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
*/

for (let i = 10; i <= 55; i++) {
  if (i % 2 == 0 && i !== 16) {
    if (i % 3 !== 0) {
      console.log(i);
    }
  }
}
