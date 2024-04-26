
//Operadores aritmeticos 

let suma = 1 + 1;
let resta = 1 - 1;
let multiplicacion = 1 * 1;
let division = 1 / 1;
let resto = 2 % 2;
console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
console.log(resto);

// Operadores logicos 

//      &&
let esVerdadreoAND = true && true
let esFalsoAND = true && false
let esFalsoAND2 = false && true;
let esFalsoAND3 = false && false;
console.log(esVerdadreoAND);
console.log(esFalsoAND);
console.log(esFalsoAND2);
console.log(esFalsoAND3);
//     || 
let esVerdaderoOR = true || true;
let esFalsoOR = true || false;
let esFalsoOR2 = false || true;
let esFalsoOR3 = false || false;
console.log(esVerdaderoOR);
console.log(esFalsoOR);
console.log(esFalsoOR2);
console.log(esFalsoOR3);
//     ! 
let falsoInvertido = !true;
let verdaderoInvertido = !false
console.log(falsoInvertido);
console.log(verdaderoInvertido);

//De comparacion

/* Igualdad (==) */
console.log(5 == 5);       // true
console.log('5' == 5);     // true (coerción de tipo)
console.log(5 == '5');     // true (coerción de tipo)
console.log(5 == 10);      // false

/* Igualdad estricta (===) */
console.log(5 === 5);      // true
console.log('5' === 5);    // false
console.log(5 === '5');    // false

/* Desigualdad (!=) */
console.log(5 != 10);      // true
console.log(5 != '5');     // false (coerción de tipo)


/* Desigualdad estricta (!==) */
console.log(5 !== '5');    // true
console.log(5 !== 5);      // false

/* Mayor que (>) */
console.log(10 > 5);       // true

/* Menor que (<) */
console.log(5 < 10);       // true

/* Mayor o igual que (>=) */
console.log(10 >= 10);     // true

/* Menor o igual que (<=) */
console.log(5 <= 10);      // true


/* De asignacion (=) */
var variableVar = "Variable" // asigna una variable string 
variableVar = 1 // Reasigna a una variable number 

//Suma y asignacón 
variableVar += 1 // === variableVar = variableVar + 1

//Resta y asignacion 
variableVar -= 1

/* De identidad */
const objeto1 = { nombre: 'Juan' };
const objeto2 = { nombre: 'Juan' };
const objeto3 = objeto1;

console.log(objeto1 === objeto2);
console.log(objeto1 === objeto3);


/* De pertenencia */

//Operador (in) en objetos 
const persona1 = {
  nombre: "Sofia",
  edad: 30
}
console.log('nombre' in persona1);  // true
console.log('apellido' in persona1);  // false
console.log(!('nombre' in persona1));   // false, ya que 'nombre' sí está presente en persona1
console.log(!('apellido' in persona1)); // true, ya que 'apellido' no está presente en persona1

//operador (in) en arrays 
const deportes = ["F1", "Moto Gp", "Motocross"]
console.log(0 in deportes); //true
console.log(!(0 in deportes)); //false
console.log(3 in deportes); //false
console.log(!(3 in deportes)); //true
// operador instanceof 
class Animal {
  sonido() {
    console.log('Hace algún sonido');
  }
}

class Perro extends Animal {
  ladrar() {
    console.log('Guau guau');
  }
}

const miPerro = new Perro();

console.log(miPerro instanceof Perro);  // true
console.log(miPerro instanceof Animal);  // true
console.log(miPerro instanceof Object);  // true, ya que todos los objetos son instancias de Object

/* Operadores de bits */

// AND     & 
var num1 = 5; // Representación binaria: 0101
var num2 = 3; // Representación binaria: 0011
var resultado = num1 & num2; // Resultado: 0001 (1 en decimal)
console.log(resultado); // Imprime 1

// OR     |
var num3 = 5; // Representación binaria: 0101
var num4 = 3; // Representación binaria: 0011
var resultado = num3 | num4; // Resultado: 0111 (7 en decimal)
console.log(resultado); // Imprime 7

// XOR     ^
var num5 = 5; // Representación binaria: 0101
var num6 = 3; // Representación binaria: 0011
var resultado = num5 ^ num6; // Resultado: 0110 (6 en decimal)
console.log(resultado); // Imprime 6

// NOT     ~
var num = 5; // Representación binaria: 0000 0000 0000 0000 0000 0000 0000 0101
var resultado = ~num; // Resultado: 1111 1111 1111 1111 1111 1111 1111 1010 (-6 en decimal)
console.log(resultado); // Imprime -6

// Desplazamiento derecha e izquierda     <<    >>
var num = 5; // Representación binaria: 0101
var resultadoIzquierda = num << 1; // Desplazamiento a la izquierda por 1: 1010 (10 en decimal)
var resultadoDerecha = num >> 1; // Desplazamiento a la derecha por 1: 0010 (2 en decimal)
console.log(resultadoIzquierda); // Imprime 10
console.log(resultadoDerecha); // Imprime 2

/* Extructuras de control */

// if - else
let edad = 20;

if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// if - else if - else 
let nota = 85;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Aprobado");
} else {
  console.log("Reprobado");
}

//Bucle while 
let contador = 0
while (contador < 10) {
  console.log(`El contador es ${contador}`);
  contador++;
}

// Bucle DO While 
let contador2 = 0
do {
  console.log(`El contador es ${contador2}`);
  contador2++;
} while (contador2 < 5);

// Sentencia break y continue 
for (let i = 0; i < 10; i++) {
  if (i === 3) {
    continue; // Saltar la iteración actual si i es igual a 3
  }
  if (i === 7) {
    break; // Salir del bucle si i es igual a 7
  }
  console.log("El valor de i es: " + i);
}




/*  DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let i = 10; i <= 55; i++) {
  if(i === 55 ){
    console.log(i);
  }
  if (i % 2 === 1 || (i === 16 || i % 3 === 0)) {
      continue;
  }
  console.log(i);
}