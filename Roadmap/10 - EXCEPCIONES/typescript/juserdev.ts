/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */

namespace challenge_10{
    // const dividir = (a: number, b: number): number =>{
    //     if (b === 0) {
    //         throw new Error("no se puede dividir entre 0")
    //     }
    //     return a / b
    // }
    
    // try {
    //     const resultado = dividir(10,0)
    //     console.log(`Resultado: ${resultado}`)
    // }
    // catch(e){
    //     console.error("Se a ocacionado un error: ", (e as Error).message)
    // }
    // console.log("Hola, que pasa!") 

    class DivisionByZeroError extends Error{
        constructor(){
            super("No se puede dividir por 0")
            this.name = "DivisionByZeroError"
        }
    }
    
    //* Esta la cree para probar mi conocimiento sobre el tema

    class StrTypeError extends Error{ 
        constructor(){
            super("el parametro no puede ser un string")
            this.name = "StrTypeError"
        }
    }

    const process_param = (params: any[])=>{
        if (params.length < 3) {
            throw new RangeError("El numero de parametros es insuficientes, se esperan al menos 3")
        } else if (params[1] === 0){
            throw new DivisionByZeroError()
        } else if (typeof params[2] !== "number") {
            // throw new Error("No determiamos la causa del error") -> si ejecuto esta linea de codigo, manda un erro generico
            throw new StrTypeError()
        }

        console.log(params)
        console.log(params[0] / params[1])
        console.log(params[2] + 5)
    }
    try{
        process_param([1,2,3,4])
    }
    catch(e){
        if (e instanceof RangeError) {
            console.error("Se ha productido el error: ", e.name, "->", e.message)
        } else if (e instanceof DivisionByZeroError) {
            console.error("Se ha productido el error: ", e.name, "->", e.message)
        } else if (e instanceof StrTypeError){ // no esta funcionando debido a que debia cargar un error generico
            console.error("Se ha productido el error: ", e.name, "->", e.message)
        } else if (e instanceof Error) {
            console.error("Se ha productido un error inesperado: ", e)
        }
    }
    finally{
        console.log("El programa ha finalizado")
    }
}

