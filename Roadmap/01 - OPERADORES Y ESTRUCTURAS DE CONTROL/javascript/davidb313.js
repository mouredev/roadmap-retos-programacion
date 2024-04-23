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
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//Operadores aritmeticos
let suma = `Suma,  ${1 + 2}`;
let resta = `Resta,  ${12 - 2}`;
let multi = `Multi,  ${3 * 2}`;
let division = `Division, ${5 / 2}`;
let residuo = `Residuo, ${10 % 2}`;

//Operadores logicos
let operadorAnd = true && false; // en && si ambos son true, da resultado true, si uno llegara a ser falso, el resultado es falso
let operadorOr = true || false; // en || si alguna variable es true, el resultado sera true, si todas son falsas, el rsultado sera falso
let operadorNot = "2" !== 2;

//Operadores de comparacion -> estos operadores devuelven un valor booleano si se cumple o no la igualdad o la comparacion
let comparacionEstricta = "3" === 3; // el resultado será false, ya que diferencia un string de un numero
let comparacionBasica = "3" == 3; // el resultado sera true, la comparacion no diferencia un string de un numero

let mayorQue = 5 > 3; //el resultado sera true
let menorQue = 6 < 1; // el resultado sera falso

let mayorOIgualQue = 5 >= 6; //el resultado es falso 5 no es mayor o igual a 6
let menorOIgualQue = 5 <= 6; //el resultado es true 5 es menor o igual a 6, se cumple la condicion de ser menor

//Estructuras de control
//estructura if - else
if (mayorOIgualQue) {
  console.log("5 es mayor o igual 6");
} else {
  console.log("5 no es mayor o igual a 6"); // la comprobacion tomará este camino, debido a que la expresion mayorOIgualQue es falsa
}

//estructura for -> aqui hara varios ciclos depende de las instrucciones, en el ejemplo i inicia en 0, mientras i sea menor o igual a 10, i aumentara en 1, y esto se hara hasta que se cumpla la instruccion de que i sea menor o igual a 10
for (let i = 0; i <= 10; i++) {
  console.log(i);
}

//estructura while -> hara el ciclo mientras se cumpla la condicion
let numeroInicial = 0;
while (numeroInicial < 8) {
  numeroInicial++;
  console.log(numeroInicial);
}

console.log(
  suma,
  resta,
  multi,
  division,
  residuo,
  operadorAnd,
  operadorOr,
  operadorNot,
  comparacionEstricta,
  comparacionBasica,
  mayorQue,
  menorQue,
  mayorOIgualQue,
  menorOIgualQue
);

// DIFICULTAD EXTRA (opcional)
const numeros = () => {
  for (i = 10; i <= 55; i++) {
    if (i !== 16 && i % 3 !== 0 && i % 2 === 0) {
      console.log(i);
    }
  }
};
numeros();
