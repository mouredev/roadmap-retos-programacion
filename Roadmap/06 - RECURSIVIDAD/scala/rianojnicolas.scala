/*###################################
#   Dev: rianojnicolas              #
###################################*/

object Source6 {
    def main(args: Array[String]): Unit = {
        // EJERCICIO

        // 1. FUNCION RECURSIVA QUE IMPRIME NÚMEROS DEL 100 AL 0
        def print_numbers(n: Int) : Unit = {
            if (n >= 0) {
                println(n)
                print_numbers(n-1)
            }
        }
        print_numbers(100) // Imprime los números del 100 al 0

        // DIFICULTAD EXTRA
        // 1. FUNCION QUE CALCULE EL FACTORIAL DE UN NÚMERO
        def calc_factorial(n:Int): Int = {
            if (n == 0) {
                return 1
            }
            else {
                return n*calc_factorial(n-1)
            }
        }

        println(calc_factorial(5))  // Imprime el factorial de 5 = 120

        // 2. FUNCION QUE CALCULE UN ELEMENTO EN LA SUCESIÓN DE FIBONACCI SEGUN SU POSICIÓN
        // Secuencia -> 0, 1, 1, 2, 3, 5, 8, 13
        // Posición ->  0, 1, 2, 3, 4, 5, 6, 7
        def calc_fibonacci(pos:Int): Int = {
            if(pos == 0){
                return 0
            }
            else if (pos == 1) {
                return 1
            }
            else {
                return calc_fibonacci(pos-1) + calc_fibonacci(pos-2)
            }
        }
        println(calc_fibonacci(6)) // Imprime el valor de la posición 6 = 8
    }
}