package main

import "fmt"

func tipos_datos(){
	var edad int = 23
	var gobernador = "nombre de alguien"
	ciudad := "Moquegua"  //solo funciona en funciones

	//tipos basicos
	var entero0 int =-10  //tambien se puede usar int8, int16, int32 e int64
	var entero1 int8 =-10
	var entero2 int16 =-10
	var entero3 int32 =-10
	var entero4 int64 =-10
	//int8, int16, int32 e int64; estos se usan segun cuanta memoria quieres que ese dato ocupe
	
	var natural0 uint= 10
	var natural1 uint8= 10
	var natural2 uint16= 10
	var natural3 uint32= 10
	var natural4 uint64= 10  //uint se usa solo para valores positivos
	//uint8 (= byte), uint16, uint32, uint64; otorgan un tamaño fijo en memoria
	
	var decimal1 float32= 3.1416
	var decimal2 float64= 3.1416

	var activo bool=true
	var negativo bool=false

	var texto string ="textaso"

	var letra rune ='G' //solo una variable de 32 bits

	var b byte = 'A'  //es 1 byte solo caracteres básicos ASCII y datos binarios

	var c complex128 = 2 + 3i  //numero complejos usando 2 decimales, uno real y otro iamginario
	var otro complex128 = 4 + 2i

	suma := c + otro

	fmt.Println(edad, gobernador, ciudad)
	fmt.Println(entero0, entero1, entero2, entero3, entero4)
	fmt.Println(natural0, natural1, natural2, natural3, natural4)
	fmt.Println(decimal1, decimal2)
	fmt.Println(activo, negativo)
	fmt.Println(texto)
	fmt.Println(letra, string(letra)) // 71 G
	fmt.Println(b, string(b))         // 65 A
	fmt.Println("variable 1:", c)
	fmt.Println("variable 2:", otro)
	fmt.Println("suma:", suma)   

}

func main(){
	tipos_datos()
}