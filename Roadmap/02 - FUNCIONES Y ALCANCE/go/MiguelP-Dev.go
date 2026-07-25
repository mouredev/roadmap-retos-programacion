package main

import (
	"fmt"
	"strings"
)

func main() {
	saludoMundo()
	fmt.Println("Suma: ", suma(2, 2))
	holaGophers("Miguel", "Portillo")
	valor := "Minuscula"
	toUpper(&valor)
	fmt.Println(valor)

	upper, lower := convert("MiGuEl")
	fmt.Println("Mayúsculas", upper, "Minúsculas", lower)

	upper2, lower2 := convert2("PoRtIlLo")
	fmt.Println("Mayúsculas", upper2, "Minúsculas", lower2)

	// nums Slice de números.
	nums := []int{1, 2, 40, 66, 34, 33, 663}
	filter(nums, func(num int) bool {
		return num > 20
	})

	fmt.Println("La suma es:", sum(1, 2, 34, 5, 6, 77, 65, 44, 44))
	fmt.Println("La suma del slice es:", sum(nums...))

	result := super(na)(nb)
	fmt.Println(result)

	fmt.Println(fizzBuzz("fizz", "buzz"))
}

/*
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 */

/*
En Golang el nombramiento de las funciones se hace en base a la convención del leguaje mismo:
Las funciones se nombran comenzando por minusculas para que sean propias solo del paquete,
pero si por el contrario son funciones que se van a exportar fuera del paquete, estas comienzan por mayúsculas,
como por ejemplos las funciones del paquete Format(fmt).
*/

// holaMundo Función simple (Sin parametros ni retorno)
func saludoMundo() {
	fmt.Println("Hola mundo")
}

// holaGophers Funcion de saludo con paramentros.
func holaGophers(firstname string, lastname string) {
	fmt.Println("Hola Gopher ", firstname, lastname)
}

// Se pueden usar las funciones para manipular datos pero esto solo haciendolo mediante referencias:
// toUpper función con parametros por valor y referencia.
func toUpper(text *string) {
	*text = strings.ToUpper(*text)
}

// suma Función que recibe enteros y devuelve enteros,
// La lista de parámetros define los datos que acepta una funcion y los tipos de datos,
// Los parámetros son un tipo de variable especial usada para pasar datos a una función.
func suma(a, b int) int {
	return a + b
}

// Las Funciones pueden devolver multiples valores; estos deben ir entre parentesis:
func convert(text string) (string, string) {
	upper := strings.ToUpper(text)
	lower := strings.ToLower(text)
	return upper, lower
}

func convert2(text string) (upper string, lower string) {
	upper = strings.ToUpper(text)
	lower = strings.ToLower(text)
	return upper, lower
}

// Nota: Al igual que se nombran y tipan los paramentros, también se puede hacer con los retornos
// Aunque esto es solo recomendable con las funciones muy pequeñas y que no crecerán.

/*
Funciones que reciben y retornan funciones.
Las funciones en golang también son un tipo de dato, por lo que puedo pasarlas a otras funciones como parametros
y recibirlas como retorno
*/

// filter: Esta función recibe como parametros: nums y la función callback, que tiene como parametro un entero
// y devuelve un booleano, la funcion filter tiene como retorno un slice de enteros que seŕia el
// resultrado de filtrar los valores del Slice en main, llamado nums.

func filter(nums []int, callback func(int) bool) []int {
	result := make([]int, 0, len(nums))

	for _, num := range nums {
		if callback(num) {
			result = append(result, num)
		}
	}
	return result
}

// sum Funcion variádicas: estas funciones se usan sobre todo cuando no estasmos seguros de la cantidad
// de parametros que pasaremos. Por ejemplo algunos de los casos de uso más comúnes de estas funciones:
// Concatenación de cadenas como los paquetes fmt.Sprintf y strings.Join.
// Procesamiento de matrices y Slices, registro de manejos de errores como la funciomn log.Printf y
// funciones auxiliares utilisadas en APIS y Bibliotecas.

func sum(nums ...int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

// super: es una función que recibe un parametro A, retorna una función que recibe un entero y retorna un entero.
func super(a int) func(int) int {
	return func(b int) int {
		return a + b
	}
}

// nota: las variables globales se declaran fuera de la función main.
// Estas variables no se pueden declarar usando el operador de variable corta(:=).
var na = 23
var nb int = 12

// Extra
func fizzBuzz(word1, word2 string) int {
	count := 0 // Variable local (solo existe dentro de la función fizzBuzz)
	for i := 1; i < 101; i++ {
		if i%15 == 0 {
			fmt.Println(word1 + word2)
		} else if i%3 == 0 {
			fmt.Println(word1)
		} else if i%5 == 0 {
			fmt.Println(word2)
		} else {
			fmt.Println(i)
			count += 1
		}
	}
	return count
}
