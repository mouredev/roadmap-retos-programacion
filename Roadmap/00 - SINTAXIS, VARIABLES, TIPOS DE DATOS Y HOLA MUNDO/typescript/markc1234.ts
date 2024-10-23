// EJERCICIO:
// Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
// https://www.typescriptlang.org


// Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
// Comentario de una linea
/*
    Comentario de
    varias 
    lineas
*/


(() => {
    // Crea una variable (y una constante si el lenguaje lo soporta).
    let cadena:string = "Cadena de texto"
    const numero = 10

    // Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    const name = "Typescript"
    const age = 20
    const isStudent = true
    const nullVal = null
    const undefinedVal = undefined

    // Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    console.log(`¡Hola, ${name}`)
})()