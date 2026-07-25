//https://developer.mozilla.org/es/docs/Web/JavaScript

/**SINTAXIS,
 * VARIABLES, TIPOS DE DATOS Y
 * HOLA MUNDO
 */

//SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// VARIABLES Y CONSTANTES

// Variable (puede cambiar su valor)
let miVariable = "Puedo cambiar";

// Constante (no puede cambiar su valor)
const MI_CONSTANTE = "No puedo cambiar";

// Variable con var (antigua forma, no recomendada)
var variableAntigua = "Mejor usar let";

// TIPOS DE DATOS PRIMITIVOS EN JAVASCRIPT

// 1. String (cadena de texto)
let texto = "Hola mundo";
let textoComillasSimples = "También con comillas simples";
let textoTemplate = `Texto con template literals`;

// 2. Number (número - enteros y decimales)
let entero = 42;
let decimal = 3.14159;
let negativo = -15;
let notacionCientifica = 2.5e6; // 2.5 * 10^6

// 3. BigInt (números enteros muy grandes)
let numeroGrande = 9007199254740991n;
let otroGrande = BigInt("123456789012345678901234567890");

// 4. Boolean (booleano - verdadero o falso)
let verdadero = true;
let falso = false;

// 5. Undefined (indefinido)
let indefinido;
let explicitamenteIndefinido = undefined;

// 6. Null (nulo - ausencia intencional de valor)
let nulo = null;

// 7. Symbol (símbolo - valor único e inmutable)
let simbolo = Symbol("descripción");
let otroSimbolo = Symbol("descripción"); // Cada Symbol es único

// IMPRESIÓN POR TERMINAL
console.log("¡Hola, JavaScript!");
