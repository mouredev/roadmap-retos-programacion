// Operadores Aritméticos
let num1 = 5 + 3; // Suma
let num2 = 5 - 3; // Resta
let num3 = 5 * 3; // Multiplicación
let num4 = 5 / 3; // División
let num5 = 5 % 3; // Módulo

console.log(num1, num2, num3, num4, num5);

// Operadores Lógicos
let bool1 = true && false; // AND
let bool2 = true || false; // OR
let bool3 = !true; // NOT

console.log(bool1, bool2, bool3);

// Operadores de Comparación
let comp1 = 5 > 3; // Mayor que
let comp2 = 5 < 3; // Menor que
let comp3 = 5 >= 3; // Mayor o igual que
let comp4 = 5 <= 3; // Menor o igual que
let comp5 = 5 === 3; // Igual que
let comp6 = 5 !== 3; // No igual que

console.log(comp1, comp2, comp3, comp4, comp5, comp6);

// Operadores de Asignación
let assign1 = 5;
assign1 += 3; // Suma y asignación
let assign2 = 5;
assign2 -= 3; // Resta y asignación
let assign3 = 5;
assign3 *= 3; // Multiplicación y asignación
let assign4 = 5;
assign4 /= 3; // División y asignación
let assign5 = 5;
assign5 %= 3; // Módulo y asignación

console.log(assign1, assign2, assign3, assign4, assign5);

// Operadores de Identidad
let ident1 = 5 === "5"; // Igualdad estricta
let ident2 = 5 !== "5"; // Desigualdad estricta

console.log(ident1, ident2);

// Operadores de Pertenencia
let arr1 = [1, 2, 3, 4, 5];
let belong1 = 3 in arr1; // Verifica si el índice existe en el array
let belong2 = 6 in arr1;

console.log(belong1, belong2);

// Operadores de Bits
let bit1 = 5 & 3; // AND a nivel de bits
let bit2 = 5 | 3; // OR a nivel de bits
let bit3 = 5 ^ 3; // XOR a nivel de bits
let bit4 = ~5; // NOT a nivel de bits
let bit5 = 5 << 2; // Desplazamiento hacia la izquierda
let bit6 = 5 >> 2; // Desplazamiento hacia la derecha

console.log(bit1, bit2, bit3, bit4, bit5, bit6);

// Estructura de control: if-else
let num = 10;
if (num > 5) {
  console.log("El número es mayor que 5");
} else {
  console.log("El número es menor o igual que 5");
}

// Estructura de control: switch
let option = 2;
switch (option) {
  case 1:
    console.log("Opción 1 seleccionada");
    break;
  case 2:
    console.log("Opción 2 seleccionada");
    break;
  default:
    console.log("Opción no reconocida");
}

// Estructura de control: while
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Estructura de control: do-while
let j = 0;
do {
  console.log(j);
  j++;
} while (j < 5);

// Estructura de control: for
for (let k = 0; k < 5; k++) {
  console.log(k);
}

// Estructura de control: for...in
let obj = { a: 1, b: 2, c: 3 };
for (let prop in obj) {
  console.log(prop + ": " + obj[prop]);
}

// Estructura de control: for...of
let arr2 = [1, 2, 3, 4, 5];
for (let element of arr2) {
  console.log(element);
}

// Estructura de control: try-catch
try {
  throw new Error("Esto es una excepción");
} catch (error) {
  console.log(error.message);
}

// Estructura de control: try-catch-finally
try {
  throw new Error("Esto es otra excepción");
} catch (error) {
  console.log(error.message);
} finally {
  console.log("Fin del bloque try-catch");
}

// Ejercicio Extra
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
