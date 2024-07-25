
//1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

//https://developer.mozilla.org/es/docs/Web/JavaScript




//2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

    // El uso de dos barras seguidas (//) sirve para comentarios de una sola linea de código tambien usando en shortcut ( control + } ), Ejemplo:

        //este es un ejemplo.

    // El uso de una barra y un asterisco como si fuera una etiqueta de apertura y de forma invertida como una etiqueta de cierra (/*  */), sirve para comentarios de varias lineas de códigos tambien usando en shortcut ( Alt + shif + A } ), Ejemplo:

        /* este es un ejemplo de
        comentar varias lineas de 
        codigo en JavaScript */



//3. Crea una variable (y una constante si el lenguaje lo soporta).

    let nombre = "Jose";
    const pi = 3.14;// por convención



//4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

    //cadenas de texto:
        let texto = "El lenguaje de programacion es JavaScript, y es ..." // ejemplo de cadena de texto

    //enteros:
        let isNumber = 23; //ejemplo de numero, puede se negarivo tambien
        let isNotNunber = NaN // cuando una variable se asigna un valor de numero pero el resultado es un valor no numerico.
    
    //flotante:
        let isFloat = 1.5; //ejemplo de numero con decimal
    
    //booleanos:
        let isBoolean1 = true;
        let isBoolean2 = false;

//5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

    let languaje = "JavaScript";
    console.log("Hola Mundo "+ languaje);
