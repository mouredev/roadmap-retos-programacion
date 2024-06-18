// ** EJERCICIOS

let error = 10 / 0
error // Infinity. En JavaScript no da error.

let paraError2 = [0, 1]
let error2 = paraError2[2]
error2 // Undefined. En JavaScript no da error.

function provocarErrores() {
    try {
        let obj = undefined; // Intentar acceder a una propiedad de undefined
        console.log(obj.propiedad);
    } catch (error) {
        console.error(`Error capturado: ${error.message}`);
    }

    try {
        funcionInexistente(); // Intentar llamar a una función que no existe
    } catch (error) {
        console.error(`Error capturado: ${error.message}`);
    }

    console.log("El programa continúa ejecutándose normalmente después de manejar las excepciones.");
}

// provocarErrores();

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------

function funcionErrores (a, b, c) {
    try {
        let a = undefined
        console.log(a.propiedad)
    } catch (error) {
        console.error(`Error 1: ${error.message}`)
        if (!error) {
            console.error('No se ha producido ningun error')
        }
    }

    try {
        funcionInexistente2(b)
    } catch (error) {
        console.error(`Error 2: ${error.message}`)
        if (!error) {
            console.error('No se ha producido ningun error')
        }
    }

    try {
        throw Error(`Error 3: Manual`)
    } catch (error) {
        console.error(error.message)
    }
}

funcionErrores('a', 'b', 'c')
