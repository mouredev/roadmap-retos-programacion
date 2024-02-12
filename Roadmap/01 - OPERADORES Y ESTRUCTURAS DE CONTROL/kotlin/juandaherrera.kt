/*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     *
     * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

fun main() {
    for (number in 10..55) {
        if (number % 2 == 0 && number != 16 && number % 3 != 0) {
            println(number)
        }
    }
}
