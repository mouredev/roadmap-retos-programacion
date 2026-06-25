/*		Operadores Aritméticos

		El \n lo utilizo por estética solamente, te hace un salto de linea en la consola

		Se usa la interpolación en el método:
			fmt.Println("Texto", variable)

*/

package main

import (
	"fmt"
	"errors"
)





func dividir(x, z float64) (float64, error) {
    if z == 0 {
        return 0, errors.New("no se puede dividir por cero")
    }
    return x / z, nil
}		





func main() {

	a := 12
	b := 21

	Suma := a + b
	fmt.Println("La suma de 12 + 21 es \n", Suma)

	Resta := b - a
	fmt.Println("La resta de 21 - 12 es \n", Resta)

	Multiplicacion := a * b
	fmt.Println("La multiplicación de 12 * 21 es \n", Multiplicacion)

	Division := b / a
	fmt.Println("La división de 21 / 12 es \n", Division)

	Modulo := b % a
	fmt.Println("El modúlo de 21 % 12 es \n", Modulo)

	// Operadores de Comparación

	IgualA := a == b
	DiferenteDe := b != a
	MayorQue := b > a
	MenorQue := a < b
	MayorOIgualQue := a >= b
	MenorOIgualQue := b <= a

	fmt.Println("¿12 es igual a 21? \n", IgualA)
	fmt.Println("¿21 es diferente a 12? \n", DiferenteDe)
	fmt.Println("¿21 es mayor a 12? \n", MayorQue)
	fmt.Println("¿12 es menor a 21? \n", MenorQue)
	fmt.Println("¿12 es mayor o igual a 21? \n", MayorOIgualQue)
	fmt.Println("¿21 es menor o igual a 12? \n", MenorOIgualQue)

	// Operadores lógicos

	c := 5
	g := 7
	f := 12

	fmt.Println("¿C es mayor que G y F es igual a 12?\n")
	fmt.Println(c > g && f == 12)
	fmt.Println("¿C es mayor que G o F es diferente a 12?\n")
	fmt.Println(c > g || f != 12)

	// Operadores de asignación

	L := 33
	fmt.Println(L)
	L += 1
	fmt.Println(L)
	L -= 1
	fmt.Println(L)
	L *= 4
	fmt.Println(L)
	L /= 4
	fmt.Println(L)
	L %= 2
	fmt.Println(L)

	/* Operadores a nivel de Bits

	^ es XOR
	&^ es BITCLEAR
	<< DESPLAZAMIENTO DE BITS A LA IZQUIERDA
	>> DESOKAZANUEBTI DE BITS A LA DERECHA

	*/

	OperadorBits1 := 10 //1010
	OperadorBits2 := 3  // 0011

	fmt.Println("AND: 10 & 3 = ", OperadorBits1&OperadorBits2)
	fmt.Println("xOR: 10 ^ 3 = ", OperadorBits1^OperadorBits2)
	fmt.Println("<<: 10 << 3 = ", OperadorBits1<<OperadorBits2)
	fmt.Println(">>: 10 >> 3 = ", OperadorBits1>>OperadorBits2)

	// Operadores condicionales

	GamerTag := "Fengario"

	if GamerTag == "Fengario" {
		fmt.Println("Bienvenido FENGADIOS")
	} else if GamerTag == "Fulanito" {
		fmt.Println("No te conozco, vete")
	} else {
		fmt.Println("Por ser tú, llamaré a la policia")
	}

	// Iterativas/Bucles
	for i := 0; i < 5; i++ {
		fmt.Println("Iteración:", i)
	}

	// For al estilo While
	contador := 0
	for contador < 3 {
		fmt.Println("Contador:", contador)
		contador++
	}
	for {
		fmt.Println("Esto sería un bucle infinito si no estuviera BREAK")
		break
	}

	// Manejo de expeciones o equivalente al TRY CATCH

    // "Try" (Intentar)
    resultado, err := dividir(10, 0)
    
    // "Catch" (Manejar el error)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    
    fmt.Println("Resultado:", resultado)

	}
