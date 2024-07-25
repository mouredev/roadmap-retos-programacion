/*

A una expresión regular es una cadena de caracteres que es utilizada para describir o encontrar
patrones dentro de otros strings, en base a las delimitadores y ciertas reglas de sintaxis.

En kotlin las regex se pueden crear de tres  formas:

Regex("a[bc]+d?") // apartir de la clase Regex

"a[bc]+d?".toRegex() // apartir de una cadena

Regex.fromLiteral("a[bc]+d?") // apartir de un metodo estatico de la clase Regex

para crear testear y probar expresiones regulares visita el siguiente link:
https://regexr.com/

*/

fun workingWithRegex() {
    val regex = Regex("[0-9]")

    val text="""
        El manga Hokuto no ken cuenta con 245 capítulos, publicados en la revista semanal Shōnen Jump,
        desde el número 41 de 1983 hasta el número 35 de 1988. Luego fue recopilado en 27 volúmenes
        por Shueisha. Se está publicando en 14 Kanzenban por Shōgakukan y una Master Edition de 27 volúmenes 
        por Coamix.
    """.trimIndent()

    val result = regex.findAll(text)
    result.forEach {
        println(it.value)
    }
}


fun validateUrl(url: String) =
      Regex("^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]").matches(url)

/* explicacion del pattern
^(https?):// : debe comenzar con http o https seguido de dos puntos y dos sla
[-a-zA-Z0-9+&@#/%?=~_|!:,.;]: puede contener caracteres alfanuméricos, guiones bajos, signos mas, ampersands o guiones y puede ir separado por puntos
*[-a-zA-Z0-9+&@#/%=~_|]: puede contener caracteres alfanuméricos, guiones bajos, signos mas puede terminar con un slash y seguido de algun caracter especial
*/


fun validateEmail(email: String) =
    Regex("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$").matches(email)

/* explicacion del pattern
  ^[a-zA-Z0-9_+&*-] : debe comenzar uno o más caracteres alfanuméricos, guiones bajos, signos más, ampersands o guiones
  +(?:\.[a-zA-Z0-9_+&*-]+): puede contener caracteres alfanuméricos, guiones bajos, signos mas, ampersands o guiones y puede ir separado por puntos
  *@(?:[a-zA-Z0-9-]+\.): debe contener un arroba  puede contener numeros o letras y debe terminar en un punto
  +[a-zA-Z]{2,7}$: debe terminar en un string de entre 2 y 7 caracteres
 */




fun validatePhone(phone: String) =
    Regex("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*\$").matches(phone)

/* explicacion del pattern
 ^[+]* : puede inicar con un signo mas
 [(]{0,1} : puede inicar con un parentesis
 [0-9]{1,4} : puede contener digitos de 0 a 9 en un rango de 1 a 4 digitos
 [-\s\./0-9]* : puede contener guiones o puntos entre cada  numero
 */

fun main() {
  workingWithRegex()
  validateUrl("https://www.google.com").let {
     println(it)
   }
   validateEmail("w0Ezy@example.com").let {
     println(it)
   }

   validatePhone("411-153-1223").let {
     println(it)
   }
}