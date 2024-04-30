/*
 * EJERCICIO:
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


