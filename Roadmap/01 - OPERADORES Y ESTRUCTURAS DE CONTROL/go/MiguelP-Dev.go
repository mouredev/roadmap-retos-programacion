package main

import "fmt"

var a, b, c = 4, 7, 9

func main() {
	/*
	   Debemos Respetar y tener en cuenta en nuestra lógica; la gerarquía de operadores.
	*/

	// Operadores aritméticos y su gerarquía
	/*
		() las operaciones entre parentesis siempre operan primero
		* Las multiplicaciones son las siguientes en la gerarquía
		/ Le siguen las diviones
		% El módulo
		+ La suma
		- Y al final la resta
	*/
	fmt.Println("(2 + 3) * 3: ", (a+b)*c) // El resultado sería 15 porque la operación entre parentesis opera primero
	fmt.Println("2 + 3 * 3: ", a+b*c)     // El resultado sería 11 porque la multiplicación opera antes que la suma.
	fmt.Println("2 * 3: ", a*b)           // 6
	fmt.Println("2 / 3: ", a/b)           // 0,666666666666666
	fmt.Println("2 % 3: ", a%b)           // 0,06
	fmt.Println("2 + 3: ", a+b)           // 5
	fmt.Println("2 - 3: ", a-b)           // -1

	// Operadores de asignación
	/*
		= Operador de asignación
		+= Opercador de asignación con suma para adicionar un valor a la variable
	*/

	// b Variable para uso de los ejemplos con operadores
	var b uint8 = 5
	fmt.Println("Valor de b: ", b)
	b = b + 2
	fmt.Println("b + 2: ", b)
	// Combinando los operadores aritméticos con el de asignación
	b += 2
	fmt.Println("b + 2: ", b)
	b -= 2
	fmt.Println("b - 2", b)
	b *= 2
	fmt.Println("b * 2: ", b)
	b /= 2
	fmt.Println("b / 2: ", b)
	b %= 2
	fmt.Println("b % 2: ", b)

	// Operadores de Incremento(++) y Decremento(--)
	/*
		Estos operadores son declaraciones, no expresiones:
		Las expresiones producen un valor a partir de sus operaciones.
		las declaraciones son instrucciones del lenguaje que realizan una acción.
	*/

	// incre Variable para el ejemplo correcto en go sobre el incremento
	incre := 7
	incre++
	fmt.Println(incre)

	// decre Variable para el ejemplo correcto en go sobre el decremento
	decre := 10
	decre--
	fmt.Println(decre)
	/*
	   Nota: Golang no permite el uso de estos operadores de decremento e incremento dentro de Print.
	   Es obligaorio operar fuera de esta y luego entregar el resultado o hacer lo que sea para lo que se use el valor reultante de la operación.
	*/

	// Operadores lógicos y de comparación.
	/*
		> Mayor que
		< Menor que
		== Operador de igualdad exacta
		!= Operador de diferencia
		>= Mayor o igual que
		<= Menor o igual que
	*/

	// mayor variable entera con número mayor para operar en los ejemplos.
	mayor := 21

	// menor variable entera con número menor para operar en los ejemplos.
	menor := 15

	// Impresion de los ejemplos de operadores de comparación.
	fmt.Println(mayor, "¿es mayor que? ", menor, ": ", mayor > menor)
	fmt.Println(mayor, "¿es menor que? ", menor, ": ", mayor < menor)
	fmt.Println(mayor, "¿es diferente? ", menor, ": ", mayor != menor)
	fmt.Println(mayor, "¿es igual que? ", menor, ": ", mayor == menor)
	fmt.Println(mayor, "¿es mayor o igual que? ", menor, ": ", mayor >= menor)
	fmt.Println(mayor, "¿es menor o igual que? ", menor, ": ", mayor <= menor)

	// Operadores lógicos
	/*
	   && Operador (Y): Usado con otros operadores para comparar más de una condición o comprobación.
	   || Operador (O): Usado con otros operadores para comparar si se cumple alguna de las condiciones o comprobaciones.
	   ! Operador de negación(Unario): Se usa para negar un resultado o más bien convertir a falso un resultado aunque este sea verdadero.
	*/

	// Operador (O)
	fmt.Println("My es mayor que MN o Mn es Mayor que My", mayor > menor || menor > mayor)
	fmt.Println("My es mayor que MN o Mn es Mayor que My", menor <= menor || menor <= mayor)

	// Operador (Y)
	fmt.Println("My es mayor que MN o Mn es Mayor que My", mayor > menor && menor < mayor)
	fmt.Println("My es mayor que MN o Mn es Mayor que My", mayor > menor && menor == mayor)

	// Operador (!) Unario
	fmt.Println("My es mayor que MN o Mn es Mayor que My", !(mayor > menor && menor == mayor))
	fmt.Println("My es mayor que MN o Mn es Mayor que My", !(mayor > menor && menor != mayor))

	// Operadores bit a bit
	ba := 12 // 1100 en binario
	bb := 10 // 1010 en binario

	// Operador AND(&): Compara cada bit de los números. Si ambos son 1, el resultado es 1,
	// de lo contrario, es 0
	result := ba & bb
	fmt.Printf("%d & %d = %d\n", ba, bb, result) //  8 o 1000 en binario.

	// Operador OR(|): Compara cada bit de dos números. S al menos 1 de los bits es 1, el resultado es 1,
	// de lo contrario será 0.
	result = ba | bb
	fmt.Printf("%d | %d = %d\n", ba, bb, result) // 14 o 1110 en binario.

	// Operador XOR(^): Compara cada bit de dos números. Si los bits son diferentes, el resuktado es 1,
	// si son iguales, es 0.
	result = ba ^ bb
	fmt.Printf("%d & %d = %d\n", ba, bb, result) // 6 o 0110 en binario.

	// Operador NOT(^): Este operador Invierte cada bit del número. Convierte los 1 en 0 y viceversa.
	// El resultado puede parecer extraño porque los número negativos usan una técnica llamada:
	// Complemento a dos, pero la idea principal es que cada bit se invierta.
	result = ^bb
	fmt.Printf("^%d = %d\n", bb, result) // -11 o 0101 en binario.

	// Operador Desplazamientos a la izquierda(<<): Este operador a la derecha los bits en base al valor seleccionado:
	// para este ejemplo 2 posiciones a la izquierda, rrellenando los espacios vacios con 0.
	// Esta equivale a multiplicar el número por el valor asignado.
	result = bb << 2
	fmt.Printf("%d << 2 = %d\n", bb, result) // 40 o 101000 en binario.

	// Operador Desplazamientos a la derecha(>>): Este operador desplaza los bits del número a la derecha,
	// eliminando los bits desplazados y rellenando los espacios vacios con 0(Para números positivos).
	// Cada Desplazamiento a la derecha equivale a dividir el número por el valor asignado
	result = ba >> 2
	fmt.Printf("%d >> 2 = %d\n", ba, result) // 3 o 0011 en binario.

	// Estructuras de control

	//  Condicionales  If y Switch
	/*
		En go es posible declarar la variable en la misma comprobación del if, así queda aislada si se necesita así.
		Los if son muy adecuados a la hora de controlar errores o como estructura de control para casos sencillos.
		Para casos donde las condiciones son muchas y es complicado anidar bien los if, es mejor switch
	*/

	if num := 80; num > 90 {
		fmt.Println("Es mayor de noventa")
	} else if num < 90 && num > 80 {
		fmt.Println("Es menor que noventa y mayor que 80")
	} else {
		fmt.Println("Es 80 o menor")
	}

	// name Variable usada en el switch
	name := "Miguel"

	/*
		Las estructuras Switch puede crearse sin pasarle una expresion para la
		comprobación y realizar la comprobación directamente en casa case, esto por si queremos evaluar
		distintas condiciones con parametros distintos cada vez.
		Nota: En golang no es necesario usar la palabra reservada "Break" para finalizar el switch
		este se detendrá al cumplirse cualquier condición o la condicion default.
	*/
	//  Este es una estrucutura de control ideal para concantenar multiples condiciones.
	switch name {
	case "Alejandro":
		fmt.Println("El nombre es Alejandro")
	case "Miguel":
		fmt.Println("El nombre es Miguel")
	default:
		fmt.Println("El nombre es Desconocido")

	}

	// Fallthrough de switch.
	// En la declaración switch de go, cada rama no cae automaticamente al siguiente caso,
	// a menos que se utilice la palabra reservada fallthrough: en el siguiente caso;
	// aunque el primer case coincide,
	// debido a la presencia de la palabra falltrough, este seguirá al siguiente caso e imprimirá
	// la frase del caso 2.
	switch name {
	case "Miguel":
		fmt.Println("EL nombre es Miguel.")
		fallthrough
	case "Alejandro":
		fmt.Println("El nombre es Alejandro.")
	default:
		fmt.Println("El nombre no coincide.")
	}

	/*
		Ramificación por tipo y ramificación perzonalizada
		La declaración switch también admite ramificación en tipos de variables,
		conocida como ramificación por tipo. Además, podemos crear condiciones
		de ramificación personalizadas más complejas.

		Nota: las ramificaciones personalizadas se pueden escribir para realizar
		juicios condicionales más complejos según sea necesario.
	*/
	// i Variable de uso en ejemplo de switch.
	var i interface{} = 1

	switch i.(type) {
	case int:
		fmt.Println("i es un entero")
	case float64:
		fmt.Println("i es un float64")
	default:
		fmt.Println("i es otro tipo")
	}

	// Ciclo for
	for i := 0; i < 5; i++ {
		fmt.Println("El valor de i es: ", i)
	}

	// Ciclo infinito: se omite la inicializacion, la expresion de condición y la declaración post del bucle.
	// Creando un bucle infinito que solo se detendrá con la palabra reservada break o un valor de retorno de una función.
	for {
		n := 0
		if n == 5 {
			break
		}
		fmt.Println("El valor de n es: ", n)
		n++
	}

	// Llamada a la función para usar defer
	callDefer()

	// Llamada a la función de divisón para uso de panic y Recover
	division(12, 2)
	division(50, 2)
	division(5, 0)
	division(10, 3)

	// Extra
	/*
		for i := 10;		Inicializo el buclue con i teniendo valor de 10.
		i <= 55; 			Comparo que i sea menor o igual que 55.
		i++ 				Le aumento a i en 1 con cada iteración.
		if i != 16			Compruebo que i no sea igual a 16.
		&& i*3 != 0			Comprueba que i no sea divisible por 3, con el operador % calculo el resto de i,
							divido por 3, si i es divisible por 3, i%3 será 0.
		fmt.Println(i)		Imprimo todo el proceso en cada iteración.
	*/
	for i := 10; i <= 55; i++ {
		if i != 16 && i*3 != 0 {
			fmt.Println(i)
		}
	}

}

func callDefer() {
	// Defer: Esta función sirve para atrasar la ejecución de alguna funcion hasta que la funcion desde donde fue llamada retorne.
	nf := 5                                             // Declararamos y asignamos valor a la variable nf
	defer fmt.Println("Impresión de la variable: ", nf) // Usamos defer para retrasar la impresion de la variable nf
	nf = 10                                             // Reasignamos el valor de la variable nf
	fmt.Println("Reimpresión de la variable: ", nf)     // Reimprimimos la variable nf (Se imprime esta primero)

}

// Panic: Nos permite detener nuestro programa.
// Recover: nos permite seguir con el programa a pesar del panic(Se recupera del panic)
func division(dividend, divisor int) {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Me recuperé del panic")
		}
	}()

	validateZero(divisor)
	fmt.Println(dividend / divisor)
}

func validateZero(divisor int) {
	if divisor == 0 {
		panic("No se puede dividir por 0")
	}
}
