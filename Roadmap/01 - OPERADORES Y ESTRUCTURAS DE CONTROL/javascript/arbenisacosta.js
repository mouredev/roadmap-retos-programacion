/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 */


/**
  En JavaScript encontramos cinco tipos de operadores:
  * Aritméticos
  * Lógicos
  * De comparación
  * Binarios
  * De asignación
  * Otros
 */

// ---- tipos de operadores ----

console.log("---- TIPOS DE OPERADORES ----");

// ---- Aritméticos
console.log("---- Aritméticos ----");

let num1 = 2, num2 = 2;

let mult = num1 * num2; // Multiplicación
console.log(mult);

let divi = num1 / num2; // División
console.log(divi);

let suma = num1 + num2; // Suma
console.log(suma);

let rest = num1 - num2; // Resta
console.log(rest);

let mod = num1 % num2; // modulo
console.log(mod);

// ---- Lógicos
console.log("---- Lógicos ----");

let facil = true, dificil = false;

console.log(!dificil); //Negación lógica ! (Not). Establece una negación lógica en una expresión

console.log(facil && dificil); //Conjunción lógica && (And). Establece una conjunción lógica de dos expresiones

console.log(facil || dificil); // Disyunción lógica || (Or). Establece una disyunción lógica de dos expresiones

console.log(facil ^ dificil); //Exclusión lógica ^ (Xor). Establece una exclusión lógica de dos expresiones

// ---- De comparación
console.log("---- De comparación ----");

console.log(1 < 2); //Menor que (<)

console.log(7 <= 8); //Menor o igual que (>=)

console.log(5 > 2); //Mayor que (>)

console.log(7 >= 8); //Mayor o igual que (>=)

console.log( 2 == "2"); //Igualdad (==) Verifica la igualdad de dos expresiones sin tener en cuenta el tipo de dato.

console.log(2 === "2"); //Igualdad estricta (===) Hace lo mismo que el anterior, pero verificando también que coincidan los tipos de datos.

console.log(2 != "2"); //Desigualdad (!=) Funciona de la misma forma que la igualdad, pero negándola.

console.log(2 !== "2"); //Desigualdad estricta (!==) Lo mismo que la igualdad estricta, pero negándola.

// ---- De asignación
console.log("---- De asignación ----");
// Asignación simple (=) Asigna un contenido a una variable o a un objeto.
/*
En JavaScript el operador de asignación tiene la
particularidad de que puede combinarse con algunos de
los operadores aritméticos, dando lugar a toda una
familia de nuevos operadores:
*/

let asign = 10;
console.log("asign = 10:", asign);
asign += 7;
console.log("asign += 7:", asign);
asign -= 4;
console.log("asign -= 4:", asign);
asign *= 4;
console.log("asign *= 2:", asign);
asign /= 2;
console.log("asign /= 2:", asign);

asign %= 4;
console.log("asign %= 4:", asign);
asign ^= 4;
console.log("asign ^= 2:", asign);
asign &= 2;
console.log("asign &= 2:", asign);
asign |= 2;
console.log("asign |= 2:", asign);



// ---- Binarios
console.log("---- Binarios ----");

// Bitwise logical operators
//  &  ->  AND
//  |  ->  OR
//  ^  ->  XOR

let x = 6, y = 12, z = 0;

// x -> 6 = 00000110
// y -> 12 = 00001100
// z -> 0 = 00000000

z = x & y;
console.log("AND = ",z);

z = x | y;
console.log("OR = ",z);

z = x ^ y;
console.log("XOR = ",z);

// Bitwise shift operators
//  <<
//  >>
//  >>>

z = x << 2;
console.log("<< = ",z);

z = x >> 2;
console.log(">> = ",z);


console.log("---- ESTRUCTURA DE CONTROL ----");


console.log("---- CONDICIONALES");
// Los condicionales nos permiten evaluar si una condición cumple o no con lo que estemos evaluando.

console.log("if else");
let mayorEdad = 18;

if (mayorEdad >= 18) {
  console.log("Es Mayor de Edad");
} else {
  console.log("Es Menor de Edad");
}

if (mayorEdad >= 18) {
  console.log("Es Mayor de Edad");
} else if(mayorEdad > 18 && mayorEdad < 25) {
  console.log("Es un adulto Joven");
} else {
  console.log("Es menor de edad");
}

console.log("---- Ciclos, Bucles o Loops");
// Se le pueden llamar, ciclos, bucles o loops, en ellos se evalua una condición n veces hasta que esta se cumpla.

console.log("For");
// Un bucle for se repite como mencione hasta que la condición que se esta evaluando se cumpla.

let pasos = 5;
for (let paso = 0; paso <= pasos; paso++) {
  console.log("Estoy dando el siguiente paso " + paso);
}

console.log("while");
// Ejecuta una sentencia mientras la condición que se este evaluando sea verdadera.

let contador = 0;
while (contador < 3) {
  contador++;
  console.log("Contador es igual a: ", contador);
}

console.log("Switch");
// Permite evaluar una expresión e intenta igual el valor de esa expresión a una etiqueta llamada case, que es el caso a evaluar.

let tipoFrutas = "Manzana"

switch (tipoFrutas) {
  case "Naranja":
    console.log("Precio de la Naranja: 5$");
    break;
  case "Manzana":
    console.log("Precio de la Manzana: 10$");
    break;
  case "Fresa":
    console.log("Precio de la Fresa: 15$");
    break;

  default:
    console.log("No tenemos ese tipo de fruta");
    break;
}

console.log("---- EXTRA ----");

/**
 *  DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

let numero = 10;

while (numero <= 55) {
    if (numero % 2 === 0 && numero !== 16 && numero % 3 !== 0) {
        console.log(numero);
    }
    numero++;
}
