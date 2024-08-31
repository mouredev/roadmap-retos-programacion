/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

// Variable Global
let resultado: number = 0;

//Función con retorno
function functionWithReturn(): string {
    return 'Hola mundo desde Typescript';
}

// Función con parametros (number) utilizando variable global
function fuctionWithParameters(valor1: number, valor2: number): void {
    // Variable global
    this.resultado = valor1 + valor2;
    console.log(`Función con parametros: ${valor1} + ${valor2} = ${this.resultado}`);
}

// Función con parametros con valor por default
function functionWithDefaultParameters(nombre: string = 'Peter', apellido: string = 'Parker'): string {
    return `${nombre} ${apellido}`;
}

/*
 * Utilización de una función dentro de otrar sin retorno 
 * y utilizando la función toUpperCase()
 */
function functionWithOtherFunction(): void {
    // Variable Local
    let resultado: string = functionWithReturn().toUpperCase();
    console.log(`Función que utiliza la función toUpperCase(): ${resultado}`);
}

// Consoles
console.log(functionWithReturn());
fuctionWithParameters(4,1);
console.log(functionWithDefaultParameters());
functionWithOtherFunction();

// Ejercicio Extra
function extraExercise(param1: string, param2: string): number {
    const array: number[] = Array.from(Array(100).keys()).map(x => x + 1);
    let numReturn = 0;
    array.forEach(num => {
        if(num % 3 == 0 && num % 5 == 0){
            console.log(param1);
        } else if(num % 5 == 0){
            console.log(param2);
        } else if(num % 3 == 0){
            console.log(`${param1} ${param2}`);
        } else {
            console.log(num);
            numReturn++;
        }
    });
    return numReturn;
}

console.log(extraExercise('Spider Man', 'Batman'));


 