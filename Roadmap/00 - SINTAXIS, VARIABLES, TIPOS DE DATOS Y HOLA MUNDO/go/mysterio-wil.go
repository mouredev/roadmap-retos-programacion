// EJERCICIO:
// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
//   https://go.dev/

package main

import "fmt"

// - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// Esto es un comentario de una línea

/*
Esto es un comentario
de varias líneas
*/

func main() {
    // - Crea una variable (y una constante si el lenguaje lo soporta).
    var myVariable string = "Mi variable"
    const myConstant = "Mi constante"

    // - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    var myString string = "Cadena de texto"
    var myInt int = 10
    var myFloat float64 = 10.5
    var myBool bool = true
    // En Go, los caracteres se representan con el tipo rune (alias de int32)
    var myRune rune = 'a'

    // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    fmt.Println("¡Hola, Go!")
}
