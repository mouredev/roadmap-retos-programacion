function divide(a, b) {
    // 2- Throw
    if (a == 0 && b == 0) {
        throw new MyCustomeError('The numbers are equal to zero', a, b)
    }
    if (b == 0) {
        throw new Error('You can not divide between zero')
    } if (a == 0) {
        throw new Error('There is nothing to divide')
    } else {
        return a / b
    }
}

// try {
//     divide(1, 0)
// } catch (error) {
//     console.log('There was an error:', error.message)
// } 

/* Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */

function errorHandling(a, b) {
    // 1- try-catch
    try {
        console.log(`${a} / ${b} is: ${divide(a, b)}`)
    } catch (error) {
        console.log('There was an error:', error.message)
    } finally {
        console.log('End of execution')
    }
}

// 3- Personalize
class MyCustomeError extends Error {
    constructor (message, a, b) {
        super(message)
        this.a = a
        this.b = b
    }
        
    printNumbers() {
        console.log(this.a, "/", this.b, '= 0')
    }
}

try {
    console.log(divide(0, 0))
} catch (error) {
    console.log('There was a personalized error: ', error.message)
    error.printNumbers()
} finally {
    console.log('End of execution')
}

errorHandling(0,0)
errorHandling(10,0)
errorHandling(0,1)
errorHandling(2,1)


