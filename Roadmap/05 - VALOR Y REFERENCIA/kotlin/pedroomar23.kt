/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

 // Asignacion de variables por valor 
 val x = 5 // El valor de variable x mantiene su valor 
 val y = x // El valor de la variable y cambia al valor de la variable x 

 prinln(x) // Imprimir en la consola el valor de la variable x 
 println(y) // Imprimir en la consola el valor de la variables y

 // Asignacion de valores por referencia 
 data class Person(nombre: String) 

 val nombre1 = Person("Carlos") 
 val nombre2 = nombre1

 // Funcion de asignacion de variables por valor 
 fun sum(a: Int) {
    println(a + 2) // Esto modifica una copia del numero y aumenta el valor en 2
 }

 fun restar(b: Int) {
    println(b - 2) // Esto modifica una copia del numero y resta el valor en 2
 }

 // Funcion de asignacion de valores por referencia 
 fun modify(person: Person) {
    person.nombre = "Juan"
 }

 val persons = Person("Oscar")
 modify(person)
 println(person.name) // En esta ocacion imprimira "Oscar" porque se ha modificado el objeto referenciado en person


