package main

import "fmt"

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

func main() {

	//  aritmeticos
	fmt.Println("*** Operadores Aritmeticas ***")
	fmt.Printf("suma %d + %d = %d \n", 4, 9, 4+9)
	fmt.Printf("resta %d - %d = %d \n", 4, 9, 4-9)
	fmt.Printf("multiplicacion %d * %d = %d \n", 4, 9, 4*9)
	fmt.Printf("division %d / %d = %d \n", 9, 4, 9/4)
	fmt.Printf("division %d / %d = %.3f \n", 9, 4, 9/4.) // div siempre es entera
	fmt.Printf("MOdulo %d %% %d = %d \n", 9, 4, 9%4)

	//  comparacion
	fmt.Println("*** Operadores comparacion ***")
	fmt.Printf("igual que %d == %d , %t \n", 4, 9, 4 == 9)
	fmt.Printf("mayor que %d > %d , %t \n", 4, 9, 4 > 9)
	fmt.Printf("menor que %d < %d , %t \n", 4, 9, 4 < 9)
	fmt.Printf("desiguales  %d != %d , %t \n", 4, 9, 4 != 9)

	//  logicos
	fmt.Println("*** Operadores logicos ***")
	fmt.Println(" AND (4 >= 2) && (9 <= 19)", (4 >= 2) && (9 <= 19))
	fmt.Println(" OR (4 <= 2) && (9 <= 19)", (4 <= 2) || (9 <= 19))
	fmt.Println(" NOT (4 <=2)", !(4 <= 2))

	// asignacion
	fmt.Println("*** Operadores asignacion ***")
	a := 1
	fmt.Println(" inicializacion  a:= 1", a)
	a = 2
	fmt.Println(" asignacion cambio valor a = 1", a)
	a += 3
	fmt.Println(" suma  y asignacion a += 3", a)
	fmt.Println(" resta  y asignacion a -= 1", a)
	fmt.Println(" multip y asignacion a *= 1", a)
	fmt.Println(" division  y asignacion a /= 1", a)
	a++
	fmt.Println(" incremento a++", a)
	a--
	fmt.Println(" decremento a--", a)

	// operadores con bit
	fmt.Println("*** Operadores con bits ***")
	var s, d uint8 = 10, 3
	fmt.Println(" and s & d ", s&d)
	fmt.Println(" or s | d ", s|d)
	fmt.Println(" xor s ^ d ", s^d)
	fmt.Println(" izquierda  s << 2 ", s<<2)
	fmt.Println(" derecha  s >> 2 ", s>>2)

	// condicionales
	fmt.Println("*** Extructuras de control condicionales ***")

	if s > d {
		fmt.Printf(" %d es mayor que %d \n", s, d)
	} else if s < d {
		fmt.Printf("%d es menor que %d \n", s, d)
	} else {
		fmt.Printf("%d y %d son iguales \n", s, d)
	}

	switch s {
	case 10:
		fmt.Println("s es igual a 10")
	case 5:
		fmt.Println("n es igual a 5")
	default:
		fmt.Println("n no es igual a 10 ni a 5")
	}

	fmt.Println("*** EXTRA ***")

	for i := 10; i < 56; i++ {
		if i%2 == 0 && i != 16 && i%3 != 0 {
			fmt.Println((i))
		}

	}

}
