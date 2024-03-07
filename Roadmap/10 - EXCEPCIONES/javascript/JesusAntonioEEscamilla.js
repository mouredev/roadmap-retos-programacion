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
    let resultado = 10 / 0;
    if (resultado == 0) {
        throw Error("No se puede dividir por 0");
    } else {
        console.log("El resultado de la division es:", resultado);
    }
} catch (error) {
    console.error("Ha ocurrido un error:", error.message);
}

/**-----DIFICULTAD EXTRA-----*/
//  Pendiente
/**-----DIFICULTAD EXTRA-----*/