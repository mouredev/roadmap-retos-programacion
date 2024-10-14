fun main(){
    
    // 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

        // EJERCICIO 00:
        // 0-01 Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

        // 0-01-a Esta es la URL del sitio oficial de kotlin | https://kotlinlang.org/ |

        // 0-01-b Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

        // Este es un comentario de una linea

        /* Sin embargo este es un comentario
         * de varias lineas lo escrito aqui
         * es un comentario.
         */

        // 0-02 Crea una variable (y una constante si el lenguaje lo soporta).

        var myVariable = "Esta es una variable de tipo sting"
        val constantePi = 3.1416
        // Pi = 5.2514 ---> esto proboca un error dado que 'val' es una constante y 'var' es una variable

        // 0-03 Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

        // 0-03-a Variables de tipo texto
        var continuarSiChar = 'Y'
        var stringCoqueto = "keh ase una shika como tu en un juglar come ete?"

        // 0-03-b Variables de tipo numerico (Hay mas como las hexadecimales entre otras, pero e puesto las mas comunes)
        var myNumByte = 3
        var myNumShort = 35
        var myNumInteger = 1518
        var myNumLong = 15487569
        var myNumDouble = 3.5934
        var myNumFloat = 3.5935488f

        // 0-03-c Variables de tipo Booleanas con sus tres posibilidades
        val myTrue = true
        val myFlase = false
        val myIndecision = null

        // 0-04 Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

        // El texto provoca un fallo de impresion en mi compilador devido a que el caracter | ¡ | 
        // igual no se encontrara en la escritura inglesa?!?!?
        println("¡Hola, kotlin!" + "¡Bienvenido al mundo!")
        
}
