package main

import "fmt"

//comentario de una sola linea sitio oficial de GO https://go.dev/

/*
Comentario de varias lineas.
Go es un lenguaje fuertemente tipado creado por Google en el año 2009,
En GO los comentarios sirven como documentación
*/

//Constante nombre
const name = "Amador Quispe"

func sumTwoNumber(a, b int) int {
	return a + b
}

func main() {
	//Declaración de variable corta
	job := "Desarrollador"
	//Declaración de variable Larga, sin inicializar
	var job1 string
	job1 = "Analista"
	//Declaración de variable larga, con inicialización
	var job2 string = "Consultor"
	//Asignación multiple
	j, k, l := "dev", 2.05, 15

	fmt.Println(name)
	fmt.Println("Trabajos")
	fmt.Println(job, job1, job2)
	fmt.Println(j, k, l)

	//Tipos de variables en GO

	//======== TIPOS PRIMITIVOS ===========//
	//Tipos booleanos
	//---------------------
	var varBoolean bool = true

	//Tipos numéricos
	//---------------------
	//Tipos numéricos enteros sin signo

	//uint8  => 8-bit integers (0 to 255)
	var varUnit8 uint8 = 255
	//uint16 => 16-bit integers (0 to 65535)
	var varUint16 uint16 = 1500
	//uint32 => 32-bit integers (0 to 4294967295)
	var varUint32 uint32 = 50000
	//uint64 => 64-bit integers (0 to 18446744073709551615)
	var varUint64 uint64 = 100000000
	//uint => either 32 or 64 bits
	var varUint uint = 1500000

	//Tipos numéricos enteros con signo

	//int8 => 8-bit integers (-128 to 127)
	var varInt8 int8 = 120
	//int16 => 16-bit integers (-32768 to 32767)
	var varInt16 int16 = 32000
	//int32 => 32-bit integers (-2147483648 to 2147483647)
	var varInt32 int32 = 21212212
	//int64 => 64-bit integers (-9223372036854775808 to 9223372036854775807)
	var varInt64 int64 = 1000000000
	//int => same size as uint
	var varInt int = 1111111112212
	//uintptr => suficientemente largo para almacenar bit no interpretados de un puntero
	var varUintptr uintptr = 12312323232334343444

	//Tipos numéricos con punto flotante

	//float32 => IEEE-754 32-bit floating-point numbers
	var varFloat32 float32 = 2500.5
	//float64 => IEEE-754 64-bit floating-point numbers
	var varFloat64 float64 = 2544412342.3434342432

	//Tipos numéricos complejos

	// complex64 complex numbers with float32 real and imaginary parts
	var varComplex64 complex64 = 2i
	// complex128 complex numbers with float32 real and imaginary parts
	var varComplex128 complex128 = 1e32i

	//Tipos alias, el tipo uint8 y int32 tienen alias
	var varAliasByte byte = 123
	var varAliasRune rune = 12355

	//Tipos cadena
	//---------------------
	var varString string = "Hola dev"

	//======== TIPOS COMPUESTOS Y ESTRUCTURADOS ===========//

	//Tipos array (matrices)
	//La capacidad de una matriz se define en el momento de su creación
	//---------------------

	var varArray [4]int = [4]int{1, 2, 3, 5}

	//Tipos slice
	//Los slices pueden verse como arreglos de longitud dinámica
	var varSlice []int = []int{1, 2, 3, 4, 5, 6}
	varSlice = append(varSlice, 7)

	//Tipos map
	//Tipo de dato que representa una colección de pares clave-valor
	var varMap map[string]string = map[string]string{"clave1": "valor2", "clave2": "valor2"}

	//Tipo Struct
	//un conjunto de campos con diferentes tipos de datos
	type Person struct {
		name string
		age  int
	}
	var person1 = Person{name: "Amador", age: 31}

	//======== TIPOS DE REFERENCIA ===========//
	//Tipo pointer
	//Representa la dirección de memoria de una variable
	var age int = 28
	var pointerAge *int = &age

	//Tipo función
	//Representa una función
	var funcSum = sumTwoNumber
	result := funcSum(5, 2)

	//Tipo interface
	//Define un conjunto de métodos que una estructura debe implementar
	type Figure interface {
		Area() float64
	}

	fmt.Println(
		varBoolean,
		varUnit8,
		varUint16,
		varUint32,
		varUint64,
		varUint,
		varInt8,
		varInt16,
		varInt32,
		varInt64,
		varInt,
		varUintptr,
		varFloat32,
		varFloat64,
		varComplex64,
		varComplex128,
		varAliasByte,
		varAliasRune,
		varString,
		varArray,
		varSlice,
		varMap,
		person1,
		pointerAge,
		result,
	)

	fmt.Print("Hola, GO!")
}
