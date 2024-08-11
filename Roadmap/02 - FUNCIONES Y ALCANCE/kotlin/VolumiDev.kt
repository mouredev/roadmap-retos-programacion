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

fun crear_funciones(){
  fun sum(){
    println("Este mensaje esta dentro de un funcion que ha sido crada dentro de otra")
  }

  println("Estamos dentro de la funcion 1")
  sum()
}


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
        indice % 3 == 0 -> println(cad1)
        indice % 5 == 0 -> println(cad2)
        (indice % 5 == 0) && (indice % 3 == 0) -> {println("$cad1 $cad2")}
        else -> {
          println(indice)
          cont++
        }
      }
      indice++
    }
    return cont
  }


fun main() {
  val cad : String = "todo en minus para probar"
  val resultado = sumar(3, 5)
  println("El resultado de la suma es: $resultado") // Salida: El resultado de la suma es: 8
  restar()
  hello("Kotlin")
  crear_funciones()
  println(variable_global)

  //Ejemplo de funcion que esta establecida en el lenguaje
  println(cad.uppercase())
  
  println("Se han impreso ${ extra("Primera cadena de texto", "Segunda cadena de texto") } numeros")



}