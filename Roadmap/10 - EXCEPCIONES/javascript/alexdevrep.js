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

//Declaramos las variables necesarias
let numero1 = 10
let numero2= 0
let listado = ["Hola","Alexdevrep","JavaScript","Mundo"]

//División
//Creamos una función que nos imprima el resultado de la división
function dividir (numero1,numero2){
    resultado= numero1/numero2
    if (resultado== Infinity){
        throw"Infinity no es un número real" //Lanzamos una excepción personalizada con throw
    }
    else{
        console.log(resultado)
    }
}

//Intentamos llamar a la función con el bloque try
try{
    dividir(numero1,numero2)
}

//Si se produce un error lo capturamos con el bloque catch para que el programa no de error
catch(e){
     console.log("ERROR: %s",e)   
}

//Finalizamos el programa con finally este bloque se ejecuta haya o no haya excepción

finally{
    console.log("Programa finalizado")
}

//Despues de finalizar el manejo de excepciones el programa continúa en vez de colapsar

//Listado
//Vamos a iterar el listado para ver sus elementos
function iterarListado(listado){
    for(i=0;i<5;i++){
        if (listado[i]===undefined){ //Si hay un elemento que sea undefined lanzamos la excepción
            throw "Solo hay 4 elementos en la lista"
        }
        else{
            console.log(listado[i])
        }
    }
}

try{
    iterarListado(listado)
}
catch(e){
    console.log("ERROR: %s",e)
}
finally{
    console.log("Programa finalizado")
}

//Dificultad EXTRA
const prompt = require('prompt-sync')()
//Crearemos un función que multiplique por 5 un número natural de una cifra
function multiplicación(parametro){
    if(parametro <0){
        throw "El número tiene que ser positivo"
    }
    else if(parametro>9){
        throw "El número no puede tener más de una cifra"
    }
    else if(parametro===undefined){
        throw "El parámetro 2 es obligatorio"
    }
    else{
        producto= 5*parametro
        console.log(producto)
    }

}

try{
    parametro=prompt("Introduce un número para multiplicarlo por 5: ")
    multiplicación(parametro)
}
catch(e){
    console.log("ERROR: %s",e)
}
finally{
    console.log("Programa finalizado")
}
