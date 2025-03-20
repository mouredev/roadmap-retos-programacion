// # #01 OPERADORES Y ESTRUCTURAS DE CONTROL
// > #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
//  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
//  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
//  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
//  *   que representen todos los tipos de estructuras de control que existan
//  *   en tu lenguaje:
//  *   Condicionales, iterativas, excepciones...
//  * - Debes hacer print por consola del resultado de todos los ejemplos.
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//  *
//  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import "fmt"

// variables universales
var a int = 5
var b int = 10

func aritmeticos() {
	// Operadores aritméticos
	suma := a + b
	resta := a - b
	multiplicacion := a * b
	division := a / b
	modulo := a % b
	fmt.Printf("La suma de %d + %d es: %d \n", a, b, suma)
	fmt.Printf("La resta de %d - %d es: %d \n", a, b, resta)
	fmt.Printf("La multiplicación de %d * %d es: %d \n", a, b, multiplicacion)
	fmt.Printf("El módulo de %d %% %d es: %d \n", a, b, modulo)
	fmt.Printf("La división de %d / %d es: %d \n", a, b, division)
}

func logicos() {
	// Operadores lógicos
	fmt.Printf("(3 < 5) && (5 > 3) es: %t \n", 3 < 5 && 5 > 3)
	fmt.Printf("(3 < 5) || (5 > 3) es: %t \n", 3 < 5 || 2 > 3)
	fmt.Printf("(3 != 5) es: %t \n", 3 != 5)
	fmt.Printf("(3 == 5) es: %t \n", 5 == 5)
}

func operadoresAsignacion() {
	// Operadores de asignación
	a += b
	fmt.Printf("a += b es: %d \n", a) // 15
	a -= b
	fmt.Printf("a -= b es: %d \n", a) // 5
	a *= b
	fmt.Printf("a *= b es: %d \n", a) // 50
	a /= b
	fmt.Printf("a /= b es: %d \n", a) // 5
	a %= b
	fmt.Printf("a %%= b es: %d \n", a) // 5

}
func condicionales() {
	// Condicionales if
	if a > b {
		fmt.Printf("%d es mayor que %d \n", a, b)
	} else if a == b {
		fmt.Printf("%d es igual a %d \n", a, b)
	} else {
		fmt.Printf("%d es menor que %d \n", a, b)
	}

	// Condicionales switch
	switch a == b {
	case true:
		fmt.Println("a es igual a b")
	case false:
		fmt.Println("a no es igual a b")
	}
}

func iterativas() {
	// Iterativas

	// for con inicialización y condición
	for i := 0; i < 10; i++ {
		fmt.Printf("Iteracion %d \n", i)
	}
	// for con condición
	i := 0
	for i < 10 {
		fmt.Printf("Iteración %d \n", i)
		i++
	}
	// for infinito
	i = 0
	for {
		fmt.Printf("Iteración %d \n", i)
		i++
		if i == 10 {
			break
		}
	}
}

// actividad extra
func funcionExtra() {
	for i := 10; i <= 55; i++ {
		if i%2 == 0 && i != 16 && i%3 != 0 {
			fmt.Printf("El numero %d es una salida del for \n", i)
		}
	}
}
func main() {
	aritmeticos()
	logicos()
	operadoresAsignacion()
	condicionales()
	iterativas()
	funcionExtra()
}
