/*
 * EJERCICIO 1:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes) */

var suma = 1 + 2;
var resta = 1 - 2;
var multiplica = 1 * 2;
var divide = 1 / 2;
var modulo = 1 % 2;
var exponente = 1 ** 2;

var estrictamenteIgualA = 1 === '2';
var distintoA = 1 !== "2";
var mayorQue = 1 > 2;
var menorQue = 1 < 2;
var mayorOigualQue = 1 >= 2;
var menorOigualQue = 1 <= 2;

var andY = 1 && 2;
var orO = 1 || 2;
var notNo = !!true;

var array = [1,2,3];
var object = {a: 1, b: 2, c: 3};

var isArray = Array.IsArray(array);

var belongsToArray = array.includes(3);
var belongsToObject = "a" in object;




/*
 * EJERCICIO 2: * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 */

 // Condicionales
if (2 < 1) {
    console.log("no way...");
} else {
    console.log("2 is not less than 1");
}

let num = 3;
switch (num) {
    case 1:
        console.log("Number is 1");
        break;
    case 2:
        console.log("Number is 2");
        break;
    case 3:
        console.log("Number is 3");
        break;
    default:
        console.log("Number is not 1, 2 or 3");
        break;
}

// Iterativas
var array = [1, 2, 3, 4, 5];

var doblaForEach = array.forEach(num => console.log("doblaForEach:", num * 2)); 
var doblaMap = array.map(num => num * 2);
console.log("Dobla con map:", doblaMap);

for (let i = 0; i < array.length; i++) {
    console.log("forLoop:", array[i]);
}

var filtra = array.filter(num => num !== 4);
console.log("Filtra:", filtra);

let counter = 0;
while (counter < 3) {
    console.log("While loop:", counter);
    counter++;
}

counter = 0;
do {
    console.log("doWhileLoop:", counter);
    counter++;
} while (counter < 3);

// Excepciones
try {
    // Intenta ejecutar este código
    let resultado = 10 / 0;
    if (!isFinite(resultado)) {
        throw new Error("División por cero no permitida");
    }
} catch (error) {
    // Maneja cualquier error que ocurra
    console.error("Error capturado:", error.message);
} finally {
    // Este bloque siempre se ejecuta
    console.log("Operación de división intentada");
}

 /*
 * EJERCICIO 3:* - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * 
 *  */
 console.log("Suma:", suma); // 3
 console.log("Resta:", resta); // -1
 console.log("Multiplica:", multiplica); // 2
 console.log("Divide:", divide); // 0.5
 console.log("Modulo:", modulo); // 1
 console.log("Exponente:", exponente); // 1
 
 console.log("Estrictamente igual a:", estrictamenteIgualA); // false
 console.log("Distinto a:", distintoA); // true
 console.log("Mayor que:", mayorQue); // false
 console.log("Menor que:", menorQue); // true
 console.log("Mayor o igual que:", mayorOigualQue); // false
 console.log("Menor o igual que:", menorOigualQue); // true
 
 console.log("AND (&&):", andY); // 2
 console.log("OR (||):", orO); // 1
 console.log("NOT (!!):", notNo); // true
 
 console.log("Es array:", isArray); // true
 
 console.log("Pertenece al array:", belongsToArray); // true
 console.log("Pertenece al objeto:", belongsToObject); // true


  /*
  * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


const programa = () => {
    const min = 10
    const max = 55
    const noPrint = 16

    for (let i = min; i <= max; i++){

        if(i !== noPrint && i % 2 === 0 && i % 3 !== 0)
        console.log("este cumple los requisitos: ", i)
    }
}

programa()