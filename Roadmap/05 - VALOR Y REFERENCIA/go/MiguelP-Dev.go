package main

import "fmt"

// Variable Global
var number = 10

// valArray Arreglo de enteros.
var valArray = [5]int{1, 2, 3, 4, 5}

func main() {

	// Asignación por valor
	var numberByValue = number
	numberByValue = 45
	fmt.Printf("Variable Copia: %d Tipo: %T Direccion en Memoria: %v\n", numberByValue, numberByValue, &numberByValue)
	number = 1234
	fmt.Printf("imprimimos la variable original: %v Dirección en Memoria: %v\n", number, &number)

	// Asignación por Referencia (En Golang esto se hace con punteros, map's y slices que son en golang un puntero a un array subyacente.)
	var numberByReference = &number
	fmt.Printf("Valor por Referencia: %v  Direccion en Memoria: %v Tipo: %T\n", *numberByReference, numberByReference, numberByReference)

	// Operando en un arreglo accediendo y modificando su valor
	fmt.Println("Arreglo principal: ", valArray)
	valArray[0] = 10
	fmt.Println("Arreglo Modificado: ", valArray)

	// Slice sobre el Arraglo de enteros(Asignación por Referencia)
	var valSlice []int
	valSlice = valArray[0:2]
	fmt.Println("Slice :", valSlice)
	valSlice = append(valSlice[:], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println("Slice :", valSlice)

	// Función con asignación por valor
	byVal(number)
	fmt.Println("Variable Original: ", number)

	byRef(&number)
	fmt.Println("Variable Original: ", number)

	changeByValue(value, value2)
	changeByReference(&value, &value2)

}

func byVal(x int) {
	x = 1000
	fmt.Printf("Funcion con declaración por Valor: %v\n", x)
}

func byRef(x *int) {
	*x = 5000
	fmt.Printf("Función con asignación por referencia: %d Tipo: %T\n", *x, x)
}

var value = 123
var value2 = 22

func changeByValue(param, param2 int) {
	fmt.Println("Valores originales :", param, param2)
	param, param2 = param2, param
	fmt.Println("Valores intercambiados: ", param, param2)
}

func changeByReference(param, param2 *int) {
	fmt.Printf("Valores originales: %v %v\n", *param, *param2)
	param, param2 = param2, param
	fmt.Printf("Valores intercambiados: %v %v\n", *param, *param2)
}
