// Operaciones con los tipos de operadores

// Operadores de asignacion

//asignacion 
let uno = 1; // uno = 1;
// Asignacion de adiccion
uno += 2; // uno = uno + 2;
// Asignacion de sustraccion
uno -= 3; // uno = uno - 3;
// Asignacion de multiplicacion
uno *= 4; // uno = uno * 4;
// Asignacion de division
uno /= 5; // uno = uno / 5;
// Asignacion de residuo
uno %= 6; // uno = uno % 6;
// Asignacion de exponenciacion
uno **= 7; // uno = uno ** 7;
// Asignacion de desplazamiento hacia la izquierda
uno <<= 8; // uno = uno << 8;
// Asignacion de desplazamiento hacia la derecha
uno >>= 9; // uno = uno >> 9;
// Asignacion de desplazamiento hacia la derecha sin signo
uno >>>= 10; // uno = uno >>> 10;
// Asignacion de AND bit a bit
uno &= 11; // uno = uno & 11;
// Asignacion de XOR bit a bit
uno ^= 12; // uno = uno ^ 12;
// Asignacion de OR bit a bit
uno |= 13; // uno = uno | 13;
// Asignacion de AND logico
uno &&= 14; // uno = uno && (uno = 14);
// Asignacion de OR logico
uno ||= 15; // uno = uno || (uno = 15);
// Asignacion de anulacion logica
uno ??= 16; // uno = uno ?? (uno = 16);

// Operadores de Comparacion

const dos = 1;
// Operador de igualdad
dos == uno; // 1 == uno -> devuelve true si es true si son iguales (pueden ser 1 == "1" y aun asi devolver true);
// Operador de desigualdad
dos != uno; // 1 != uno -> Devuelve true si los operandos no son iguales (Tambien pueden ser 1 != '2' y aun asi devolver true);
// Operador de igualdad estricta
dos === uno; // Devuelve true si los operando son iguales y del mismo tipo.
// Operador de desigualdad estricta
dos !== uno; // Devuelve true si los operando son del mismo tipo pero no iguales, o si son de diferente tipo
// Operador mayor que
dos > uno; // Devuelve true si el operando izquierdo es mayor que el operado derecho, de lo contrario devuelve false
// Operador menor que
dos < uno; // Devuelve true si el operando derecho es mayor que el operando izquierdo, de lo contrario devuelve false
// Operador mayor o igual que
dos >= uno; // Devuelve true si el operando izquiero es mayor o igual que el operado derecho, de lo contrario devuelve false
// Operador menor o igual que
dos <= uno; // Devuelve true si el operando derecho es mayor o igual que el operando izquierdo, de lo contrario devuelve false

// Operadores aritmeticos

let tres = 0;
// Operador de adiccion
tres + 1; // tres = 1
// Operador de sutraccion
tres - 2; // tres = -1
// Operador de multiplicacion
tres * 3; // tres = -3
// Operador de division
tres / 4; // tres = -0.75
// Operador de modulo
tres % 5; // tres = 4.25
// Operador de incremento
tres++; // tres = 5.25
// Operador de decremento
tres--; // tres = 4.25
// Operador de negacion unitaria
-tres; // Devuelve la negacion de su operando
// Operador positivo unitario
+tres; // Intenta convertir su operando en un numero si aun no lo es
// Operador de exponenciacion
tres ** dos; // Calcula la base a la potencia del exponente, es decir baseexponente
/*
  * Tener en cuenta que los operadores apartir de los de incremento y decremento se pueden
  * Colocar en diferente posicion si quieres que se haga
  * Ante o despues --tres, ++tres el decremento y el incremento se hara antes de cualquier operacion con el numero
  * Ejemplo: tres = dos - ++uno -> tres = 1 - 2 : tres = dos + uno++ -> tres = 1 + 1, uno = 2
*/

// Operadores Bit a Bit
// And a nivel de bit
let cuatro = tres & dos; // Devuelve un uno en cada posicion de bit para los que bits correspondientes de ambos operando son unos
// OR a nivel de bit
cuatro = tres | dos; // Devuelve un cero en cada posicion de bit para los cual los bits correspondientes  de ambos operando  son ceros
// XOR a nivel de bit
cuatro = tres ^ dos; // Devuelve un cero en cada posicion de bit para que los bits correspondientes son iguales, y uno cuando son diferentes
// NOT a nivel de bit
cuatro = ~tres; // Invierte los bits de su operando
// Desplazamiento a la izquierda
cuatro = tres << dos; // Desplaza 'tres' en representacion binaria 'dos' bits a la izquierda, desplazando en ceros desde la derecha
// Desplazamiento a la derecha propagacion de signo
cuatro = tres >> dos; // Desplaza 'tres' en representacion binaria 'dos' bits a la derecha, descatando los bits desplazados
// Desplazamiento a la derecha de relleno cero
cuatro = tres >>> dos; // Desplaza 'tres' en representacion binaria 'dos' bits a la derecha, descartado los los bits desplazados y desplazandose en ceros desde la izquierda

// Operadores logicos

// Operador AND
let cinco = tres > uno && tres > dos; // Devuelve true si las dos expresiones se cumplen
// Operador OR
cinco = tres > uno || dos > uno; // Devuelve true si una de las dos expresiones se cumple
// Operador NOT
cinco = !(tres > uno); // Devuelve el valor contrario al resultado de la expresion si tres > uno era true !(tres > uno) es false y viceversa

// Operador ternario
const seis = cinco > cuatro ? "Si es mayor" : "No es mayor"; // Si la condicion es true, el operador devuelve el primer valor proporcionado despues del signo ? si es false devuelve el valor despues de :

// Control de flujo

// Condicionales

// If - else
const siete = tres > dos;
if (siete) {
  console.log(siete);
} else {
  console.log(siete);
}

// Switch
switch (siete) {
  case true:
    console.log(siete);
    break;
  default:
    console.log(siete);
    break;
}

// Iterativas

// for - for-in - for-of - for-each
for (let i = 0; i < 11; i++) {
  console.log(i); // Imprime los numeros del 0 al 10, se pone que i < 11 porque la i comienza en 0;
};

const ocho = ["uno", "dos", "tres"];
for (const element of ocho) {
  console.log(element); // "uno", "dos", "tres"
}

const nueve = {
  a: "uno",
  b: "dos",
  c: "tres"
}
for (const property in nueve) {
  console.log(`${property} : ${nueve[property]}`); // "a": "uno", "b" : "dos", "c" : "tres"
}

const diez = {
  a: 1,
  b: 2,
  c: 3
}
diez.forEach(number => console.log(number)); // 1, 2, 3


// While - do-while
let condition = 1;
while (condition < 10) {
  console.log(condition);
  condition++;
  // Output 1, 2, 3, 4, 5, 6, 7, 8, 9
}

do {
  console.log(condition);
  condition++;
} while (condition < 5); // 1,2,3,4,5

// Exception

// Try-catch-finally

try {
  console.log("No ha ocurrido errores");
} catch (err) {
  console.log("Ha ocurrido un error: ", err);
} finally {
  console.log("Exception termined");
}


// Retor extra
// * Crea un programa que imprima por consola todos los números comprendidos
// * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && !(i % 3 === 0) && i !== 16) console.log(i);
}
