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

// Función sin parámetros ni retorno
function holaMundo() : void {
    console.log(`Hola mundo`);
}

holaMundo();

// Función con varios parámetros y retorno
function sumar(a: number, b: number): number {
    return a + b;
}

console.log(`El resultado de sumar 2 y 4 es ${sumar(2, 4)}`);

// Variable global
let global : string = 'Global';

// Función flecha dentro de otra función y variable local
function localGlobal(): void {
    let local : string = "Local";
    console.log(global);
    console.log(local);
    let funcion = () => {
        console.log('Función dentro de otra');
    }
    funcion();
};

localGlobal();

// Ejemplo función ya creada en el lenguaje
let notas : number[] = [10, 4, 5, 2, 6];
console.log(notas.sort((a, b) => a - b));

// Ejercicio extra
function imprimeCadena(str1: string, str2: string){
    let k: number = 0;
    for(let i = 0; i < 100; i++){
        if(i % 3 === 0 && i % 5 === 0){
            console.log(`${str1+str2}`)
        }else if(i % 3 === 0){
            console.log(`${str1}`)
        }else if(i % 3 === 0){
            console.log(`${str2}`)
        }else{
            console.log(i)
            k++;
        }
    }
    console.log(`El número se ha impreso ${k} veces.`);
}

imprimeCadena("fizz", "buzz");