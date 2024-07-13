package main

import "fmt"

func main() {
	//variableAssignment()
	var x int = 45
	fnByValue(x)
	fmt.Println("Valor de 'x' luego pasar por la función fnByValue", x)
	fnByReference(&x)
	fmt.Println("Valor de 'x' luego pasar por la función fnByReference", x)
	var slice []int = []int{1, 2, 3}
	modifySlice(slice)
	fmt.Println("Slice luego de pasar por la función 'modifySlice'", slice)

	//Paso por valor
	fmt.Println("---------------------------------------")
	a, b := 5, 6
	a1, b1 := swapByValue(a, b)
	fmt.Printf("Valor original a=%d y b=%d\n", a, b)
	fmt.Printf("Valor intercambiado a1=%d y b1=%d\n", a1, b1)
	//Paso por referencia
	fmt.Println("---------------------------------------")
	y, z := 10, 20
	y1, z1 := swapByRef(&y, &z)
	fmt.Printf("Valor original y=%d y z=%d\n", y, z)
	fmt.Printf("Valor intercambiado y1=%d y z1=%d\n", y1, z1)

}

func fnByValue(x int) {
	x += 100 //Esto no modifica a 'x' ya que recibe por valor
}
func fnByReference(x *int) {
	*x += 100 //Esto modifica a 'x' ya que recibe por referencia (apunta a la misma dirección de memoria)
}
func modifySlice(slice []int) {
	//Los slice por defecto se pasan por referencia
	for i, v := range slice {
		slice[i] = v * 2
	}
}
func swapByValue(a, b int) (int, int) {
	a, b = b, a
	return a, b
}

func swapByRef(a, b *int) (int, int) {
	*a, *b = *b, *a
	return *a, *b
}

func VariableAssignment() {
	//POR VALOR
	//Todo los tipos básicos se asignan  por valor
	var varInt int = 35
	var varInt1 int = varInt
	varInt1 = 50
	fmt.Printf("'varInt'= %d, 'varInt1=' %d \n", varInt, varInt1)

	var varUint uint = 1500000
	var varUint1 uint = varUint
	varUint1 = 1500
	fmt.Printf("'varUint'= %d, 'varUint1'= %d \n", varUint, varUint1)

	var varFloat32 float32 = 2500.5
	var varFloat32_1 float32 = varFloat32
	varFloat32_1 = 1500.23
	fmt.Printf("'varFloat32'= %f, 'varFloat32_1'= %f \n", varFloat32, varFloat32_1)

	var varString string = "Hola dev"
	var varString1 string = varString
	varString1 = "amsoft.dev"
	fmt.Printf("'varString'= %s, 'varString_1'= %s \n", varString, varString1)

	var varComplex64 complex64 = 2i
	var varComplex64_1 complex64 = varComplex64
	varComplex64_1 = 5i
	fmt.Printf("'varComplex64'= %v, 'varComplex64_1'= %v \n", varComplex64, varComplex64_1)

	var varRune rune = 'A'
	var varRune1 rune = varRune
	varRune1 = 'B'
	fmt.Printf("'varRune'= %v, 'varRune_1'= %v \n", varRune, varRune1)

	var array [3]int = [3]int{1, 2, 3}
	var array1 [3]int = array
	array1[0] = 20
	fmt.Println(array)
	fmt.Println(array1)

	//POR REFERENCIA, tipos de datos por referencia
	//slices
	fmt.Println("TIPOS POR REFERENCIA")
	fmt.Println("--------------------")
	var slice []int = []int{1, 2, 3}
	var slice1 []int = slice
	slice1[0] = 20
	fmt.Println(slice)
	fmt.Println(slice)

	//mapas
	var varMap map[string]string = map[string]string{"clave1": "valor1", "clave2": "valor2"}
	var varMap1 map[string]string = varMap
	varMap1["clave1"] = "valor 1 modificado"
	fmt.Println(varMap)
	fmt.Println(varMap1)

	//Punteros
	var var1 uint = 3
	var var2 *uint = &var1
	*var2 = 15
	println(var1, *var2) //var1 y var2 apuntan a la misma dirección de memoria
}
