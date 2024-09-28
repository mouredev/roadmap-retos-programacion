// Ejercicio 1
    // Por Índice
        //  EL try catch intenta hacer un trozo de código que le mandemos
        let lista: Array<number> = [2, 3, 4];
        try {
            if (lista.length <= 10) {
                throw new Error('El índice está fuera del rango del array.');
            }
            lista[10] = 0; // Intentamos acceder a un índice que no existe en el array
        } catch (error) {
            console.error('Ha ocurrido un error:' + error);
        } finally {
            console.log('La ejecución del bloque try-catch ha terminado.');
        }


    //Dividiendo 10/0
    try {
        let divisor = 0;
    
        if (divisor === 0) {
            throw new Error('División por cero no está permitida.');
        }
    
        let result = 10 / divisor;
        console.log('Resultado:' + result);
    } catch (error) {
        console.error('Ha ocurrido un error:' + error);
    } finally {
        console.log('La ejecución del bloque try-catch ha terminado.');
    }


    // Ejercicio Extra
    class CustomError extends Error {
        constructor(message: string) {
            super(message);
            this.name = "CustomError";
        }
    }

    function procesarParametros(param1: number, param2: number): void {
        try {
            const resultado = param1 / param2;
            console.log('Resultado del procesamiento: ' +resultado);
        } catch (error) {
            if (error instanceof CustomError) {
                console.error('Error personalizado: ' + error.message);
            } else if (error instanceof TypeError) {
                console.error('Error de tipo: ' + error.message);
            } else {
                console.error('Error desconocido: ' + error.message);
            }
        } finally {
            console.log('La ejecución ha finalizado');
        }
    }

    // Ejemplo de uso
    try {
        procesarParametros(10, 0); // Lanza una excepción personalizada
        procesarParametros(20, 1); // Lanza una excepción de tipo
        procesarParametros(30, 5); // No se produce ningún error
    } catch (error) {
        console.error('Error capturado fuera de la función: ' + error.message);
    }