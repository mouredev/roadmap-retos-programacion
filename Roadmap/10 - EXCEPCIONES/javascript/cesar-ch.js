/*
    #10 EXCEPCIONES
*/

try {
    const x = 10 / 0
    console.log(`El resultado de la division es: ${x}`)
} catch (error) {
    console.log(`Error: ${error.message}`)
} finally {
    console.log('Ejecución finalizada')
}

/*
    DIFICULTAD EXTRA 
*/

class ErrorPersonalizado extends Error {
    constructor(message) {
        super(message);
        this.name = 'ErroPersonalizado';
    }
}

function procesarParametros(parametro1, parametro2) {
    if (typeof parametro1 !== "number" || typeof parametro2 !== "number") {
        throw new ErrorPersonalizado('Los parametros deben ser numericos')
    }
    if (parametro2 === 0) {
        throw new Error('No se puede dividir por cero')
    }
    return parametro1 / parametro2
}

try {
    const resultado = procesarParametros("10", 0)
    console.log(`El resultado de la division es: ${resultado}`)
} catch (error) {
    if (error instanceof ErrorPersonalizado) {
        console.log(`Error: ${error.message}`)
    } else {
        console.log(`Error: ${error.message}`)
    }
} finally {
    console.log('Ejecución finalizada')
}