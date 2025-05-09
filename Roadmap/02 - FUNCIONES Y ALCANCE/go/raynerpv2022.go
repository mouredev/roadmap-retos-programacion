package main

import "fmt"

func func_sin_p() {
	fmt.Println("hoy es   6 de agosto")
}

func func_1_p(mes string) {
	fmt.Printf("hoy es  6 de %s \n", mes)
}

func func_2_p(dia int, mes string) {
	fmt.Printf("hoy es %d de %s \n", dia, mes)
}

// funcion variatica para valores por defecto
func func_value_default(fecha ...string) {
	dia := "26"
	mes := "enero"
	if len(fecha) > 0 {
		dia = fecha[0]
		mes = fecha[1]
	}
	fmt.Printf("hoy es  %s de %s \n", dia, mes)
}

func returnMult(dia, mes string) (string, string) {
	return dia, mes
}

func Mult3y5(tres, cinco string) int {
	number := 0
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println(tres, cinco)
		} else if i%3 == 0 {
			fmt.Println(tres)
		} else if i%5 == 0 {
			fmt.Println(cinco)
		} else {
			number++
			fmt.Println(i)
		}
	}
	return number

}

func func_var_param(names ...string) {
	long := len(names)
	if long > 0 {
		fmt.Printf("existen %d parametros\n", long)
		for _, fecha := range names {
			fmt.Println(fecha)
		}
	} else {
		fmt.Println("no existen parametros")

	}
}

func main() {
	fmt.Println(Mult3y5("TRES", "CINCO"))
	func_1_p("noviembre")
	func_2_p(3, "octubre")
	func_sin_p()
	func_value_default()
	func_value_default("31", "diciembre")
	dia, mes := returnMult("1", "enero")
	fmt.Println(dia, mes)
	func_var_param()
	func_var_param("31", "mayo")

}
