// main: es el paquete principal del programa
package main

// area de importación de paquetes
import (
	"fmt" /* Paquete Format: usado para formatear texto e imprimirlo en consola.*/)

// Sitio oficial del lenguaje Go(Golang): https://go.dev/
// Sitio oficial de ejemplos de uso del lenguaje: https://gobyexample.com/
// Sitio oficial de codigo en linea: https://go.dev/play/

/*
Comentarios de una línea(en go si se usan correctamente podemos generar la documentación a partir de estos)
Para que la documentación se genere a partir de los comentarios debemos comentar de manera acertiva.
Siempre se comienza por el nombre de la variable, constante, funcion, etc...

// firstName Variable que contiene el nombre del usuario.
var firstName string = "Miguel"


Los comentarios en bloque en go se usan sobre todo para bloques de código que no necesitemos usar en el momento
pero estos bloques de código no deben quedar ahí como comentarios sin usar, esto haría el código muy sucio.
*/
// main Es la función principal del programa
func main() {

	// firstName declaración de variables simples
	var firstName string

	// Asignación del valor de la variable
	firstName = "Miguel"

	// lastName declaración y asignación de variables simples en la misma línea.
	var lastName string = "Portillo"

	// correo delcaración y asignacion de una variable usando la asignación de variable corta(go infiere el tipo de dato)
	email := "miguelportillo@gmail.com"

	// declaracion de variables multiples y con variedad de tipos de datos, (Age es Int y birthDate es un String)
	var age, birthDate = 31, "13 - 10 - 1993"

	/*
		A diferencia de las variables que se puede declarar y asignar su valor con solo una asignación corta (:=)
		las cosntantes se declaran con la palabra reservada const
	*/
	// isDeveloper declaración de constantes simple
	const isDeveloper = true

	/*
		Aquí se usa iota para asignar un entero a cada més, que va desde 1 a 12. Iota es un metodo para asignar rapidamente
		el valor a las constantes si se quieren usar números.
	*/
	// declaración de constantes en bloque
	const (
		enero      = iota + 1 // 1
		febrero               // 2
		marzo                 // 3
		abril                 // 4
		mayo                  // 5
		junio                 // 6
		julio                 // 7
		agosto                // 8
		septiembre            // 9
		octubre               // 10
		noviembre             // 11
		diciembre             // 12
	)

	// Tipos de datos en go.

	// Booleanos(Valores 1 y 0, o Verdadero y falso)
	var a bool = false

	// Los tipos de datos "UINT" aunque son enteros solo almacenan valores positivos.

	// u8 Variable uint8 Almacena desde 0 a 255
	var u8 uint8 = 255

	// u16 Variable uint16 Alamcane de 0 a 65535
	var u16 uint16 = 65535

	// u32 Almacena desde 0 a 4294967295
	var u32 uint32 = 4294967295

	// u64 Alamacena de 0 a 18446744073709551615
	var u64 uint64 = 18446744073709551615

	// u Se ajusta a los bits del sistema operativo, es decir que si es de 32Bits(Raro hoy dia) se ajusta a este, lo mismo para 64bits.
	var u uint = 18446744073709551615

	// Los tipos Int permiten valores tanto negativos coomo positivos.

	// i8 Almacena desde -128 hasta 127
	var i8 int8 = -128

	// i16 Alamacena desde -32768 hasta 32767
	var i16 int16 = -32768

	// i32 Alamacena desde -2147483648 hasta 2147483647
	var i32 int32 = -2147483648

	// i64 Alamacena desde -9223372036854775807  hasta 9223372036854775807
	var i64 int64 = -9223372036854775808

	// i Alamacena desde - hasta
	var i int = -9223372036854775808

	/*
		Almacenar un valor mayor es overflow(Desbordamiento).
		Usar un tipo int que toma como referencia los bits del sistema operativo para asignar el valor: 64bits es igual a int64. Esto no es recomendable sobre todo si es una variable que almacena por ejemplo la edad, para eso el uint8 es más que suficiente.
	*/

	// Imprimiendo valores - Nota: Las variable declaradas deben ser usadas, en GO no se puede y no se debe declarar sin usar.
	/*
		La unica forma de declararlas es con el ID Blank que se hace con un guión bajo.
		se usa cuando queres tener la variable sin comentarla porque se usara más tarde,
		pero solo las variables que estamos seguros de usar.
	*/
	// Alias de los tipos de datos.
	// b byte:es alias para uint8 (0 a 255)
	var b byte = 99

	// Nota: para obtener valores unicode los datos van entre comillas simples.
	// r rune: alias para int32 o unicode
	var r rune = -214748364
	var r2 rune = 'a' // valor unicode = 97

	// f32 Float32 es una variable de números decimales pero este solo deja un digito luego de la coma.
	var f32 float32 = 990.3

	// f64 Float64 al contrario qe float32 si toma multiples digitos luego de la coma.
	var f64 float64 = 990.325

	var chain string = "¡Hola!"

	// impresión de la primera variable nombre.
	fmt.Println("nombre :", firstName, "Apellido: ", lastName, "Edad: ", age, "Correo: ", email, "Nacimineto: ", birthDate)

	// Impriendo valores de algunas constantes.
	fmt.Println("enero: ", enero, "agosto: ", agosto, "diciembre: ", diciembre)

	/*
	   Imprimiendo con Printf se pueden ver los placeholders(Verbos) de las variables y
	   datos impresos(incluso su dirección en memoria.)
	   estas impresiones se pueden y deben simplificar en una funcion para que las imprima una a una,
	   pero no es para este primer objetivo de la ruta.
	*/
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", a, a)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", u8, u8)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", u16, u16)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", u32, u32)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", u64, u64)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", u, u)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", i8, i8)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", i16, i16)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", i32, i32)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", i64, i64)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", i, i)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", r, r)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", r2, r2)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", b, b)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", f32, f32)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %v\n", f64, f64)
	fmt.Printf("Tipo de dato: %T, Valor alamacenado: %q\n", chain, chain)

	fmt.Println("Hola, Go.")

}
