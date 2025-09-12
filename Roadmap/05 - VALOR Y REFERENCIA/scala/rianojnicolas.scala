/*###################################
#   Dev: rianojnicolas              #
###################################*/
import scala.collection.mutable.ArrayBuffer

object Source5 {
    def main(args: Array[String]): Unit = {

        // 1. Asignacion de variables por valor y referencia
    
        // En Scala, todas las variables y parámetros de funciones se pasan por valor.
        // Esto significa que siempre se pasa una copia de lo que contiene la variable
        //  a. Para tipos primitivos como Int, Double, Boolean, etc., la copia es simplemente el valor en sí.
        //  b. Para objetos (listas, clases, arrays, etc.), la copia es la referencia al objeto, no el objeto
        //     completo. Entonces, aunque la referencia se pasa por valor, ambas variables (la original y la
        //     copia) apuntan al mismo objeto en memoria.
        //
        // Aunque Scala fomenta el uso de inmutabilidad (con val), las variables mutables (definidas con var)
        // permiten cambiar la referencia que almacenan, lo que significa que puedes hacer que una variable
        // apunte a un objeto diferente.
        // 
        // Mutabilidad e inmutabilidad: Si bien las variables val son inmutables (no pueden cambiar de 
        // referencia), si el objeto que apuntan es mutable, el contenido del objeto puede cambiar.
        
        // 1.1 Variables por valor
        
        println("1. Asignacion de variables por valor - para tipos primitivos")

        // var
        println("1.1.a Asignacion de variables por valor con definicion var")
        var myIntA = 10
        var myIntB = myIntA
        //myIntB = 20
        myIntA = 50
        println(myIntA)
        println(myIntB)
        println("\n")

        // val
        println("1.1.b Asignacion de variables por valor con definicion val")
        val myIntC = 10
        val myIntD = myIntC
        // myIntD = 20 // Error: val cannot be reassigned
        // myIntC = 50 // Error: val cannot be reassigned
        println(myIntC)
        println(myIntD)
        println("\n")

        // 1.2 Variables por referencia
        println("1.2 Variables por referencia")
        //   Como se explicó anteriormente, en Scala no existe la dinamica de variables por referencia, pero a nivel
        //   de objetos, las variables son referencias a objetos. Es decir que una copia del objeto es la referencia
        //   al objeto, no el objeto completo.
        //   Por ejemplo: Cuando se trabaja con objetos (especialmente los mutables), aunque técnicamente se están 
        //       pasando referencias por valor, la referencia apunta al mismo objeto.
        //   Ahora a nivel codigo sería algo así:
        println("1.2.a. Variables por referencia con definicion val, objeto mutable:")
        // Se utiliza una variable de tipo val "inmutable" para definir una referencia a un objeto. Pero
        // en este caso, el objeto es mutable, por lo que puedes modificar su contenido.
        // En este caso, la referencia apunta al mismo objeto que el objeto original.
        val array1 = ArrayBuffer(1, 2, 3)
        val array2 = array1  // Ambas referencias apuntan al mismo objeto
        array2 += 4  // Modificamos el objeto referenciado
        println(array1)  // Imprime ArrayBuffer(1, 2, 3, 4)
        
        println("1.2.b. Variables por referencia con definicion var, objeto mutable:")
        // Pero si utilizamos una variable de tipo var, la referencia tambien apunta al objeto original.
        var array3 = ArrayBuffer(4,5,6)  
        var array4 = array3  // La referencia apunta al mismo objeto
        array4 += 7  // Modificamos el objeto referenciado
        println(array3)  // Imprime ArrayBuffer(4, 5, 6, 7)
        println(array4)  // Imprime ArrayBuffer(4, 5, 6, 7)

        println("1.2.c. Variables por referencia con definicion var, objeto inmutable:")
        // Pero si utilizamos una variable de tipo var, con un objeto Lista que es inmutable,
        // la referencia sigue apuntando al objeto original. pero si "modificamos el objeto"
        // referenciado, la referencia no cambia porque este tipo de objeto no permite modificaciones. Por lo tanto,
        // el objeto original sigue siendo el mismo objeto y se crea una copia nueva con la modificacion.
        var my_listA = List(10, 20)
        var my_listB = my_listA  // La referencia apunta al mismo objeto
        println("my_listA - inicial : " + my_listA) // Imprime List(10, 20)
        println("my_listB - inicial : " + my_listB) // Imprime List(10, 20)
        my_listB :+ 50 // Modificamos el objeto referenciado, crea un NUEVO objeto List(10, 20, 50)
        println("my_listA - Final : " + my_listA) // Imprime List(10, 20)
        println("my_listB - Final : " + my_listB) // Imprime List(10, 20, 50)

        // 2. Ejemplos de funciones por valor y por referencia
        println("2. Ejemplos de funciones por valor y por referencia")

        // 2.1 Funciones con datos por valor
        println("2.1 Funciones con datos por valor")
        def fillCoupValue(fill: Int): Int = {
            // El parametro fill Scala lo toma por valor, por lo que no se puede modificar
            // Por lo tanto, creamos una variable mutable
            var modifiedFill = fill 
            val fill1 = 99 
            modifiedFill = fill1 // Modificamos el valor de la variable
            println(modifiedFill) // Imprime 99
            return modifiedFill // Devuelve el valor 99
        }
        
        var my_fill = 50
        fillCoupValue(my_fill) // Modificamos el valor de la variable con el valor 99
        println(my_fill) // Imprime 50

        //2.2 Funciones con datos por referencia
        println("2.2 Funciones con datos por referencia")
        // Como se explicó anteriormente, en Scala no existe la dinamica de variables por referencia o de
        // funciones con datos por referencia, pero a nivel de objetos, las variables son referencias a objetos.
        // Es decir que una copia del objeto es la referencia al objeto, no el objeto completo.
        
        def fillCoupHistory(fill: ArrayBuffer[Int]):ArrayBuffer[Int] = {
            fill += 25 
            
            val fill_a = fill
            fill_a += 45

            println(fill)
            println(fill_a)
            return fill
        }

        val my_fill_history = ArrayBuffer(0, 10, 5, 50, 20)
        fillCoupHistory(my_fill_history)
        println(my_fill_history)
        
        // Dificultad Extra
        // Caso 1: Parametros por valor
        def byValue(a: Int, b: Int):(Int, Int) = {
            var a_mod = a
            var b_mod = b
            val c = a_mod
            a_mod = b_mod
            b_mod = c
            return (a_mod, b_mod)
        }

        // Caso 2: Parametros por referencia
        def byRefer(a: ArrayBuffer[Int], b: ArrayBuffer[Int]):(ArrayBuffer[Int], ArrayBuffer[Int]) = {
            var a_mod = a
            var b_mod = b
            val c = a_mod
            a_mod = b_mod
            b_mod = c
            return (a_mod, b_mod)
        }
        
        // Ejecucion final
        def run(): Unit = {
            // Caso 1: Parametros por valor
            var my_val_1 = 10
            var my_val_2 = 20
            val (my_val_3, my_val_4) = byValue(my_val_1, my_val_2)
            println("Los valores retornados son: ")
            println(my_val_3)
            println(my_val_4)
            println("Los valores originales son: ")
            println(my_val_1)
            println(my_val_2)

            // Caso 2: Parametros por referencia
            var my_ref_1 = ArrayBuffer(10, 30, 50)
            var my_ref_2 = ArrayBuffer(20, 40, 60)
            val (my_ref_3, my_ref_4) = byRefer(my_ref_1, my_ref_2)
            println("Los valores retornados son: ")
            println(my_ref_3)
            println(my_ref_4)
            println("Los valores originales son: ")
            println(my_ref_1)
            println(my_ref_2)

        }
        
        run()
    }
}