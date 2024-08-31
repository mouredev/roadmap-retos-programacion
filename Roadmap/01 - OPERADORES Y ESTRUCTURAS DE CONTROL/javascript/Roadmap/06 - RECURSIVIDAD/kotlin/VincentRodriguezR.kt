class recursion{
    fun main(){
        //Ejercicio de recursividad
        fun printNumber(number:Int){
            if(number >= 0){
                println(number)
                //La recrsividad es cuando una funcion se llama a si misma generando un bucle de ejecucion de si misma
                printNumber(number - 1)
            }
        }

        //Ejercicio Extra
        fun factorial(number: Int): Int{
            if(number<0){
                println("El numero no es valido")
                return(0)
            }else if(number == 0){
                return(1)
            }else{
                return(number * factorial(number-1))
            }
        }

        fun fibonacci(number: Int): Int{
            if(number<0){
                println("La posicion tiene que ser mayor que cero")
                return(0)
            }else if(number == 1){
                return(0)
            }else if(number == 2){
                return(1)
            }else{
                return (fibonacci(number-1)+fibonacci(number-2))
            }
        }

        printNumber(100)
        println(factorial(5))
        println(fibonacci(4))

    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val obj = recursion()
            obj.main()
        }
    }
}