// https://www.typescriptlang.org/
// Esto es un comentario en una sola línea.
/*
 * Esto es un comentario
 * usando varías líneas
 * para describir el código.
 */
// Variable
var saludo = '¡Hola, ';
// Constante
const PROGRAMMING_LANGUAGE = 'TypeScript!';
// Datos Primitivos
// String
var palabra = 'Palabra';
printMessage("palabra", palabra);
var texto = 'Este string es un texto';
printMessage("texto", texto);
// Numbers
var numero = 123;
printMessage("numero", numero);
var decimal = 3.1415926535;
printMessage("decimal", decimal);
var negativo = -123;
printMessage("negativo", negativo);
var enteroGrande = 1234567890123456789012345678901234567890n;
printMessage("enteroGrande", enteroGrande);
// Booleans
var verdadero = true;
printMessage("verdadero", verdadero);
var falso = false;
printMessage("falso", falso);
// Symbol
var simbolo = Symbol('mi-simbolo');
printMessage("simbolo", simbolo);
// Undefined
var indefinido = undefined;
printMessage("indefinido", indefinido);
// Null
var nulo = null;
printMessage("texto", texto);
// Imprimir por terminal
console.log(saludo + PROGRAMMING_LANGUAGE);
function printMessage(string, any) {
    if (typeof (any) == "symbol") {
        console.log("La descripción de '" + string + "' es: " + any.description + ", y su tipo es: "
            + typeof (any));
    }
    else {
        console.log("El valor de '" + string + "' es: " + any + ", y su tipo es: "
            + typeof (any));
    }
}
