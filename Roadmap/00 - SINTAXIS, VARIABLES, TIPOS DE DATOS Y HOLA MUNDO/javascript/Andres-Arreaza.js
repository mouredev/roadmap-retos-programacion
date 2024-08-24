// Documentación de Javascript ==> https://developer.mozilla.org/es/docs/Web/JavaScript


//----------------------- Tipos de Comentarios -----------------------//

//Este tipo de comentario, nos permite comentar toda una linea de codigo.

/*
    Este tipo de comnetario
    se usa para comentar varias
    lineas de codigo
*/ 


//----------------------- Variables (VAR/LET/CONST) -----------------------//

//Variable var: Se usa en naveagdores viejos, y no es recomendable usarla.
var variableVar = "Variable Antigua";

//Variable let: Se usa para declarar vatiable de forma moderna.
let variableLet = "Variable Moderna";

//Variable const: Se usa para declarar una variable constante, la cual no va a cambiar y siempre tiene que ser inicializada.
const variableConst = "Variable const";


//----------------------- Tipos de Variables (NUMBER/BIGINT/DECIMAL/STRING/BOOLEAN/NULL/UNDEFINED/SYMBOL) -----------------------//

//Let Number: Este tipo de variable se usa para numeros enteros.
let number = 1;

//Let BigInt: Este tipo de variable se usa para numeros enteros grandes.
let bigInt = 122332122121;

//Let Decimal: Este tipo de variable se usa pata numeros que tengan decimales, en pocas palabras que tengan coma.
let decimal = 3.1416;

//Let String: Este tipo de variable se usa para una cadena de texto.
let string = 'Hola mi Nombre es Andrés Arreaza';

//Let Boolean: Este tipo de variable se usa para decir que es TRUE (verdadero), o false (falso).
let boolean = true;

//Let Null: Se utiliza para indicar la ausencia intencional de un valor.
let nombre = null;

//let Undefined: Este tipo de variable indica que una variable ha sido declarada pero no se le ha asignado un valor.
let appellido = undefined;
let lastName;

//Let Symbol: Este tipo de variable se utiliza para crear identificadores únicos.
let symbol = symbol("Simbolo");


//----------------------- Imprimir por consola) -----------------------//
console.log("¡Hola, Javascript!");
