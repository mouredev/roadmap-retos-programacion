/*
######################33 Operadores en Javascript 
*/

// ------------------------------> Operadores Aritmeticos

let suma = 34 + 12; // Este operador nos permite sumar dos valores de tipo númerico.
console.log("Result - Suma: ", suma);

let saludo = "Hola gente" + " ¿Como están?"; // Cuando es usado con strings los concatena (los une)
console.log("Result - Saludo: ", saludo);

const resta = 100 - 80; // Genera una resta de los valores involucrados en la operacion.
console.log("Result - Resta: ", resta);

const yoPuedoMultiplicar = 12 * 24; // Este simboolo de manera unica genera una multiplicación.
console.log("Result - Multiplicación: ", yoPuedoMultiplicar);

let operacionDeExponentes = 2 ** 3; // Usando el simbolo anterior dos veces podemos hacer una exponenciación.
console.log("Result - Exponenciación: ", operacionDeExponentes);

const paraDividir = 36 / 12; // Con este obtenemos el resultado de la operación de división.
console.log("Result - División: ", paraDividir);

let estoSeLlamaUnResiduo = 36 % 6; // El operador de modulo, nos permite conocer sí y cuál es el entero de una división.
console.log("Result - Residuo: ", estoSeLlamaUnResiduo);

/*
 * Aca podemos ver aplicaciones interesantes con estos operadores que si no se tiene cuidado pueden confidir,
 * cuando se ejecuta el codigo normalmente se va de izquierda a derecha.
 * Al usar algunas de las  ventajas de los operadores aritmeticos podemos obtener resultados inesperados
 * si no manejamos esto con cuidado, recuerda siempre tener presente que si quieres aplicar el cambio
 * en esa misma operación debes usar las ventajas de ++variable y --variable desde el lado izquierdo al derecho,
 * pues podrias llegar a ver el resultado en la siguiente lectura del valor y no en la inmediata.
 **/

let a = 3;
// Value of a=4 and returns 4
console.log(++a);
// Value of a=5 and returns 4
console.log(a++);
// Value of a=5 and returns 5
console.log(a);

let b = 3;
// Value of b=2 and returns 2
console.log(--b);
// Value of b=1 and returns 2
console.log(b--);
// Value of b=1 and returns 1
console.log(b);

// Recurso obtenido :https://ifgeekthen.nttdata.com/es/tipos-de-datos-y-operadores-en-javascript

// ------------------------------> Operadores de Asignación

const asignandoUnHola = "Hola"; // Lo hemos usado para asignar desde el reto pasado pero, no ahi que olvidarlo.
console.log("Result - Asignación: ", asignandoUnHola);

let asignaUnaSuma = 34;
asignaUnaSuma += 5; // Aqui estamos generando una asignación con una suma dentro tal como: a = a+b
console.log("Result - Asignación y sumale 5: ", asignaUnaSuma);

let asignaUnaResta = 52;
asignaUnaResta -= 12; // Aqui estamos generando una asignación con una resta dentro tal como: a = a-b
console.log("Result - Asignación y restale 12: ", asignaUnaResta);

let asignaUnaMultiplicacion = 12;
asignaUnaMultiplicacion *= 4; // Aqui estamos generando una asignación con una multiplicación dentro tal como: a = a*b
console.log(
  "Result - Asignación y multiplica por 4: ",
  asignaUnaMultiplicacion,
);

// Puedes aplicarlo tal cuál para la división, modulo y exponenciación.

// ------------------------------> Operadores de Comparación.

console.log("Igualdad No estricto: ", 4 == "4"); // Operador de igualdad NO estricto. Este operador compara el valor pero ignora el tipo R/=True.

console.log("Desigualdad NO Estricto: ", 4 != "4"); // Operador de desigualdad NO estricto. Este operador compara el valor y ignora el tipo R/=False.

console.log("Igualdad Estricto: ", 4 === "4"); // Operador de igualdad Estricto. Este operador compara el valor y el tipo R/=False.

console.log("Desigualdad Estricto: ", 4 !== "4"); // Operador de desigualdad Estricto. Este operador compara el valor y el tipo R/=True.

console.log("Mayor que: ", 32 > 12); // Operador "Mayor que", compara si la primera expresión es mayor que la segunda R/=True.

console.log("Menor que: ", 12 < 34); // Operador "Menor que", compara si la primera expresión es menor que la segunda R/=True.

console.log("Mayor o igual que: ", 12 >= 14); // Operador "Mayor o igual que", compara si la primera expresión es mayor o igual que la segunda R/=False.

console.log("Menor o igual que", 12 <= 14); // Operador "Menor o igual que", compara si la primera expresión es menor o igual que la segunda R/=True.

// ------------------------------> Operadores Logicos.

