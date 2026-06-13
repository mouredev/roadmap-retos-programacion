//Operadores Aritméticos
let Numero1 = 1;
let Numero2 = 2;

let i = 0;

console.log("Numero1 + Numero2 =", Numero1 + Numero2); // Suma
console.log("Numero1 - Numero2 =", Numero1 - Numero2); // Resta
console.log("Numero1 * Numero2 =", Numero1 * Numero2); // Multiplicación
console.log("Numero1 / Numero2 =", Numero1 / Numero2); // División
console.log("Numero1 % Numero2 =", Numero1 % Numero2); // Módulo
console.log("Numero1 ** Numero2 =", Numero1 ** Numero2); // Exponente

//Operadores de Adición y Asignación
let a = 1;
console.log("a = 1:", a);
a += 2;
console.log("a += 2:", a);
a -= 1;
console.log("a -= 1:", a);
a *= 3;
console.log("a *= 3:", a);
a /= 2;
console.log("a /= 2:", a);
a %= 1;
console.log("a %= 1:", a);
a **= 2;
console.log("a **= 2:", a);


// Operadores de Comparación
console.log("\nOperadores de Comparación:");
console.log("Numero1 == Numero2:", Numero1 == Numero2); // Igual
console.log("Numero1 != Numero2:", Numero1 != Numero2); // No igual
console.log("Numero1 > Numero2:", Numero1 > Numero2); // Mayor que
console.log("Numero1 < Numero2:", Numero1 < Numero2); // Menor que
console.log("Numero1 >= Numero2:", Numero1 >= Numero2); // Mayor o igual que
console.log("Numero1 <= Numero2:", Numero1 <= Numero2); // Menor o igual que

// Operadores Lógicos

//AND
let edad = 20;
let tieneLicencia = true;

if (edad >= 18 && tieneLicencia) {
  console.log("Puede conducir");
}

//OR
let tieneDinero = false;
let tieneTarjeta = true;

if (tieneDinero || tieneTarjeta) {
  console.log("Puede pagar");
}

//NOT
let estaLogueado = false;

if (!estaLogueado) {
  console.log("Debe iniciar sesión");
}

//Estructuras de Control

//Condicional if-else
let edad2 = 17;

if (edad >= 18) {
  console.log("Es mayor de edad");
} else {
  console.log("Es menor de edad");
}

//Condicional switch
let dia = 2;

switch (dia) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  default:
    console.log("Otro día");
}
//Iterativa bucle for

for (let i = 0; i < 5; i++) {
  console.log("Iteración:", i);
}

//While

while (i < 5) {
  console.log(i);
  i++;
}

//do-while

do {
  console.log(i);
  i++;
} while (i < 5);

//Para manejo de errores

try {
  let resultado = 10 / 0;
  console.log(resultado);
} catch (error) {
  console.log("Ocurrió un error");
}

//Dificultad extra
for (let numero = 10; numero <= 55; numero++) {

  if (
    numero % 2 === 0 && // es par
    numero !== 16 &&   // no es 16
    numero % 3 !== 0   // no es múltiplo de 3
  ) {
    console.log(numero);
  }

}