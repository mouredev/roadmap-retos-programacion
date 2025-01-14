/** #10 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Las excepciones son eventos inusuales o errores que pueden ocurrir
 * durante la ejecución de un programa.
 * Cuando se produce una excepción, cuando algo ocurre con la ejecución normal
 * del programa se interrumpe y se busca un bloque de código llamado
 * "manejado de excepciones" para manejar la situación.
 */

//-----SINTAXIS-----
//Se empieza con TRY donde se ejecuta cuando todo sale bien
try {
    //El THROW permite personalizar un error
    throw new Error("Este es un ejemplo de excepción"); // Lanzar un error de Tipo Error
    throw expression; // Expresión es el valor personalizado que sera Lanzando
    throw 17; // Lanzar un error de tipo número
    throw true; // Lanzar un error de tipo boolean
    throw {toString:function(){ return "Error personalizado";   }   } // Lanzar un error de un tipo Objeto

} catch (error) {   //Se usa CATCH para macar un error si el código no funciona
    //Aquí se pone el error en mensaje ya sea en consola o a la vista del usuario
    console.error("Se produjo un error:", error.message);
}finally{   //Esta excepción es opcional y es FINALLY siempre se ejecuta, ocurra o no el programa
    //Manda mensaje siempre, ejecutado o no ejecutado el programa
    console.log("Este bloque se ejecuta siempre");
}


//---EJEMPLOS---
//  Hacemos un ejemplo de 10/0 para demostrar el try-catch
try {
    //  Vemos la operación ejecución
    let resultado = 10 / 0;
    //  Aquí validamos que no se 0
    if (resultado == 0) {
        //  Este es un error personalizado
        throw Error("No se puede dividir por 0");
    } else {
        //  Si no es 0 entonces que lo imprima
        console.log("El resultado de la division es:", resultado);
    }
} catch (error) {
    //Error si algo sale mal en el TRY
    console.error("Ha ocurrido un error:", error.message);
}

//  Hacemos con una lista
try {
    // Código que puede generar un error
    let array = [1, 2, 3];
    let elemento = array[10];  // Intenta acceder a un índice que está fuera del rango del array
    if (elemento == undefined) {
        throw Error(`La lista es de ${array.length}.`)
    } else {
        console.log(elemento);
    }
} catch (error) {
    // Captura el error y realiza acciones necesarias
    console.error("Se ha producido un error al acceder al índice:", error.message);
} 

/**-----DIFICULTAD EXTRA-----*/

// Mi excepción Personalizados
class excepciónPersonalizado extends Error{
    constructor(message){
        super(message);
        this.name = 'Mi_Excepción_Personalizada';
    }
}

// La función del programa (Utilize una lista)
function procesarParámetros(lista) {
    if (lista.length < 3) {
        throw new TypeError("Tiene que ser mas de 3 elementos");
    }
    if(typeof lista[2] !== 'number'){
        throw new Error("Los parámetros tiene que ser el mismo tipo");
    }
    if (lista === 'vació') {
        throw new excepciónPersonalizado("La lista no valida");
    }
    console.log('La ejecución ha finalizado sin errores');
}

// El TRY-CATCH-FINALLY para la ejecución
try {
    procesarParámetros([1, 2, 3, 4]);
} catch (error) {
    console.error("Ocurrió un error:", error.message);
} finally{
    console.log('Programa Finalizado')
}

/**-----DIFICULTAD EXTRA-----*/