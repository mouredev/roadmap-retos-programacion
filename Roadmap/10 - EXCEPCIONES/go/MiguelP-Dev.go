package main

import (
	"errors"
	"fmt"
	"strconv"
)

/*
En golang no existen las excepciones, pero si existen las funciones de manejo de errores.

Los errores son parte importante de golang porque se decidió desde su diseño inicial, tabajar con ellos
en vez de excepciones porque estas en la mayoria de los casos no son controladas por el desarrollador

La idea es que los errores sean controlados apenas se presenten, esta es la razón de que las funciones
devuelvan multiples valores. Usualmente las funciones como ultimo argumento devuelven un error, para que
podamos validar si la función ejecutada genera un error y lo podamos controlar.

Controlar los errores e golang es muy cómodo, además saves siempre de donde viene el error si lo haces
correctamente. Para controlar los errores y darle más personalización existe el paquete "errors" o
la función 'errorf' del paquete "fmt", además go, cuenta con funciones como "panic y recover".

En golang usamos el ok para comprobar errores (Usamos el operador unario con el ok).
Ok es una variable booleana usada comunmente para verificar si una operación se realizó con éxito,
premitiendo un manejo más preciso y seguro de los errores y condiciones.
*/

// val Variable para guardar el valor obtenido de la conversión en la función
var val = strToInt("24")

// found Variable que se redefinirá su valor durate los ejercicios y ejemplos
var found string

// stringToInt Ejemplo 1 de manejo de errores(Simple)
func strToInt(s string) int {
	num, err := strconv.Atoi(s)
	if err != nil {
		fmt.Println("Error: informacion no válida.", err)
		return -1
	}
	return num
}

// errNotFound es una variable que almacena un mensaje personalizado para controlar un error.
var errNotFound = errors.New("Not Found.")

// fastFood mapa de comida rápida
var fastFood = map[int]string{
	24: "Hamburguesa", 22: "Perro Caliente", 23: "Arroz Chino", 25: "Pizza",
}

// search funcion de busqueda por un mapa.
func search(key string) (string, error) {
	num, err := strconv.Atoi(key)
	if err != nil {
		return "", fmt.Errorf("strconv.Atoi: %w", err)
	}

	value, err := okVariable(num)
	if err != nil {
		return "", err
	}
	return value, nil
}

// okVariable Usando el ok y el operador unario y se llama desde search()
func okVariable(num int) (string, error) {
	value, ok := fastFood[num]
	if !ok {
		return "", fmt.Errorf("OkVariable(): Valor inexistente")
	}
	return value, nil
}

// animals mapa de animales
var animals = map[int]string{
	1: "Gato", 2: "Perro", 3: "León",
}

// search funcion de busqueda por un mapa.
func searchAnimals(key string) (string, error) {
	number, err := strconv.Atoi(key)
	if err != nil {
		return "", fmt.Errorf("strconv.Atoi(): %w", err)
	}
	value, err := findAnimal(number)
	if err != nil {
		return "", fmt.Errorf("findAnimal(): %w", err)
	}
	return value, nil
}

func findAnimal(num int) (string, error) {
	number, ok := animals[num]
	if !ok {
		return "", errNotFound
	}
	return number, nil
}

/*
En estos ejercicios simple no se alcanza a ver la complejidad, por tanto es simple controlarlos así, pero para casos más complejos
hay que llevar un correcto seguimineto de estos errores,sobretodo cuando hay un anidamiento de procedimientos,
para eso es muy util el paquete format(fmt) con su función errorf, donde aparte
de poner texto de error personalizado puedo entregar específicamente desde que funcion o método viene el error.
*/

var number1 = 12
var number2 = 0

// division Funcion de division por cero
func division(n1, n2 int) (int, error) {
	if n2 == 0 {
		return -1, errNotFound
	}
	result := n1 / n2
	return result, nil

}

// Otra opcion que tiene golang para manejar errores sin se que se detenga la aplicación es con panic y recover
// Panic se usa para generar un panico tras un error y recover para recuperarse de su error y continuar
// con las operaciones dejando un mensaje de error.

// extraFunction: Es la función creada para el ejercicio extra de la roadmap
func extraFunction(n string, n2 int) (int, error) {
	// Con una funcion anónima en una cola de ejecucion con difer, verificamos si se produce un panic y nos recuperamos de él
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Me recuperé del panic.")
		}
	}()

	str, err := strconv.Atoi(n)
	if err != nil {
		return 0, fmt.Errorf("strconv.Atoi(): El parámetro no es válido para operar: %w", err)
	}
	// Validamos si el divisor es igual a cero
	validateZero(n2)

	fmt.Printf("No hubo errores, Resultado de dividir %v entre %v: ", str, n2)
	return str / n2, nil
}

func validateZero(n int) {
	if n == 0 {
		panic("No es posible dividir por cero")
	}
}

func main() {
	// Primer ejemplo: simple
	fmt.Printf("Value: %d Tipo de datos: %T\n", val, val)

	// Segúndo ejemplo: manejo con paquete errors (Personalizado.)
	found, err := search("22")
	if err != nil {
		fmt.Println("search(): ", err)
		return
	}
	fmt.Println(found)

	// Tercer ejemplo: comprobación ok con unario. (Uso sin search para buscar el valor directamente)
	found, err = okVariable(val)
	if err != nil {
		fmt.Println("okVariable():", err)
		return
	}
	fmt.Println(found)

	// Conprobación espesífica de errores
	found, err = searchAnimals("4")
	if errors.Is(err, errNotFound) {
		fmt.Println("Pudimos controlar el error.")
		return
	}
	if err != nil {
		fmt.Println("searchAnimals(): ", err)
		return
	}
	fmt.Println(found)

	// Divición por cero
	div, err := division(number1, number2)
	if err == errNotFound {
		fmt.Println("No es posible dividir por 0")
		return
	}
	fmt.Printf("Resultado de dividir %d entre %d, es: %d\n", number1, number2, div)

	// Extra
	divisionExtra, err := extraFunction("12", 2)
	if err != nil {
		fmt.Printf("Mensaje de error: %s, Tipo: %T\n", err, err)
		return
	}
	fmt.Println(divisionExtra)
	fmt.Println("La Ejecución finalizó.")
}
