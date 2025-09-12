/*
<-------------- Manejo de excepciones -------------->
Si no se atrapan los errores en nuestro código, lo que pasará es que el script se morirá inmediatamente e imprimirá un mensaje
con el error "por consola". Pero, si se atrapa el error con un bloque conocido como "try" (intentar) "catch" (atrapar), en lugar
de que el script muera de manera inesperada y solo muestre el error por consola, se puede hacer algo más razonable como por ejemplo,
mostrar un mensaje que pueda indicar de una manera más clara qué fue lo qué pasó y cómo podría solucionarse.
EL bloque try...catch permite atrapar errores en "tiempo de ejecución".
*/

// Sintaxis de try...catch

try {

    // código o script a ejecutar

} catch (err) {  // "err" es la variable que va a contener el error, puede tener un nombre diferente a "err"

    // manipulación del error

} finally {

    // Este bloque se ejecuta siempre, ponerlo es opcional
}


// Ejecución sin errores

try {    // Si el try no contiene ningún error, se ignora el catch

    console.log('Hola, no tengo errores.')

    // No hay ningún error

    console.log('Fin de la ejecución del try.')

} catch (err) {   // Si el try contiene algún error, el catch pasa a gestionar el error

    console.log(`El error en el escript es: ${err}`)

}

// Ejecución con errores

try {   

    console.log("Hola, sí tengo errores.")

    holaLola  // Error, variable no definida
    
    console.log('Fin de la ejecución del try (No se llegó hasta aquí).')

} catch (err) {  

    console.log(`El error en el escript es: ${err}`)

    // Propiedades principales del objeto "err":
    console.log(err.name)     // Nombre del error, por ejemplo: ReferenceError
    console.log(err.message)  // Mensaje con detalles del error
    console.log(err.stack)    // Pilla de llamadas actual

}
console.log('El error fue atrapado en catch y yo pude ser impreso en consola, sin el try...catch el script se hubiera detenido antes de llegar a mí.')


// Operación 10/0 = Infinity

function dividirPorCero(x,y) {
    return x/y
}

try {

    let resultado =  dividirPorCero(10,0)
    console.log(resultado)  // Infinity


    if(resultado === Infinity) {
        throw new Error(`La división no tiene solución, no puede dividir entre 0.`) // Error personalizado: este mensaje es el que va a imprimir "err"
    }

    console.log('No me ejecuto porque el throw actúa como un return que salta directamente al catch.')

} catch (err) {
    
    console.log(`Throw me dice: ${err.message}`)
    
}


// <-------------- Extra -------------->

function excepciones(param1, param2) {
    try {
        
        if(param1 === undefined || param2 === undefined) {
            throw new ReferenceError('variable no definida')
        }

        if(typeof param1 !== 'number' || typeof param2 !== 'number') {
            throw new TypeError('tipo de dato incorrecto, ambos datos deben ser números')
        }

        if (param1 > 100 || param2 > 100 ) {
            throw new Error('Los valores deben ser números menores a 100')
        }
    
        console.log('No se ha producido ningún error.')

    } catch (err) {
    
        if(err instanceof ReferenceError) {
            console.log(err.name)
            console.log(err.message)
        } else if(err instanceof TypeError) {
            console.log(err.name)
            console.log(err.message)
        } else {
            console.log(err.name)
            console.log(err.message)
        }
    
        
    } finally {
    
        console.log('La ejecución ha finalizado.')
    
    }
}

excepciones(50)         // variable no definida
excepciones(50, 'diez') // tipo de dato incorrecto, ambos datos deben ser números
excepciones(50, 101)    // Los valores deben ser números menores a 100
excepciones(50, 10)     // No se ha producido ningún error