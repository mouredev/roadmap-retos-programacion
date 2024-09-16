/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
    
// ------------------------  Operaciones  ------------------------
    
// Operaciones Aritmeticas
    
val suma = 5 + 2
println(suma)
    
val resta = 8 - 5
println(resta)
    
val multiplicacion = 3 * 5
println(multiplicacion)
    
val division = 10 / 2
println(division)
    
val modulo = 10 % 3
println(modulo)
    
    
// Operaciones Logicas
    
println("${(12 + 5 == 10) && (5 + 12 == 17)}")   // operacion AND se utiliza &&
println("${(12 + 5 == 10) || (5 + 12 == 17)}")   // operacion OR se utiliza ||
println("${!(12 + 5 == 10)}")   // operacion NOT se utiliza !
    
    
// Operaciones de comparacion
    
val a = 7
val b = 3

println("igualdad: ${a == b}")
println("desigualdad: ${a != b}")
println("mayor que: ${a > b}")
println("menor que: ${a < b}")
println("mayor o igual que: ${a >= b}")
println("menor o iguial que: ${a <= b}")
    
    
// Operaciones de asignacion
    
var c = 8   // asignacion numero a variable
println(c)
    
c += 5   // suma y asignacion
println(c)
    
c ++   // suma 1 a la variable
println(c)
    
c -= 6   // resta y asignacion
println(c)
    
c --   // resta 1 a la variable
println(c)
    
c *= 3   // multiplica y asignacion
println(c)
    
c /= 2   // division y asignacion
println(c)
    
    
// Operaciones de pertenencia
    
val ciudades = listOf("España", "Italia", "Alemania", "Francia", "Bulgaria")
    
println("Alemania" in ciudades)
println("Noruega" !in ciudades)
    
    
// ------------------------ Estructura de control ------------------------
    
// Condicionales
    
val edad = 36
    
if (edad >= 18){
    println("eres mayor de edad")
}else if (edad > 0){
    println("eres menor de edad")    
}else {
    println("no es una edad valida")
}
    
    
// ------------------------  Iteraciones  ------------------------
    
// for
    
val nombre = listOf("Carlos", "David", "Sarah", "Lucia", "Cristian")
    
for (n in nombre){
    println("me llamo $n")
}
    
for (i in 1..10){
    println(i)
}
    
    
// while
      
var contador = 1
    
while (contador <= 5){
    println("contado = $contador")
    contador ++
}
    
    
// do while
    
contador = 1
    
do {
    println("contado = $contador")
    contador ++
} while (contador <= 5)
    
    
// when
    
var diaDeLaSemana = 5
    
when (diaDeLaSemana){
    1 -> println("Lunes")
    2 -> println("Martes")
    3 -> println("Miercoles")
    4 -> println("Jueves")
    5 -> println("Viernes")
    6 -> println("Sabado")
    7 -> println("Domingo")               
}
    
// ------------------------  Ejercicio Extra  ------------------------
    
for (i in 10..55){
    if (i % 2 == 0 && i != 16 && i % 3 != 0 ){
        println(i)
    }        
}