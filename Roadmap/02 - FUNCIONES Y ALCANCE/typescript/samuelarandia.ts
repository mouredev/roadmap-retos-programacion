/*--- Tipo de funciones ---*/

// Funcion autoejectuable
(function(){
    console.log('Funcion autoejectuable')
})()

//Sin parametros ni retorno

function sinParametros(): void{ 
    console.log('Sin parametros')
}
sinParametros()

//Con un parametro y retorno

function unParametro(numero: number): number{
    return numero
}

console.log(unParametro(5))

//Con varios parametros y retorno

function variosParametros(a: number, b: number): number{
    return a + b
}

console.log(variosParametros(2, 3))


//Funcion dentro de funcion

function funcionExterna(){
    function funcionInterna(){
        console.log('Funcion interna')
    }
    funcionInterna()
}

funcionExterna()

//Funciones ya creadas en el lenguaje

const arrayEjemplo: number[] = [1, 2, 3, 4, 5]
const restaArray = arrayEjemplo.reduce((a, b) => a - b, 0)
console.log("Resta del array:", restaArray)


//Variable local y global

let variableGlobal: number = 100

function mostrarVariableGlobal(): void {
  console.log("Variable global dentro de la función:", variableGlobal)
}

function cambiarVariableGlobal(): void {
  let variableLocal: number = 50
  variableGlobal = variableLocal
  console.log("Variable global cambiada dentro de la función:", variableGlobal)
}

// Llamadas a toda la funciones creadas

sinParametros()
console.log("Resultado de unParametro(4):", unParametro(4))
console.log("Resultado de variosParametros(3, 7):", variosParametros(3, 7))
funcionExterna()
console.log("Variable global fuera de la función:", variableGlobal)
mostrarVariableGlobal()
cambiarVariableGlobal()


/*
 * EJERCICIO:
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
// Funcion que recibe dos paremetros

function cadenasRetornoNumero( cadena1: string, cadena2: string): number{
    if (typeof cadena1 !== "string" || typeof cadena2 !== "string") {
        throw new Error("Los argumentos deben ser cadenas de texto")
    }
    let contadorNumeros: number[] = [];
    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(cadena1 + cadena2, i);
        } else if (i % 3 === 0) {
            console.log(cadena1, i);
        } else if (i % 5 === 0) {
            console.log(cadena2, i);
        } else {
            contadorNumeros.push(i);
        }
    }
    return contadorNumeros.length;
}

console.log("Número de veces que se imprimió un número:", cadenasRetornoNumero( "fizz", "buzz"))

