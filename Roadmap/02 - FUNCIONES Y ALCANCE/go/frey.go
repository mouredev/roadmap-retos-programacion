// # #02 FUNCIONES Y ALCANCE
// > #### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

// ## Ejercicio

// ```
// /*
//  * EJERCICIO:
//  * - Crea ejemplos de funciones básicas que representen las diferentes
//  *   posibilidades del lenguaje:
//  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
//  * - Comprueba si puedes crear funciones dentro de funciones.
//  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
//  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
//  * - Debes hacer print por consola del resultado de todos los ejemplos.
//  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
//  *
//  * DIFICULTAD EXTRA (opcional):
//  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
//  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
//  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
//  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
//  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
//  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
//  *
//  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
//  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
//  */
// ```
// #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

package main

import "fmt"

// Variables universales
var nombre string = "frey"
var apellido string = "fonseca"
var ciudad string = "santiago"

// funcion con parametro
func saludar(nombre string) {
	fmt.Println("esta funcion recibe un parametro string el cual es:", nombre)
}

// funcion con varios parametros
func variosParametros(a, b, c string) string {
	resultado := fmt.Sprintf("hola mi nombre es %s %s y vivo en %s", a, b, c)
	fmt.Println(resultado)
	return resultado

}

// Uso de funciones estándar del lenguaje
func usarFuncionesNativas() {
	longitud := len("Hola, mundo")
	fmt.Println("Longitud de la cadena:", longitud)
}

// Ejercicio extra

func problemaFizzBuzz(string1, string2 string) int {
	contador := 0
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println(string1 + string2)
		} else if i%3 == 0 {
			fmt.Println(string1)
		} else if i%5 == 0 {
			fmt.Println(string2)
		} else {
			fmt.Println(i)
			contador++
		}
	}
	return contador
}

func main() {
	saludar(nombre)
	variosParametros(nombre, apellido, ciudad)
	usarFuncionesNativas()
	contador := problemaFizzBuzz("fizz", "buzz")
	fmt.Println("El contador es:", contador)
}
