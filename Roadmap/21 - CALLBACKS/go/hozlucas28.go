package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

/* -------------------------------------------------------------------------- */
/*                                  FUNCTIONS                                 */
/* -------------------------------------------------------------------------- */

func MapArray[T int | string](array []T, callback func(currentValue T, indexOfCurrentValue int) T) {
	for index, value := range array {
		array[index] = callback(value, index)
	}
}

func prepareDish(dishName string, onConfirm func(dishName string), onReady func(dishName string), onDeliver func(dishName string)) {
	onConfirm(dishName)

	var randomTimeout int = rand.Intn(10) + 1

	for i := 0; i < randomTimeout; i++ {
		time.Sleep(time.Second)
	}
	onReady(dishName)

	onDeliver(dishName)
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

func main() {
	/*
		Callbacks...
	*/

	fmt.Println("Callbacks...")

	var numbers []int = []int{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
	fmt.Printf("\nNumbers array before 'MapArray' function call: %d\n", numbers)

	MapArray(numbers, func(currentValue int, indexOfCurrentValue int) int {
		return currentValue - 1
	})
	fmt.Printf("Numbers array after 'MapArray' function call: %d\n", numbers)

	var people []string = []string{"Juan", "Lucas", "Manuel", "Jose"}
	fmt.Printf("\nPeople array before 'MapArray' function call: %s\n", people)

	MapArray(people, func(currentValue string, indexOfCurrentValue int) string {
		return fmt.Sprintf("Hi %s!", currentValue)
	})
	fmt.Printf("People array after 'MapArray' function call: %s\n", people)

	fmt.Println("\n# ---------------------------------------------------------------------------------- #")

	/*
		Additional challenge...
	*/

	fmt.Printf("\nAdditional challenge...\n\n")

	var wg sync.WaitGroup

	onConfirm := func(dishName string) {
		fmt.Printf("%s in preparation.\n", dishName)
	}

	onReady := func(dishName string) {
		fmt.Printf("%s is ready to deliver.\n", dishName)
	}

	onDeliver := func(dishName string) {
		fmt.Printf("%s delivered.\n", dishName)
		wg.Done()
	}

	wg.Add(2)
	go prepareDish("Spaghetti", onConfirm, onReady, onDeliver)
	go prepareDish("Soup", onConfirm, onReady, onDeliver)
	wg.Wait()
}
