package main

import (
	"fmt"
	"errors"
)

func main() {

	// Dividir 10/0
	_, err := divide(10, 0)
	if err != nil {
		fmt.Println("Error al dividir: ", err)
	}

	// Acceder a un índice no existente de un listado
	list := []int{1, 2, 3}
	_, err = iterateList(list)
	if err != nil {
		fmt.Println("Error al iterar: ", err)
	}

	// Extra: Procesar parámetros
	value1, err := process(10, 2)
	if err != nil {
		fmt.Println("Error al procesar parámetros: ", err)
	} else {
		fmt.Println("Parametros procesados correctamente: ", value1)
	}

	value2, err := process(13, 2)
	if err != nil {
		fmt.Println("Error al procesar parámetros: ", err)
	} else {
		fmt.Println("El resultado es: ", value2)
	}

	fmt.Println("El programa continua, no termina inesperadamente al haber errores ya que los estamos manejando...")
}

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("No se puede dividir por 0")
	}
	return a / b, nil
}

func iterateList(list []int) (int, error) {
	for i := 0; i < len(list)+1; i++ {
		if i >= len(list) {
			return 0, errors.New("Indice fuera de rango")
		}
		fmt.Println(list[i])
	}
	return 0, nil
}

// Extra:

type MyError struct {
	code int
	msg string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("Error %d: %s", e.code, e.msg)
}

func process(a, b int) (int, error) {
	if a <= 0 {
		return 0, errors.New("El primer parámetro no puede ser negativo ni 0")
	}
	if b <= 0 {
		return 0, errors.New("El segundo parámetro no puede ser negativo ni 0")
	}
	if a == 13 {
		return 0, &MyError{code: 13, msg: "El primer parámetro no puede ser 13"}
	}
	if b == 13 {
		return 0, &MyError{code: 13, msg: "El segundo parámetro no puede ser 13"}
	}
	fmt.Println("Ejecucion finalizada sin errores.")
	return a + b, nil
}