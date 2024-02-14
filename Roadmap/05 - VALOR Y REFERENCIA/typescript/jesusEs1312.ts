/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

//--- Variables por valor
let numero: number = 21;
let numero2: number = numero + 10;
let numero3: number = numero2;
console.log(`numero: ${numero} | numero2: ${numero2} | numero3: ${numero3}`);

//--- Variables por referencia
let numArray: number[] = [10, 20, 30];
let numArray2: number[] = numArray;
numArray2.push(50);
console.log(`${numArray} | ${numArray2}`);

//--- Función que muestra el comportamiento de variables por valor
const variablePorValor = (num: number) => {
    num = num * 2;
    console.log(`El valor de num dentro de la función: ${num}`);
};

variablePorValor(numero);//Ejecutamos la función pasandole por parametro la variable 'numero' que vale 21
console.log(`El valor de num fuera de la función: ${numero}`);

//--- Función que muestra el comportamiento de variable por referencia
let arrayNumbers: number[] = [1, 2, 3];
const variablePorReferencia = (arrayNumbers) => {
    arrayNumbers[0] = arrayNumbers[0] * 10;
    console.log(`El valor dentro de la función de arrayNumbers[0] es: ${arrayNumbers[0]}`);
};

variablePorReferencia(arrayNumbers);//Ejecutamos la función pasandole por parametro el arrayNumbers 
console.log(`El valor fuera de la función de arrayNumbers[0] es: ${arrayNumbers[0]}`);

//--- Ejercicio Extra

//--- Función por valor 
let variableOriginal1: number = 5;
let variableOriginal2: number = 9;

function programaPorValor(param1: number, param2: number): [number, number] {
    let tempParam1 = param1;
    param1 = param2;
    param2 = tempParam1;
    return [param1, param2];
}

console.log(`Variable Original 1: ${variableOriginal1}`);
console.log(`Variable Original 1: ${variableOriginal2}`);

let nuevasVariablesPorValor: [number, number] = programaPorValor(variableOriginal1, variableOriginal2);
console.log(`Nueva Variable 1: ${nuevasVariablesPorValor[0]}`);
console.log(`Nueva Variable 2: ${nuevasVariablesPorValor[1]}`);

//--- Función por referencia
function programaPorReferencia(persona1: Persona, persona2: Persona): [string, string]{
    let tempHobbie: string = persona1.hobbie; 
    persona1.hobbie = persona2.hobbie;
    persona2.hobbie = tempHobbie;
    return [persona1.hobbie, persona2.hobbie]; 
}

let personaOriginal1: Persona = {
    nombre: "Peter",
    edad: 23,
    hobbie: "Fotografia"
}

let personaOriginal2: Persona = {
    nombre: "Chuy",
    edad: 25,
    hobbie: "Guitarra"
}

console.log(`Hobbie de persona 1 Original: ${personaOriginal1.hobbie}`);
console.log(`Hobbie de persona 2 Original: ${personaOriginal2.hobbie}`);

let nuevasPersonas: [string, string] = programaPorReferencia(personaOriginal1, personaOriginal2);

console.log(`Nuevo Hobbie de persona 1: ${nuevasPersonas[0]}`);
console.log(`Nuevo Hobbie de persona 2: ${nuevasPersonas[1]}`);

interface Persona {
    nombre: string,
    edad: number,
    hobbie: string
}