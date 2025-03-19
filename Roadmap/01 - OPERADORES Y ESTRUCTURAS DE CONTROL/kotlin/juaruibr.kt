/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


// Lenguaje Kotlin

/* Operadores de Signo
   Comenzamos con los operadores unarios que representan la propiedad de un número de ser negativo,
   representado por -, o positivo, representado por +.

   Operador	Expresión	Función equivalente
      +	       +a	       a.unaryPlus()
      -	       -a	       a.unaryMinus()
*/
fun operadoresDeSignos() {
    val a = -3
    println("a=${-a}") // Negar valor con valor de -3, por resultado nos dará a=3
}

// Operadores Aritméticos
fun operadoresAritmeticos() {
    val a = 10
    val b = 20

    println("($a + $b)= ${a + b}") // Suma
    println("($a - $b)= ${a - b}") // Resta
    println("($a x $b)= ${a * b}") // Multiplicación
    println("($a / $b)= ${a / b}") // Divisón
    println("($a % $b)= ${a % b}") // Residuo
}

/* Operadores de Asignación Compuesta
   Estos operadores son la combinación entre el operador de asignación y los operadores aritméticos,
   con el fin de usar como operando la variable de resultado.

   Por ejemplo: si quieres acumular el valor de b en a, la abreviación para el operador compuesto
                de suma es la siguiente: a += b // a = a + b

   Operador	Expresión simplificada	Expresión Completa	Función Equivalente
      +=	       a+=b	                   a=a+b	      a.plusAssign(b)
      -=	       a-=b	                   a=a-b	      a.minusAssign(b)
      *=	       a*=b	                   a=a*b	      a.timesAssign(b)
      /=	       a/=b	                   a=a/b	      a.divAssign(b)
      %=	       a%=b	                   a=a%b	      a.remAssign(b)
 */
fun operadoresAsignacionCompuesta() {
    var a = 100
    val b = 5

    a += b
    println("+= $a")
    a -= b
    println("-= $a")
    a *= b
    println("*= $a")
    a /= b
    println("/= $a")
    a %= b
    println("%= $a")
}

/* Operadores de Incremento y Decremento
   El operador de incremento, representado por dos signos de suma (++), incrementa en la unidad
   al operando.

   monstersKilled++

   Análogamente, el operador de decremento, doble signo menos (--), disminuye en la unidad al
   operando.

   hearts--

   El incremento depende de si el operador es prefijo o sufijo del operando:

    Prefijo: Se realiza el incremento sobre la variable y luego es usada en la expresión que la
    contiene.

    Sufijo: Se usa la variable en la expresión y luego si se aplica el incremento.
    Ejemplo: Declarar una variable entera con el valor de 2 e imprimir su valor luego de incrementar
             con prefijo y decrementar con sufijo.
 */
fun operadoresDeIncrementoyDecremento() {
    var a = 2

    println("De $a a ${++a}") // De 2 a 3
    println("De $a a ${a--}") // De 3 a 3
    println("Valor final > $a") // Valor final > 2

    // Aunque el valor es disminuido en la segunda impresión, este no se hace efectivo sino hasta
    // que se termina la línea.
    // Por eso el resultado final es 2 en la tercera impresión.
}

/* Operadores Relacionales
   Los operadores relacionales te permiten verificar enunciados de igualdad y desigualdad entre dos
   valores. El tipo de dato resultante de la expresión es Boolean, indicando la veracidad del
   enunciado expresado.

   Aquí hay una la tabla de estos operadores:

    Operador	  Enunciado	           Expresión	       Función Equivalente
      ==	    a es igual a b	          a==b	       a?.equals(b) ?: (b === null)
      !=	    a es diferente de b	      a!=b	      !(a?.equals(b) ?: (b === null))
       <	    a es menor que b	      a<b	            a.compareTo(b)<0
       >	    a es mayor que b	      a>b	            a.compareTo(b)>0
      <=	    a es menor ó igual que b  a<=b	            a.compareTo(b)<=0
      >=	    a es mayor o igual que b  a>=b	            a.compareTo(b)>=0

    Ejemplo: Usar los operadores relacionales entre los números 17 y 20.
 */
