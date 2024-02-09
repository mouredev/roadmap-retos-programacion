object Main {
    def main(args: Array[String]): Unit = {
        // Operadores Aritmeticos
        val a = 2
        val b = 10
        println("OPERADORES ARITMETICOS")
        val suma: Int  = a + b 
        println(s"La suma entre $a y $b es igual a $suma")
        val resta: Int = a - b
        println(s"La resta entre $a y $b es igual a $resta")
        val division = a/b
        println(s"La division entre $a y $b es igual a $division")
        val producto: Int = a*b
        println(s"La multiplicacion entre $a y $b es igual a $producto")
        val modulo = a%b
        println(s"El resto de la division entre $a y $b es igual a $modulo")
        println("")

        // Operadores Relacionales
        println("OPERADORES RELACIONALES")
        val igualdad = a == b
        println(s"¿ Son iguales $a y $b ? RTA -> $igualdad")
        val diferencia = a != b
        println(s"¿ Son diferentes $a y $b ? RTA -> $diferencia")
        val mayor = a > b
        println(s"¿ $a es mayor a $b ? RTA -> $mayor")
        val menor = a < b
        println(s"¿ $a es menor a $b ? RTA -> $menor")
        val menorIgual = a <= b
        println(s"¿ $a es menor e igual a $b ? RTA -> $menorIgual")
        val mayorIgual = a >= b
        println(s"¿ $a es mayor e igual a $b ? RTA -> $mayorIgual")
        print("")

        // Operadores de Asignacion
        println("OPERADORES DE ASIGNACION")
        println("""
            Asignación
            """)
        var x = 5
        println(s"A la variable *x* le asignamos el valor $x, con la siguiente sintaxis x = 1 \n")

        println("CONTADOR DE SUMA")
        x += 1
        println(s"La operacion (x += 1), es equivalente x = x + 1, que da como resultado $x \n")

        println("CONTADOR DE RESTA")
        x -= 2
        print(s"La operacion (x -= 2), es equivalente x = x - 2, que da como resultado $x \n")

        println("CONTADOR DE PRODUCTO")
        x *= 5
        println(s"La operacion (x *= 5), es equivalente x = x * 5, que da como resultado $x \n")

        println("CONTADOR DE DIVISION")
        x /= 5
        println(s"La operacion (x /= 5), es equivalente x = x / 5, que da como resultado $x \n")

        println("CONTADOR DE MODULO")
        println(s"La operacion (x %= 2), es equivalente al residuo de la división entre $x / 2")
        x %= 2
        println(s"Esta operacion da como resultado $x \n")

        // Operadores Logicos
        val A = true
        val B = false
        println("OPERADORES LOGICOS")
        // AND
        println(s"$A and $B = ${A && B}")
        println(s"$B and $A = ${B && A}")
        println(s"$A and $A = ${A && A} \n")

        // OR
        println(s"$B or $A = ${B || A}")
        println(s"$A or $B = ${A || B}")
        println(s"$A or $A = ${A || A}")
        println(s"$B or $B = ${B || B} \n")

        // NOT
        println(s"not($A) = ${!A}")
        println(s"not($B) = ${!B} \n")
        
        // Operadores de Pertenencia
        println("""OPERADORES DE PERTENCIA
                    En Scala no hay operadores de este tipo,
                    Pero existen metodos para una estructura de datos
                    como lo son las listas o los conjuntos
                """)
        val my_list = List(1, 10, 4, 5, 100)
        println(s"La lista es: ${my_list.toString}")
        val element = 2
        println(s"¿$element esta en la lista? RTA->${my_list.contains(element)}\n")
        
        val my_set = Set(1, 2, 3, 4, 5)
        println(s"El conjunto es: ${my_set.toString}")
        println(s"¿$element esta en el conjunto? RTA->${my_set(element)}\n")

        // Operadores de Identidad
        println("""OPERADORES DE IDENTIDAD
                    En Scala no hay operadores de este tipo,
                    Pero existen un metodo denominado eq
                    que es equivalente al operador is de Python
                """)
        val d = List(1, 2, 3)
        val e = List(1, 2, 3)
        val f = d
        println(s"¿${d.toString} es el mismo objeto que ${e.toString}? RTA->${d eq e}")
        println(s"¿${d.toString} es el mismo objeto que ${f.toString}? RTA->${d eq f}\n")
        
        // Operadores Bit a Bit
        println("OPERADORES BIT A BIT")
        val x1 = 10 // binario es 00001010
        val y1 = 12 // binario es 00001100

        // AND - bit a bit
        var z = x1 & y1 // decimal es 8 - binario es 00001000
        println(s"La operacion: $x1 & $y1 = $z")

        // OR - bit a bit
        z = x1 | y1 // decimal es 14 - binario es 00001110      
        println(s"La operacion: $x1 | $y1 = $z")

        // XOR - bit a bit
        z = x1 ^ y1 // decimal es 6 - binario es 00000110
        println(s"La operacion: $x1 ^ $y1 = $z")

        // NOT - bit a bit
        z = ~x1 // decimal es -11 - binario es 11110101
        println(s"La operacion: ~$x1 = $z")

        // Desplazamiento a la izquierda - bit a bit
        z = x1 << 2 // decimal es 40 - binario 00101000
        println(s"La operacion: $x1 << 2 = $z")

        // Desplazamiento a la derecha - bit a bit
        z = x1 >> 2 // decimal es 2 - binario es 00000010
        println(s"La operacion: $x1 >> 2 = $z \n")

        // Estructuras de Control
        // Ciclo IF
        println("CICLO IF")
        if (x1%2 == 0) {
            println(s"$x1 es multiplo de 2")
        }
        else if (x1%3 == 0) {
            println(s"$x1 es multiplo de 3")
        }
        else {
            println(s"$x1 no es multiplo de 2 ni de 3")
        }

        // Ciclo WHILE
        println("\nCICLO WHILE")
        while (z <= 10) {
            println(z.toString)
            z += 1
        }

        // Ciclo FOR
        println("\nCICLO FOR")
        for (i <- 1 to 5) {
            println(i.toString)
        }

        // Match
        println("\nESTRUCTURA MATCH")
        val ciudad = "Bogota"

        ciudad match {
            case "Bogota" => println(s"La ciudad $ciudad es la capital de Colombia\n")
            case "Caracas" => println(s"La ciudad $ciudad es la capital de Venezuela\n")
            case "Quito" => println(s"La ciudad $ciudad es la capital de Ecuador\n")
        }

        // Manejo de Excepciones
        println("Try-Catch - Excepciones")
        try{
            println("Ingresa el dividendo de la division: ")
            val dividendo = scala.io.StdIn.readLine().toInt
            println("Ingresa el divisor de la division: ")
            val divisor = scala.io.StdIn.readLine().toInt
            val division = dividendo/divisor
            println(s"La division entre $dividendo / $divisor es igual a $division \n")
        }
        catch {
            case e: ArithmeticException => println("No se puede dividir por cero \n")
        }

        // Dificultad Extra
        println("EJERCICIO EXTRA")
        import scala.util.control.Breaks._
        for (i <- 9 to 56) {
            breakable {
                if (i == 16) {
                    break
                }
                else if (i%3==0) {
                    break
                }
                println(i)    
            }
        }
    }
}