// Existen 3 tipos de comentarios en JavaScript:
// - Comentario de una linea:
// Este es un comentario de una linea
// - Comentario de varias lineas:
/* Y Este es un comentario de varias lineas, como puedes ver estoy intentando escribir un comentario lo suficientemente largo
para ensenarte que de esta manera se puede hacer un comentario de varias lineas, gracias por leer. */


// Creando una variable (var, let) y una constante:
/* Creando una variable usando var (function scope (si se declara dentro de un bloque condicional, se podra usar fuera de la condicional), 
    se puede volver a declarar con el mismo nombre y debido al hoisting estas variables
    durante la fase de compilacion son movidas al comienzo del ambito o scope en el que se encuentran, si no han sido declaradas antes 
    de una ejecucion devolvera undefined) */
    var variable_var = "Soy una variable var"; // Actualmente var no se usa, ya que no es una practica usada en el JavaScript moderno
    console.log(variable_var)
    // Creando una variable usando let (local scope (dependiendo en donde se declare y no se puede volver a redeclarar (mas optima de usar)))
    let variableLet = "Soy una variable let";
    console.log(variableLet)
    /* Creando una variable const (Una variable constante (no podra volver a cambiar su valor), tiene que
    declararse con un valor sino dara error y tiene ambito de bloque (block scope)) */
    const variableConstante = "Soy una variable constante y no podre volver a ser asignada";
    console.log(variableConstante)
    
    // Tipos de datos primitivos de JavaScript
    // String: Sirve para almacenar cadenas de texto.
    let cadena = "Hola, mundo!";
    console.log(cadena)
    // Number: Sirve para almacenar numeros
    let numero = 40;
    console.log(numero)
    /* BigInt: Sirve para almacenar numeros más grandes que el tipo 'number'. Se define
    agregando la letra "n" al final del número seguido de "n". */
    let numeroBigInt = 1234567890123456789012345678901234567890n;
    console.log(numeroBigInt)
    // Boolean: Sirve para almacenar tipos booleanos que son true y false
    let booleano = true;
    console.log(booleano)
    // Undefined: Las variables que son de tipo undefined significa que ya han sido declarado pero no les asignaron un valor
    let variableUndefined;
    let variableUndefinedExplicita = undefined
    console.log(variableUndefined) // undefined
    console.log(variableUndefinedExplicita)
    // Symbol: Es un tipo de dato que sus instancias son unicas e inmutables
    let variableSymbol = Symbol("foo");
    console.log(variableSymbol)
    
    // IMPRIMIR POR CONSOLA "HOLA, [NOMBRE DEL LENGUAJE]!"
    console.log("¡Hola, JavaScript!")