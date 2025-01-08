// Ejercicio #00 - Mickel Arroz

/*
Web Oficial de Documentacion:  
https://developer.mozilla.org/es/docs/Web/JavaScript
*/

// Comentario simple (de una sola linea)
/*
    Comentario de varias lineas
    (comentario extenso)
*/

// VARIABLES
// Se usa 'let' en lugar de 'var', ya que permite trabajar con el scope de la variable, mientras 'var' no.
let variable = "valor";

// CONSTANTES
// Valor inmutable. Por convenio se suelen crear constantes en mayusculas, para visualmente identificarlas.
const CONSTANTE = "valor inmutable";

// TIPOS DE DATOS PRIMITIVOS EN JAVASCRIPT
// Se definen datos primitivos a los que no son objetos ni poseen metodos.

// String
// Secuencia de caracteres
let texto = "Texto de ejemplo. String es Primitivo";

// Number
// Tipo de dato numerico
let num = 1;

// Bigint
// Tipo de dato numerico tambien, pero que permite almacenar numeros mucho mas grandes.
// Para indicar que es un Bigint se agg la 'n' al final del numero.
let big = 123456789123456789n;

// Boolean
// Indica un valor de verdad o falso (1 o 0)
let bool = false;

// Undefined
// Son datos que no estan definidos. Es decir "sin definir".
// Al crear una variable sin asignarle un valor, se crea un Undefined
let und;

// Symbol
//  Se utiliza principalmente para crear propiedades de objetos que son garantizadas como únicas.
let sim = Symbol();

// IMPRIMIR POR TERMINAL
console.log("¡Hola, JavaScript!");
