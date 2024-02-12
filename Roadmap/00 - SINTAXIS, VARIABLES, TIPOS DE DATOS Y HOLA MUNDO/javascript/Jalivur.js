/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
*/



//https://developer.mozilla.org/es/docs/
//COMENTARIOS:

// un comentario de una línea

/* 
este es un comentario
más largo, de varias líneas
*/

//* Sin embargo, no puedes /* anidar comentarios */ SyntaxError */

//DECLARACIONES:

    var firstVar ="En desuso"; //declaracion en sesuso, no tiene ambito de declaracion de bloque
    console.log(firstVar);
    console.log(typeof(firstVar));
    firstVar=5;
    console.log(firstVar);
    console.log(typeof(firstVar));
    let secondVar; 
    console.log(secondVar);
    secondVar= "Uso actual"; //declaracion variable local y de bloque, se pueden inicializar con valor o no.
    console.log(secondVar);
    console.log(typeof(secondVar));
    secondVar=5;
    console.log(secondVar);
    console.log(typeof(secondVar));
    const firstConst = "No puedo cambiar" //Declara un nombre de constante de solo lectura y ámbito de bloque.
    console.log(firstConst);
    console.log(typeof(firstConst));
    //firstConst =5; no se puede cambiar su valor

/*
Utiliza variables como nombres simbólicos para valores en tu aplicación. 
Los nombres de las variables, llamados identificadores, se ajustan a ciertas reglas.
Un identificador de JavaScript debe comenzar con una letra, un guión bajo (_) o un signo de dólar ($). 
Los siguientes caracteres también pueden ser dígitos (0-9).
*/

//javaScript tiene siete tipos de datos que son primitivos:
    //booleano
    let myBool=true;
    console.log(myBool);
    console.log(typeof(myBool));
    myBool=false;
    console.log(myBool);
    console.log(typeof(myBool));
    /*nulo o null Una palabra clave especial que denota un valor nulo. 
    (Dado que JavaScript distingue entre mayúsculas y minúsculas, 
    null no es lo mismo que Null, NULL o cualquier otra variante).*/
    let myNull = null;
    console.log(myNull);
    console.log(typeof(myNull));
    //undefined, o sin definir.
    let myUndefined;
    console.log(myUndefined);
    console.log(typeof(myUndefined));
    //Number. Un número entero o un número con coma flotante. Por ejemplo: 42 o 3.14159.
    let myNumber = 5;
    console.log(myNumber);
    console.log(typeof(myNumber));
    myNumber = -596.5;
    console.log(myNumber);
    console.log(typeof(myNumber));
    //Bigint. Un número entero con precisión arbitraria. Por ejemplo: 9007199254740992n.
    const myBigint=5896n;
    console.log(myBigint);
    console.log(typeof(myBigint));
    myNumber=4796;
    let mySecondBigint=BigInt(myNumber);
    console.log(mySecondBigint);
    console.log(typeof(mySecondBigint));
    //String. Una secuencia de caracteres que representan un valor de texto. Por ejemplo: "Hola".
    let myString="Hola, Me llamo Alberto";
    console.log(myString);
    console.log(typeof(myString));
    //Simbol (nuevo en ECMAScript 2015). Un tipo de dato cuyas instancias son únicas e inmutables. Se utiliza para crear identificaodres únicos para los objetos.
    let mySymbol = Symbol();
    console.log(mySymbol);
    console.log(typeof(mySymbol));
//Hola Mundo:
    // Imprimir por terminal:
    console.log("¡Hola, JavaScript!");

