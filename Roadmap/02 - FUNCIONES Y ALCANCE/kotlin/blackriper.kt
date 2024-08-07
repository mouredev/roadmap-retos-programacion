/*
  convenciones del lenguaje kotlin
  1.- clases y objectos  deben empezar con  mayuscula y usar camelcase
      ejemplos :
      class DeclarationProcessor { /*...*/ }
      object DeclarationProcessor { /*...*/ }

  2.- funciones y variables  deben empezar con minuscula y usar camelcase no guiones bajos
      ejemplos :
      fun DeclarationProcessor() { /*...*/ }
      var declarationCounter = 0

  3.- factorys usados para crear instancias pueden tener el mismo nombre
      ejemplos:
      interface Foo { /*...*/ }
      class FooImpl : Foo { /*...*/ }
      fun Foo(): Foo { return FooImpl() }

   4.- los metodos para test solo para testing pueden ir entre comilla (backticks) y usar guiones bajos
      ejpmplos:
          @Test fun `ensure everything works`() { /*...*/ }
          @Test fun ensureEverythingWorks_onAndroid() { /*...*/ }

   5.- las constastes de nivel superior o global se usan en mayusculas y pueden usar guines bajos(snake case)
      ejemplos:
          const val VERSION = 1
          const val VERSION_API = 2.0


   6.-objectos y instancias pueden usar camelcase, las instacias pueden iniciar con mayuscula
      ejemplos:
          val mutableCollection: MutableSet<String> = HashSet()
          val PersonComparator: Comparator<Person> = /*...*/

   7.- los atributos de clases que tengan el mismo nombre pero que uno sea publico y privado
        ejemplos:
           class C {
               private val _elementList = mutableListOf<Element>()
               val elementList: List<Element>
                    get() = _elementList
               }
   8.- muchos puntos no se han visto en el roadmap pero es bueno dejar notar cuando se ocupen
    recuerda usar nombre consisos a la funcion o clase o etc  de acuerdo a lo que representan la
    aplicacion y no nombrar tus variables como palabras reservedas del lenguaje.

 */


// variables globales
val dragonBallCharacters =listOf("Goku", "Vegeta", "Trunks", "Gohan", "Piccolo", "Krillin")

// funcion sin parametros
fun printDragonBallCharacters() {
    for (character in dragonBallCharacters) {
        println(character)
    }
}

// funcion con parametro
fun printDragonBallCharacters(character: String) {
    // variable local
    val existCharacter= character in dragonBallCharacters
    println("""$character exist? $existCharacter""")
}

// funcion con mas de un parametro y usando parametros por defecto
fun printDragonBallTecnique(character: String="Krillin", tecnique: String="Kienzan") {
   // find funcion para encontrar algun elemento de una lista y .let para llamar una funcion o sentencia dado el valor de otra funcion previa
   dragonBallCharacters.find { it == character }?.let { println("$character used $tecnique") }
}

// funcion con con retorno
fun getDragonBallCharacter(): String {
    return dragonBallCharacters.find { it=="Vegeta"}.toString()
}

// una funcion dentro de otra funcion
fun printDragonBallTecniques() {
    fun printTecnique() {
       val tecniques = mapOf("Goku" to "Kaioken", "Vegeta" to "Harlic ho!!", "Piccolo" to "makankosapo")
       for ((character, tecnique) in tecniques) {
           println("$character used $tecnique")
       }
   }
  printTecnique()
}

fun printNumberOrText(text1: String, text2: String): Int {
    var num=0
    for(i in 1..100){
        when{
           i%3==0 -> println("$text1")
           i%5==0 -> println("$text2")
           i%15==0 -> println("$text1 $text2")
           else -> {
               println("$i")
               num++
           }
        }
    }
  return num
}



fun main() {
   println("\nfuncion sin parametros\n")
   printDragonBallCharacters()
   println("\nfuncion con parametro\n")
   printDragonBallCharacters("Bulma")
   println("\nfuncion con mas de un parametro\n")
   printDragonBallTecnique("Goku", "Kamehameha")
   printDragonBallTecnique()
   println("\nfuncion con retorno\n")
   println(getDragonBallCharacter())
   println("\nfuncion dentro de otra funcion\n")
   printDragonBallTecniques()
   println("\nExtra\n")
   val rep=printNumberOrText("Hulk", "Aplasta")
   println("Numbers printed: $rep")
}


/* Notas
   it refiere a this en otros lenguajes y es una forma de referirce a un elemento actual  de la lista
   overloading de metodos algunos lenguajes permiten nombrar una funcion de la misma manera siempre y
   cuando sus parametros sean diferentes.
*/