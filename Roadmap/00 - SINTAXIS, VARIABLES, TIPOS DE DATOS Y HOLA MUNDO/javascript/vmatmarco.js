/* 1- SITIO WEB OFFICAL DE JAVASCRIPT */
//Puedes encontrar la documentación oficial de JavaScript en https://developer.mozilla.org/es/docs/Web/JavaScript


/* 2- TIPOS DE COMENTARIOS EN */
/*  
    En JavaScript, existen dos tipos de comentarios:
    1. Comentarios de una línea comienzan con // y se extienden hasta el final de la línea.
    2. Comentarios de varias líneas comienzan con /* y terminan con * / (sin espacio entre * y /) 
*/


/* 3- DECLARACION DE VARIABLES */

    var variableVar; //Variable global (Actualmente en desuso)
    let variableLet; //Variable local
    const variableConst = 3.1415; //Variable constante (No se puede modificar su valor)


/* 4- TIPOS DE DATOS PRIMITIVOS */

    //1. String: Para representar una cadena de caracteres se utilizan las comillas simples o dobles.
        let nombre = "Vicente";

    //2. Number: Para representar numeros enteros o decimales.
        let edad = 23;
        let altura = 1.75;

    //3. Boolean: Para representar valores lógicos. Solo puede ser true o false.
        let esEstudiante = true;
        let esMayorDeEdad = false;

    //4. Undefined: Representa una variable sin valor asignado.
        let variableSinValor;

    //5. Null: Representa una variable con valor nulo.
        let variableNula = null;

    //6. Symbol: Representa un valor único e inmutable, puede ser utilizado como clave de las propiedades de los objetos.
        let simbolo = Symbol('mi-simbolo');

    //7. BigInt: Permite representar números enteros mayores que (2^53 - 1) o menor que -(2^53 - 1).
        let numeroGrande = 1234567890123456789012345678901234567890n;


/* 5- IMPRIMIR POR CONSOLA */

    console.log("¡Hola, JavaScript!");