fun operadoresRelacionales() {
    val a = 17
    val b = 20

    println("$a es igual a $b: ${a == b}")  // 20: false
    println("$a es diferente a $b: ${a != b}") // 20: true
    println("$a es menor que $b: ${a < b}")  // 20: true
    println("$a es mayor que $b: ${a > b}")  // 20: false
    println("$a es menor o igual que $b: ${a <= b}")  // 20: true
    println("$a es mayor o igual que $b: ${a >= b}")  // 20: false
}

/* Operadores Logicos
   Los operadores lógicos te permiten crear expresiones de lógica proposicional como lo son
   conjunción, disyunción y negación.

   && / Conjunción (and): el resultado es true si a y b son true / a && b
   || / Disyunción (or): el resultado es true si a o b son true / a || b
   !  / Negación (not): el resultado es false si a es true, o viceversa / !a

   Ejemplo: Usar las proposiciones «5 mayor que 0» y «5 es par» para comprobar el funcionamiento
   de los operadores lógicos.
 */

fun operadoresLogicos() {
    val input = 5
    var res: Boolean

    val greaterThanZero = input > 0
    val isEven = input % 2 == 0

    res = greaterThanZero && isEven
    println("Es mayor que cero y par:$res")

    res = greaterThanZero || isEven
    println("Es mayor que cero o par:$res")

    res = greaterThanZero && !isEven
    println("Es mayor que cero e impar:$res")
}

/* Operadores a nivel de Bits
   Kotlin provee funciones para los tipos primitivos enteros, que actúan como operadores a nivel
   de bits.

   and()	and bit a bit	a and b
   or()	    or bit a bit	a or b
   xor()	xor bit a bit	a xor b
   inv()	not bit a bit	a.inv()
   shl()	Desplazamiento de bits a la izquierda	          a shl b
   shr()	Desplazamiento de bits a la derecha	              a shr b
   ushr()	Desplazamiento de bits a la derecha sin signo	  a ushr b

   Ejemplo: Operar a nivel de bits los números enteros 5 y 7.
 */

fun operadoresaNivelDeBits() {
    val a = 5
    val b = 7

    println("a and b: ${a and b}")   // a and b: 5
    println("a or b: ${a or b}")     // a or b: 7
    println("a xor b: ${a xor b}")   // a xor b: 2
    println("a.inv(): ${a.inv()}")   // a.inv(): -6
    println("a shl b: ${a shl b}")   // a shl b: 640
    println("a shr b: ${a shr b}")   // a shr b: 0
    println("a ushr b: ${a ushr b}") // a ushr b: 0
}

// *************************************************************************************************
// ESTRUCTURAS DE CONTROL
/*
    Las estructuras de programación en Kotlin son las construcciones fundamentales que te permiten
    controlar el flujo de ejecución de un programa. Las principales estructuras de programación en
    Kotlin son:

    Estructuras Condicionales:

    if: Permite ejecutar un bloque de código si una condición es verdadera.
    when: Similar a un switch-case en otros lenguajes, pero más versátil y poderoso.

    Estructuras Repetitivas:

    for: Utilizado para iterar sobre una secuencia de elementos (como un rango numérico).
    while: Ejecuta un bloque de código mientras una condición sea verdadera.
    do-while: Ejecuta un bloque de código al menos una vez y luego verifica una condición.

    Control de Flujo:
    return: Devuelve un valor y sale de una función.
    break: Sale de un bucle antes de que termine su ejecución normal.
    continue: Salta a la siguiente iteración de un bucle.
 */

/* ESTRUCTURAS CONDICIONALES */

//Estructura if basico
val edad = 18
if (edad >= 18) { println("Eres mayor de edad") }
else { println("Eres menor de edad") }

