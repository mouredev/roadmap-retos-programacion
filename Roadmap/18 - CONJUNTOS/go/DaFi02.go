package main

import "fmt"

type data struct {
	elements []interface{}
}

/* Funciones para que se use cada punto */

/*Imprimir valors*/

func printData(d *data) {
	for i, element := range d.elements {
		if i != len(d.elements)-1 {
			fmt.Print(element, ", ")
		} else {
			fmt.Print(element)

		}

	}
	fmt.Println()
}

/* añadir elemento al final */
func addData(d *data, element interface{}) {
	d.elements = append(d.elements, element)
}

/*Añadir elementos al inicio*/
func addFirstData(d *data, element interface{}) {
	d.elements = append([]interface{}{element}, d.elements...)
}

/*Añadir varios elementos en bloque*/
func addBlockDataFinal(d *data, elements ...interface{}) {
	d.elements = append(d.elements, elements...)
}

func addBlockDataPosition(d *data, position int, elements ...interface{}) {
	d.elements = append(d.elements[:position], append(elements, d.elements[position:]...)...)
}

func deleteDataPosition(d *data, position int) {
	d.elements = append(d.elements[:position], d.elements[position+1:]...)
}

func updateDataPosition(d *data, position int, element interface{}) {
	d.elements[position] = element
}

func verificationElementInData(d *data, element interface{}) string {
	for _, el := range d.elements {
		if el == element {
			return "'" + element.(string) + "'" + " is here!"
		}
	}
	return "'" + element.(string) + "'" + " is not here! :c"
}

func deleteAllData(d *data) {
	d.elements = []interface{}{}
}

func unionData(d1 *data, d2 *data) *data {
	dUnion := data{}
	dUnion.elements = append(d1.elements, d2.elements...)
	return &dUnion
}

func intersectionData(d1 *data, d2 *data) *data {
	dIntersection := data{}
	for _, el1 := range d1.elements {
		for _, el2 := range d2.elements {
			if el1 == el2 {
				dIntersection.elements = append(dIntersection.elements, el1)
			}
		}
	}
	return &dIntersection
}

func differenceData(d1 *data, d2 *data) *data {
	dDiference := data{}
	for _, el1 := range d1.elements {
		isIn := false
		for _, el2 := range d2.elements {
			if el1 == el2 {
				isIn = true
			}
		}
		if !isIn {
			dDiference.elements = append(dDiference.elements, el1)
		}
	}
	return &dDiference
}

func symmetricaldDifferenceData(d1 *data, d2 *data) *data {
	dDiference := differenceData(d1, d2)
	d2Diference := differenceData(d2, d1)
	dSymmetricalDifference := unionData(dDiference, d2Diference)
	return dSymmetricalDifference
}

/* funcion main */

func main() {
	initialData := data{
		elements: []interface{}{1, "MoureDev", 3, "hello", "DaFi"},
	}

	fmt.Println("Initial Data:")
	fmt.Println(initialData.elements)

	fmt.Println("-------------------------")
	fmt.Println("Adding elements at the end:")
	addData(&initialData, "Voy al Final")
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Adding elements at the beginning:")
	addFirstData(&initialData, "Voy al principio")
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Adding multiple elements at the end:")
	addBlockDataFinal(&initialData, "Voy al final 2.0", 987654, "Voy al final 3.0")
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Adding multiple elements at a specific position:")
	addBlockDataPosition(&initialData, 2, "Voy en la Posición 2", "Voy seguido al de la posición 2")
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Deleting element at a specific position:")
	deleteDataPosition(&initialData, 2)
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Updating element at a specific position:")
	updateDataPosition(&initialData, 4, "Elemento Actualizado")
	printData(&initialData)

	fmt.Println("-------------------------")
	fmt.Println("Verifying if an element is in the data:")
	fmt.Println(verificationElementInData(&initialData, "MoureDev"))
	fmt.Println(verificationElementInData(&initialData, "Elemento finisimo"))

	copyData := initialData

	fmt.Println("-------------------------")
	fmt.Println("Deleting all elements:")
	deleteAllData(&initialData)
	printData(&initialData)
	fmt.Println("NO HAVE DATA! XD")

	/* Dificultad Extra */

	seconData := data{
		elements: []interface{}{1, "MoureDev", 3, "hello", "DaFi"},
	}
	fmt.Println("-------------------------")
	fmt.Println("Initial Data:")
	printData(&copyData)
	fmt.Println("Second Data:")
	printData(&seconData)

	fmt.Println("-------------------------")
	fmt.Println("Union of the two data:")
	dUnion := unionData(&copyData, &seconData)
	printData(dUnion)

	fmt.Println("-------------------------")
	fmt.Println("Intersection of the two data:")
	dIntersection := intersectionData(&copyData, &seconData)
	printData(dIntersection)

	fmt.Println("-------------------------")
	fmt.Println("Difference of the two data, First Case:")
	dDiference := differenceData(&copyData, &seconData)
	printData(dDiference)
	fmt.Println("Difference of the two data, Second Case:")
	d2Diference := differenceData(&seconData, &copyData)
	printData(d2Diference)

	fmt.Println("-------------------------")
	fmt.Println("Symmetrical Difference of the two data:")
	dSymmetricalDifference := symmetricaldDifferenceData(&copyData, &seconData)
	printData(dSymmetricalDifference)

}
