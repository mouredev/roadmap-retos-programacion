fun main (){
    mostrarMensaje()
    mostrarMensaje2("Bienvenido")
    areaTriangulo(2,5)
    val resultado=Mayorde3(5,6,11)
    println("El mayor es $resultado")
    saludarPersona()
    outerFunction()
    val cuenta=extra("multiplo3","multiplo5")
    println("Total de intercambios por texto en el extra: $cuenta")
    
    
    }
    
    
    //funciones básicas que representen las diferentes posibilidades del lenguaje
    
    //Sin parámetros ni retorno
    
    fun mostrarMensaje () {
        println("________________________________")
        println("Hola, bienvenido a las funciones")
        println("********************************")
    }
    
    //con uno o varios parámetros
    
    fun mostrarMensaje2(cadena:String){
        println("________________________________")
        println(cadena)
        println("********************************")
    }
    
    fun areaTriangulo (base: Int, altura:Int){
        println("El area del triangulo con base=$base y altura=$altura es ${(base*altura)/2}")
    
    }
    
    //con retorno
    fun Mayorde3(v1:Int, v2:Int, v3:Int):Int {
    when{
    v1>v2 && v1>v3 -> return v1
    v2>v3-> return v2
    v3>v2-> return v3
    else->return v2
    }
    
    }
    
    //otras posibilidades
    
    // funcion con parametros determinados:
    fun saludarPersona(nombre: String = "Invitado") {
        println("Hola, $nombre!")
    }
    
    
    //funciones dentro de funciones
    fun outerFunction() {
        println("Esta es la función externa.")
    
        fun innerFunction() {
            println("Esta es la función interna.")
        }
    
        innerFunction()//llamo a la función interna solo desde la funcion externa
    }
    
    
    // extra
    
    /* 
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
     *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
     *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
     *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
     * */
    
     
     fun extra (cadena1:String, cadena2:String):Int{
        var cuenta = 0
        for (i in 1..100){
            when{
                i%5==0 && i%3==0 ->{
                println(cadena1+cadena2)
                cuenta++
                } 
            i%3==0->{
                println(cadena1)
                cuenta++
                }
            i%5==0->{
                println(cadena2)
                cuenta++
                }
            else->println(i)
            }
                    }
    return cuenta
                }
    
        
    
    
    