// Estructura if como expresión
val calificacion = 85
val resultado = if (calificacion >= 60) { "Aprobado" }
else { "Reprobado" } println("El resultado es: $resultado")

// Estructura when
// La estructura when es similar a un switch-case en otros lenguajes, pero más poderosa y flexible.
val dia = 3
when (dia) {
    1 -> println("Lunes")
    2 -> println("Martes")
    3 -> println("Miércoles")
    4 -> println("Jueves")
    5 -> println("Viernes")
    else -> println("Día no válido")
}

// También puedes usar el when con expresiones:
val calificacion = 85
val resultado = when {
    calificacion >= 90 -> "Excelente"
    calificacion >= 80 -> "Bueno"
    calificacion >= 70 -> "Regular"
    else -> "Insuficiente" }
    println("El resultado es: $resultado")

/* ESTRUCTURAS REPETITIVAS */
/*
    En Kotlin, al igual que en otros lenguajes de programación, puedes utilizar estructuras
    repetitivas para ejecutar un bloque de código varias veces. Las estructuras repetitivas más
    comunes son los bucles for, while y do-while. Aquí tienes ejemplos de cómo usarlos:
 */

// Bucle for
// El bucle for se utiliza para iterar sobre una secuencia de elementos
// (por ejemplo, un rango numérico).

for (i in 1..5) { println("Iteración $i") }

// Bucle while
// El bucle while se ejecuta siempre que la condición especificada sea verdadera.

var contador = 1 while (contador <= 5) { println("Iteración $contador") contador++ }

// Bucle do-while
// El bucle do-while se ejecuta al menos una vez, ya que primero se ejecuta el bloque y
// luego se verifica la condición.

var contador = 1 do { println("Iteración $contador") contador++ } while (contador <= 5)

// Uso de breal y continue
// Puedes usar la instrucción break para salir de un bucle antes de que se complete su iteración
// normal. Y puedes usar la instrucción continue para omitir la iteración actual y pasar a
// la siguiente.

for (i in 1..10) { if (i == 5) {
    break
}
// Sale del bucle cuando i es 5 } if (i % 2 == 0) { continue // Salta la iteración cuando i es par }
// println("Número impar: $i") }

// Estos son ejemplos básicos de cómo utilizar estructuras repetitivas en Kotlin.
// Puedes combinar estas estructuras con condiciones y lógica adicional para lograr comportamientos
// más complejos en tu programa.


/* ESTRUCTURAS CONTROL DE FLUJO */
/*
   ¡Por supuesto! Aquí tienes un ejemplo de control de flujo en Kotlin que utiliza una estructura
   condicional (if) y una estructura repetitiva (while) para simular un juego de adivinanza:
 */

    fun main() {
        val numeroSecreto = (1..100).random()
        var intentos = 0
        var adivinanza: Int

        println("¡Bienvenido al juego de adivinanza!")
        println("Intenta adivinar el número secreto entre 1 y 100.")

        while (true) {
            print("Ingresa tu suposición: ")
            adivinanza = readLine()!!.toInt()
            intentos++

            if (adivinanza == numeroSecreto) {
                println("¡Felicidades! Adivinaste el número en $intentos intentos.")
                break
            } else if (adivinanza < numeroSecreto) {
                println("El número es mayor.")
            } else {
                println("El número es menor.")
            }
        }
    }

/*
    En este ejemplo, el programa genera un número secreto aleatorio entre 1 y 100. Luego, utiliza
    un bucle while que se ejecuta hasta que el jugador adivine correctamente el número.
    Dentro del bucle, se lee la suposición del jugador y se compara con el número secreto
    utilizando la estructura condicional if. Si el número adivinado es igual al número secreto,
    se muestra un mensaje de felicitaciones y se muestra la cantidad de intentos realizados.
    Si no, se proporciona una pista indicando si el número es mayor o menor.

    Este es solo un ejemplo de cómo se puede implementar el control de flujo en Kotlin.
    Puedes ajustar y expandir el programa según tus necesidades y creatividad.
 */