/*
 * La interpretación que reciben los valores con estos operadores tiene unas caracteristicas que tenemos que
 * tener en cuenta. Para empezar, si estás comparando valores no binarios (que no son ni 0 ó 1, ni True ó false)estos
 * operadores intepretaran en base al tipo de valor si se puede convertir en un false o true por ellos mismos
 * y ejecutaran la comparación si se da el caso.
 *
 */

console.log("AND Logico => &&: ", true && false); // Este operador necesita que los dos operadores sean true para dar True.

console.log("Or Logico => || : ", true || false); // Este operador necesita que haya un operador true para dar True.

console.log("NOT Logico, !: ", !true); // Este operador devuleve falso si la expresión se puede interpretar como True.

// ------------------------------> Operadores bitwise.
/*Bitwise se puede interpretar como una operación bit a bit, lo cuál es lo que sucede aqui.
 * Estos operadores generan una acción primitiva sobre los los bits individuales de los numeros binarios.
 */

console.log("Bitwise AND &: ", 4 & 1); // Esta operación compara con el and y da un resultado de tipo binario R/= 0 (False).

console.log("Bitwise OR |: ", 4 | 1); // Esta operación compara con el or y da un resultado de tipo binario R/= 5 (True).

console.log("Bitwise XOR ^: ", 4 ^ 1); // Esta operación compara con el or de forma exclusiva en cada operando R/= 5 (True).

console.log("Bitwise NOT ~: ", ~4); // Esta operación invierte los bits del operando.

console.log("Bitwise << : ", 4 << 1); // Este operador desplaza los bits del primer número a la izquierda la cantidad del segundo.

console.log("Bitwise >> : ", 4 >> 1); // Este operador desplaza los bits del primer número a la derecha la cantidad del segundo.

// ------------------------------> Operadores Especiales

// Operador Ternario.
const edadDelChacho = 17;
let siEsMenorDeEdad =
  edadDelChacho < 18 ? "No puedes pasar, !!MOCOS0¡¡" : "Pase Adelante Señor...";
console.log("Que edad tienes joven?: ", siEsMenorDeEdad); // Este es un if abreviado, usarlo encadenado requiere cuidado.

// Operador typeof.
const queSeraEstaVariable = "Soy un String sumerce";
console.log(
  "!!He descubierto el tipo de la variable¡¡ JAJAJAJA, es... : ",
  typeof queSeraEstaVariable,
);
//Este operador nos permite identifica el tipo de dato que contiene uan variable, en JS con su libertad de lenguaje,
//podemos a veces perderle la pista a este tipo de cosas, por eso es necesario usarlo.

// -------------------------> Estructuras de Control.

// ---------->> IF/ELSE
let soyLaCondicion = true;

if (soyLaCondicion === true) {
  // La estructura if verifica una condición y en base a la misma ejecuta o pasa de largo.
  console.log("!! He entrado¡¡");
} else if (soyLaCondicion === false) {
  // Esta es otra medida en este sistema de manejo de condiciones que nos permite controlar mas
  // las opciones requeridas en el programa.
  console.log("Ja soy falso, noooo");
} else {
  // Esta estructura nos permite controlar el rechazo de un if con el cuál podemos manejar las negativas de la
  //condicion.
  console.log("!!NO eh entrado¡¡");
}

// ------------>> WHILE/DO-WHILE
//
let soyElContadorDelWhile = 0;
while (soyElContadorDelWhile < 10) {
  // La estructura del while se define por el hecho de iterar, de generar una ejecución
  // continua de el codigo que contiene hasta que se cumple la condición que procesa.
  console.log(`Estamos contando en el while vamos en ${soyElContadorDelWhile}`);
  soyElContadorDelWhile++;
}

do {
  // Esta estructura mantiene las mismas base de el while pero se ejecutara al menos uan vez.
  console.log("Pooooor lo menos una vez, ejecuuuutame.");
  soyElContadorDelWhile++;
} while (soyElContadorDelWhile === 10);

// ------------->> SWITCH
let diaDeDescanso = "Martes";
switch (
  diaDeDescanso // El switch obtiene una variable a traves de la cuál puede selecionar la opcion a ejecutar.
) {
  case "Lunes":
    console.log("Pues el lunes sera.");
    break;
  case "Martes":
    console.log("Uy si, el martes");
    break;
  default:
    console.log("Pues no se man...");
    break;
}

// -------------->> FOR

for (let index = 10; index > 0; index--) {
  // For nos permite controlar la cantidad de ejecuciones que queremos tener
  // de un codigo en especifico.
  console.log(`Despegando en ${index}`);
}

// -------------------------> Programa NoSoyNiInparNiMultiploDeTres.

function NoSoyNiInparNiMultiploDeTres(startLine = 10, FinalLIne = 55) {
  for (let index = startLine; index <= FinalLIne; index++) {
    if (index % 2 == 0 && index % 3 != 0 && index != 16) {
      console.log("No soy ni inpar, ni multiplo de tres, ni 16: ", index);
    }
  }
}

NoSoyNiInparNiMultiploDeTres();
