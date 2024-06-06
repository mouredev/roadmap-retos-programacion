// Operadores 
//Aritméticos:
console.log(2 + 3); // Suma: 5
console.log(5 - 2); // Resta: 3
console.log(4 * 3); // Multiplicación: 12
console.log(12 / 3); // División: 4
console.log(10 % 3); // Resto: 1

// Exponenciación (a partir de ES7)
console.log(2 ** 3); // 8

//Lógicos:
JavaScript
console.log(true && true); // AND: true
console.log(true || false); // OR: true
console.log(!true); // NOT: false

//De comparación:
console.log(2 === 2); // Igualdad estricta: true
console.log(2 == 2); // Igualdad no estricta: true
console.log(2 > 1); // Mayor que: true
console.log(2 >= 2); // Mayor o igual que: true
console.log(1 < 2); // Menor que: true
console.log(1 <= 2); // Menor o igual que: true

//Asignación:
let x = 10;
x += 5; // x = 15
x -= 2; // x = 13
x *= 3; // x = 39
x /= 2; // x = 19.5
x %= 4; // x = 3.5

//Identidad:
const a = 10;
const b = 10;
console.log(a === b); // true (mismo valor y tipo)
const c = "10";
console.log(a === c); // false (mismo valor, diferente tipo)

//Pertenencia:
const lista = ["a", "b", "c"];
console.log("a" in lista); // true
console.log("d" in lista); // false

//Bits
console.log(1 | 2); // OR a nivel de bits: 3
console.log(1 & 2); // AND a nivel de bits: 0
console.log(1 ^ 2); // XOR a nivel de bits: 3
console.log(~1); // NOT a nivel de bits: -2

//Estructuras de Control
//Condicionales:
const numero = 10;
if (numero > 0) {
  console.log("El número es positivo");
} else {
  console.log("El número es negativo");
}

//Iterativas:
// Bucle for
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
      console.log(i);
    }
  }
  
  // Bucle while
  let j = 10;
  while (j <= 55) {
    if (j % 2 === 0 && j !== 16 && j % 3 !== 0) {
      console.log(j);
    }
    j++;
  }
  
  // Bucle do-while
  let k = 10;
  do {
    if (k % 2 === 0 && k !== 16 && k % 3 !== 0) {
      console.log(k);
    }
    k++;
  } while (k <= 55);

  //Excepciones:
  try {
    throw new Error("Error personalizado");
  } catch (error) {
    console.log(error.message);
  }

  /*
  Dificultad Extra:
  * Crea un programa que imprima por consola todos los números comprendidos
  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  */
  for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
      console.log(i);
    }
  }