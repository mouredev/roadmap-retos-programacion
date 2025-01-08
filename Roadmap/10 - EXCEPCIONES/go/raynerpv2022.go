package main

import "fmt"

/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */

func DivInteger(a, b int) (div_ab float32, err error) {

	defer func() {

		r := recover()
		if r != nil {
			err = fmt.Errorf("Error  como P^$!a : %v ", r)
			div_ab = 0
		}
	}()

	div_ab = float32(a) / float32(b)
	if b == 0 {
		panic("B == 0")
	}
	return div_ab, nil
}
func sliceOutofRange(lista []int, index int) (num int, err error) {
	defer func() {
		r := recover()
		if r != nil {
			err = fmt.Errorf("Eeeeerrror %v", r)
			num = -1
		}
	}()
	num = lista[index]
	return num, nil

}

/* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 */

func CustomError(Index int, list []int) (prom float32, err error) {

	defer func() {
		r := recover()
		if r != nil {
			err = fmt.Errorf("error.. %v", r)
		}
	}()
	Longitud := len(list)
	// verifico que el index este entre 0 y max longitud de la cadena
	if (Longitud < Index) || (Index < 0) {

		panic(" Acceso a valores fuera de rango")
	}

	if list[Longitud-1] == 10 {
		panic(" el ultimo elemento no puede ser 10")
	}

	prom = float32(list[Longitud-1]) / float32(list[0])

	// controlo la division por cero
	if float32(list[0]) == 0 {

		panic("Division por cero no permitida")

	}
	return prom, nil

}

func main() {
	fmt.Println("Reto #10 Exception")
	var a, b int

	fmt.Print("Numerador :")
	fmt.Scanln(&a)
	fmt.Print("Denominador :")
	fmt.Scanln(&b)
	div_ab, ok := DivInteger(a, b)
	if ok == nil {
		fmt.Println("No hay error")
		fmt.Printf(" %v / %v = %v\n", a, b, div_ab)
	} else {
		fmt.Printf("Error div x 0 is a chaos... %v\n", ok)
	}

	index := 10
	num, e := sliceOutofRange([]int{0, 1, 2, 3}, index)
	if e != nil {
		fmt.Printf("Error %v\n", e)
	} else {
		fmt.Printf("in %v position is %v\n", index, num)
	}

	fmt.Println("EXTRA")
	fmt.Println()

	prom, er := CustomError(3, []int{20, 2, 3, 4, 1, 1, 1, 100})
	if er != nil {
		fmt.Println(er)
	} else {
		fmt.Println("No se ha producido ningun error")
		fmt.Println("Promedio es: ", prom)
	}

	fmt.Println("El programam ha finalizado")

}
