/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

package main

import "fmt"

func main() {
    fmt.Println("### OPERADORES ###")

    // Operadores Aritméticos
    fmt.Println("\n--- Aritméticos ---")
    a, b := 10, 3
    fmt.Printf("Suma: 10 + 3 = %d\n", a+b)
    fmt.Printf("Resta: 10 - 3 = %d\n", a-b)
    fmt.Printf("Multiplicación: 10 * 3 = %d\n", a*b)
    fmt.Printf("División: 10 / 3 = %d\n", a/b)
    fmt.Printf("Módulo: 10 %% 3 = %d\n", a%b)

    // Operadores Lógicos
    fmt.Println("\n--- Lógicos ---")
    fmt.Printf("AND (true && false): %t\n", true && false)
    fmt.Printf("OR (true || false): %t\n", true || false)
    fmt.Printf("NOT (!true): %t\n", !true)

    // Operadores de Comparación
    fmt.Println("\n--- Comparación ---")
    fmt.Printf("Igualdad (10 == 3): %t\n", 10 == 3)
    fmt.Printf("Desigualdad (10 != 3): %t\n", 10 != 3)

    // Operadores de Asignación
    fmt.Println("\n--- Asignación ---")
    x := 5
    x += 2
    fmt.Printf("Suma y asignación: x += 2 -> x = %d\n", x)

    // Operadores de Bits
    fmt.Println("\n--- Bits ---")
    p, q := 10, 3 // 1010, 0011
    fmt.Printf("AND a nivel de bits (10 & 3): %d\n", p&q)
    fmt.Printf("OR a nivel de bits (10 | 3): %d\n", p|q)

    /*
     * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
     *   que representen todos los tipos de estructuras de control que existan
     *   en tu lenguaje:
     *   Condicionales, iterativas, excepciones...
     */

    fmt.Println("\n### ESTRUCTURAS DE CONTROL ###")

    // Condicionales
    fmt.Println("\n--- Condicionales (if, else) ---")
    edad := 18
    if edad < 18 {
        fmt.Println("Eres menor de edad.")
    } else {
        fmt.Println("Eres mayor de edad.")
    }

    // Iterativas (Go solo tiene `for`)
    fmt.Println("\n--- Iterativas (for) ---")
    for i := 1; i <= 3; i++ {
        fmt.Println(i)
    }

    fmt.Println("\n--- Iterativas (for como while) ---")
    contador := 3
    for contador > 0 {
        fmt.Println(contador)
        contador--
    }

    // Manejo de errores (defer, panic, recover)
    fmt.Println("\n--- Manejo de errores ---")
    func() {
        defer func() {
            if r := recover(); r != nil {
                fmt.Printf("Se recuperó de un pánico: %v\n", r)
            }
        }()
        panic("Este es un pánico de ejemplo")
    }()
    fmt.Println("El programa continúa después del pánico.")

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que imprima por consola todos los números comprendidos
     * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
     */

    fmt.Println("\n### DIFICULTAD EXTRA ###")
    for numero := 10; numero <= 55; numero++ {
        if numero%2 == 0 && numero != 16 && numero%3 != 0 {
            fmt.Println(numero)
        }
    }
}
