  var variable_global : String = "GLOBAL (podemos usarla en todas las funciones)"

// Ejemplo de una funcion que recibe parametros y tiene un return
fun sumar(a: Int, b: Int): Int {
  return a + b
}

// Funcion que no recibe parametros ni tiene retorno
fun restar(){
  var variable_local : String = "Esta es una varible local, solo para el ambito de esta funcion"
  var a = 10
  var b = 5
  println("El resutaldo es de ${a-b}")
  println(variable_local)
}

// Funcion que recibe un solo parametro
fun hello(cadena : String){
  println("Hello $cadena !!!")
}
// Funcion con parametros predeterminado
fun predet_fun(cad: String = "Este es el valor predeterminado"){
  println("$cad")
}

// creamos una funcion dentro de otra
fun crear_funciones(){
  fun sum(){
    println("Este mensaje esta dentro de un funcion que ha sido crada dentro de otra")
  }

  println("Estamos dentro de la funcion 1")
  sum()
}

// Funciones de extension
fun String.combi() : String {
  var cadena = this.uppercase()
  cadena = cadena.reversed()
  return cadena
}

// Funciones de orden superior
fun calcular(a: Int, b: Int, operacion: (Int, Int) -> Int): Int {
  return operacion(a, b)
}

// Funciones lambdas 
val multiplicacion = {a: Int, b: Int -> a * b}


  // Dificultad extra del ejercicio 02
  /*  DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos. */
  
fun extra(cad1 : String, cad2 : String) : Int {
    var cont : Int = 0
    var indice : Int = 0
    while(indice <= 100){
      when{
        indice % 5 == 0 && indice % 3 == 0 -> {print(" $cad1$cad2")}
        indice % 3 == 0 -> print(" $cad1")
        indice % 5 == 0 -> print(" $cad2")
        else -> {
          print(" $indice")
          cont++
        }
      }
      indice++
    }
    return cont
  }


fun main() {
  var cad : String = "todo en minus para probar"
  val resultado = sumar(3, 5)
  println("El resultado de la suma es: $resultado") // Salida: El resultado de la suma es: 8
  restar()
  predet_fun()
  predet_fun("Este es el mensaje que le hemos pasado por parametro")
  hello("Kotlin")
  crear_funciones()
  println(variable_global)

  //Ejemplo de funcion que esta establecida en el lenguaje
  println(cad.uppercase())

  // Vamos a probar una funcion de extension
  var cadena1 = "Funciones de extension"
  cadena1 = cadena1.combi()
  println("$cadena1")
  
  print("Se han impreso ${ extra("fizz", "buzz") } numeros")

  println("FUNCIONES DE ORDEN SUPERIOR")
  println("Este es el resultado de una funcion de orden superior: ${calcular(5, 4) {x, y -> x - y}}")

  println("FUNCIONES LAMBDA")
  println("Este es el resultado de una funcion lambda: ${multiplicacion(4, 3)}")
  
}