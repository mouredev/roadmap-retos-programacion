// https://www.typescriptlang.org/

// Esto es un comentario en una sola línea.

/*
 * Esto es un comentario
 * usando varías líneas
 * para describir el código.
 */

// Variable
let saludo: string = '¡Hola, '

// Constante
const PROGRAMMING_LANGUAGE: string = 'TypeScript!'

// Datos Primitivos
// String
let palabra: string = 'Palabra'
printMessage("palabra", palabra);
let texto: string = 'Este string es un texto'
printMessage("texto", texto);

// Numbers
let numero: number = 123
printMessage("numero", numero);
let decimal: number = 3.1415926535
printMessage("decimal", decimal);
let negativo: number = -123
printMessage("negativo", negativo);
let enteroGrande: bigint = 1234567890123456789012345678901234567890n
printMessage("enteroGrande", enteroGrande);

// Booleans
let verdadero: boolean = true
printMessage("verdadero", verdadero);
let falso: boolean = false
printMessage("falso", falso);

// Symbol
let simbolo: symbol = Symbol('mi-simbolo') 
printMessage("simbolo", simbolo);

// Undefined
let indefinido: undefined = undefined
printMessage("indefinido", indefinido);

// Null
let nulo: null = null
printMessage("texto", texto);

// Imprimir por terminal
console.log(saludo + PROGRAMMING_LANGUAGE)

function printMessage(string: string, any: any) {
    if (typeof (any) == "symbol") {
        console.log("La descripción de '" + string + "' es: " + any.description + ", y su tipo es: "
            + typeof (any))
    } else {
        console.log("El valor de '" + string + "' es: " + any + ", y su tipo es: "
            + typeof (any))
    }
}